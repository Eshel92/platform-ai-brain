<!-- Converted from reference/api/events.txt (reStructuredText). Includes are inlined. -->

# Events

The `events` resource allows you to retrieve events.

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

## Endpoints

The following lists the endpoints available for events.

### Organization Event Endpoints

**Note:** Limited to Organization Member Role

Only users with the `Organization Member` role can request
these endpoints.

| Method | Endpoint | Description |
|---|---|---|
| GET | /orgs/{ORG-ID}/events | Get all events for an organization. |
| GET | /orgs/{ORG-ID}/events/{EVENT-ID} | Get one specific event for an organization. |

### Project Event Endpoints

**Note:** Limited to Project Read Only Role

Only users with the `Project Read Only` role can request
these endpoints.

| Method | Endpoint | Description |
|---|---|---|
| GET | /groups/{PROJECT-ID}/events | Get all events for a project. |
| GET | /groups/{PROJECT-ID}/events/{EVENT-ID} | Get one specific event for a project. |

**Note:** Hidden Events Limited to Global Read Only Role

Only users with the `Global Read Only` role can see
the hidden events in these endpoints.
