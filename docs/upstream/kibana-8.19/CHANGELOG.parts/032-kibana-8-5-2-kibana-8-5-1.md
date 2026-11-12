<!-- Part 32 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.5.2

Review the following information about the Kibana 8.5.2 release.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking change, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.5.2.

{kibana-ref-all}/8.4/release-notes-8.4.0.html#breaking-changes-8.4.0[8.4.0] | {kibana-ref-all}/8.3/release-notes-8.3.0.html#breaking-changes-8.3.0[8.3.0] | {kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Enhancement

Security::
* Adds a `Content-Security-Policy` header to all `/api/*` responses {kibana-pull}144902[#144902]

### Bug fixes

APM::
* Limits the number of source map artifacts {kibana-pull}144963[#144963]
* Fixes an incorrect documentation link {kibana-pull}145077[#145077]
* Suppresses error toast when data view cannot be created {kibana-pull}143639[#143639]

Dashboard::
Fixes unexpected suggestions for text/keyword multi-fields {kibana-pull}145177[#145177]

Discover::
Fixes % for field stats calculations (edge cases) {kibana-pull}144962[#144962]

Management::
Fixes autocomplete_entities API crash when response size is too big {kibana-pull}140569[#140569]

Uptime::
Adjust formula for synthetics monitor availability {kibana-pull}144868[#144868]


## Kibana 8.5.1

Review the following information about the Kibana 8.5.1 release.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking change, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.5.1.

{kibana-ref-all}/8.4/release-notes-8.4.0.html#breaking-changes-8.4.0[8.4.0] | {kibana-ref-all}/8.3/release-notes-8.3.0.html#breaking-changes-8.3.0[8.3.0] | {kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Enhancements

Elastic Security::
For the Elastic Security 8.5.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

### Bug fixes

APM::
* Fixes a bug where Metadata API does not filter by environment {kibana-pull}144472[#144472]
* Fixes a bug where AWS lambda checks for an undefined value {kibana-pull}143987[#143987]
* Limits the number of source map artifacts {kibana-pull}144963[#144963]
* Fixes an incorrect documentation link {kibana-pull}145077[#145077]

Dashboard::
* Removes support for scripted fields in options list {kibana-pull}144643[#144643]
* Fixes help documentation link for dashboard {kibana-pull}143894[#143894]

Elastic Security::
For the Elastic Security 8.5.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Fleet::
Make asset tags space aware {kibana-pull}144066[#144066]

Machine Learning::
* Correcting the size of the free ML node on cloud {kibana-pull}144512[#144512]
* Fixes model testing flyout reload {kibana-pull}144318[#144318]
* Explain Log Rate Spikes: Wrap analysis in try/catch block {kibana-pull}143651[#143651]
* Explain Log Rate Spikes: Fix uncompressed streams and backpressure handling {kibana-pull}142970[#142970]

Osquery::
* Fixes a bug that prevented users from viewing Osquery results if they were in a non-default Kibana space {kibana-pull}144210[#144210]

Platform::
Fixes the execution pipeline not to stop on a flaky subexpression {kibana-pull}143852[#143852]

Uptime::
* Adjust forumla for synthetics monitor availability {kibana-pull}144868[#144868]
* TLS alert - do not alert when status cannot be determined {kibana-pull}144767[#144767]
