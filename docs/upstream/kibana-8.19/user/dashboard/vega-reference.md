<!-- Converted from user/dashboard/vega-reference.asciidoc (AsciiDoc). Includes are inlined. -->

#### Vega reference

Learn more about Kibana extension, additional *Vega* resources, and examples.

##### Reference for Kibana extensions

Kibana has extended Vega and Vega-Lite with extensions that support:

* Automatic sizing
* Default theme to match Kibana
* Writing Elasticsearch queries using the time range and filters from dashboards
* experimental[] Using the Elastic Map Service in Vega maps
* Additional tooltip styling
* Advanced setting to enable URL loading from any domain
* Debugging support using the Kibana inspector or browser console
* (Vega only) Expression functions which can update the time range and dashboard filters

###### Automatic sizing

Most users will want their Vega visualizations to take the full available space, so unlike
Vega examples, `width` and `height` are not required parameters in Kibana because your
spec will be merged with the default Kibana settings in most cases:

```
autosize: {
  type: fit
  contains: padding
}
width: container
height: container
```

These default settings are *not* applied if:

* Your spec uses `type=map`
* Your spec is Vega-Lite and contains a facet, row, column, repeat, or concat operator. In these
cases, providing `width` and `height` will affect the child size.

To set the width or height manually, set `autosize: none` and provide the exact pixel sizes, including
padding for the title, legend and axes.

```
autosize: none
width: 600
height: 200
padding: {
  top: 20
  bottom: 20
  left: 55
  right: 150
}
```

