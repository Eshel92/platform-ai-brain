<!-- Converted from settings/banners-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Banner settings in Kibana

Banners are disabled by default. You need to manually configure them in order to use the feature.

You can configure the `xpack.banners` settings in your `kibana.yml` file.

**Note:**
Banners are a [subscription feature](https://www.elastic.co/subscriptions).

`xpack.banners.placement`::
Set to `top` to display a banner above the Elastic header. Defaults to `disabled`.

`xpack.banners.textContent`::
The text to display inside the banner, either plain text or Markdown.

`xpack.banners.textColor`::
The color for the banner text. Defaults to `#8A6A0A`.

`xpack.banners.backgroundColor`::
The color of the banner background. Defaults to `#FFF9E8`.

`xpack.banners.disableSpaceBanners`::
If true, per-space banner overrides will be disabled. Defaults to `false`.
