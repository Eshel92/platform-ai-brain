<!-- Converted from licensing/get-trial-status.asciidoc (AsciiDoc). Includes are inlined. -->

### Get trial status API

**New API reference**
For the most up-to-date API details, refer to [Licensing APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-license).

Enables you to check the status of your trial.

#### Request

`GET /_license/trial_status`

#### Description

If you want to try all the subscription features, you can start a 30-day trial. 

**Note:** You are allowed to initiate a trial only if your cluster has not
already activated a trial for the current major product version. For example, if
you have already activated a trial for v6.0, you cannot start a new trial until
v7.0. You can, however, request an extended trial at {extendtrial}.

For more information about features and subscriptions, see
https://www.elastic.co/subscriptions.

#### Authorization

You must have `monitor` cluster privileges to use this API.
For more information, see
security-privileges.

#### Examples

The following example checks whether you are eligible to start a trial:

```console
GET /_license/trial_status
```

Example response:

```console-result
{
  "eligible_to_start_trial": true
}
```