To learn more, read about
[Vega autosize](https://vega.github.io/vega/docs/specification/#autosize)
and [Vega-Lite autosize](https://vega.github.io/vega-lite/docs/size.html).

**Note:** Autosize in Vega-Lite has [several limitations](https://vega.github.io/vega-lite/docs/size.html#limitations)
which can affect the height and width of your visualization, but these limitations do not exist in Vega.
If you need full control, convert your spec to Vega using the browser console
`VEGA_DEBUG.vega_spec` output.
To disable these warnings, you can add extra options to your spec.

###### Default theme to match Kibana

Kibana registers a default [Vega color scheme](https://vega.github.io/vega/docs/schemes/)
with the id `elastic`, and sets a default color for each `mark` type.
Override it by providing a different `stroke`, `fill`, or `color` (Vega-Lite) value.

###### Writing Elasticsearch queries in Vega

Kibana extends the Vega [data](https://vega.github.io/vega/docs/data/) elements
with support for direct Elasticsearch queries specified as `url`.

Kibana is **unable to support dynamically loaded data**,
which would otherwise work in Vega. All data is fetched before it's passed to
the Vega renderer.

To define an Elasticsearch query in Vega, set the `url` to an object. Kibana parses
the object looking for special tokens that allow your query to integrate with Kibana.

Tokens include the following:

* `%context%: true`: Set at the top level, and replaces the `query` section with filters from dashboard
* `%timefield%: <name>`: Set at the top level, integrates the query with the dashboard time filter
* `{%timefilter%: true}`: Replaced by an Elasticsearch range query with upper and lower bounds
* `{%timefilter%: "min" | "max"}`: Replaced only by the upper or lower bounds
* `{%timefilter: true, shift: -1, unit: 'hour'}`: Generates a time range query one hour in the past
* `{%autointerval%: true}`: Replaced by the string which contains the automatic Kibana time interval, such as `1h`
* `{%autointerval%: 10}`: Replaced by a string which is approximately dividing the time into 10 ranges, allowing
  you to influence the automatic interval
* `"%dashboard_context-must_clause%"`: String replaced by object containing filters
* `"%dashboard_context-filter_clause%"`: String replaced by an object containing filters
* `"%dashboard_context-must_not_clause%"`: String replaced by an object containing filters

**Note:** Vega supports the `interval` parameter, which is unsupported Elasticsearch 8.0.0 and later. To use intervals, use `fixed_interval` or `calendar_interval` instead.

For example, the following query counts the number of documents in a specific index:

```yaml
// An object instead of a string for the URL value
// is treated as a context-aware Elasticsearch query.
url: {
  // Specify the time filter.
  %timefield%: @timestamp
  // Apply dashboard context filters when set
  %context%: true

  // Which indexes to search
  index: kibana_sample_data_logs
  // The body element may contain "aggs" and "query" keys
  body: {
    aggs: {
      time_buckets: {
        date_histogram: {
          // Use date histogram aggregation on @timestamp field
          field: @timestamp <1>
          // interval value will depend on the time filter
          // Use an integer to set approximate bucket count
          interval: { %autointerval%: true }
          // Make sure we get an entire range, even if it has no data
          extended_bounds: {
            min: { %timefilter%: "min" }
            max: { %timefilter%: "max" }
          }
          // Use this for linear (e.g. line, area) graphs
          // Without it, empty buckets will not show up
          min_doc_count: 0
        }
      }
    }
    // Speed up the response by only including aggregation results
    size: 0
  }
}
```

<1> `@timestamp` &mdash; Filters the time range and breaks it into histogram
buckets.

The full result includes the following structure:

```yaml
{
  "aggregations": {
    "time_buckets": {
      "buckets": [{
          "key_as_string": "2015-11-30T22:00:00.000Z",
          "key": 1448920800000,<1>
          "doc_count": 28
        }, {
          "key_as_string": "2015-11-30T23:00:00.000Z",
          "key": 1448924400000, <1>
          "doc_count": 330
        }, ...
```

<1> `"key"` &mdash; The unix timestamp you can use without conversions by the
Vega date expressions.

For most visualizations, you only need the list of bucket values. To focus on
only the data you need, use `format: {property: "aggregations.time_buckets.buckets"}`.

Specify a query with individual range and dashboard context. The query is
equivalent to `"%context%": true, "%timefield%": "@timestamp"`,
except that the time range is shifted back by 10 minutes:

```yaml
{
  body: {
    query: {
      bool: {
        must: [
          // This string will be replaced
          // with the auto-generated "MUST" clause
          "%dashboard_context-must_clause%"
          {
            range: {
              // apply timefilter (upper right corner)
              // to the @timestamp variable
              @timestamp: {
                // "%timefilter%" will be replaced with
                // the current values of the time filter
                // (from the upper right corner)
                "%timefilter%": true
                // Only work with %timefilter%
                // Shift current timefilter by 10 units back
                shift: 10
                // week, day (default), hour, minute, second
                unit: minute
              }
            }
          }
        ]
        must_not: [
          // This string will be replaced with
          // the auto-generated "MUST-NOT" clause
          "%dashboard_context-must_not_clause%"
        ]
        filter: [
          // This string will be replaced
          // with the auto-generated "FILTER" clause
          "%dashboard_context-filter_clause%"
        ]
      }
    }
  }
}
```

**Note:** When using `"%context%": true` or defining a value for `"%timefield%"` the body cannot contain a query. To customize the query within the VEGA specification (e.g. add an additional filter, or shift the timefilter), define your query and use the placeholders as in the example above. The placeholders will be replaced by the actual context of the dashboard or visualization once parsed.

The `"%timefilter%"` can also be used to specify a single min or max
value. The date_histogram's `extended_bounds` can be set
with two values - min and max. Instead of hardcoding a value, you may
use `"min": {"%timefilter%": "min"}`, which will be replaced with the
beginning of the current time range. The `shift` and `unit` values are
also supported. The `"interval"` can also be set dynamically, depending
on the currently picked range: `"interval": {"%autointerval%": 10}` will
try to get about 10-15 data points (buckets).

##### Access Elastic Map Service files

experimental[] Access the Elastic Map Service files via the same mechanism:

```yaml
url: {
  // "type" defaults to "elasticsearch" otherwise
  %type%: emsfile
  // Name of the file, exactly as in https://maps.elastic.co
  name: World Countries
}
// The result is either a topojson file or a geojson file. 
// Refer to the Default format for the file at https://maps.elastic.co
// Get its features to use this data source with the "shape" marks
// https://vega.github.io/vega/docs/marks/shape/
// For a topojson file use
format: {type: "topojson", feature: "data"}

// For a geojson file use
format: {property: "features"}
```

#### Vega with a Map

experimental[] To enable *Maps*, the graph must specify `type=map` in the host configuration:

```yaml
{
  "config": {
    "kibana": {
      "type": "map",

      // Initial map position
      "latitude": 40.7,   // default 0
      "longitude": -74,   // default 0
      "zoom": 7,          // default 2

      // Defaults to 'true', disables the base map layer.
      "mapStyle": false,

      // When 'mapStyle' is 'undefined' or 'true', sets the EMS-layer for the map.
      // May either be: "road_map", "road_map_desaturated", "dark_map".
      // If 'emsTileServiceId' is 'undefined', it falls back to the auto-switch-dark-light behavior.
      "emsTileServiceId": "road_map",

      // default 0
      "minZoom": 5,

      // defaults to the maximum for the given style,
      // or 25 when base is disabled
      "maxZoom": 13,

      // Defaults to 'true', shows +/- buttons to zoom in/out
      "zoomControl": false,

      // Defaults to 'false', disables mouse wheel zoom. If set to
      // 'true', map may zoom unexpectedly while scrolling dashboard
      "scrollWheelZoom": false,

      // When false, repaints on each move frame.
      // Makes the graph slower when moving the map
      "delayRepaint": true, // default true
    }
  },
  /* the rest of Vega JSON */
}
```

The visualization automatically injects a `"projection"`, which you can use to
calculate the position of all geo-aware marks.
Additionally, you can use `latitude`, `longitude`, and `zoom` signals.
These signals can be used in the graph, or can be updated to modify the
position of the map.

experimental[] You can use the *Vega* [data](https://vega.github.io/vega/docs/data/) element to access [Elastic Maps Service (EMS)](https://www.elastic.co/elastic-maps-service) vector shapes of administrative boundaries in your Vega map by setting `url.data` to `emsFile`:

```yaml
  "data": [
    {
      "name": "countries",
      "url": {
        // "type" defaults to "elasticsearch" otherwise
        %type%: emsfile
        // Name of the file, exactly as in the Region map visualization
        name: World Countries
      },
      // The result is a topojson file, get its features to use
      // this data source with the "shape" marks
      // https://vega.github.io/vega/docs/marks/shape/
      "format": {"type": "topojson", "feature": "data"},
    }
  ],
  "marks": [
    {
      "type": "shape",
      "from": {"data": "countries"},
      "transform": [{"type": "geoshape", "projection": "projection"}]
    }
  ]
```

###### Additional tooltip styling

Kibana has installed the [Vega tooltip plugin](https://vega.github.io/vega-lite/docs/tooltip.html),
so tooltips can be defined in the ways documented there. Beyond that, Kibana also supports
a configuration option for changing the tooltip position and padding:

```js
{
  config: {
    kibana: {
      tooltips: {
        position: 'top',
        padding: 15,
        textTruncate: true,
      }
    }
  }
}
```

###### Enable URL loading from any domain

*Vega* can load data from any URL. To enable, set `vis_type_vega.enableExternalUrls: true` in `kibana.yml`,
then restart Kibana.

The files that the external URLs load must allow [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).
The remote URL must include `Access-Control-Allow-Origin`, which allows requests from the Kibana URL.

You can make the current time range part of the external as a millisecond timestamp by using the placeholders `%timefilter_min%` and `%timefilter_max%`, e.g. `http://<example-url>?min=%timefilter_min%`.

###### Vega Inspector

Use the contextual *Inspect* tool to gain insights into different elements. 

###### Inspect Elasticsearch requests

*Vega* uses the [Elasticsearch search API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/search-search.html) to get documents and aggregation
results from Elasticsearch. To troubleshoot these requests, click *Inspect*, which shows the most recent requests.
In case your specification has more than one request, you can switch between the views using the *View* dropdown.

(Figure: images/vega_tutorial_inspect_requests.png)

##### Vega debugging

With the *Vega debug* view, you can inspect the *Data sets* and *Signal Values* runtime data.

The runtime data is read from the
[runtime scope](https://vega.github.io/vega/docs/api/debugging/#scope).

(Figure: images/vega_tutorial_inspect_data_sets.png)

To debug more complex specs, access to the `view` variable.  For more information, refer to
the Vega browser debugging process.

###### Asking for help with a Vega spec

Because of the dynamic nature of the data in Elasticsearch, it is hard to help you with
*Vega* specs unless you can share a dataset. To do this, click *Inspect*, select the *Vega debug* view,
then select *Spec*.

(Figure: images/vega_tutorial_getting_help.png)

To copy the response, click *Copy to clipboard*. Paste the copied data to
[gist.github.com](https://gist.github.com/), possibly with a .json extension. Use the [raw] button,
and share that when asking for help.

##### Browser debugging console

experimental[] Use browser debugging tools (for example, F12 or CtrlShiftJ in Chrome) to
inspect the `VEGA_DEBUG` variable:

* `view` &mdash; Access to the Vega View object. See [Vega Debugging Guide](https://vega.github.io/vega/docs/api/debugging/)
on how to inspect data and signals at runtime. For Vega-Lite,
`VEGA_DEBUG.view.data('source_0')` gets the pre-transformed data, and `VEGA_DEBUG.view.data('data_0')`
gets the encoded data. For Vega, it uses the data name as defined in your Vega spec.

* `vega_spec` &mdash; Vega JSON graph specification after some modifications by Kibana. In case
of Vega-Lite, this is the output of the Vega-Lite compiler.

* `vegalite_spec` &mdash; If this is a Vega-Lite graph, JSON specification of the graph before
Vega-Lite compilation.

##### (Vega only) Expression functions which can update the time range and dashboard filters

Kibana has extended the Vega expression language with these functions. 
These functions will trigger new data to be fetched, which by default will reset Vega signals. 
To keep signal values set `restoreSignalValuesOnRefresh: true` in the Vega config.

```js
/**
  * @param {object} query Elastic Query DSL snippet, as used in the query DSL editor
  * @param {string} [index] as defined in Kibana, or default if missing
  * @param {string} Custom label of the filter shown in the filter bar
  */
kibanaAddFilter(query, index, alias)

/**
  * @param {object} query Elastic Query DSL snippet, as used in the query DSL editor
  * @param {string} [index] as defined in Kibana, or default if missing
  */
kibanaRemoveFilter(query, index)

kibanaRemoveAllFilters()

/**
  * Update dashboard time filter to the new values
  * @param {number|string|Date} start
  * @param {number|string|Date} end
  */
kibanaSetTimeFilter(start, end)
```

##### Additional configuration options

```yaml
{
  config: {
    kibana: {
      // Placement of the Vega-defined signal bindings.
      // Can be `left`, `right`, `top`, or `bottom` (default).
      controlsLocation: top
      // Can be `vertical` or `horizontal` (default).
      controlsDirection: vertical
      // If true, hides most of Vega and Vega-Lite warnings
      hideWarnings: true
      // Vega renderer to use: `svg` or `canvas` (default)
      renderer: canvas
      // Defaults to 'false', restores Vega signal values on refresh
      restoreSignalValuesOnRefresh: false
    }
  }
}
```

#### Resources and examples

To learn more about Vega and Vega-Lite, refer to the resources and examples.

##### Vega editor

The [Vega Editor](https://vega.github.io/editor/) includes examples for Vega & Vega-Lite, but does not support any
Kibana-specific features like Elasticsearch requests and interactive base maps.

##### Vega-Lite resources

* [Tutorials](https://vega.github.io/vega-lite/tutorials/getting_started.html)
* [Docs](https://vega.github.io/vega-lite/docs/)
* [Examples](https://vega.github.io/vega-lite/examples/)

##### Vega resources

* [Tutorials](https://vega.github.io/vega/tutorials/)
* [Docs](https://vega.github.io/vega/docs/)
* [Examples](https://vega.github.io/vega/examples/)

**Tip:** When you use the examples in Kibana, you may
need to modify the "data" section to use absolute URL. For example,
replace `"url": "data/world-110m.json"` with
`"url": "https://vega.github.io/editor/data/world-110m.json"`.
