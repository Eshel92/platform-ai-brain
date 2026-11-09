<!-- Converted from tutorial/create-operator-credentials.txt (reStructuredText). Includes are inlined. -->

# Create Credentials for the Kubernetes Operator

For the Kubernetes Operator to create or update [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) in your Cloud Manager or Ops Manager
Project, you need to store your Programmatic API Key in your secret storage tool. 

Multiple secrets can exist in the same namespace. Each user should
have their own secret.

You can follow the create-k8s-secret-procedure below to 
manually store the Programmatic API Key as a Kubernetes [secret](https://kubernetes.io/docs/concepts/configuration/secret/). Alternatively, you can: 

- Use the MongoDB Cloud Manager `UI` or the 
  Ops Manager `UI` to 
  automatically generate the Kubernetes secret YAML file, which you can 
  then apply to your Kubernetes environment.
- Store the Programmatic API Key as a
  Vault secret using the procedure to Create a Vault Secret. 
  To use Vault, you must also configure the secret storage.

## Prerequisites

To create credentials for the Kubernetes Operator, you must:

1. Have or create an Ops Manager
   `Organization`.

#. Have or generate a
   Programmatic API Key.

#. Grant this new Programmatic API Key:

   - The `Organization Owner` or `Global Owner`
     role, if you want the Kubernetes Operator to create projects and manage
     them. 

   - The `Project Owner` role, if you want the Kubernetes Operator
     to only manage projects.

   **Note:**

   You must grant the Programmatic API Key the 
   `Organization Owner` or `Global Owner` role.
   If you want to grant the Programmatic API Key only the `Project Owner` role, you must first create the project and then the
   Programmatic API Key for the project with the `Project Owner`
   role. The Kubernetes Operator can't create projects if the
   Programmatic API Key has only the `Project Owner` role. 

#. Add the IP (Internet Protocol) or CIDR (Classless Inter-Domain Routing) block of any hosts that serve the
   Kubernetes Operator to the
   `API Access List`.

## Procedure

To create your Kubernetes secret:

**Step 1: Create a new Kubernetes secret**

a. Ensure you have the Public and Private Keys for your desired
   Ops Manager Programmatic API Key.

b. Invoke the following Kubernetes command to create your secret:

   ```sh
   kubectl -n <metadata.namespace> \
   create secret generic <mycredentials> \
   --from-literal="publicKey=<publicKey>" \
   --from-literal="privateKey=<privateKey>"
   ```

   The `-n` flag limits the [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) to which this secret applies.
   All MongoDB Kubernetes resources must exist in the same namespace as the
   [secrets](https://kubernetes.io/docs/concepts/configuration/secret/) and [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/). The Kubernetes Operator doesn't use
   either the secrets or ConfigMaps.

   **Note:**

   The deprecated version of this command specifies a `user` and `publicApiKey`
   instead of a `publicKey` and `privateKey`. Kubernetes Operator accepts
   either version for authentication.

**Step 2: Verify your new Kubernetes secret**

Invoke the following Kubernetes command to verify your secret:

```sh
kubectl describe secrets/<mycredentials> -n <metadata.namespace>
```

This command returns a secret description in the shell:

```sh
Name:         <mycredentials>
Namespace:    <metadata.namespace>
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
privateKey:  31 bytes
publicKey:          22 bytes
```
