<!-- Converted from watcher/managing-watches.asciidoc (AsciiDoc). Includes are inlined. -->

## Managing watches

Watcher provides as set of APIs you can use to manage your watches:

* Use the create or update watch API to add or update watches
* Use the get watch API to retrieve watches
* Use the delete watch API to delete watches
* Use the activate watch API to activate watches
* Use the deactivate watch API to deactivate watches
* Use the ack watch API to acknowledge watches

### Listing watches

Currently there is not dedicated API for listing the stored watches. However,
since Watcher stores its watches in the `.watches` index, you can list them
by executing a search on this index.

**Important:** You can only perform read actions on the `.watches` index. You must
            use the Watcher APIs to create, update, and delete watches. If Elasticsearch
            security features are enabled, we recommend you only grant users
            `read` privileges on the `.watches` index.

For example, the following returns the first 100 watches:

```console
GET /_watcher/_query/watches
{
  "size" : 100
}
```
