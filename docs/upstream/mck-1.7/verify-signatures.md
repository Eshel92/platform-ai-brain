<!-- Converted from verify-signatures.txt (reStructuredText). Includes are inlined. -->

# Verify MongoDB Signatures

You can require that the MongoDB Agent verifies the signature file after it 
downloads the MongoDB binary by enabling a setting in the k8s-om-specification. 
Once you enable signature verification, the MongoDB Agent requires signature files 
for all MongoDB deployments that your Ops Manager instance manages. 
You can enable signature verification for 
local or remote deployments.

## Prerequisites

Your Ops Manager server must run over HTTPS (Hypertext Transfer Protocol Secure) so the MongoDB Agent downloads the 
signature files. To learn more, see config-https.

## Procedure

**Step 1: **

In the k8s-om-specification, add 
`spec.configuration.mms.featureFlag.automation.verifyDownloads` and set to `enabled`. 
For example:

```yaml
spec:
  configuration:
    mms.featureFlag.automation.verifyDownloads=enabled
```

**Note:**

Once you enable signature verification, the MongoDB Agent requires signature 
files for all MongoDB binaries that it downloads. 

**Step 2: **

Ensure the MongoDB Agent can locate the MongoDB binary and its signature (.sig) 
file from the same directory, the location of which depends on whether your 
deployment is local or remote.

**remote:**

If your Ops Manager instance can access the Internet or a custom HTTPS (Hypertext Transfer Protocol Secure) 
server and you download the MongoDB binary from the official sources, 
the MongoDB Agent automatically downloads the signature file along with 
the MongoDB binary.

If you don't download the MongoDB binary from the official sources, 
configure your HTTPS (Hypertext Transfer Protocol Secure) server to locate the MongoDB binary and its 
signature file from the same link.

**local:**

If your Ops Manager instance can't access the Internet, the MongoDB binary 
and its signature file are stored in `/mongodb-ops-manager/mongodb-releases/`
by default. Ensure the signature file is named the same as the MongoDB 
binary and both are in the same directory. For example: 

```sh
/mongodb-ops-manager/mongodb-releases/mongodb-linux-x86_64-rhel80-8.0.0.tgz.sig
/mongodb-ops-manager/mongodb-releases/mongodb-linux-x86_64-rhel80-8.0.0.tgz
```

**Step 3: **

Save and apply the k8s-om-specification.

```sh
kubectl apply -f <my-ops-manager-resource-specification>.yaml
```

After you've applied the k8s-om-specification, the MongoDB Agent performs a 
rolling restart on the cluster nodes, reconciling 
the changes.
