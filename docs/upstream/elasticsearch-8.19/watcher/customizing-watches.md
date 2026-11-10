<!-- Converted from watcher/customizing-watches.asciidoc (AsciiDoc). Includes are inlined. -->

## Customizing watches

Now that you've seen how to set up simple watches to
watch your log data and
monitor your cluster health, let's take a closer
look at how you can customize a watch by modifying its inputs,
conditions, transforms, and
actions.

### Changing inputs

The Watch Input is called when the watch triggered to load an initial payload.
This payload is stored in the _Watch Execution Context_ and from then on is
available for other watch elements to access (e.g. watch conditions can
be evaluated based on the data in this payload).

Watcher supports four types of inputs simple,
search, http, and
chain.

#### Loading a static payload with the simple input

To load static data into the watch payload for testing purposes, you can use the
simple input. For example, the following input stores three
fields in the payload:

```js
"input" : {
  "simple" : {
    "color"  : "red",
    "status" : "error",
    "count"  : 3
  }
}
```

See input-simple for more details.

#### Loading a payload from Elasticsearch with the search input

You can use the `search` input to load Elasticsearch search results as the watch
initial payload.

A search input contains a `request` object that specifies the
indices you want to search, the search type,
and the search request body. The `body` field of a search input is the same as
the body of an Elasticsearch `_search` request, making the full Elasticsearch
Query DSL available for you to use.

For example, the following `search` input loads the latest VIX quote:

```js
{
  "input" : {
    "search" : {
      "request" : {
        "indices" : [ "<stock-quotes-{now/d}>" ], <1>
        "body" : {
          "size" : 1,
          "sort" : {
            "timestamp" : { "order" : "desc"}
          },
          "query" : {
            "term" : { "symbol" : "vix"}
          }
        }
      }
    }
  }
}
```
<1> Will resolve to today's daily quotes index

See input-search for more details.

#### Loading a payload from a remote HTTP service with HTTP input

Use the `http` input to issue an HTTP request and load the returned response as
the watch initial payload. This input expects the response body content type
to either be JSON or YAML.

For example, the following `http` input loads the current weather forecast for
Amsterdam using [OpenWeatherMap](http://openweathermap.org/appid) online service:

```js
{
  "input" : {
    "http" : {
      "request" : {
        "url" : "http://api.openweathermap.org/data/2.5/weather",
        "params" : {
          "lat" : "52.374031",
          "lon" : "4.88969",
          "appid" : "<your openweathermap appid>"
        }
      }
    }
  }
}
```
See input-http for more details.

#### Chaining inputs

You can create an input chain to load data from multiple sources
into a watch payload. The inputs in a chain are processed in order, so the
data loaded by one input can be used by subsequent inputs.

See input-chain for more details.

### Changing conditions

The Watch Condition is evaluated as part of the watch execution. The condition
determines whether the actions associated with the watch should execute or not.

Watcher supports four types of conditions always,
never, compare, and
script.

The first two are pretty self-explanatory--they are shortcuts for setting a
watch's condition to `true` or `false`.

#### Simple value comparison with the compare condition

The `compare` condition enables you to perform simple comparisons against values
in the Watch payload. While you can also do this with a `script` condition, with
`compare` you can define inline comparisons without having to enable dynamic
scripting.

For example, the following compare condition checks to see if the `search` input
returned any hits:

```js
"condition" : {
    "compare" : { "ctx.payload.hits.total" : { "gt" : 0 }}
  },
```
See condition-compare for more details.

#### Powerful comparison logic with the script condition

For more complex conditional logic you can use the `script` condition. The
`script` condition accepts a script that when executed returns `true` (indicating
the condition is met) or `false` (indicating the condition is not met). The script
language defaults to the default script language in Elasticsearch, but you can
also use any other supported language in the system.

**Note:** Starting with 5.0, Elasticsearch is shipped with the new
      Painless scripting language.
      Painless was created and designed specifically for use in Elasticsearch.
      Beyond providing an extensive feature set, its biggest trait is that it's
      properly sandboxed and safe to use anywhere in the system (including in
      Watcher) without the need to enable dynamic scripting.

For example, the following `script` condition checks if the change in the latest
VIX quote loaded by the `http` input is either greater than 5% or lower than -5%:

```js
"condition" : {
  "script" : {
    "source" : "Math.abs(ctx.payload.hits.hits[0]._source.ChangePercent) > 5",
    "lang" : "painless"
  }
}
```
See condition-script for more details.

### Using transforms

Transforms are constructs in a watch that can change the current payload
associated with the watch execution context.

Watcher supports three types of transforms search,
script and chain. A `search` transform
replaces the existing payload with the response of a new search request. You can
use `script` transforms to modify the existing payload. A `chain` transform
enables you to perform a series of `search` and `script` transforms.

See transform for more details.

### Customizing actions

Actions are associated with a watch and are executed as part of the watch execution
only when the watch condition is met.

Watcher supports the following action types: email,
slack, pagerduty,
index, logging, and webhook.

To use the `email` action, you need to configure an email account
in `elasticsearch.yml` that Watcher can use to send email. Your custom email
messages can be plain text or styled using HTML. You can include information from
the watch execution payload using templates, as well as attach the
entire watch payload to the message.

For example, the following email action uses a template in the email body and
attaches the payload data to the message:

```js
"actions" : {
  "send_email" : { <1>
    "email" : { <2>
      "to" : "email@example.org",
      "subject" : "Watcher Notification",
      "body" : "{{ctx.payload.hits.total}} error logs found",
      "attachments" : {
        "data_attachment" : {
          "data" : {
            "format" : "json"
          }
        }
      }
    }
  }
}
```
<1> The id of the action
<2> The action type, in this case it's an `email` action

Another example for an action is the `webhook` action. This enables you to send
a request to any external webservice. For example, the following `webhook` action
creates a new issue in GitHub

```js
"actions" : {
  "create_github_issue" : {
    "webhook" : {
      "method" : "POST",
      "url" : "https://api.github.com/repos/<owner>/<repo>/issues", <1>
      "body" : "{
        \"title\": \"Found errors in 'contact.html'\",
        \"body\": \"Found {{ctx.payload.hits.total}} errors in this page in the last 5 minutes\",
        \"assignee\": \"web-admin\",
        \"labels\": [ \"bug\", \"sev2\" ]
      }",
      "auth" : {
        "basic" : {
          "username" : "<username>", <2>
          "password" : "<password>" <3>
        }
      }
    }
  }
}
```
<1> `<owner>` is the owner of the GitHub repo and `<repo>` is the name of the repo.
<2> The username that creates the issue
<3> The password of that user

To learn how to create other actions see actions.
