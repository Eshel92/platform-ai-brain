<!-- Part 36 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.3.3

Review the following information about the Kibana 8.3.3 release.

### Breaking change

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking change, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.3.3.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Bug fixes

Dashboard::
* Fixes `z-index` of `embPanel__header--floater` {kibana-pull}136463[#136463]
* Filter out experimental visualizations when labs setting is disabled {kibana-pull}136332[#136332]

Discover::
Fixes filter in / filter out buttons for empty values {kibana-pull}135919[#135919]

Elastic Security::
For the Elastic Security 8.3.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Fleet::
* Pass start_time to actions when the maintenance window for rolling upgrades is set to immediately {kibana-pull}136384[#136384]
* Allow agent bulk actions without specific licence restrictions {kibana-pull}136334[#136334]
* Adds reinstall button to integration settings page {kibana-pull}135590[#135590]

Lens & Visualizations::
Fixes normalizeTable performance bottleneck in *Lens* {kibana-pull}135792[#135792]


## Kibana 8.3.2

Review the following information about the Kibana 8.3.2 release.

### Breaking change

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking change, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.3.2.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Bug fixes

Alerting::
Fixes an issue where alerting rules that were created or edited in 8.2.0 stopped running when you upgraded Kibana to 8.3.0 or 8.3.1 {kibana-pull}135663[#135663]

Discover::
* Hide Alerts menu item when user does not have access to Stack Rules {kibana-pull}135655[#135655]
* Fixes loading of a single doc JSON when using index alias based data views {kibana-pull}135446[#135446]

Elastic Security::
For the Elastic Security 8.3.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Fleet::
Keep all agents selected in query selection mode {kibana-pull}135530[#135530]

Machine Learning::
* Fixes put anomaly detection job endpoint when payload contains datafeed {kibana-pull}134986[#134986]
* Fixes trained model map associating wrong model to job {kibana-pull}134849[#134849]
* Use time range when validating datafeed preview {kibana-pull}134073[#134073]

Maps::
* Do not show layer error for term joins when terms aggregation does not return results {kibana-pull}135564[#135564]
* Fixes Vector map layers will not render when runtime field has '%' {kibana-pull}135491[#135491]


## Kibana 8.3.1

Review the following information about the Kibana 8.3.1 release.

### Known issues

**URL arguments cause API requests in Dev Tools to fail**
*Details* +
When you add any URL arguments, such as `?v` or `?pretty`, to API requests, the requests fail  {kibana-issue}133965[#133965]

*Impact* +
The known issue only impacts Kibana Dev Tools. All other sources of API requests are unaffected, such as curl and Elastic Cloud API console.

**Alerting rules stop running when you upgrade to 8.3.0 or 8.3.1**
*Details* +
In 8.3.0 and 8.3.1, there is a known issue where alerting rules that were created or edited in 8.2.0 stop running when you upgrade Kibana. When you upgrade to 8.3.0 or 8.3.1, and your alerting rules have stopped running, the following error appears:

```text
<rule-type>:<UUID>: execution failed - security_exception: [security_exception] Reason: missing authentication credentials for REST request [/_security/user/_has_privileges], caused by: ""
```

*Impact* +
If you have upgraded to 8.3.0 or 8.3.1, and your alerting rules fail, reset the rules by disabling, then re-enabling them. When you disable, then re-enable your alerting rules, Kibana generates a new API key using the credentials of the user that manages the rules.

To disable, then re-enable your alerting rules:

. Open the main menu, then click *{stack-manage-app} > {rac-ui}*.

. Select the failed alerting rules.

. Click **Manage rules > Disable**, then click **Manage rules > Enable**.

For more details about API key authorization, refer to alerting-authorization.

### Breaking change

Breaking changes can prevent your application from optimal operation and performance.
Before you upgrade, review the breaking change, then mitigate the impact to your application.

There are no breaking changes in Kibana 8.3.1.

To review the breaking changes in previous versions, refer to the following:

{kibana-ref-all}/8.2/release-notes-8.2.0.html#breaking-changes-8.2.0[8.2.0] | {kibana-ref-all}/8.1/release-notes-8.1.0.html#breaking-changes-8.1.0[8.1.0] | {kibana-ref-all}/8.0/release-notes-8.0.0.html#breaking-changes-8.0.0[8.0.0] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc2.html#breaking-changes-8.0.0-rc2[8.0.0-rc2] | {kibana-ref-all}/8.0/release-notes-8.0.0-rc1.html#breaking-changes-8.0.0-rc1[8.0.0-rc1] | {kibana-ref-all}/8.0/release-notes-8.0.0-beta1.html#breaking-changes-8.0.0-beta1[8.0.0-beta1] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha2.html#breaking-changes-8.0.0-alpha2[8.0.0-alpha2] | {kibana-ref-all}/8.0/release-notes-8.0.0-alpha1.html#breaking-changes-8.0.0-alpha1[8.0.0-alpha1]

### Enhancements

Operations::
Adds EsArchiver datastream support {kibana-pull}132853[#132853]

### Bug fixes

Alerting::
Prevent negative snooze intervals {kibana-pull}134935[#134935]

Elastic Security::
For the Elastic Security 8.3.1 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].

Fleet::
* Fixes dropping select all {kibana-pull}135124[#135124]
* Improves bulk actions for more than 10k agents {kibana-pull}134565[#134565]

Infrastructure::
Query persistent queue size for metricbeat documents {kibana-pull}134569[#134569]

Observability::
* Fixes a bug that displayed a toast error when deleting a rule {kibana-pull}135132[#135132]
* Fixes viewInAppUrl for custom metrics for Inventory Threshold Rule {kibana-pull}134114[#134114]

Platform::
* Fixes an issue where importing/copying the same saved object to the same space multiple times using the "Check for existing objects" option could fail or cause duplicates to be created {kibana-pull}135358[#135358]
* Fixes a bug where Elasticsearch nodes that stopped, then started again, were unreachable by Kibana for a given amount of requests when Kibana was configured to connect to multiple Elasticsearch nodes {kibana-pull}134628[#134628]
