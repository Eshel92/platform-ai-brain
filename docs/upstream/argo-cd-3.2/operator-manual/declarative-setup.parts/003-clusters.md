<!-- Part 3 of 4 of operator-manual/declarative-setup.md (split because the page is big). -->

## Clusters

Cluster credentials are stored in secrets same as repositories or repository credentials. Each secret must have label
`argocd.argoproj.io/secret-type: cluster`.

The secret data must include following fields:

* `name` - cluster name
* `server` - cluster api server url
* `namespaces` - optional comma-separated list of namespaces which are accessible in that cluster. Setting namespace values will cause cluster-level resources to be ignored unless `clusterResources` is set to `true`.
* `clusterResources` - optional boolean string (`"true"` or `"false"`) determining whether Argo CD can manage cluster-level resources on this cluster. This setting is only used when namespaces are restricted using the `namespaces` list.
* `project` - optional string to designate this as a project-scoped cluster.
* `config` - JSON representation of the following data structure:

```yaml
# Basic authentication settings
username: string
password: string
# Bearer authentication settings
bearerToken: string
# IAM authentication configuration
awsAuthConfig:
    clusterName: string
    roleARN: string
    profile: string
# Configure external command to supply client credentials
# See https://godoc.org/k8s.io/client-go/tools/clientcmd/api#ExecConfig
execProviderConfig:
    command: string
    args: [
      string
    ]
    env: {
      key: value
    }
    apiVersion: string
    installHint: string
# Proxy URL for the kubernetes client to use when connecting to the cluster api server
proxyUrl: string
# Transport layer security configuration settings
tlsClientConfig:
    # Base64 encoded PEM-encoded bytes (typically read from a client certificate file).
    caData: string
    # Base64 encoded PEM-encoded bytes (typically read from a client certificate file).
    certData: string
    # Server should be accessed without verifying the TLS certificate
    insecure: boolean
    # Base64 encoded PEM-encoded bytes (typically read from a client certificate key file).
    keyData: string
    # ServerName is passed to the server for SNI and is used in the client to check server
    # certificates against. If ServerName is empty, the hostname used to contact the
    # server is used.
    serverName: string
# Disable automatic compression for requests to the cluster 
disableCompression: boolean
```

!!! important
    When `namespaces` is set, Argo CD will perform a separate list/watch operation for each namespace. This can cause
    the Application controller to exceed the maximum number of idle connections allowed for the Kubernetes API server.
    To resolve this issue, you can increase the `ARGOCD_K8S_CLIENT_MAX_IDLE_CONNECTIONS` environment variable in the
    Application controller.

