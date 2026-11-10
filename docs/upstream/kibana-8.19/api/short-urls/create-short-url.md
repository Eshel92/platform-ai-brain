<!-- Converted from api/short-urls/create-short-url.asciidoc (AsciiDoc). Includes are inlined. -->

### Create short URL API

experimental[] Create a Kibana short URL. Kibana URLs may be long and cumbersome, short URLs are much
easier to remember and share.

Short URLs are created by specifying the locator ID and locator parameters. When a short URL is
resolved, the locator ID and locator parameters are used to redirect user to the right Kibana page.

#### Request

`POST <kibana host>:<port>/api/short_url`

#### Request body

`locatorId`::
  (Required, string) ID of the locator.

`params`::
  (Required, object) Object which contains all necessary parameters for the given locator to resolve
  to a Kibana location.
**Warning:** When you create a short URL, locator params are not validated, which allows you to pass
arbitrary and ill-formed data into the API that can break Kibana. Make sure
any data that you send to the API is properly formed.

`slug`::
  (Optional, string) A custom short URL slug. Slug is the part of the short URL that identifies it.
  You can provide a custom slug which consists of latin alphabet letters, numbers and `-._`
  characters. The slug must be at least 3 characters long, but no longer than 255 characters.

`humanReadableSlug`::
  (Optional, boolean) When the `slug` parameter is omitted, the API will generate a random
  human-readable slug, if `humanReadableSlug` is set to `true`.

#### Response code

`200`::
    Indicates a successful call.

#### Example

```sh
$ curl -X POST api/short_url  -H 'kbn-xsrf: true' -H 'Content-Type: application/json' -d '
{
  "locatorId": "LOCATOR_ID",
  "params": {},
  "humanReadableSlug": true
}'
```

The API returns the following:

```sh
{
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", <1>
  "slug": "adjective-adjective-noun", <2>
  "locator": {
    "id": "LOCATOR_ID",
    "version": "x.x.x", <3>
    "state": {} <4>
  },
  "accessCount": 0,
  "accessDate": 1632680100000,
  "createDate": 1632680100000
}
```

<1> A random ID is automatically generated.
<2> A random human-readable slug is automatically generated if the `humanReadableSlug` parameter is set to `true`. If set to `false` a random short string is generated.
<3> The version of Kibana when short URL was created is stored.
<4> Locator params provided as `params` property are stored.
