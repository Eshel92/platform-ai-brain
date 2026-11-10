<!-- Converted from settings/telemetry-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Telemetry settings in Kibana

Usage Collection (also known as Telemetry) is enabled by default. This allows us to learn what our users are most interested in, so we can improve our products and services.

Refer to our [Privacy Statement](https://www.elastic.co/legal/product-privacy-statement) to learn more.

You can control whether this data is sent from the Kibana servers, or if it should be sent
from the user's browser, in case a firewall is blocking the connections from the server. Additionally, you can disable this feature either in *Stack Management > Kibana > Advanced Settings > Global Settings > Usage collection* or the config file with the following settings.

#### General telemetry settings

[[telemetry-optIn]] `telemetry.optIn`::
  Set to `false` to stop sending any telemetry data to Elastic. Reporting your
cluster statistics helps us improve your user experience. *Default: `true`.* +
This setting can be changed at any time in Advanced Settings.
To prevent users from changing it,
set `telemetry.allowChangingOptInStatus` to `false`.

`telemetry.allowChangingOptInStatus`::
  Set to `false` to disallow overwriting the `telemetry.optIn` setting via the Advanced Settings in Kibana. *Default: `true`.*

`telemetry.sendUsageFrom`::
  Set to `'server'` to report the cluster statistics from the Kibana server.
  If the server fails to connect to our endpoint at https://telemetry.elastic.co/, it assumes
  it is behind a firewall and falls back to `'browser'` to send it from users' browsers
  when they are navigating through Kibana. *Default: `'server'`.*

`xpack.apm.telemetryCollectionEnabled`::
  Collects information about APM data and API performance. Set this to `false` to specifically disable APM's collector. *Default: `'true'`.*
