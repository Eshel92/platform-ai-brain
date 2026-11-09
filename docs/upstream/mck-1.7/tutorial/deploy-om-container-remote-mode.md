<!-- Converted from tutorial/deploy-om-container-remote-mode.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Configure an Ops Manager Resource to use Remote Mode

In a default configuration, the MongoDB Agent\'s and Backup Daemons
access MongoDB installation archives over the Internet from MongoDB, Inc.

You can configure Ops Manager to run in **Remote Mode** so that the Backup 
Daemons and managed MongoDB resources download installation archives 
only from Ops Manager, which proxies download requests to an HTTP endpoint 
on a local web server or S3-compatible store deployed to your Kubernetes 
cluster.

## Prerequisites and Considerations

deploy-om-container.

## Procedure

The following procedure deploys an Nginx HTTP server to your Kubernetes 
cluster to host the MongoDB installation archives.

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

**Step 2: Create a [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) for Nginx.**

The ConfigMap in this tutorial configures Nginx to: 

- Run an HTTP server named `localhost` listening on port `80` on a
  node in your Kubernetes cluster, and 
- Route HTTP requests for specific resources to locations that serve
  the the MongoDB Server and MongoDB Database Tools installation
  archives.

a. Paste the following example Nginx ConfigMap into a text editor:

   ```yaml
   ---
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: nginx-conf
   data:
     nginx.conf: |
       events {}
       http {
         server {
           server_name localhost;
           listen 80;
           location /linux/ {
             alias /mongodb-ops-manager/mongodb-releases/linux/;
           }
           location /tools/ {
             alias /tools/;
           }
         }
       }
   ...
   ```

#. Save this file with a `.yaml` file extension.

#. Create the Nginx ConfigMap by invoking the following
   `kubectl` command on the ConfigMap file you created:

   ```sh
   kubectl apply -f <nginix-configmap>.yaml
   ```

**Step 3: Deploy Nginx to your Kubernetes cluster.**

The Nginx resource configuration in this tutorial:

- Deploys one Nginx replica,
- Creates volume mounts to store MongoDB Server and MongoDB Database
  Tools installation archives, and
- Defines `init containers` that use `curl`
  commands to download the installation archives that Nginx serves to
  MongoDB Database resources you deploy in your Kubernetes cluster.

**k8s:**

a. Paste the following example Nginx resource configuration
   into a text editor: 

   ```yaml
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx-deployment
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         labels:
           app: nginx
       spec:
         containers:
           - image: nginx:1.14.2
             imagePullPolicy: IfNotPresent
             name: nginx
             ports:
               - containerPort: 80
             volumeMounts:
               - mountPath: /mongodb-ops-manager/mongodb-releases/linux
                 name: mongodb-versions
               - mountPath: /tools/db/
                 name: mongodb-tools
               - name: nginx-conf
                 mountPath: /etc/nginx/nginx.conf
                 subPath: nginx.conf
         initContainers:
           - name: setting-up-rhel-mongodb
             image: curlimages/curl:latest
             command:
               - curl
               - -L
               - https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel80-8.0.0.tgz
               - -o
               - /mongodb-ops-manager/mongodb-releases/linux/mongodb-linux-x86_64-rhel80-8.0.0.tgz
             volumeMounts:
               - name: mongodb-versions
                 mountPath: /mongodb-ops-manager/mongodb-releases/linux
           - name: setting-up-rhel-mongodb-tools
             image: curlimages/curl:latest
             command:
               - curl
               - -L
               - https://fastdl.mongodb.org/tools/db/mongodb-database-tools-rhel80-x86_64-100.6.0.tgz
               - -o
               - /tools/db/mongodb-database-tools-rhel80-x86_64-100.6.0.tgz
             volumeMounts:
               - name: mongodb-tools
                 mountPath: /tools/db/
         restartPolicy: Always
         terminationGracePeriodSeconds: 30
         volumes:
           - name: mongodb-versions
             emptyDir: {}
           - name: mongodb-tools
             emptyDir: {}
           - configMap:
               name: nginx-conf
             name: nginx-conf
   ...
   ```

