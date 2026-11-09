<!-- Converted from tutorial/webhook-integration.txt (reStructuredText). Includes are inlined. -->

# Integrate with Webhooks in Ops Manager

You can configure Ops Manager to send alert notifications to a webhook
endpoint as HTTP (Hypertext Transfer Protocol) POST requests for programmatic processing.
Webhooks allow you to integrate Ops Manager alerts with custom
monitoring systems, incident management platforms, or automation
workflows.

## Required Access

To integrate Ops Manager with webhooks, you must have
`Project Monitoring Admin` access to the project.

## Configure a Webhook Integration

**Step 1: Navigate to the Project Integrations page.**

a. If it is not already displayed, select the
   organization that contains your desired project from
   the `office` Organizations menu in the navigation bar.

#. If it is not already displayed, select your desired
   project from the Projects menu in the
   navigation bar.

#. Click Integrations in the left navigation
   panel under the Settings heading.

**Step 2: Click Configure for Webhook Settings.**

**Step 3: Enter the webhook URL.**

In the Webhook URL field, enter the endpoint
URL (Uniform Resource Locator) where Ops Manager should send alert notifications.

**Step 4: (Optional) Enter a webhook secret.**

In the Webhook Secret field, enter a secret
key. Ops Manager uses this secret to generate the
`X-MMS-Signature` header for request verification.

**Step 5: Click Save.**

To send alerts to your webhook, configure alert notifications.
To learn more, see configure-alerts.

## Request Headers

Ops Manager includes the following HTTP (Hypertext Transfer Protocol) headers with each webhook
request:

Ops Manager adds a request header called `X-MMS-Event` to
distinguish between various alert states. The possible values
for this header are:

|  |  |
|---|---|
| `alert.open` | The alert was just opened. |
| `alert.close` | The alert was resolved. |
| `alert.update` | A previously opened alert is still open. |
| `alert.acknowledge` | The alert was acknowledged. |
| `alert.cancel` | The alert became invalid and was canceled. |
| `alert.inform` | Represents an informational alert, which is a point-in-time event, such as "Primary Elected." |

If you specify a key in the Webhook Secret field,
MongoDB Ops Manager adds the `X-MMS-Signature` request header. This
header contains the base64-encoded HMAC (hash-based message authentication code)-SHA-1 signature of the
request body. MongoDB Ops Manager creates the signature using the provided
secret.

## Request Body

The request body contains a JSON (Javascript Object Notation) document that uses the same
format as the Ops Manager API (Application Programming Interface)
Alerts resource. The payload
includes key fields such as:

- `id`: Unique identifier for the alert.
- `eventTypeName`: Type of event that triggered the alert.
- `created`: Timestamp when the alert was created.
- `status`: Current status of the alert (for example, `OPEN`,
  `CLOSED`).
- `humanReadable`: Human-readable description of the alert.

For a complete list of fields, refer to the
Get One Alert
endpoint documentation.

### Example Webhook Payload

The following example shows a sample webhook payload for a
metric threshold alert:

```json
{
  "id": "5d1b6f8e8c2e4e2d3c4a5b6c",
  "groupId": "5d1b6f8e8c2e4e2d3c4a5b6d",
  "eventTypeName": "OUTSIDE_METRIC_THRESHOLD",
  "status": "OPEN",
  "created": "2024-01-15T10:30:00Z",
  "updated": "2024-01-15T10:30:00Z",
  "lastNotified": "2024-01-15T10:30:00Z",
  "humanReadable": "Disk space used on data partition is
    95.2%.",
  "metricName": "DISK_PARTITION_SPACE_USED_DATA",
  "currentValue": {
    "number": 95.2,
    "units": "RAW"
  }
}
```

## Customize Webhook Templates

You can customize the request headers and body content using
FreeMarker templates. For detailed information about webhook
templating, including available template variables, regex
helpers, and examples, see
Configure Webhook Templating.

## Authenticate Webhook Requests

The Webhook Secret field stores a secret that Ops Manager
uses solely to generate the `X-MMS-Signature` header for
request verification. Ops Manager does not send the secret directly
as an authentication header or bearer token.

If your webhook endpoint requires authentication, you must
handle it independently using one of the following methods:

- **Query Parameters**: Include authentication credentials in
  the Webhook URL as query parameters. For example:
  `https://example.com/webhook?token=your-auth-token`

- **IP Access List**: Configure your webhook endpoint to accept
  requests only from your Ops Manager instance's IP addresses.

- **Reverse Proxy or API Gateway**: Use a reverse proxy or
  API (Application Programming Interface) gateway that handles authentication before forwarding
  requests to your webhook endpoint.

### Verify Webhook Requests

To verify that a webhook request originated from Ops Manager,
validate the `X-MMS-Signature` header:

**Step 1: Retrieve the `X-MMS-Signature` header value from the incoming request.**

**Step 2: Calculate the Base64-encoded HMAC (hash-based message authentication code)-SHA-1 signature of the request body using your webhook secret.**

**Step 3: Compare your calculated signature with the `X-MMS-Signature` header value.**

If they match, the request is authentic.

## Limitations

When you use webhook integrations, consider the following
limitations:

### Alert Severity Not Included

The webhook payload does not include the alert severity level
that you configure in Ops Manager. To retrieve the configured
severity, make an additional call to the
Get One Alert Configuration endpoint using
the `alertConfigId` from the webhook payload.

### No Manual Test Alerts

Ops Manager does not provide a way to trigger test alerts manually.
To test your webhook endpoint, you can temporarily set up an
alert with conditions that are easy to trigger, such as:

- A low disk space threshold on a test deployment.
- A connection count threshold that you can trigger by opening
  multiple connections.
- A replication lag threshold on a test replica set.

After you confirm your webhook receives alerts correctly, you
can delete the test alert configuration.

## Firewall Configuration

Since Ops Manager is self-hosted, ensure your network allows
outbound HTTP (Hypertext Transfer Protocol) requests from the Ops Manager server to your
webhook endpoint. If your webhook endpoint is behind a
firewall, add the Ops Manager server's IP address to the
endpoint's IP access list.

## Troubleshoot Webhook Delivery Issues

If your webhook does not receive alerts:

**Step 1: Verify that the webhook URL is correct and accessible from the Ops Manager server.**

**Step 2: Check that your firewall allows outbound requests from the Ops Manager server to the webhook endpoint.**

**Step 3: Ensure your webhook endpoint returns a 2xx HTTP status code.**

Ops Manager considers other status codes as failures.

**Step 4: Review your alert configuration to ensure alerts are enabled and the webhook is selected as a notification method.**

**Step 5: Check the Activity Feed in the Ops Manager UI for any webhook delivery errors.**
