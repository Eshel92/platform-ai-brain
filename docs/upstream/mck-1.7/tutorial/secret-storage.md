<!-- Converted from tutorial/secret-storage.txt (reStructuredText). Includes are inlined. -->

# Configure Secret Storage

You can choose the secret storage tool for Kubernetes Operator. The secret
storage tool is a secure place to store sensitive information for the components
that Kubernetes Operator manages. This includes secrets for MongoDB databases, Ops Manager, and AppDB.

Once you configure secret storage, Kubernetes Operator accesses the tool, retrieves
the secrets, and uses them to establish connections securely.

## Supported Secret Storage Tools

Kubernetes Operator supports the following secret storage tools:

- Kubernetes: store sensitive information as [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) (the built-in secret
  storage for Kubernetes). Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
  store authentication credentials so that only Kubernetes can access them.
- [HashiCorp Vault](https://www.vaultproject.io/): store sensitive information in Vault, a third
  party service for secret management.
  

## Secrets You Can Store

You can use any supported secret storage tool for any secret in the MongoDB Controllers for Kubernetes Operator
documentation except those listed in the limitations. 

**Important:**

After configuration, Kubernetes Operator uses your selected secret storage tool
for **all** secrets except those listed in the limitations.
You can't mix and match secret storage tools.

## Limitations

The following limitations exist for the supported secret storage tools:

- Some registries, such as OpenShift, require imagePullSecrets
  to pull images from the repository. The Kubernetes Operator can't provide imagePullSecrets from
  [HashiCorp Vault](https://www.vaultproject.io/). You can `specify a kubelet image credential provider`
  to retrieve credentials for a container image registry using Kubernetes instead.

## Set the Secret Storage Tool

To set the secret storage tool, select one of the following options:

**usek8s:**

All tutorials in this MongoDB Controllers for Kubernetes Operator documentation use Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) by default.
To use Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) to store secrets for the Kubernetes Operator, proceed with
installation of the Kubernetes Operator and follow the steps in the tutorials.

**usevault:**

