<!-- Converted from api/features.asciidoc (AsciiDoc). Includes are inlined. -->

## Get features API

experimental[] Retrieves all Kibana features. Features are used by spaces and security to refine and secure access to Kibana.

### Request

`GET <kibana host>:<port>/api/features`

### Response code

`200`::
  Indicates a successful call.

### Example

The API returns the following:

```sh
  {
    "id": "discover",
    "name": "Discover",
    "app": [
      "kibana"
    ],
    "catalogue": [
      "discover"
    ],
    "privileges": {
      "all": {
        "savedObject": {
          "all": [
            "search",
            "url"
          ],
          "read": [
            "config",
            "index-pattern"
          ]
        },
        "ui": [
          "show",
          "createShortUrl",
          "save"
        ]
      },
      "read": {
        "savedObject": {
          "all": [],
          "read": [
            "config",
            "index-pattern",
            "search",
            "url"
          ]
        },
        "ui": [
          "show"
        ]
      }
    }
  },
  {
    "id": "visualize",
    "name": "Visualize",
    "app": [
      "kibana"
    ],
    "catalogue": [
      "visualize"
    ],
    "privileges": {
      "all": {
        "savedObject": {
          "all": [
            "visualization",
            "url"
          ],
          "read": [
            "config",
            "index-pattern",
            "search"
          ]
        },
        "ui": [
          "show",
          "createShortUrl",
          "delete",
          "save"
        ]
      },
      "read": {
        "savedObject": {
          "all": [],
          "read": [
            "config",
            "index-pattern",
            "search",
            "visualization"
          ]
        },
        "ui": [
          "show"
        ]
      }
    }
  },
  {
    "id": "dashboard",
    "name": "Dashboard",
    "app": [
      "kibana"
    ],
    "catalogue": [
      "dashboard"
    ],
    "privileges": {
      "all": {
        "savedObject": {
          "all": [
            "dashboard",
            "url"
          ],
          "read": [
            "config",
            "index-pattern",
            "search",
            "visualization",
            "canvas-workpad"
          ]
        },
        "ui": [
          "createNew",
          "show",
          "showWriteControls"
        ]
      },
      "read": {
        "savedObject": {
          "all": [],
          "read": [
            "config",
            "index-pattern",
            "search",
            "visualization",
            "canvas-workpad",
            "dashboard"
          ]
        },
        "ui": [
          "show"
        ]
      }
    }
  },
  {
    "id": "dev_tools",
    "name": "Dev Tools",
    "app": [
      "kibana"
    ],
    "catalogue": [
      "console",
      "searchprofiler",
      "grokdebugger"
    ],
    "privileges": {
      "all": {
        "api": [
          "console"
        ],
        "savedObject": {
          "all": [],
          "read": [
            "config"
          ]
        },
        "ui": [
          "show"
        ]
      },
      "read": {
        "api": [
          "console"
        ],
        "savedObject": {
          "all": [],
          "read": [
            "config"
          ]
        },
        "ui": [
          "show"
        ]
      }
    },
    "privilegesTooltip": "User should also be granted the appropriate Elasticsearch cluster and index privileges"
  },
```
