<!-- Converted from tutorial/migrate-k8s-images.txt (reStructuredText). Includes are inlined. -->

# Migrate MongoDB Controllers for Kubernetes Operator from Ubuntu-based Images to UBI-based Images

To migrate MongoDB Controllers for Kubernetes Operator from Ubuntu-based images to UBI-based images, edit
your Kubernetes Operator 
configuration file to pull
images from the appropriate UBI repositories by suffixing the existing
image repository path with `-ubi`. You don't need to perform this
procedure if you are using OpenShift, as you are already using UBI 
images.

The following example compares a default configuration for the 
`INIT_APPDB_IMAGE_REPOSITORY` setting with an updated configuration
that pulls a UBI image.

**Example:**

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: INIT_APPDB_IMAGE_REPOSITORY
              value: quay.io/mongodb/mongodb-kubernetes-init-appdb
```

After adding the necessary suffix, your configuration should match the
configuration below:

```yaml
spec:
  template:
    spec:
      serviceAccountName: mongodb-kubernetes-operator
      containers:
        - name: mongodb-kubernetes-operator
          image: <operatorVersionUrl>
          imagePullPolicy: <policyChoice>
          env:
            - name: INIT_APPDB_IMAGE_REPOSITORY
              value: quay.io/mongodb/mongodb-kubernetes-init-appdb
```

After saving the changes, reapply your configuration file.

For users running vanilla Kubernetes: 

```sh
kubectl apply -f mongodb-kubernetes.yaml
```

For users running OpenShift:

```sh
oc apply -f mongodb-kubernetes-openshift.yaml
```

Repeat this procedure for the following repository 
configurations by applying the same `-ubi` suffix, saving the changes
and reapplying the configuration each time to migrate the images 
separately:

- `AGENT_IMAGE`
- `INIT_DATABASE_IMAGE_REPOSITORY`
- `INIT_OPS_MANAGER_IMAGE_REPOSITORY`
- `MONGODB_ENTERPRISE_DATABASE_IMAGE`
- `OPS_MANAGER_IMAGE_REPOSITORY`
