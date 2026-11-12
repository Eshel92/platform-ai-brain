<!-- Part 40 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.1.2

Review the following information about the Kibana 8.1.2 release.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking changes, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.1.2.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Enhancement

Dashboard::
Improve controls management UX {kibana-pull}127524[#127524]

### Bug fixes

Discover::
* Fixes toggle table column for classic table {kibana-pull}128603[#128603]
* Fixes selection popover close action without making a selection in Document Explorer {kibana-pull}128124[#128124]

Elastic Security::
For the Elastic Security 8.1.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Management::
Handle scenario when user has no indices {kibana-pull}128066[#128066]

Monitoring::
Rename "APM & Fleet Server" to "Integrations Server" {kibana-pull}128574[#128574]

Platform::
Fixes KQL typeahead missing description and improve display for long field names {kibana-pull}128480[#128480]


## Kibana 8.1.1

Review the following information about the Kibana 8.1.1 release.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade to 8.1.1, review the breaking changes, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.1.1.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Enhancement

Dashboard::
Improves controls empty state {kibana-pull}125728[#125728]

### Bug fixes

Data ingest::
The dot expander processor in the Ingest Pipelines UI now allows setting a wildcard (`*`) for the field parameter {kibana-pull}123522[#123522]

Elastic Security::
For the Elastic Security 8.1.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Enterprise Search::
For the Elastic Enterprise Search 8.1.1 release information, refer to {enterprise-search-ref}/changelog.html[_Elastic Enterprise Search Documentation Release notes_].

Fleet::
* Adds a new validation message {kibana-pull}127239[#127239]
* Fixes empty assets on package install {kibana-pull}127070[#127070]
* Hide enroll command when user creates a new agent policy in the Add agent flyout {kibana-pull}126431[#126431]
* Makes input IDs unique in agent policy yaml {kibana-pull}127343[#127343]
* Fixes links to Agent logs for APM, Endpoint, Synthetics, and OSQuery {kibana-pull}127480[#127480]
