<!-- Converted from reference/api/performance-advisor.txt (reStructuredText). Includes are inlined. -->

# Performance Advisor

Use the following resources to retrieve existing and suggested indexes
for a deployment, as well as the namespaces on which slow queries were
run and the queries that were slow.  For more information, see
/tutorial/performance-advisor.

To view field values in a sample query in the Performance
Advisor, you must be a user with at least one of the following
project roles:

- `Project Owner`

- `Project Data Access Admin`

- `Project Data Access Read/Write`

- `Project Data Access Read Only`

Users without one of these roles see redacted data rather than the
field values.

For more information about slow queries, see /tutorial/performance-advisor.

**Note:**

Groups and projects are synonymous terms. Your `{PROJECT-ID}` is the
same as your project id. For existing groups, your group/project id
remains the same. This page uses the more familiar term group when
referring to descriptions. The endpoint remains as stated in the
document.

Base URL: `https://{OPSMANAGER-HOST}:{PORT}/api/public/v1.0`

| Method | Endpoint | Description |
|---|---|---|
| `GET` | /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/namespaces | Retrieves the namespaces for all collections or specified collections experiencing slow queries on a specified host. |
| `GET` | /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/slowQueryLogs | Get slow queries as determined by the Performance Advisor. |
| `GET` | /groups/{PROJECT-ID}/hosts/{HOST-ID}/performanceAdvisor/suggestedIndexes | Get suggested indexes as determined by the Performance Advisor. |
