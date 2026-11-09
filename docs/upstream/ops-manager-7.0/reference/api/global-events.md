<!-- Converted from reference/api/global-events.txt (reStructuredText). Includes are inlined. -->

# Global Events

**New in version:** 4.0

The `globalEvents` resource allows you to retrieve global events.

**Note:** Limited to Global Read Only Role

Only users with the `Global Read Only` can request these
endpoints.

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for global events.

| Method | Endpoint | Description |
|---|---|---|
| GET | /globalEvents | Get all global events. |
| GET | /globalEvents/{EVENT-ID} | Get one specific global event. |
