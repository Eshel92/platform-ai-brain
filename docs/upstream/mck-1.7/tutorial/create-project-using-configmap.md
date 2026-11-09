<!-- Converted from tutorial/create-project-using-configmap.txt (reStructuredText). Includes are inlined. -->

# Create One Project Per MongoDB Deployment Using a ConfigMap

The MongoDB Controllers for Kubernetes Operator uses a Kubernetes [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) to link to a single and unique
Ops Manager `Project`. If the 
referenced project doesn't exist, the Kubernetes Operator creates it 
according to the `projectName` that you provide in the ConfigMap.

To create a Kubernetes Operator ConfigMap, you can edit a few lines of the
example ConfigMap YAML (Yet Another Markup Language) file and apply
the ConfigMap. To view a full example, see the project.yaml file.

Alternatively, you can use the MongoDB Cloud Manager `UI` or the Ops Manager 
`UI` to create or 
choose a project, and automatically generate the ConfigMap YAML file, 
which you can then apply to your Kubernetes environment. 

## Considerations

1. You can deploy only one MongoDB resource per project. This limit 
   applies because Ops Manager supports only one authentication method for 
   database user access per project. To learn more, see 
   k8s-deploy-mdb-resources.

2. You must pair a MongoDB Controllers for Kubernetes Operator deployment to a unique
   Ops Manager `Project`. 
   You can either create a distinct ConfigMap for each MongoDB Controllers for Kubernetes Operator instance
   you deploy, or you can reuse the same ConfigMap for any number of deployments
   by omitting the `data.projectName` from your ConfigMap, so that
   project names align with deployed resource names. Where a project name is 
   provided in the config map, if that project does not 
   exist yet it will be created.

**Important:**

- You can use the Kubernetes Operator to deploy MongoDB resources with
  Cloud Manager and with Ops Manager version 6.0.x or later.

- You can use the Atlas Operator
  to deploy MongoDB resources to Atlas.

## Prerequisites

- Kubernetes version 1.11 or later or Openshift version
  3.11 or later.
- MongoDB Controllers for Kubernetes Operator
  installed.

## Create One Project Using a ConfigMap

**Step 1: Configure `kubectl` to default to your namespace.**

If you have not already, run the following command to execute all 
`kubectl` commands in the namespace you created.

**Note:**

If you are deploying an Ops Manager resource in a multi-Kubernetes cluster MongoDB deployment:

- Set the `context` to the name of the central cluster, such as:
  `kubectl config set context "$MDB_CENTRAL_CLUSTER_FULL_NAME"`.

- Set the `--namespace` to the same scope
  that you used for your multi-Kubernetes cluster MongoDB deployment, such as: `kubectl config --namespace "mongodb"`.

```sh
kubectl config set-context $(kubectl config current-context) --namespace=<metadata.namespace>
```

**Step 2: Invoke the following command to create a ConfigMap.**

```sh
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-project
  namespace: mongodb
data:
  projectName: myProjectName # this is an optional parameter; when omitted, the Operator creates a project with the resource name
  orgId: 5b890e0feacf0b76ff3e7183 # this is a required parameter
  baseUrl: https://ops.example.com:8443

EOF
```

| Key | Type | Description | Example |
|---|---|---|---|
| `metadata.name` | string | Name of the Kubernetes [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/). Resource names must be 44 characters or less. This name must follow RFC1123 naming conventions, containing only lowercase alphanumeric characters or `-` , and starting and ending with an alphanumeric character. To learn more, see Kubernetes documentation on [names](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/). | `my-project` |
| `metadata.namespace` | string | Kubernetes [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) where the Kubernetes Operator creates this `MongoDB` resource and other [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/). | `mongodb` |
| `data.projectName` | string | Label for your `Ops Manager` `Project`. The Kubernetes Operator creates the `Ops Manager` project if it does not exist. If you omit the `projectName`, the Kubernetes Operator creates a project with the same name as your Kubernetes resource. To use an existing project in a Cloud Manager or Ops Manager organization, locate the `projectName` by clicking the All Clusters link at the top left of the Cloud Manager or Ops Manager page, and searching by name in the Search box, or scrolling to find the name in the list. Each card in this list represents the combination of one Cloud Manager or Ops Manager **Organization** and **Project**. | `myProjectName` |
| `data.orgId` | string | *Required*. 24 character hex string that uniquely identifies your Cloud Manager or Ops Manager `Organization`. You can use the Kubernetes Operator to deploy MongoDB resources with Cloud Manager and with Ops Manager version 6.0.x or later. You can use the Atlas Operator to deploy MongoDB resources to Atlas. Specify an `existing Organization`: a. Find the organization's ID. Click Settings in the left navigation bar. #. Copy and paste the orgId into the URL. Select your organization, view the current URL (Uniform Resource Locator) in your browser and copy the value displayed in the `<orgId>` placeholder as follows: `https://ops.example.com:8443/` `v2#/org/<orgId>/projects` You must have the `Organization Project Creator` role to create a new project within an existing Cloud Manager or Ops Manager organization. If you provide an empty string as your `orgId`, Kubernetes Operator creates an organization with the same name as your project. | `5b890e0feacf0b76ff3e7183` |
| `data.baseUrl` | string | URL (Uniform Resource Locator) to your Ops Manager Application including the FQDN (fully qualified domain name) and port number. IMPORTANT: If you deploy Ops Manager with the Kubernetes Operator and Ops Manager will manage MongoDB database resources deployed **outside** of the Kubernetes cluster it's deployed to, you must set `data.baseUrl` to the same value of the `spec.configuration.mms.centralUrl` setting in the Ops Manager resource specification. To learn more, see mdb-resource-deployment-locations. If you're using Cloud Manager, set the `data.baseUrl` value to `https://cloud.mongodb.com`. | `https://ops.example.com:8443` |

