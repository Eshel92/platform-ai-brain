<!-- Converted from settings/search-sessions-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Search sessions settings in Kibana

deprecated::[8.15.0,Search Sessions are deprecated and will be removed in a future version.]

Configure the search session settings in your `kibana.yml` configuration file.

deprecated:[8.15.0] `data.search.sessions.enabled` ::
Set to `true` (default) to enable search sessions.

deprecated:[8.15.0] `data.search.sessions.notTouchedTimeout` ::
How long Kibana stores search results from unsaved sessions,
after the last search in the session completes. The default is `5m`.

deprecated:[8.15.0] `data.search.sessions.maxUpdateRetries` ::
How many retries Kibana can perform while attempting to save a search session. The default is `10`.

deprecated:[8.15.0] `data.search.sessions.defaultExpiration` ::
How long search session results are stored before they are deleted.
Extending a search session resets the expiration by the same value. The default is `7d`.
