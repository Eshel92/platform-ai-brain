<!-- Converted from maps/headers/tile-pbf.asciidoc (AsciiDoc). Includes are inlined. -->

```bash
$ curl -I 'https://tiles.maps.elastic.co/data/v3/1/1/0.pbf?elastic_tile_service_tos=agree&my_app_name=kibana&my_app_version={version}' \
-H 'User-Agent: curl/7.81.0' \
-H 'Accept: */*' \
-H 'Accept-Encoding: gzip, deflate, br'
```

Server response

```regex
HTTP/2 200 
content-encoding: gzip
content-length: 144075
access-control-allow-origin: *
access-control-allow-methods: GET, OPTIONS, HEAD
access-control-allow-headers: Origin, Accept, Content-Type, kbn-version, elastic-api-version
access-control-expose-headers: etag
x-varnish: 3269455 5976667
accept-ranges: bytes
varnish-age: 9045
via: 1.1 varnish (Varnish/7.0), 1.1 google
date: Mon, 20 Nov 2023 15:08:19 GMT
age: 78827
last-modified: Thu, 16 Sep 2021 17:14:41 GMT
etag: W/"232cb-zYEfNgd8rzHusLotRFzgRDSDDGA"
content-type: application/x-protobuf
vary: Accept-Encoding
cache-control: public,max-age=3600
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
TE: trailers
```
```regex
content-encoding: gzip
content-length: 101691
access-control-allow-origin: *
access-control-allow-methods: GET, OPTIONS, HEAD
access-control-allow-headers: Origin, Accept, Content-Type, kbn-version, elastic-api-version
access-control-expose-headers: etag
x-varnish: 4698676 3660338
accept-ranges: bytes
varnish-age: 9206
via: 1.1 varnish (Varnish/7.0), 1.1 google
date: Mon, 20 Nov 2023 15:05:29 GMT
age: 75788
last-modified: Thu, 16 Sep 2021 17:14:41 GMT
etag: W/"18d3b-ot9ckSsdpH7n+yJz4BXXQp6Zs08"
content-type: application/x-protobuf
vary: Accept-Encoding
cache-control: public,max-age=3600
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
```