To use [HashiCorp Vault](https://www.vaultproject.io/) to store secrets for the
Kubernetes Operator, complete the following procedure.

### Prerequisites

Before you begin, you must:

- Set up a Vault instance. The Kubernetes cluster where the
  Kubernetes Operator is running must have access to the Vault
  instance.

  **Note:**

  Ensure that Vault is **not** running in [dev mode](https://www.vaultproject.io/docs/concepts/dev-server) 
  and that your Vault installation follows any applicable
  [configuration recommendations](https://learn.hashicorp.com/tutorials/vault/production-hardening).

- Enable [Kubernetes Authentication](https://www.vaultproject.io/docs/auth/kubernetes)
  for the Vault instance. This allows you to authenticate with
  Vault.
- [Deploy the Vault Agent sidecar injector](https://learn.hashicorp.com/tutorials/vault/kubernetes-sidecar)
  in the Kubernetes cluster. This allows you to inject secrets from
  Vault into your Kubernetes Pods.
- Download the four [Vault policy files](https://github.com/mongodb/mongodb-kubernetes/tree/1.7.0/public/vault_policies)
  for the Kubernetes Operator, MongoDB database, Ops Manager, and AppDB.
- [Create a role](https://developer.hashicorp.com/vault/docs/auth/approle)
  in Vault with the name `mongodbenterprise`. The configuration
  of secrets in the Kubernetes Operator relies on the presence of this
  role and its exact name.

### Procedure

**Step 1: Add the Vault policies for the Kubernetes Operator and its components.**

Write the policies for Kubernetes Operator, MongoDB database, Ops Manager, and AppDB resources
to Vault using the following command, replacing the variables with the values in the table:

| Placeholder | Description |
|---|---|
| {PolicyName} | Human-readable label that identifies the policy you're creating in Vault. |
| {PathToPolicyFile} | The absolute path to the policy file you downloaded. |

```sh
vault policy write {PolicyName} {PathToPolicyFile}
```

Repeat the command for all the resources you're adding to Vault.

**Step 2: Bind the Vault roles to the Vault policies for the Kubernetes Operator and its components.**

Bind Vault roles to the policies for Kubernetes Operator, MongoDB database,
Ops Manager, and AppDB resources using the following four commands, replacing the
variables with the values in the table:

| Placeholder | Description |
|---|---|
| {OperatorPolicyName} | A human-readable label that identifies the Kubernetes Operator policy in Vault. |
| {DatabasePolicyName} | A human-readable label that identifies the MongoDB database policy in Vault. |
| {OpsManagerPolicyName} | A human-readable label that identifies the Ops Manager policy in Vault. |
| {AppDBPolicyName} | A human-readable label that identifies the AppDB policy in Vault. |
| {ServiceAccountNamespace} | Label that identifies the namespace for the service account bound to your pod. |

```sh
vault write auth/kubernetes/role/{OperatorPolicyName}
bound_service_account_names=enterprise-operator bound_service_account_namespaces={ServiceAccountNamespace}
```

```sh
vault write auth/kubernetes/role/{DatabasePolicyName}
bound_service_account_names=mongodb-kubernetes-database-pods bound_service_account_namespaces={ServiceAccountNamespace}   
```

```sh
vault write auth/kubernetes/role/{OpsManagerPolicyName}
bound_service_account_names=mongodb-kubernetes-ops-manager bound_service_account_namespaces={ServiceAccountNamespace}
```

```sh
vault write auth/kubernetes/role/{AppDBPolicyName}
bound_service_account_names=mongodb-kubernetes-appdb bound_service_account_namespaces={ServiceAccountNamespace} 
```

These commands ensure that each component's pods have only the access specified in their
policy.

**Note:**

This step grants the Kubernetes Operator access to
Vault. To use Vault with applications that the
Kubernetes Operator doesn't manage, you must write and bind Vault policies for those
applications.

You can adapt the commands in this step to bind other policies by
replacing the name of the [service accounts](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/). To configure other
applications to use Vault, replace the
{ServiceAccountName} in the following command with the service account used
for the application's pod:

```sh
vault write auth/kubernetes/role/{PolicyName}
bound_service_account_names={ServiceAccountName} bound_service_account_namespaces={ServiceAccountNamespace} 
```

**Step 3: Add the annotations to the Kubernetes deployment file.**

Before running commands in this step, ensure that you have
[created a Vault role](https://developer.hashicorp.com/vault/docs/auth/approle)
with the name `mongodbenterprise`.

Add the following highlighted lines to the `spec.template.metadata.annotations` section of your
Kubernetes Operator deployment file. For most users, this file's name is `mongodb-kubernetes.yaml` or
`mongodb-kubernetes-openshift.yaml`.

**Note:**

If you installed the Kubernetes Operator using Helm and set operator.vaultSecretBackend.enabled
to `true`, the Kubernetes Operator adds the following annotations. You can proceed to the next step.

```sh
apiVersion: apps/v1
kind: Deployment
metadata:
   name: mongodb-kubernetes-operator
   namespace: production
spec:
   replicas: 1
   template:
      metadata:
        annotations:
          vault.hashicorp.com/agent-inject: "true"
          vault.hashicorp.com/role: "mongodbenterprise"
```

If you're running Vault in TLS (Transport Layer Security) mode, and specified the
operator.vaultSecretBackend.tlsSecretRef value,
the Kubernetes Operator adds the following annotations. Otherwise, add the following
highlighted line to the file, replacing `{TLSSecret}` with the name of the secret
containing a `ca.crt` entry. The content of the `ca.crt` entry must match
the certificate of the CA (Certificate Authority) used to generate the Vault TLS certificates.

```sh
        annotations:
          vault.hashicorp.com/agent-inject: "true"
          vault.hashicorp.com/role: "mongodbenterprise"
          vault.hashicorp.com/tls-secret: {TLSSecret}
          vault.hashicorp.com/ca-cert: /vault/tls/ca.crt
```

**Step 4: Define the environment variable in Kubernetes.**

Add the following highlighted lines to the `spec.env` section of your
Kubernetes Operator deployment file. For most users, this file's name is `mongodb-kubernetes.yaml` or
`mongodb-kubernetes-openshift.yaml`.

```sh
apiVersion: apps/v1
kind: Deployment
metadata:
   name: mongodb-kubernetes-operator
   namespace: production
spec:
   env:
   - name: OPERATOR_ENV
     value: ENVIRONMENT_NAME
   - name: SECRET_BACKEND
     value: VAULT_BACKEND
```

This [defines the environment variable](https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/)
for Vault in Kubernetes.

**Step 5: Create a file with the Vault configuration information.**

Using your preferred text editing application, create a file named `config`.
Paste the following text into the file:

```sh
apiVersion: v1
kind: ConfigMap
metadata:
  name: secret-configuration
  namespace: {Namespace}
data:
  VAULT_SERVER_ADDRESS: {VaultServerAddress}
  OPERATOR_SECRET_BASE_PATH: mongodbenterprise/operator
  DATABASE_SECRET_BASE_PATH: mongodbenterprise/database
  OPS_MANAGER_SECRET_BASE_PATH: mongodbenterprise/opsmanager
  APPDB_SECRET_BASE_PATH: mongodbenterprise/appdb
```

The paths in this file are the default paths. You can replace them with your
base paths if you customized your Kubernetes Operator configuration.

If you're running Vault in TLS (Transport Layer Security) mode, you must also add the following
highlighted line to the file:

```sh
   OPS_MANAGER_SECRET_BASE_PATH: mongodbenterprise/opsmanager
   APPDB_SECRET_BASE_PATH: mongodbenterprise/appdb
   TLS_SECRET_REF: {TLSSecret}
```

**Step 6: Replace the placeholders in the Vault configuration information.**

Replace the placeholders in the `config` file with these values. Save
the file with a YAML (Yet Another Markup Language) file type by replacing the `.txt` file extension with
`.yaml`.

| Placeholder | Description |
|---|---|
| {Namespace} | The namespace you created for the Kubernetes Operator. The default namespace is `mongodb`. |
| {VaultServerAddress} | The address that the Kubernetes Operator should use to connect to Vault. |
| {TLSSecret} | Name of a secret containing a `ca.crt` entry. The content of the `ca.crt` entry must match the certificate of the CA (Certificate Authority) used to generate the Vault TLS certificates. |

**Step 7: Create a ConfigMap with the Vault configuration.**

Issue the following command to create a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) containing the Vault information:

```sh
kubectl create configmap secret-configuration --from-file=config.yaml
```

This creates a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) named `secret-configuration`. This
[ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) contains the contents of the `config` file. 

**Step 8: Manually migrate secrets that don't migrate automatically**

You must manually migrate the following secrets to store them in Vault:

- Any existing user-created secrets, including Operator credentials stored as Kubernetes secrets,
  if applicable
- The gen-key secret
  Kubernetes Operator creates
- The Ops Manager admin credentials/admin key
  Kubernetes Operator creates
- TLS secrets

To manually migrate or create new secrets, add them to Vault.  
After you add them to Vault, you can remove them from Kubernetes.

All other secrets that the Kubernetes Operator creates migrate automatically, and Kubernetes Operator uses
Vault for new secrets. User-created secrets must be added to Vault.

**Note:**

cert-manager automatically recreates the Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) that
it generates if you delete them from Kubernetes. You must manually manage the
removal of these secrets or stop using cert-manager to avoid storing
the secrets in Kubernetes.

## Next Steps

After you configure the secret storage tool for the MongoDB Controllers for Kubernetes Operator, you can:

- Read the Considerations.
- Complete the Prerequisites.
- Install the Kubernetes Operator.
