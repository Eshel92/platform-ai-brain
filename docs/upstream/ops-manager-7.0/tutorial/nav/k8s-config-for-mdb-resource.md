<!-- Converted from tutorial/nav/k8s-config-for-mdb-resource.txt (reStructuredText). Includes are inlined. -->

# Configure Kubernetes for Deploying MongoDB Resource

You can use the MongoDB Enterprise Kubernetes Operator to deploy MongoDB resources such as 
`a replica set`, `a sharded 
cluster`, or `a standalone 
instance` using an [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/). 
Ops Manager can generate the YAML files you need to configure your Kubernetes
environment for deploying a MongoDB Database resource.

To generate the YAML files:

- k8s-config-mdb-res-roles
- Learn about the MongoDB Resource in Kubernetes
- k8s-config-mdb-res-create-procedure

## Verify Permissions

You must have one of the following roles to access the Ops Manager UI for 
setting up Kubernetes:

- `Organization Owner`
- `Project Owner`
- `Project Data Access Admin`

## Overview of MongoDB Resource in Kubernetes

To create or link your Ops Manager project, the MongoDB Enterprise Kubernetes Operator requires that you
configure a Kubernetes ConfigMap. Using the Kubernetes ConfigMap, you can:

- Connect to a HTTPS-enabled Ops Manager that is using a custom Certificate Authority, or
- Link to a Ops Manager project that isn't using a custom Certificate Authority.

You can use the Ops Manager Kubernetes Setup page to automatically
generate the ConfigMap. The generated YAML file for the ConfigMap looks
similar to the following: 

**connect:**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-project
  namespace: mongodb
data:
  baseUrl: https://cloud.mongodb.com

  # Optional Parameters
  # projectName: <your-project-name>

  orgId: <your-org-id>

  sslMMSCAConfigMap: <root-ca-configmap-name>
  sslRequireValidMMSServerCertificates: 'true'
```

**link:**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-project
  namespace: mongodb
data:
  baseUrl: https://cloud.mongodb.com

  # Optional Parameters
  # projectName: <your-project-name>

  orgId: <your-org-id>
```

To create or update [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in your Ops Manager project, configure your
Programmatic API Key as a Kubernetes secret.
The secret stores authentication credentials so only Kubernetes can access them.

The following procedures provide the detailed steps.

## Procedures

- k8s-config-mdb-res-nav
- k8s-setup-custom-ca-configmap-om-settings
- k8s-generate-yaml

### Navigate to the Kubernetes Setup Page in the Ops Manager UI

To access the Kubernetes Setup page in the Ops Manager UI: 

**Step 1: Log in to Ops Manager and select the organization that contains your project from the `office` Organizations menu in the navigation bar.**

**Step 2: Select your project from the Project menu in the navigation bar.**

**Step 3: Click the Add dropdown and select Prepare Kubernetes Configuration to display the Kubernetes Setup page.**

If you are a `Global Owner` or `Organization 
Owner`, you can also access the Kubernetes Setup page in
the Ops Manager UI by following these steps:

**Step 1: Log in to Ops Manager and select your organization from the `office` Organizations menu in the navigation bar.**

**Step 2: Click Kubernetes Setup in the sidebar or the navigation bar.**

### Create a Secret, a ConfigMap, and Ops Manager Settings for Kubernetes

To create a secret, a ConfigMap file, and Ops Manager settings for Kubernetes:

**Step 1: Create a secret file with your API keys.**

Create a YAML file that contains your Programmatic API Key in the `/mongodb-ops-manager/` folder.

**Step 2: Create a ConfigMap to link to your Ops Manager instance.**

Create a YAML file that contains the ConfigMap to connect to your 
HTTPS (Hypertext Transfer Protocol Secure)\-enabled Ops Manager instance in the `/mongodb-ops-manager/` 
folder.

**Step 3: Configure the Ops Manager settings for Kubernetes.**

In your server's `conf-mms.properties` file, configure the 
following settings:

- `kubernetes.templates.credentialsFilePath`. Path to the YAML file
  that contains the ConfigMap to use to link to your Ops Manager project.
  This file must be in YAML format and must be stored under the
  `/mongodb-ops-manager/` directory. The file corresponds to
  `Kubernetes ConfigMap Setup`.

- `kubernetes.templates.projectFilePath`. Path to the YAML file that
  contains your Programmatic API Key as a
  Kubernetes secret to create or update [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in your Ops Manager project.
  This file must be in YAML format and must be stored under the
  `/mongodb-ops-manager/` directory. The file corresponds to
  `Kubernetes Secret Setup`.

To learn more, see conf-mms.properties-k8s.

### Generate the ConfigMap YAML Files

To generate the Kubernetes configuration files for a MongoDB resource:

**connect:**

**Step 1: In the Kubernetes Setup page, toggle the switch for Configure HTTPS-enabled Ops Manager Using a Custom CA from OFF to ON to generate a ConfigMap for HTTPS-enabled Ops Manager that is using a custom CA.**

**Step 2: In the CA ConfigMap Name field, enter the name of your ConfigMap containing the root CA certificate in the same namespace as your database pods.**

**Step 3: Select the Require Valid Server Certificate checkbox to force the MongoDB Enterprise Kubernetes Operator to require a valid TLS (Transport Layer Security) certificate from Ops Manager.**

**Step 4: Specify the API keys for accessing your Ops Manager project.**

- Click Create New API Keys to generate new API keys.
- Click Use Existing API Keys to specify your existing 
  public and private keys.

**Step 5: Enter the IP addresses to add to your Ops Manager project's IP access list to grant programmatic access from your Kubernetes environment.**

If you disabled the `mms.publicApi.whitelistEnabled` setting in 
your Ops Manager configuration, the 
Access List Entry field is not visible in the UI. 

**Step 6: Generate ConfigMap and Kubernetes secret YAML files.**

To generate the ConfigMap and Kubernetes secret YAML files:

- Click Generate Key and YAML if you are generating new 
  API keys.
- Click Generate YAML if you are using existing API keys.

**Step 7: Follow the steps in the Generated ConfigMap and Secret YAML file modal to apply the generated ConfigMap and Kubernetes secret YAML files to your Kubernetes environment.**

**link:**

**Step 1: Specify the API keys for accessing your Ops Manager project.**

- Click Create New API Keys to generate new API keys.
- Click Use Existing API Keys to specify your existing 
  public and private keys.

**Step 2: Enter the IP addresses to add to your Ops Manager project's IP access list to grant programmatic access from your Kubernetes environment.**

If you disabled the `mms.publicApi.whitelistEnabled` setting in 
your Ops Manager configuration, the 
Access List Entry field is not visible in the UI. 

**Step 3: Generate ConfigMap and Kubernetes secret YAML files.**

To generate the ConfigMap and Kubernetes secret YAML files:

- Click Generate Key and YAML if you are generating new 
  API keys.
- Click Generate YAML if you are using existing API keys.

**Step 4: Follow the steps in the Generated ConfigMap and Secret YAML file modal to apply the generated ConfigMap and Kubernetes secret YAML files to your Kubernetes environment.**