!!! important 
    Note that if you specify a command to run under `execProviderConfig`, that command must be available in the Argo CD image. See [BYOI (Build Your Own Image)](custom_tools.md#byoi-build-your-own-image).

Cluster secret example:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mycluster-secret
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: mycluster.example.com
  server: https://mycluster.example.com
  config: |
    {
      "bearerToken": "<authentication token>",
      "tlsClientConfig": {
        "insecure": false,
        "caData": "<base64 encoded certificate>"
      }
    }
```

### EKS

EKS cluster secret example using argocd-k8s-auth and [IRSA](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mycluster-secret
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: "eks-cluster-name-for-argo"
  server: "https://xxxyyyzzz.xyz.some-region.eks.amazonaws.com"
  config: |
    {
      "awsAuthConfig": {
        "clusterName": "my-eks-cluster-name",
        "roleARN": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_ROLE_NAME>"
      },
      "tlsClientConfig": {
        "insecure": false,
        "caData": "<base64 encoded certificate>"
      }        
    }
```

This setup requires:

1. [IRSA enabled](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html) on your Argo CD EKS cluster
2. An IAM role ("management role") for your Argo CD EKS cluster that has an appropriate trust policy and permission policies (see below)
3. A role created for each cluster being added to Argo CD that is assumable by the Argo CD management role
4. An [Access Entry](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) within each EKS cluster added to Argo CD that gives the cluster's role (from point 3) RBAC permissions
to perform actions within the cluster
    - Or, alternatively, an entry within the `aws-auth` ConfigMap within the cluster added to Argo CD ([depreciated by EKS](https://docs.aws.amazon.com/eks/latest/userguide/auth-configmap.html))

#### Argo CD Management Role

The role created for Argo CD (the "management role") will need to have a trust policy suitable for assumption by certain 
Argo CD Service Accounts *and by itself*.

The service accounts that need to assume this role are:

- `argocd-application-controller`,
- `argocd-applicationset-controller`
- `argocd-server`

If we create role `arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ARGO_CD_MANAGEMENT_IAM_ROLE_NAME>` for this purpose, the following
is an example trust policy suitable for this need. Ensure that the Argo CD cluster has an [IAM OIDC provider configured](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ExplicitSelfRoleAssumption",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "ArnLike": {
                  "aws:PrincipalArn": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ARGO_CD_MANAGEMENT_IAM_ROLE_NAME>"
                }
            }
        },
        {
            "Sid": "ServiceAccountRoleAssumption",
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::<AWS_ACCOUNT_ID>:oidc-provider/oidc.eks.<AWS_REGION>.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "oidc.eks.<AWS_REGION>.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:sub": [
                        "system:serviceaccount:argocd:argocd-application-controller",
                        "system:serviceaccount:argocd:argocd-applicationset-controller",
                        "system:serviceaccount:argocd:argocd-server"
                    ],
                    "oidc.eks.<AWS_REGION>.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:aud": "sts.amazonaws.com"
                }
            }
        }
    ]
}
```

#### Argo CD Service Accounts

The 3 service accounts need to be modified to include an annotation with the Argo CD management role ARN.

Here's an example service account configurations for `argocd-application-controller`, `argocd-applicationset-controller`, and `argocd-server`.

!!! warning
Once the annotations has been set on the service accounts, the application controller and server pods need to be restarted.

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    eks.amazonaws.com/role-arn: "<arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ARGO_CD_MANAGEMENT_IAM_ROLE_NAME>"
  name: argocd-application-controller
---
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    eks.amazonaws.com/role-arn: "<arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ARGO_CD_MANAGEMENT_IAM_ROLE_NAME>"
  name: argocd-applicationset-controller
---
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    eks.amazonaws.com/role-arn: "<arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ARGO_CD_MANAGEMENT_IAM_ROLE_NAME>"
  name: argocd-server
```

#### IAM Permission Policy

The Argo CD management role (`arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ARGO_CD_MANAGEMENT_IAM_ROLE_NAME>` in our example) additionally
needs to be allowed to assume a role for each cluster added to Argo CD.

If we create a role named `<IAM_CLUSTER_ROLE>` for an EKS cluster we are adding to Argo CD, we would update the permission 
policy of the Argo CD management role to include the following:

```json
{
    "Version" : "2012-10-17",
    "Statement" : {
      "Effect" : "Allow",
      "Action" : "sts:AssumeRole",
      "Resource" : [
        "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_CLUSTER_ROLE>"
      ]
    }
  }
```

This allows the Argo CD management role to assume the cluster role.

You can add permissions like above to the Argo CD management role for each cluster being managed by Argo CD (assuming you
create a new role per cluster).

#### Cluster Role Trust Policies

As stated, each EKS cluster being added to Argo CD should have its own corresponding role. This role should not have any
permission policies. Instead, it will be used to authenticate against the EKS cluster's API. The Argo CD management role
assumes this role, and calls the AWS API to get an auth token via argocd-k8s-auth. That token is used when connecting to
the added cluster's API endpoint.

If we create role `arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_CLUSTER_ROLE>` for a cluster being added to Argo CD, we should
set its trust policy to give the Argo CD management role permission to assume it. Note that we're granting the Argo CD 
management role permission to assume this role above, but we also need to permit that action via the cluster role's
trust policy.

A suitable trust policy allowing the `IAM_CLUSTER_ROLE` to be assumed by the `ARGO_CD_MANAGEMENT_IAM_ROLE_NAME` role looks like this:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ARGO_CD_MANAGEMENT_IAM_ROLE_NAME>"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

#### Access Entries

Each cluster's role (e.g. `arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_CLUSTER_ROLE>`) has no permission policy. Instead, we
associate that role with an EKS permission policy, which grants that role the ability to generate authentication tokens
to the cluster's API. This EKS permission policy decides what RBAC permissions are granted in that process.

