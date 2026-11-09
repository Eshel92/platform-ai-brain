<!-- Converted from reference/api/global-alert-configurations-test-one.txt (reStructuredText). Includes are inlined. -->

# Test Global Alert Configuration

Triggers a test notification for a specific notification method in a global alert configuration. This endpoint sends a test payload with dummy data and rendered templates to validate your webhook configuration.

## Request

```http
POST /api/public/v1.0/globalAlertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test
```

### Request Path Parameters

| Parameter | Type | Description |
|---|---|---|
| ALERT-CONFIG-ID | string | Unique 24-hexadecimal digit string that identifies the global alert configuration. |
| NOTIFICATION-ID | string | Unique 24-hexadecimal digit string that identifies the notification method within the global alert configuration. |

### Request Query Parameters

This endpoint does not use HTTP request query parameters.

### Request Body Parameters

This endpoint does not use HTTP request body parameters.

## Response

### Response Elements

If you set the query parameter `pretty=true`, the response displays in a readable format.

| Parameter | Type | Description |
|---|---|---|
| success | boolean | Flag that indicates whether the test notification was sent successfully. |
| message | string | Human-readable message describing the result of the test operation. |
| details | object | Additional details about the test notification. |
| details.notificationType | string | Type of notification that was tested (e.g., `WEBHOOK`, `EMAIL`). |
| details.destination | string | Destination where the test notification was sent. For webhooks, this is the webhook URL. |
| details.timestamp | string | ISO 8601 timestamp when the test notification was sent. |

## Example Request

```bash
curl --user "{PUBLIC-KEY}:{PRIVATE-KEY}" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request POST "https://ops-manager.example.com:8080/api/public/v1.0/globalAlertConfigs/{ALERT-CONFIG-ID}/{NOTIFICATION-ID}/test?pretty=true"
```

## Example Response

### Response Header

```http
HTTP/1.1 200 OK
Vary: Accept-Encoding
Content-Type: application/json
Strict-Transport-Security: max-age=300
Date: {dateInUnixFormat}
Connection: keep-alive
Content-Length: {requestLengthInBytes}
```

### Response Body

```json
{
  "success": true,
  "message": "Test notification sent successfully",
  "details": {
    "notificationType": "WEBHOOK",
    "destination": "https://example.com/webhook",
    "timestamp": "2025-01-15T10:30:00Z"
  }
}
```
