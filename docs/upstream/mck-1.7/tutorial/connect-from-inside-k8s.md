<!-- Converted from tutorial/connect-from-inside-k8s.txt (reStructuredText). Includes are inlined. -->

# Connect to a MongoDB Database Resource from Inside Kubernetes

The following procedure describes how to connect to a MongoDB resource
deployed by Kubernetes from inside of the Kubernetes cluster.

## Considerations

You must be able to connect to the host and port where you deployed your
Kubernetes resource. To learn more about connecting to your deployment, see
`Connect to a MongoDB Process`.

## Procedure

Retrieve and run the connection command for your deployment. You can retrieve
the connection command from the `Ops Manager` or
`Cloud Manager`
application, depending on where your clusters are hosted. You can also retrieve the connection command from
the Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/) that the Kubernetes Operator creates automatically when you
add a MongoDB user with SCRAM authentication or X509.

The procedure for connecting to a MongoDB Database resource varies based
on how you want to retrieve your connection string:

**UsingTheApplication:**

Perform the following steps in the `Ops Manager` or `Cloud Manager`
application, depending on where your clusters are hosted:

**Step 1: Open the Topology view for your deployment.**

Click Deployment in the left navigation.

**Step 2: Click `ellipsis` for the deployment to which you want to connect.**

**Step 3: Click Connect to this instance.**

**Step 4: Copy the connection command displayed in the Connect to your Deployment dialog.**

**Step 5: Run the connection command in a terminal to connect to the deployment.**

**Example:**

To connect to a sharded cluster resource named
`shardedcluster`, you might use the following connection
string:

```none
mongosh --host shardedcluster-mongos-0.shardedcluster-svc.mongodb.svc.cluster.local \
  --port 27017
```

When connecting to a resource from inside of Kubernetes, the
hostname to which you connect has the following form:

```sh
<k8s-pod-name>.<k8s-internal-service-name>.<k8s-namespace>.<cluster-name>
```

**UsingK8sSecret:**

When you create a new MongoDB database user, Kubernetes Operator automatically
creates a new Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/). The Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/)
contains the following information about the new database user:

- `username`: Username for the database user
- `password`: Password for the database user
- `connectionString.standard`: Standard connection string
  that can connect you to the database as this database user.
- `connectionString.standardSrv`: DNS seed list connection string that can
  connect you to the database as this database user.

**Note:**

Alternatively, you can specify an optional 
`spec.connectionStringSecretName` field in the 
mongodbuser-specification to specify 
the name of the connection string secret that the 
Kubernetes Operator creates.

Perform the following steps to view the credentials and
use the connection string to connect to MongoDB:

**Step 1: Run the command to view the Kubernetes secret file.**

Run the following command in a terminal to view the [secret](https://kubernetes.io/docs/concepts/configuration/secret/), replacing
the variables with the values in the table:

| Placeholder | Description |
|---|---|
| {MongoDB-Resource-Name} | Human-readable label that identifies the MongoDB resource. |
| {User-Name} | Human-readable label that identifies the MongoDB user. |

```none
kubectl get secret {MongoDB-Resource-Name}-{User-Name}-admin -o jsonpath='{.data}'
```

If this command returns an error, you can verify the name of the [secret](https://kubernetes.io/docs/concepts/configuration/secret/) by
running the following command and retrieving the correct name:

```none
kubectl get secrets
```

**Step 2: Copy the `connectionString.standard` value displayed in the Kubernetes secret file.**

**Step 3: Run the connection command.**

Use the `connectionString.standard` value within a connection string
to connect to the deployment.

```none
mongosh {connectionString.standard}
```

**Step 4: (Optional) Mount the Kubernetes secret in your pod.**

You can `mount the secret in your pod`
to ensure that your applications can access the credentials.
