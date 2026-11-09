<!-- Converted from reference/command/getnonce.txt (reStructuredText). Includes are inlined. -->

# getnonce

**`getnonce`**

**Deprecated since version:** 4.0

Client libraries use `getnonce` to generate a one-time
password for authentication.

Applications should not invoke `getnonce` directly.

This command will be removed in a future release.   

## Behavior

### Client Disconnection

Starting in MongoDB 4.2, if the client that issued `getnonce`
disconnects before the operation completes, MongoDB marks `getnonce` 
for termination using `killOp`.
