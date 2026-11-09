<!-- Converted from tutorial/verify-mongodb-packages.txt (reStructuredText). Includes are inlined. -->

# Verify the Integrity of the MongoDB Controllers for Kubernetes Operator Packages

MongoDB release team digitally signs MongoDB Controllers for Kubernetes Operator packages to certify that they are valid and
unaltered MongoDB releases. Before you install MongoDB Controllers for Kubernetes Operator, validate the
package using the provided PGP signature or SHA-256 checksum.

PGP signatures provide the strongest guarantees by checking both the
authenticity and integrity of a file to prevent tampering.

## Verify Linux/macOS Packages

### Prerequisites

Run the following command to obtain our signing key:

```
wget https://cosign.mongodb.com/mongodb-enterprise-kubernetes-operator.pem 
```

### Use Cosign

MongoDB signs each release branch with a signature file. You can verify
the authenticity of the binary with our public key file.

**Step 1: Download the MongoDB kubectl plugin file.**

To download the `1.0.0` release using Darwin with an ARM64 architecture, run the following command:

```
wget https://github.com/mongodb/mongodb-kubernetes/releases/download/1.0.0/public/kubectl-mongodb_1.0.0_darwin_arm64.tar.gz
```

Output:

```
Saving : « kubectl-mongodb_1.0.0_darwin_arm64.tar.gz »
```

**Step 2: Unzip the MongoDB kubectl plugin file.**

```
tar -xvzf kubectl-mongodb_1.0.0_darwin_arm64.tar.gz
```

Output:

```
x kubectl-mongodb.bundle
x kubectl-mongodb     
```

**Step 3: Verify the MongoDB kubectl plugin file.**

Run the following command:

```
cosign verify-blob --key mongodb-enterprise-kubernetes-operator.pem --insecure-ignore-tlog --bundle kubectl-mongodb.bundle kubectl-mongodb
```

Output:

```
Verified OK
```

### Use Images

You can also verify the signature of any published Docker images. The
following example shows how to verify the signature of the MongoDB Controllers for Kubernetes Operator 1.0.0
image:

```
cosign verify --key mongodb-enterprise-kubernetes-operator.pem quay.io/mongodb/mongodb-enterprise-kubernetes-operator:1.0.0 --insecure-ignore-tlog
```

Output:

```
WARNING: Skipping tlog verification is an insecure practice that lacks of transparency and auditability verification for the signature.

Verification for quay.io/mongodb/mongodb-kubernetes-operator:1.0.0 --
The following checks were performed on each of these signatures:
- The cosign claims were validated
- The signatures were verified against the specified public key

[{"critical":{"identity":{"docker-reference":"quay.io/mongodb/mongodb-kubernetes-operator:1.0.0"},"image":{"docker-manifest-digest":"sha256:9281935b4c36e0e4feebcf577abf21291ce0b517e7f637e6eaaf9769642abdd3"},"type":"cosign container image signature"},"optional":null}]
```
