<!-- Converted from tutorial/upgrade-mdb-version.txt (reStructuredText). Includes are inlined. -->

# Upgrade MongoDB Version

You can upgrade the major or minor versions of
your MongoDB resource. Configure these settings in your k8s-specification.

## Overview

To upgrade your resource's major or minor versions, set the
`spec.version` setting to the desired MongoDB version.

**Note:**

If you update this value to a later version of MongoDB for your 
database resources, the feature compatibility version remains 
at the MongoDB version you're upgrading from to give you the option to downgrade if necessary.
If you want the feature compatibility version to match the new MongoDB version, you must manually set 
`spec.featureCompatibilityVersion` to the new version or to `AlwaysMatchVersion`.
To learn more, see `spec.featureCompatibilityVersion`.

## Procedure

To upgrade the standalone deployment's MongoDB version from `8.0.0`
to `8.0.1`, complete the steps in the following example.

**Step 1: Set `spec.version` to the desired MongoDB version.**

```yaml
---
apiVersion: mongodb.com/v1
kind: MongoDB
metadata:
 name: my-standalone-downgrade
spec:
 version: "8.0.1"
 type: Standalone
 project: my-project
 credentials: my-credentials
 persistent: false
...
```

**Step 2: Reapply the configuration to Kubernetes.**

```none
kubectl apply -f <standalone-config>.yaml
```

Kubernetes automatically reconfigures your deployment with the new 
specifications. You can see these changes reflected in your `Ops Manager` or 
`Cloud Manager` application.