An [access entry](https://docs.aws.amazon.com/eks/latest/userguide/access-entries.html) (and the policy associated to the role) can be created using the following commands:

```bash
# For each cluster being added to Argo CD
aws eks create-access-entry \
    --cluster-name my-eks-cluster-name \
    --principal-arn arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_CLUSTER_ROLE> \
    --type STANDARD \
    --kubernetes-groups [] # No groups needed

aws eks associate-access-policy \
    --cluster-name my-eks-cluster-name \
    --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy \
    --access-scope type=cluster \
    --principal-arn arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_CLUSTER_ROLE>
```

The above role is granted cluster admin permissions via `AmazonEKSClusterAdminPolicy`. The Argo CD management role that
assume this role is therefore granted the same cluster admin permissions when it generates an API token when adding the 
associated EKS cluster.

**AWS Auth (Deprecated)**

Instead of using Access Entries, you may need to use the depreciated `aws-auth`.

If so, the `roleARN` of each managed cluster needs to be added to each respective cluster's `aws-auth` config map (see
[Enabling IAM principal access to your cluster](https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html)), as
well as having an assume role policy which allows it to be assumed by the Argo CD pod role.

An example assume role policy for a cluster which is managed by Argo CD:

```json
{
    "Version" : "2012-10-17",
    "Statement" : {
      "Effect" : "Allow",
      "Action" : "sts:AssumeRole",
      "Principal" : {
        "AWS" : "<arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ARGO_CD_MANAGEMENT_IAM_ROLE_NAME>"
      }
    }
  }
```

Example kube-system/aws-auth configmap for your cluster managed by Argo CD:

```yaml
apiVersion: v1
data:
  # Other groups and accounts omitted for brevity. Ensure that no other rolearns and/or groups are inadvertently removed, 
  # or you risk borking access to your cluster.
  #
  # The group name is a RoleBinding which you use to map to a [Cluster]Role. See https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-binding-examples  
  mapRoles: |
    - "groups":
      - "<GROUP-NAME-IN-K8S-RBAC>"
      "rolearn": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_CLUSTER_ROLE>"
      "username": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_CLUSTER_ROLE>"
```

Use the role ARN for both `rolearn` and `username`.

#### Alternative EKS Authentication Methods
In some scenarios it may not be possible to use IRSA, such as when the Argo CD cluster is running on a different cloud
provider's platform. In this case, there are two options:
1. Use `execProviderConfig` to call the AWS authentication mechanism which enables the injection of environment variables to supply credentials
2. Leverage the new AWS profile option available in Argo CD release 2.10

Both of these options will require the steps involving IAM and the `aws-auth` config map (defined above) to provide the 
principal with access to the cluster.

##### Using execProviderConfig with Environment Variables
```yaml
---
apiVersion: v1
kind: Secret
metadata:
  name: mycluster-secret
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: mycluster
  server: https://mycluster.example.com
  namespaces: "my,managed,namespaces"
  clusterResources: "true"
  config: |
    {
      "execProviderConfig": {
        "command": "argocd-k8s-auth",
        "args": ["aws", "--cluster-name", "my-eks-cluster"],
        "apiVersion": "client.authentication.k8s.io/v1beta1",
        "env": {
          "AWS_REGION": "xx-east-1",
          "AWS_ACCESS_KEY_ID": "{{ .aws_key_id }}",
          "AWS_SECRET_ACCESS_KEY": "{{ .aws_key_secret }}",
          "AWS_SESSION_TOKEN": "{{ .aws_token }}"
        }
      },
      "tlsClientConfig": {
        "insecure": false,
        "caData": "{{ .cluster_cert }}"
      }
    }
```

This example assumes that the role being attached to the credentials that have been supplied, if this is not the case
the role can be appended to the `args` section like so:

```yaml
...
    "args": ["aws", "--cluster-name", "my-eks-cluster", "--role-arn", "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_ROLE_NAME>"],
...
```
This construct can be used in conjunction with something like the External Secrets Operator to avoid storing the keys in
plain text and additionally helps to provide a foundation for key rotation.

