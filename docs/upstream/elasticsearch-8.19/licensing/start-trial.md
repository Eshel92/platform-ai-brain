<!-- Converted from licensing/start-trial.asciidoc (AsciiDoc). Includes are inlined. -->

### Start trial API

Starts a 30-day trial.

#### Request

`POST /_license/start_trial`

#### Description

The `start trial` API enables you to start a 30-day trial, which gives access to
all subscription features.

**Note:** You are allowed to initiate a trial only if your cluster has not already
activated a trial for the current major product version. For example, if you
have already activated a trial for v6.0, you cannot start a new trial until v7.0.
You can, however, request an extended trial at {extendtrial}.

To check the status of your trial, use get-trial-status. 

For more information about features and subscriptions, see
https://www.elastic.co/subscriptions.

#### Authorization

You must have `manage` cluster privileges to use this API.
For more information, see
security-privileges.

#### Examples

The following example starts a 30-day trial. The acknowledge parameter is
required as you are initiating a license that will expire.

```console
POST /_license/start_trial?acknowledge=true
```

Example response:
```js
{
  "trial_was_started": true,
  "acknowledged": true
}
```
