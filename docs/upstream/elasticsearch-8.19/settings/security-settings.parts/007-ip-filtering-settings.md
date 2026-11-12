<!-- Part 7 of 7 of settings/security-settings.md (split because the page is big). -->

### IP filtering settings

You can configure the following settings for IP filtering.

`xpack.security.transport.filter.allow`::
(Dynamic)
List of IP addresses to allow.

`xpack.security.transport.filter.deny`::
(Dynamic)
List of IP addresses to deny.

`xpack.security.http.filter.allow`::
(Dynamic)
List of IP addresses to allow just for HTTP.

`xpack.security.http.filter.deny`::
(Dynamic)
List of IP addresses to deny just for HTTP.

`transport.profiles.$PROFILE.xpack.security.filter.allow`::
(Dynamic)
List of IP addresses to allow for this profile.

`transport.profiles.$PROFILE.xpack.security.filter.deny`::
(Dynamic)
List of IP addresses to deny for this profile.

`xpack.security.remote_cluster.filter.allow`::
(Dynamic)
List of IP addresses to allow just for the
remote cluster server configured with the API key based model.

`xpack.security.remote_cluster.filter.deny`::
(Dynamic)
List of IP addresses to deny just for the remote cluster server configured with
the API key based model.

(See `settings/security-hash-settings.md`)
