<!-- Converted from maps/headers/tile-json.asciidoc (AsciiDoc). Includes are inlined. -->

```bash
curl -I 'https://tiles.maps.elastic.co/v{minor-version}/manifest?elastic_tile_service_tos=agree&my_app_name=kibana&my_app_version={version}' \
-H 'User-Agent: curl/7.81.0' \
-H 'Accept: */*' \
-H 'Accept-Encoding: gzip, deflate, br'
```

Server response

```regex
HTTP/2 200 
server: BaseHTTP/0.6 Python/3.11.4
date: Mon, 20 Nov 2023 15:08:46 GMT
content-type: application/json; charset=utf-8
elastic-api-version: 2023-10-31
access-control-allow-origin: *
access-control-allow-methods: GET, OPTIONS, HEAD
access-control-allow-headers: Origin, Accept, Content-Type, kbn-version, elastic-api-version
access-control-expose-headers: etag
content-encoding: gzip
vary: Accept-Encoding
x-varnish: 844076 5416505
accept-ranges: bytes
varnish-age: 85285
cache-control: private, max-age=86400
via: 1.1 varnish (Varnish/7.0), 1.1 google
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
```
```regex
Host: tiles.maps.elastic.co
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: {ems-headers-url}/app/maps/map
Origin: {ems-headers-url}
Connection: keep-alive
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Pragma: no-cache
Cache-Control: no-cache
TE: trailers
```
```regex
server: BaseHTTP/0.6 Python/3.11.4
date: Mon, 20 Nov 2023 17:53:10 GMT
content-type: application/json; charset=utf-8
elastic-api-version: 2023-10-31
access-control-allow-origin: *
access-control-allow-methods: GET, OPTIONS, HEAD
access-control-allow-headers: Origin, Accept, Content-Type, kbn-version, elastic-api-version
access-control-expose-headers: etag
content-encoding: gzip
vary: Accept-Encoding
x-varnish: 8848609 1142291
accept-ranges: bytes
varnish-age: 65725
cache-control: private, max-age=86400
content-length: 341
via: 1.1 varnish (Varnish/7.0), 1.1 google
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
```