##### Using An AWS Profile For Authentication
The option to use profiles, added in release 2.10, provides a method for supplying credentials while still using the
standard Argo CD EKS cluster declaration with an additional command flag that points to an AWS credentials file:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mycluster-secret
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: "mycluster.com"
  server: "https://mycluster.com"
  config: |
    {
      "awsAuthConfig": {
        "clusterName": "my-eks-cluster-name",
        "roleARN": "arn:aws:iam::<AWS_ACCOUNT_ID>:role/<IAM_ROLE_NAME>",
        "profile": "/mount/path/to/my-profile-file"
      },
      "tlsClientConfig": {
        "insecure": false,
        "caData": "<base64 encoded certificate>"
      }        
    }
```
This will instruct Argo CD to read the file at the provided path and use the credentials defined within to authenticate to AWS. 
The profile must be mounted in both the `argocd-server` and `argocd-application-controller` components in order for this to work.
For example, the following values can be defined in a Helm-based Argo CD deployment:

```yaml
controller:
  extraVolumes:
    - name: my-profile-volume
      secret:
        secretName: my-aws-profile
        items:
          - key: my-profile-file
            path: my-profile-file
  extraVolumeMounts:
    - name: my-profile-mount
      mountPath: /mount/path/to
      readOnly: true

server:
  extraVolumes:
    - name: my-profile-volume
      secret:
        secretName: my-aws-profile
        items:
          - key: my-profile-file
            path: my-profile-file
  extraVolumeMounts:
    - name: my-profile-mount
      mountPath: /mount/path/to
      readOnly: true
```

Where the secret is defined as follows:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-aws-profile
type: Opaque
stringData:
  my-profile-file: |
    [default]
    region = <aws_region>
    aws_access_key_id = <aws_access_key_id>
    aws_secret_access_key = <aws_secret_access_key>
    aws_session_token = <aws_session_token>
```

> ⚠️ Secret mounts are updated on an interval, not real time. If rotation is a requirement ensure the token lifetime outlives the mount update interval and the rotation process doesn't immediately invalidate the existing token


### GKE