#. Modify the lines highlighted in the example to specify the
   MongoDB Server versions that you want to install. 

   For example, to replace MongoDB version `8.0.0` with
   a different database version, update the following block:

   ```yaml
   - name: setting-up-rhel-mongodb
     image: curlimages/curl:latest
     command:
       - curl
       - -L
       - https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel80-8.0.0.tgz
       - -o
       - /mongodb-ops-manager/mongodb-releases/linux/mongodb-linux-x86_64-rhel80-8.0.0.tgz
   ```

   Update this block to modify the MongoDB Database Tools
   version:

   ```yaml
   - name: setting-up-rhel-mongodb-tools
     image: curlimages/curl:latest
     command:
       - curl
       - -L
       - https://fastdl.mongodb.org/tools/db/mongodb-database-tools-rhel80-x86_64-100.6.0.tgz
       - -o
       - /tools/db/mongodb-database-tools-rhel80-x86_64-100.6.0.tgz
   ```

#. To load multiple versions, append `curl` commands
    to the appropriate initContainer for each version you want
    Nginx to serve. 

    For example, to configure Nginx to serve MongoDB `8.0.0`:

    ```yaml
    - name: setting-up-rhel-mongodb
      image: curlimages/curl:latest
      command:
        - curl
        - -L
        - https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel80-8.0.0.tgz
        - -o
        - /mongodb-ops-manager/mongodb-releases/linux/mongodb-linux-x86_64-rhel80-8.0.0.tgz
    ```

#. Save this file with a `.yaml` file extension.

#. Deploy Nginx by invoking the following `kubectl`
   command on the Nginx resource file you created:

   ```sh
   kubectl apply -f <nginix>.yaml
   ```

**os:**

a. Paste the following example Nginx resource configuration
   into a text editor: 

   ```yaml
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx-deployment
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         labels:
           app: nginx
       spec:
         containers:
           - image: nginx:1.14.2
             imagePullPolicy: IfNotPresent
             name: nginx
             ports:
               - containerPort: 80
             volumeMounts:
               - mountPath: /mongodb-ops-manager/mongodb-releases/linux
                 name: mongodb-versions
               - mountPath: /tools/db/
                 name: mongodb-tools
               - name: nginx-conf
                 mountPath: /etc/nginx/nginx.conf
                 subPath: nginx.conf
         initContainers:
           - name: setting-up-rhel-mongodb
             image: curlimages/curl:latest
             command:
               - curl
               - -L
               - https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel<version>-8.0.0.tgz
               - -o
               - /mongodb-ops-manager/mongodb-releases/linux/mongodb-linux-x86_64-rhel<version>-8.0.0.tgz
             volumeMounts:
               - name: mongodb-versions
                 mountPath: /mongodb-ops-manager/mongodb-releases/linux
           - name: setting-up-rhel-mongodb-tools
             image: curlimages/curl:latest
             command:
               - curl
               - -L
               - https://fastdl.mongodb.org/tools/db/mongodb-database-tools-rhel<version>-x86_64-100.1.0.tgz
               - -o
               - /tools/db/mongodb-database-tools-rhel<version>-x86_64-100.1.0.tgz
             volumeMounts:
               - name: mongodb-tools
                 mountPath: /tools/db/
         restartPolicy: Always
         terminationGracePeriodSeconds: 30
         volumes:
           - name: mongodb-versions
             emptyDir: {}
           - name: mongodb-tools
             emptyDir: {}
           - configMap:
               name: nginx-conf
             name: nginx-conf
   ...
   ```

#. Modify the lines highlighted in the example to specify the
   MongoDB Server versions that you want to install. 

   For example, to replace MongoDB version `8.0.0` with
   a different database version, update the following block:

   ```yaml
   - name: setting-up-rhel-mongodb
     image: curlimages/curl:latest
     command:
       - curl
       - -L
       - https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel<version>-8.0.0.tgz
       - -o
       - /mongodb-ops-manager/mongodb-releases/linux/mongodb-linux-x86_64-rhel<version>-8.0.0.tgz
   ```

   Update this block to modify the MongoDB Database Tools
   version:

   ```yaml
   - name: setting-up-rhel-mongodb-tools
     image: curlimages/curl:latest
     command:
       - curl
       - -L
       - https://fastdl.mongodb.org/tools/db/mongodb-database-tools-rhel<version>-x86_64-100.1.0.tgz
       - -o
       - /tools/db/mongodb-database-tools-rhel<version>-x86_64-100.1.0.tgz
   ```

#. To load multiple versions, append `curl` commands
   to the appropriate initContainer for each version you want
   Nginx to serve.

   For example, to configure Nginx to serve MongoDB `8.0.0`:

   ```yaml
   - name: setting-up-rhel-mongodb
     image: curlimages/curl:latest
     command:
       - curl
       - -L
       - https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel80-8.0.0.tgz
       - -o
       - /mongodb-ops-manager/mongodb-releases/linux/mongodb-linux-x86_64-rhel80-8.0.0.tgz
   ```

