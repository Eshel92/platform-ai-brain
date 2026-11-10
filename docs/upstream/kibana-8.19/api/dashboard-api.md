<!-- Converted from api/dashboard-api.asciidoc (AsciiDoc). Includes are inlined. -->

## Import and export dashboard APIs

deprecated::[7.15.0,Both of these APIs have been deprecated and will be removed in 9.0.0]

Import and export dashboards with the corresponding saved objects, such as visualizations, saved
searches, and data views.

**Warning:** Do not write documents directly to the `.kibana` index. When you write directly
to the `.kibana` index, the data becomes corrupted and permanently breaks future Kibana versions.

The following import and export dashboard APIs are available:

* Import dashboard API to import dashboards and corresponding saved objects

* Export dashboard API to export dashboards and corresponding saved objects

(See `api/dashboard/import-dashboard.md`)
(See `api/dashboard/export-dashboard.md`)
