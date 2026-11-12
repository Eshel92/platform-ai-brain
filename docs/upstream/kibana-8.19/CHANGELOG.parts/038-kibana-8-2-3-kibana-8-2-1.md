<!-- Part 38 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.2.3

Review the following information about the Kibana 8.2.3 release.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking changes, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.2.2.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Bug fixes

Elastic Security::
For the Elastic Security 8.2.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Elastic Agent integration now installs automatically if agent monitoring is turned on in the agent policy {kibana-pull}133530[#133530]
* Removes Beats tutorials from the Elastic Stack category {kibana-pull}132957[#132957]
Management::
Fixes an edge case in the Inspector request selector where duplicate request names could result in a UI bug {kibana-pull}133511[#133511]
Operations::
Fixes an issue where `node.options` was reset between upgrades in deb and rpm packages {kibana-pull}133249[#133249]
Platform::
defaultIndex attribute was migrated for config saved object {kibana-pull}133339[#133339]


## Kibana 8.2.2

Review the following information about the Kibana 8.2.2 release.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking changes, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.2.2.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Bug fix

Machine Learning::
Fixes width of icon column in Messages table {kibana-pull}132444[#132444]


## Kibana 8.2.1

Review the following information about the Kibana 8.2.1 release.

### Breaking changes

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking changes, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.2.1.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Enhancements

Elastic Security::
For the Elastic Security 8.2.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Monitoring::
* Adds the ability collect Telemetry {kibana-pull}130498[#130498]
* Adds the ability to report panels in dashboards by type {kibana-pull}130166[#130166]

### Bug fixes

Discover::
* Fixes Document Explorer infinite height growth {kibana-pull}131723[#131723]
* Fixes links in helper callouts {kibana-pull}130873[#130873]
Elastic Security::
For the Elastic Security 8.2.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Removes legacy component templates on package install {kibana-pull}130758[#130758]
Lens & Visualizations::
* Fixes time shift bug in *Lens* {kibana-pull}132000[#132000]
* Fixes single color palette configuration {kibana-pull}131128[#131128]
Machine Learning::
* Removes alerting_rules from general job list items {kibana-pull}131936[#131936]
* Fixes management app docs links {kibana-pull}130776[#130776]
Management::
* Restores data view management field type conflict detail modal {kibana-pull}132197[#132197]
* Fixes test data for import and export between versions tests {kibana-pull}131470[#131470]
* Fixes condition auto-completion for templates in Console {kibana-pull}126881[#126881]
Maps::
* Fixes background tiles in a map panel might not load in a screenshot report {kibana-pull}131185[#131185]
Observability::
* Services without application metrics display an error {kibana-pull}131347[#131347]
* Correctly interprets the `resetting` and `reverting` job states {kibana-pull}129570[#129570]
Platform::
* Migrations incorrectly detects cluster routing allocation setting as incompatible {kibana-pull}131712[#131712]
* Fixes resetting image values {kibana-pull}131610[#131610]
* Fixes a bug causing the newsfeed to not be properly displayed in locales other than english {kibana-pull}131315[#131315]
