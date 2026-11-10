<!-- Converted from watcher/troubleshooting.asciidoc (AsciiDoc). Includes are inlined. -->

## Troubleshooting Watcher

### Dynamic mapping error when trying to add a watch

If you get the _Dynamic Mapping is Disabled_ error when you try to add a watch,
verify that the index mappings for the `.watches` index are available. You can
do that by submitting the following request:

```console
GET .watches/_mapping
```

If the index mappings are missing, follow these steps to restore the correct
mappings:

. Stop the Elasticsearch node.
. Add `xpack.watcher.index.rest.direct_access : true` to `elasticsearch.yml`.
. Restart the Elasticsearch node.
. Delete the `.watches` index:
```console
DELETE .watches
```
. Disable direct access to the `.watches` index:
.. Stop the Elasticsearch node.
.. Remove `xpack.watcher.index.rest.direct_access : true` from `elasticsearch.yml`.
.. Restart the Elasticsearch node.

### Unable to send email

If you get an authentication error indicating that you need to continue the
sign-in process from a web browser when Watcher attempts to send email, you need
to configure Gmail to
[Allow Less Secure Apps to access your account](https://support.google.com/accounts/answer/6010255?hl=en).

If you have two-step verification enabled for your email account, you must
generate and use an App Specific password to send email from Watcher. For more
information, see:

- Gmail: [Sign in using App Passwords](https://support.google.com/accounts/answer/185833?hl=en)
- Outlook.com: [App passwords and two-step verification](http://windows.microsoft.com/en-us/windows/app-passwords-two-step-verification)

### Watcher not responsive

Keep in mind that there's no built-in validation of scripts that you add to a
watch. Buggy or deliberately malicious scripts can negatively impact Watcher
performance. For example, if you add multiple watches with buggy script
conditions in a short period of time, Watcher might be temporarily unable to
process watches until the bad watches time out.
