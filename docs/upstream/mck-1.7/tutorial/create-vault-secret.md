<!-- Converted from tutorial/create-vault-secret.txt (reStructuredText). Includes are inlined. -->

# Create Secrets in Vault

After you set your secret storage tool to
[HashiCorp Vault](https://www.vaultproject.io/), you must also create secrets in Vault. This applies
when you're manually migrating your existing Kubernetes [secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
or you're creating secrets for the first time.

For a list of secrets that you must manually migrate to Vault, see the
Vault section of Configure Secret Storage.

The following tutorial stores your Programmatic API Key in Vault. You can adapt the commands in this
procedure to add other secrets to Vault by changing the base path, the
namespace, and the secret name.

To learn more about secret storage tools, see Configure Secret Storage.

## Prerequisites

To create credentials for the Kubernetes Operator in Vault, you must:

1. Have or create an Ops Manager
   `Organization`.

#. Have or generate a
   Programmatic API Key.

#. Grant this new Programmatic API Key the `Project Owner` role.

#. Add the IP (Internet Protocol) or CIDR (Classless Inter-Domain Routing) block of any hosts that serve the
   Kubernetes Operator to the
   `API Access List`.

#. Set up a Vault instance and [enable Vault](https://www.vaultproject.io/docs/secrets/kv/kv-v2#setup). 

   **Note:**

   Ensure that Vault is **not** running in [dev mode](https://www.vaultproject.io/docs/concepts/dev-server) 
   and that your Vault installation follows any applicable
   [configuration recommendations](https://learn.hashicorp.com/tutorials/vault/production-hardening).

## Procedure

To create your secret in Vault:

**Step 1: Obtain the Ops Manager public and private Keys.**

Make sure you have the public and private keys for your desired
Ops Manager Programmatic API Key.

**Step 2: Create the secret in Vault.**

Invoke the following Vault command to create your secret, replacing
the variables with the values in the table:

| Placeholder | Description |
|---|---|
| {Namespace} | Label that identifies the namespace where you deployed Kubernetes Operator. |
| {SecretName} | Human-readable label that identifies the secret you're creating in Vault. |
| {PublicKey} | The public key for your desired Ops Manager Programmatic API Key. |
| {PrivateKey} | The private key for your desired Ops Manager Programmatic API Key. |

```sh
  vault kv put secret/data/mongodbenterprise/operator/{Namespace}/{SecretName} publicKey={PublicKey} privateKey={PrivateKey}

The path in this command is the default path. You can replace ``mongodbenterprise/operator`` with
your base path if you customized your Kubernetes Operator configuration.
```

**Step 3: Verify the Vault secret creation was successful.**

Invoke the following Vault command to verify your secret, replacing
the variables with the values in the following table:

| Placeholder | Description |
|---|---|
| {Namespace} | Label that identifies the namespace where you deployed Kubernetes Operator. |
| {SecretName} | Human-readable label that identifies the secret you're creating in Vault. |

```sh
vault kv get secret/data/mongodbenterprise/operator/{Namespace}/{SecretName}
```

This command returns a secret description in the shell:

```sh
====== Metadata ======
Key              Value
---              -----
created_time     2021-12-15T17:20:22.985303Z
deletion_time    n/a
destroyed        false
version          1

======= Data =======
Key          Value
---          -----
publicKey    {PublicKey} 
privateKey   {PrivateKey}
```