#. Save this file with a `.yaml` file extension.

#. Deploy Nginx by invoking the following `oc`
   command on the Nginx resource file you created:

   ```sh
   oc apply -f <nginix>.yaml
   ```

**Step 4: Create a Kubernetes service to make Nginx accessible from other pods in your cluster.**

The service in this tutorial exposes Nginx to traffic from other nodes
in your Kubernetes cluster over port `80`. This allows the MongoDB
Database resource pods you deploy using the Kubernetes Operator to download
the installation archives from Nginx.

Run the following command to create a service your Nginx deployment:

a. Paste the following example service into a text editor:

   ```yaml
   ---
   apiVersion: v1
   kind: Service
   metadata:
    name: nginx-svc
    labels:
      app: nginx
   spec:
    ports:
    - port: 80
      protocol: TCP
    selector:
      app: nginx
   ...
   ```

#. Save this file with a `.yaml` file extension.

#. Create the service by invoking the following
   `kubectl` command on the service file you created:

   ```sh
   kubectl apply -f <nginix-service>.yaml
   ```

**Step 5: Copy and update the highlighted fields of this Ops Manager resource.**

The highlighted section uses the following Ops Manager configuration
settings:  

- `automation.versions.source: remote` in 
  `spec.configuration` to enable Remote Mode.

- `automation.versions.download.baseUrl` in
  `spec.configuration` to provide the base URL of the
  HTTP resources that serve the MongoDB installation archives.

  Update this line to replace `<namespace>` with the namespace to 
  which you deploy resources with the Kubernetes Operator.

- ``automation.versions.download.baseUrl.allowOnlyAvailableBuilds: 
  "false"`` in `spec.configuration` to help ensure 
  enterprise builds have no issues.

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDBOpsManager
metadata:
 name: ops-manager-localmode
spec:
 replicas: 1
 version: "8.0.0"
 adminCredentials: ops-manager-admin-secret
 configuration:
   # this enables remote mode in Ops Manager
   automation.versions.source: remote
   automation.versions.download.baseUrl: "http://nginx-svc.<namespace>.svc.cluster.local:8080"
   automation.versions.download.baseUrl.allowOnlyAvailableBuilds: "false"

 backup:
   enabled: false

 applicationDatabase:
   members: 3
...
```

**Step 6: Paste the copied example section into your existing Ops Manager resource.**

Open your preferred text editor and paste the [object](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)
specification into the appropriate location in your resource file.

**Step 7: Save your Ops Manager config file.**

**Step 8: Apply changes to your Ops Manager deployment.**

Invoke the following `kubectl` command on the filename of the
Ops Manager resource  definition:

```sh
kubectl apply -f <opsmgr-resource>.yaml
```

**Step 9: Track the status of your Ops Manager instance.**

To check the status of your Ops Manager resource, invoke the following
command:

```sh
kubectl get om -o yaml -w
```

See /reference/troubleshooting for information about the
resource deployment statuses.

After the Ops Manager resource completes the `Pending` phase, the 
command returns output similar to the following:

```yaml
status:
  applicationDatabase:
    lastTransition: "2020-05-15T16:20:22Z"
    members: 3
    phase: Running
    type: ReplicaSet
    version: "8.0.0-ubi8"
  backup:
    phase: ""
  opsManager:
    lastTransition: "2020-05-15T16:20:26Z"
    phase: Running
    replicas: 1
    url: http://ops-manager-localmode-svc.mongodb.svc.cluster.local:8080
    version: "8.0.0"
```

Copy the value of the `status.opsManager.url` field, which states 
the resource's connection URL (Uniform Resource Locator). You use this value when you create a
[ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) later in the procedure.

**Step 10: Deploy a MongoDB Database Resource.**

a. If you have not done so already, complete the following 
   prerequisites:

   - /tutorial/create-operator-credentials
   - /tutorial/create-project-using-configmap

#. Deploy a MongoDB Database resource 
   in the same namespace to which you deployed Ops Manager. 
   Ensure that you:

   i. Match the `spec.opsManager.configMapRef.name` of the resource 
      to the `metadata.name` of your ConfigMap.
   #. Match the `spec.credentials` of the resource to the name of 
      the secret you created that contains an Ops Manager programmatic 
      API key pair.

MongoDB Agent\'s running in MongoDB database resource containers that
you create with the Kubernetes Operator download the installation archives
from Ops Manager via Nginx instead of from the Internet.
