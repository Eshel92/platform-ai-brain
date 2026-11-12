<!-- Part 34 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.4.3

Review the following information about the Kibana 8.4.3 release.

### Breaking change

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking change, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.4.3.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.3/release-notes-8.3.0.html#breaking-changes-8.3.0[8.3.0] | {kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Bug fixes

Cases::
Fixes an issue where the recent cases widget shows cases from other solutions {kibana-pull}141221[#141221]

Discover::
* Fixes scrolling prevented by saved search embeddable on touch devices {kibana-pull}141718[#141718]
* Fixes columns management for saved search embeddable {kibana-pull}140799[#140799]

Elastic Security::
For the Elastic Security 8.4.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Graph::
* Fixes the position of Add fields popover {kibana-pull}141040[#141040]
* Fixes responsive styles of field manager {kibana-pull}140948[#140948]

Machine Learning::
Fixes an issue where Data visualizer was unable to update distribution when changing shard size, forbidden error with recognize modules on basic license {kibana-pull}141313[#141313]

Management::
Fixes the removal of a single field formatter {kibana-pull}141078[#141078]

Observability::
Fixes an alert summary widget issue in non-default space {kibana-pull}140842[#140842]


## Kibana 8.4.2

Review the following information about the Kibana 8.4.2 release.

### Breaking change

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking change, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.4.2.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.3/release-notes-8.3.0.html#breaking-changes-8.3.0[8.3.0] | {kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Enhancements

Security::
Logs a hash of the saved objects encryption key (`xpack.encryptedSavedObjects.encryptionKey`) when Kibana starts to assist in identifying mismatched encryption keys {kibana-pull}139874[#139874]

### Bug fixes

Connectors::
The connectors table now uses "compatibility" rather than "availability" {kibana-pull}139024[#139024]

Discover::
Fixes saved search embeddable rendering {kibana-pull}140264[#140264]

Elastic Security::
For the Elastic Security 8.4.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Fleet::
* Applies fixes for package policy upgrade API with multiple ids {kibana-pull}140069[#140069]
* Improves performance for many integration policies {kibana-pull}139648[#139648]

Lens & Visualizations::
* Fixes "Collapse by" for table and XY visualizations with multiple metrics in *Lens* {kibana-pull}140381[#140381]
* Fixes action menu in *Lens* {kibana-pull}139588[#139588]

Machine Learning::
* Explain Log Rate Spikes: Histogram fixes {kibana-pull}139933[#139933]
* Explain Log Rate Spikes: Improve streaming headers for certain proxy configs {kibana-pull}139637[#139637]
* Fixes navigation for the Basic licence {kibana-pull}139469[#139469]
* Corrects file.path field name in v3_windows_anomalous_script job {kibana-pull}139109[#139109]

Management::
Bfetch` response headers now include `X-Accel-Buffering: no` {kibana-pull}139534[#139534]

Maps::
* Fixes issue where percentile aggregation was not working with vector tiles {kibana-pull}140318[#140318]
* Fixes Map app crashing on file upload request timeout {kibana-pull}139760[#139760]

Monitoring::
* Ensures GlobalState class has it's destroy() method called on unmount {kibana-pull}139908[#139908]
* Adds KibanaThemeProvider to Stack Monitoring UI {kibana-pull}139839[#139839]

Uptime::
Fixes an issue where decryption errors caused the entire suite of monitors to fail syncing {kibana-pull}140549[#140549]


## Kibana 8.4.1

Review the following information about the Kibana 8.4.1 release.

### Breaking change

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking change, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.4.1.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.3/release-notes-8.3.0.html#breaking-changes-8.3.0[8.3.0] | {kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Bug fixes

Alerting::
* Fixes alert tab crash on rule details page {kibana-pull}139372[#139372]
* Fixes issue where some 8.3.x clusters failed to upgrade with a saved object migration failure {kibana-pull}139427[#139427]

Lens & Visualizations::
* Fixes table pagination in *Lens* and *Aggregation-based* visualization editors {kibana-pull}139160[#139160]