GKE cluster secret example using argocd-k8s-auth and [Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mycluster-secret
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: mycluster.example.com
  server: https://mycluster.example.com
  config: |
    {
      "execProviderConfig": {
        "command": "argocd-k8s-auth",
        "args": ["gcp"],
        "apiVersion": "client.authentication.k8s.io/v1beta1"
      },
      "tlsClientConfig": {
        "insecure": false,
        "caData": "<base64 encoded certificate>"
      }
    }
```

Note that you must enable Workload Identity on your GKE cluster, create GCP service account with appropriate IAM role and bind it to Kubernetes service account for argocd-application-controller and argocd-server (showing Pod logs on UI). See [Use Workload Identity](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) and [Authenticating to the Kubernetes API server](https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication).

### AKS

Azure cluster secret example using argocd-k8s-auth and [kubelogin](https://github.com/Azure/kubelogin).  The option *azure* to the argocd-k8s-auth execProviderConfig encapsulates the *get-token* command for kubelogin.  Depending upon which authentication flow is desired (devicecode, spn, ropc, msi, azurecli, workloadidentity), set the environment variable AAD_LOGIN_METHOD with this value.  Set other appropriate environment variables depending upon which authentication flow is desired.

|Variable Name|Description|
|-------------|-----------|
|AAD_LOGIN_METHOD|One of devicecode, spn, ropc, msi, azurecli, or workloadidentity|
|AZURE_CLIENT_CERTIFICATE_PATH|Path to AAD client cert in pfx.  Used in spn login and WorkloadIdentityLogin flow|
|AZURE_CLIENT_CERTIFICATE_PASSWORD|Password for the client cert in pfx.  Used in spn login|
|AZURE_CLIENT_ID|AAD client application ID|
|AZURE_CLIENT_SECRET|AAD client application secret|
|AAD_USER_PRINCIPAL_NAME|Used in the ropc flow|
|AAD_USER_PRINCIPAL_PASSWORD|Used in the ropc flow|
|AZURE_TENANT_ID|The AAD tenant ID.|
|AZURE_AUTHORITY_HOST|Used in the WorkloadIdentityLogin flow|
|AZURE_FEDERATED_TOKEN_FILE|Used in the WorkloadIdentityLogin flow|

In addition to the environment variables above, argocd-k8s-auth accepts two extra environment variables to set the AAD environment, and to set the AAD server application ID.  The AAD server application ID will default to 6dae42f8-4368-4678-94ff-3960e28e3630 if not specified.  See [here](https://github.com/azure/kubelogin#exec-plugin-format) for details.

|Variable Name|Description|
|-------------|-----------|
|AAD_ENVIRONMENT_NAME|The azure environment to use, default of AzurePublicCloud|
|AAD_SERVER_APPLICATION_ID|The optional AAD server application ID, defaults to 6dae42f8-4368-4678-94ff-3960e28e3630|

This is an example of using the [federated workload login flow](https://github.com/Azure/kubelogin#azure-workload-federated-identity-non-interactive).  The federated token file needs to be mounted as a secret into argoCD, so it can be used in the flow.  The location of the token file needs to be set in the environment variable AZURE_FEDERATED_TOKEN_FILE.

If your AKS cluster utilizes the [Mutating Admission Webhook](https://azure.github.io/azure-workload-identity/docs/installation/mutating-admission-webhook.html) from the Azure Workload Identity project, follow these steps to enable the `argocd-application-controller` and `argocd-server` pods to use the federated identity:

1. **Label the Pods**: Add the `azure.workload.identity/use: "true"` label to the `argocd-application-controller` and `argocd-server` pods.

2. **Create Federated Identity Credential**: Generate an Azure federated identity credential for the `argocd-application-controller` and `argocd-server` service accounts. Refer to the [Federated Identity Credential](https://azure.github.io/azure-workload-identity/docs/topics/federated-identity-credential.html) documentation for detailed instructions.

3. **Add Annotations to Service Account** Add `"azure.workload.identity/client-id": "$CLIENT_ID"` and `"azure.workload.identity/tenant-id": "$TENANT_ID"` annotations to the `argocd-application-controller` and `argocd-server` service accounts using the details from the federated credential.

4. **Set the AZURE_CLIENT_ID**: Update the `AZURE_CLIENT_ID` in the cluster secret to match the client id of the newly created federated identity credential.


```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mycluster-secret
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: mycluster.example.com
  server: https://mycluster.example.com
  config: |
    {
      "execProviderConfig": {
        "command": "argocd-k8s-auth",
        "env": {
          "AAD_ENVIRONMENT_NAME": "AzurePublicCloud",
          "AZURE_CLIENT_ID": "fill in client id",
          "AZURE_TENANT_ID": "fill in tenant id", # optional, injected by workload identity mutating admission webhook if enabled
          "AZURE_FEDERATED_TOKEN_FILE": "/opt/path/to/federated_file.json", # optional, injected by workload identity mutating admission webhook if enabled
          "AZURE_AUTHORITY_HOST": "https://login.microsoftonline.com/", # optional, injected by workload identity mutating admission webhook if enabled
          "AAD_LOGIN_METHOD": "workloadidentity"
        },
        "args": ["azure"],
        "apiVersion": "client.authentication.k8s.io/v1beta1"
      },
      "tlsClientConfig": {
        "insecure": false,
        "caData": "<base64 encoded certificate>"
      }
    }
```

This is an example of using the spn (service principal name) flow.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mycluster-secret
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: mycluster.example.com
  server: https://mycluster.example.com
  config: |
    {
      "execProviderConfig": {
        "command": "argocd-k8s-auth",
        "env": {
          "AAD_ENVIRONMENT_NAME": "AzurePublicCloud",
          "AZURE_CLIENT_SECRET": "fill in your service principal client secret",
          "AZURE_TENANT_ID": "fill in tenant id",
          "AZURE_CLIENT_ID": "fill in your service principal client id",
          "AAD_LOGIN_METHOD": "spn"
        },
        "args": ["azure"],
        "apiVersion": "client.authentication.k8s.io/v1beta1"
      },
      "tlsClientConfig": {
        "insecure": false,
        "caData": "<base64 encoded certificate>"
      }
    }
```