**Step 3: Invoke the following Kubernetes command to verify your [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/).**

```sh
kubectl describe configmaps <configmap-name>
```

This command returns a ConfigMap description in the shell:

```sh
Name:           <configmap-name>
Namespace:      <namespace>
Labels:         <none>
Annotations:    <none>

Data
====
baseUrl:
----
<myOpsManagerURL>
Events:  <none>
```

## Connect to HTTPS-enabled Ops Manager Using a Custom CA

You might have chosen to use your own TLS (Transport Layer Security) certificate to enable
HTTPS (Hypertext Transfer Protocol Secure) for your Ops Manager instance. If you used a custom certificate,
you need to add the CA that signed that custom certificate to the
Kubernetes Operator. To add your custom CA, complete the following:

**Step 1: Create a ConfigMap for the certificate authority (CA) certificate.**

The Kubernetes Operator requires the root CA (Certificate Authority) certificate of the
CA (Certificate Authority) that issued the `Ops Manager` host's certificate. Run the following
command to create a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) containing the root CA (Certificate Authority) in the
same namespace of your database Pods:

```sh
kubectl -n <metadata.namespace> create configmap <root-ca-configmap-name> \
  --from-file=mms-ca.crt
```

**Important:**

The Kubernetes Operator requires that you name the Ops Manager resource's
certificate `mms-ca.crt` in the ConfigMap.

**Step 2: Copy the highlighted section of the following example `ConfigMap`.**

```yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: <my-configmap>
  namespace: <my-namespace>
data:
  projectName: <my-ops-manager-project-name> # this is an optional parameter
  orgId: <org-id> # this is a required parameter
  baseUrl: https://<my-ops-manager-URL>
```

```yaml
  sslMMSCAConfigMap: <root-ca-configmap-name>
  sslRequireValidMMSServerCertificates: ‘true’
...
```

**Step 3: Add the highlighted section to your project's ConfigMap.**

a. Invoke the following command to edit your project's ConfigMap in
   the default configured editor:

   ```sh
   kubectl edit configmaps <my-configmap> -n <metadata.namespace>
   ```

b. Paste the highlighted section in the example [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) at
   the end of the project ConfigMap.

**Step 4: Specify the TLS settings**

Change the following TLS (Transport Layer Security) keys:

| Key | Type | Description | Example |
|---|---|---|---|
| `sslMMSCAConfigMap` | string | Name of the [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) created in the first step containing the root CA (Certificate Authority) certificate used to sign the Ops Manager host's certificate. This mounts the CA certificate to the Kubernetes Operator and database resources. | `my-root-ca` |
| `sslRequireValidMMSServerCertificates` | boolean | Forces the Operator to require a valid TLS (Transport Layer Security) certificate from `Ops Manager`. IMPORTANT: The value must be enclosed in single quotes or the operator will throw an error. | `'true'` |

**Step 5: Save your updated ConfigMap.**

**Step 6: Invoke the Kubernetes command to verify your [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/).**

```sh
kubectl describe configmaps <my-configmap> -n <metadata.namespace>
```

**Important:**

Always include the namespace option with `kubectl`.
[kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) defaults to an empty namespace if you don't specify the
`-n` option, resulting in deployment failures. You must specify
the value of the `<metadata.namespace>` field. The
Kubernetes Operator, [secret](https://kubernetes.io/docs/concepts/configuration/secret/), and `MongoDB` resource\s should run in the
same unique namespace.

This command returns a ConfigMap description in the shell:

```sh
Name:           <my-configmap>
Namespace:      <namespace>
Labels:         <none>
Annotations:    <none>

Data
====
sslMMSCAConfigMap:
----
<root-ca-configmap-name>
sslRequireValidMMSServerCertificates:
----
true
Events:  <none>
```

## Next Steps

Now that you created your ConfigMap, create-k8s-secret before
you start deploying MongoDB resources.
