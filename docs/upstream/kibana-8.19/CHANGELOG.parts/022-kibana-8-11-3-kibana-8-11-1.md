<!-- Part 22 of 44 of CHANGELOG.md (split because the page is big). -->

## Kibana 8.11.3

The 8.11.3 release includes the following bug fixes.

### Bug Fixes

Elastic Security::
For the Elastic Security 8.11.3 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Fixes a 500 error in the Fleet API when a request for the product versions endpoint throws `ECONNREFUSED` ({kibana-pull}172850[#172850]).
* Fixes agent policy timeout to accept only integers ({kibana-pull}172222[#172222]).
Machine Learning::
* Fixes data drift numeric fields not displaying correctly ({kibana-pull}172504[#172504]).
* Fixes Data visualizer, ML field stats, and Data Frame Analytics so the `_tier` field can be excluded ({kibana-pull}172223[#172223]).
Operations::
* Fixes an issue where running `kibana-keystore` commands required `kibana.yml` to exist ({kibana-pull}172943[#172943]).


## Kibana 8.11.2

The 8.11.2 release includes the following bug fixes.

### Security updates

* The 8.11.2 patch release contains a fix for a potential security vulnerability. [Please see our security advisory for more details](https://discuss.elastic.co/c/announcements/security-announcements/31).

### Enhancements

APM::
* Added `context_propagation_only` APM agent setting ({kibana-pull}170405[#170405]).
Elastic Security::
For the Elastic Security 8.11.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Improve UX for policy secrets ({kibana-pull}171405[#171405]).
Observability::
* Adds `date_formats` to SLI ingest pipeline template ({kibana-pull}172377[#172377]).
Platform::
* It is now possible to hot reload Kibana's TLS (`server.ssl`) configuration by updating it and then sending a `SIGHUP` signal to the Kibana process ({kibana-pull}171823[#171823]).

### Bug Fixes

Dashboard::
* Fixes reference extract method ({kibana-pull}171360[#171360]).
* Adds Dashboard title to browser tab title ({kibana-pull}171255[#171255]).
Elastic Security::
For the Elastic Security 8.11.2 release information, refer to {security-guide}/release-notes.html[_Elastic Security Solution Release Notes_].
Fleet::
* Support integration secrets in a local package registry with variables `secret: true` and `required: false` ({kibana-pull}172078[#172078]).
* Fixes agents metrics retrieval on the agent list page, previously displaying N/A for metrics for users with more than 10 agents. ({kibana-pull}172016[#172016]).
* Only add `time_series_metric` if TSDB is enabled ({kibana-pull}171712[#171712]).
* Fixes inability to upgrade agents from version 8.10.4 to version 8.11 ({kibana-pull}170974[#170974]).
Lens & Visualizations::
* Handle invalid values gracefully for static value operation in *Lens* ({kibana-pull}172198[#172198]).
* Make the dashboard SO lighter ({kibana-pull}172130[#172130]).
Machine Learning::
* Fixes blocked jobs polling interval ({kibana-pull}171878[#171878]).
Management::
* Fixes autocomplete to show suggestions even if user types in every letter ({kibana-pull}171952[#171952]).
* Fixes wrong autocomplete suggestions when using the slash symbol ({kibana-pull}171948[#171948]).
* Fixes clusters and shards table expanded row not updating when request is changed ({kibana-pull}171232[#171232]).
Maps::
* Fixes using `max_result_window` to set up a mapbox vector tile (MVT) size request leading to all results not showing ({kibana-pull}171344[#171344]).
Observability::
* Fixes the custom threshold document link ({kibana-pull}171125[#171125]).
SharedUX::
* Fixes custom branding for users without "Saved Object Management" privilege ({kibana-pull}171308[#171308]).
* Fixes the custom threshold document link ({kibana-pull}171125[#171125]).
Uptime::
* Fixes advanced fields broken for ICMP monitors ({kibana-pull}171161[#171161]).
Ê


## Kibana 8.11.1

For information about the Kibana 8.11.1 release, review the following information.

### Security updates

* An issue was discovered by Elastic whereby sensitive information is recorded
in Kibana logs in the event of an error. The error message recorded in the log
may contain account credentials for the `kibana_system` user, API Keys, and
credentials of Kibana end users.
The issue impacts Kibana Kibana versions on or after 8.0.0 and before 8.11.1. The
issue is resolved in Kibana 8.11.1.

**Nov 15, 2023 Update:** After additional investigation, it has been determined
that Kibana 7.x versions are not affected by this issue. We previously reported
this issue impacted Kibana versions before 7.17.15.

For more information, see our related
https://discuss.elastic.co/t/8-11-1-7-17-15-security-update-esa-2023-25/347149[security
announcement].

### Bug Fixes

Fleet::
* Append space ID to security solution tag ({kibana-pull}170789[#170789]).
* Modify bulk unenroll to include inactive agents ({kibana-pull}170249[#170249]).
Lens & Visualizations::
* Fixes error handling for ES|QL nested error messages ({kibana-pull}170005[#170005]).
Machine Learning::
* Disable anomaly detection job creation from ES|QL lens visualizations ({kibana-pull}170711[#170711]).
Presentation::
* Fixes vector tile layer with joins stuck in loading state when not visible ({kibana-pull}170984[#170984]).
* Fixes expand layer control is not clickable when layers are loading ({kibana-pull}170912[#170912]).
