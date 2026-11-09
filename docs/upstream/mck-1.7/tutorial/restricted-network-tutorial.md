<!-- Converted from tutorial/restricted-network-tutorial.txt (reStructuredText). Includes are inlined. -->

# Deploy in Restricted Networks

This tutorial demonstrates how to deploy the Kubernetes Operator, 
an Ops Manager instance, and a MongoDB replica set using the 
Kubernetes Operator in a restricted network OpenShift environment.

## Procedure

**Step 1: Mirror the Operator catalog and disable the default catalog.**

Red Hat Operator catalogs contain metadata that OLM 
(Operator Lifecycle Manager) queries to install Operators 
and their dependencies on a cluster. You must create a copy of 
the Operator catalog and then disable the default catalog as a 
cluster administrator. 

The `relatedImages` in the operator bundle lists the following 
images:

- Images directly used by the operator, which are the current 
  version of `mongodb-kubernetes-init-database`, 
  `mongodb-kubernetes-init-ops-manager`, 
  `mongodb-kubernetes-init-appdb`, 
  `mongodb-kubernetes-init-database`.
- All currently supported images of Ops Manager, AppDB and 
  `mongodb-agent` that can be configured in an Ops Manager 
  deployment.

For `init` images, use only the version that is present in the
latest Kubernetes Operator version.

The size of all related images referenced by the operator bundle 
is over 26 GB.

Your mirroring command won't pick unsupported versions of the 
AppDB images. If you want to use any other unsupported version, 
you must manually provide these images to the mirror registry. For
other versions for a given operator version, see [image for Deployment](https://github.com/mongodb/mongodb-kubernetes/blob/1.7.0/public/mongodb-kubernetes.yaml).

For the full list of images defined in the `RELATED_IMAGE_*`
environment variables, see the CSV (cluster service versions)
[file](https://github.com/redhat-openshift-ecosystem/certified-operators/blob/main/operators/mongodb-kubernetes/1.7.0/manifests/mongodb-kubernetes.clusterserviceversion.yaml).

a. To mirror, see [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/disconnected_environments/mirroring-in-disconnected-environments#installing-mirroring-disconnected-about).

   When you run the `oc adm catalog mirror` command to mirror the 
   catalog, it generates the `imageContentSourcePolicy.yaml` file, 
   which you must [apply](https://access.redhat.com/documentation/en-us/red_hat_openshift_container_storage/4.5/html/preparing_to_deploy_in_a_disconnected_environment/creating-operator-imagecontentsourcepolicy_rhocs) 
   to remap original source to mirrored images. For example:

   ```shell
   oc apply -f ./<output dir>/imageContentSourcePolicy.yaml
   ```

   For a list of supported MongoDB versions for each Ops Manager version,
   see `Compatible MongoDB Version`. 

#. To disable the default catalog, add 
   `disableAllDefaultSources: true` to the `OperatorHub` object. 

To learn more, see [Using Operator Lifecycle Manager on restricted networks](https://docs.openshift.com/container-platform/latest/operators/admin/olm-restricted-networks.html). 

**Step 2: Install the Kubernetes Operator.**

To learn more, see: 

- plan-k8s-operator-install
- install-k8s

**Step 3: Deploy Ops Manager in Local Mode.**

To deploy Ops Manager in Local Mode, you must do the following:

a. Copy the following example Ops Manager Kubernetes [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) and save it as
   a `.yaml` file. 

   - Use the Ops Manager configuration setting 
     `automation.versions.source: local` in 
     `spec.configuration` to enable Local Mode.

   - Define a [Persistent Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) for the Ops Manager StatefulSet to store the 
     MongoDB installation archive. MongoDB Agent\'s running in MongoDB
     database resource containers that you create with the Kubernetes Operator
     download the installation archives from Ops Manager instead of from the
     Internet.

   ```yaml
   apiVersion: mongodb.com/v1
   kind: MongoDBOpsManager
   metadata:
    name: ops-manager-localmode
   spec:
    replicas: 2
    version: "8.0.0"
    adminCredentials: ops-manager-admin-secret
    configuration:
      # this enables local mode in Ops Manager
      automation.versions.source: local
    statefulSet:
      spec:
        # the Persistent Volume Claim will be created for each Ops Manager Pod
        volumeClaimTemplates:
         - metadata:
             name: mongodb-versions
           spec:
             accessModes: [ "ReadWriteOnce" ]
             resources:
               requests:
                 storage: "20Gi"
      template:
        spec:
          containers:
            - name: mongodb-ops-manager
              volumeMounts:
              - name: mongodb-versions
                # this is the directory in each Pod where all MongoDB
                # archives must be put
                mountPath: /mongodb-ops-manager/mongodb-releases
    backup:
     enabled: false
    applicationDatabase:
     members: 3
     persistent: true
   ```

   To learn more about the settings, see deploy-om-container.

#. Configure `oc` to default to your namespace.

   ```sh
   oc config set-context $(oc config current-context) --namespace=<metadata.namespace>
   ```

#. Copy the following Ops Manager resource settings, paste into 
   your existing Ops Manager resource, and save your Ops Manager config 
   file.

   ```yaml
   configuration:
     # this enables local mode in Ops Manager
     automation.versions.source: local
   statefulSet:
     spec:
       # the Persistent Volume Claim will be created for each Ops Manager Pod
       volumeClaimTemplates:
         - metadata:
           name: mongodb-versions
           spec:
             accessModes: [ "ReadWriteOnce" ]
             resources:
               requests:
                 storage: "20Gi"
     template:
       spec:
         containers:
           - name: mongodb-ops-manager
             volumeMounts:
             - name: mongodb-versions
               # this is the directory in each Pod where all MongoDB
               # archives must be put
               mountPath: /mongodb-ops-manager/mongodb-releases
   ```

#. Copy the MongoDB installation archive to the Ops Manager Persistent 
   Volume.

   To learn how to copy MongoDB installation archive, see step 10 in
   the Configure an Ops Manager Resource to use Local Mode procedure. 

#. Create credentials and store them as a secret.

   Run the following command:

   **Note:**

   Provide your public and private key values for the following 
   parameters. To learn more, see create-k8s-credentials.

   ```sh
   oc \
     create secret generic ops-manager-admin-key \
     --from-literal="publicKey=<publicKey>" \
     --from-literal="privateKey=<privateKey>"
   ```

#. Create a ConfigMap similar to the following:

   ```sh
   cat <<EOF | oc apply -f -
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: my-project
     namespace: mongodb
   data:
     projectName: myProjectName # this is an optional parameter
     orgId: 5b890e0feacf0b76ff3e7183 # this is a required parameter
     baseUrl: https://ops.example.com:8443
   EOF
   ```

   To learn more about the settings in the ConfigMap, see step 7 in 
   the openshift-quick-start-ref.

To learn more about deploying Ops Manager in Local Mode, see 
deploy-om-container-local-mode.

**Step 4: Deploy a MongoDB Database Resource.**

You can deploy-replica-set or a deploy-sharded-cluster. 
To learn more, see k8s-deploy-mdb-resources.
