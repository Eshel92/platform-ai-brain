<!-- Converted from tutorial/prometheus-integration.txt (reStructuredText). Includes are inlined. -->

# Integrate with Prometheus

[Prometheus](https://prometheus.io/) collects metrics from configured targets at given
intervals, evaluates rule expressions, displays the results, and can
trigger alerts when it observes specific conditions. 

Our integration allows you to configure Ops Manager to send metric data
about your deployment to your [Prometheus](https://prometheus.io/) instance.

## Prerequisites

- [Prometheus](https://prometheus.io/) integration is available in automation managed clusters that use MongoDB Agent 12.0.15.7646 or
  later. MongoDB Agent 12.0.15.7646 is released with Ops Manager 6.0.7.

- Have a working [Prometheus](https://prometheus.io/) instance. To set up a working instance, see
  their
  [Installation Guide](https://prometheus.io/docs/prometheus/latest/installation/).

- (Optional) Use [Grafana](https://prometheus.io/docs/visualization/grafana/) to
  visualize your Prometheus metrics.

## Procedure

To integrate Ops Manager with [Prometheus](https://prometheus.io/):

**Step 1: Navigate to the Integrations page for your project.**

a. If it is not already displayed, select the organization that
   contains your desired project from the `office` Organizations menu in the
   navigation bar.

#. If it is not already displayed, select your desired project
   from the Projects menu in the navigation bar.

#. Next to the Projects menu, expand the
   Options menu, then click Integrations.

**Step 2: Click Configure for the Prometheus integration card.**

**Step 3: Enter your preferred username and password.**

**Important:**

Copy your username and password in a secure location. You can't
access the password after you leave this screen.

**Step 4: Enter your IP address and port.**

**Tip:**

The default value, `0.0.0.0:9216`, scrapes metrics on port
`9216` on all IPv4 (Internet Protocol version 4) addresses on the local machine.

**Step 5: (Optional) Encrypt all Prometheus metrics.**

If you enable this setting, Ops Manager assures that your Prometheus
instance uses `https` to scrape metrics.

* - Fields
  - Description

* - TLS Certificate Key File Path
  -  `PEM` file path that contains certificate and key required
     to spin up a `https` Prometheus scraping endpoint. 

     You are responsible for the following:

     - TLS Certificate Key File issuance and renewal.
     - Checking if the endpoint started correctly in the automation agent logs.

* - TLS Certificate Key File Password
  - Required if the certificate key file is encrypted.

**Step 6: Select your preferred service discovery method.**

* - Discovery Method
  - Description

* - [HTTP SD](https://prometheus.io/docs/prometheus/latest/http_sd/)
  - This method requires Prometheus v2.28 and later. It
    generates the [scrape_config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config)
    part of your [configuration file](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file)
    to discover targets over an HTTP endpoint.

* - [File Service Discovery](https://prometheus.io/docs/guides/file-sd/#use-file-based-service-discovery-to-discover-scrape-targets)
  - This method allows Prometheus to read YAML (Yet Another Markup Language) or JSON (Javascript Object Notation)
    documents to configure the targets to scrape from.

    You are responsible for providing the targets by making a request to the Discovery API and storing its results in a `targets.json` file.

    To make the request, substitute the placeholder text in one of
    the following tabs or create your own script in another language.

    **shell-command:**

    ```sh
    # Sets the `Authorization` header on every scrape
    # request with the username and password from the
    # previous step. The URL that Prometheus fetches the
    # targets from. 
    # Replace the <group-id> with the project ID of your
    # Ops Manager instance.

    curl --header 'Accept: application/json' \
         --user <username>:<password> \
         --request GET "https://cloud.mongodb.com/prometheus/v1.0/groups/{GROUP-ID}/discovery" 
    ```

    **python-script:**

    If you need to install the `requests` library,
    see their
    [Installation Guide](https://prometheus.io/docs/prometheus/latest/installation).

    ```python
    import time, json, requests

    # This script sets the `Authorization` header on every
    # scrape request with the configured username and
    # password. Then it tells Prometheus to fetch targets
    # from the specified URL. 
    #
    # Note: Replace the <username> and <password> with the
    # values in the previous step, and <group-id> with the
    # project ID of your Ops Manager instance.

    basic_auth_user="<username>"
    basic_auth_password="<password>"
    discovery_api_url="https://cloud.mongodb.com/prometheus/v1.0/groups/{GROUP-ID}/discovery"

    # The script updates your targets.json file every
    # minute, if it successfully retrieves targets.
    #
    # Note: Replace the <path-to-targets.json> with the
    # path to your targets.json file.

    starttime = time.time()
    while True:
      r = requests.get(discovery_api_url, auth=(basic_auth_user, basic_auth_password))
      if  r.status_code == 200:
        with open('<path-to-targets.json>', 'w') as f:
          json.dump(r.json(), f)
      time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    ```

    To learn more about the Discovery API, see
    prometheus-discovery-endpoint-mms.

**Step 7: Click Save.**

**Step 8: View Your Cluster Metrics on Prometheus.**

a. Copy the generated snippet into the
   [scrape_configs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) section of your 
   [configuration file](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file)
   and substitute the placeholder text. 

   For an example of the configuration file in either method, see
   example-prometheus-configurations-mms.

#. Restart your Prometheus instance.

#. In your Prometheus instance, click `Status` in the top navigation
   bar, and click `Targets` to see the metrics of your deployment.

## Example Configurations

The following shows examples of the
[configuration file](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file)
when you use the HTTP Service Discovery or
File Service Discovery method.

The configuration file in both methods contains the following fields:

| Field | Description |
|---|---|
| `scrape_interval` | Time that indicates how frequently to scrape targets. This setting supports a minimum time of 10s. |
| `job_name` | Human-readable label assigned to scraped metrics. |
| `metrics_path` | HTTP resource path that indicates where to fetch metrics from targets. |
| `scheme` | Your Prometheus protocol scheme configured for requests, either `http` or `https`. If you configure `https`, you must specify `tlsPemPath`. |
| `basic_auth` | Authorization header to use on every scrape request. |

  

### HTTP Service Discovery

The HTTP Service Discovery method also contains the `http_sd_configs`
field with the following sub-fields:

| Field | Description |
|---|---|
| `url` | URL from which Prometheus fetches the targets. |
| `refresh_interval` | Time that indicates when to re-query the endpoint. |
| `basic_auth` | Credentials to use for authenticating to the API server. |

```yaml
global:
  scrape_interval: 15s

scrape_configs:

  - job_name: "CM-Testing-mongo-metrics"
    scrape_interval: 10s
    metrics_path: /metrics
    scheme : https
    basic_auth:
      username: prom_user_61e6e34e93eac1632d39f457
      password: V7hTyLfkjwiWQbv
    http_sd_configs:
      - url: https://cloud.mongodb.com/prometheus/v1.0/groups/61e6e34e93eac1632d39f457/discovery
        refresh_interval: 60s
        basic_auth:
          username: prom_user_61e6e34e93eac1632d39f457
          password: V7hTyLfkjwiWQbv
```

### File Service Discovery

The File Service Discovery method also contains the
`file_sd_configs` field with the following sub-field:

| Field | Description |
|---|---|
| `files` | List that contains the files from which to extract the metrics scraping targets. |

```yaml
global:
  scrape_interval: 15s

scrape_configs:

  - job_name: "CM-Testing-mongo-metrics"
    scrape_interval: 10s
    metrics_path: /metrics
    scheme : https
    basic_auth:
      username: prom_user_61e6e34e93eac1632d39f457
      password: V7hTyLfkjwiWQbv
    file_sd_configs:
      - files:
        - /usr/local/etc/targets.json
```

## Import a Sample Grafana Dashboard

To import a sample Grafana dashboard:

**Step 1: Navigate to the Import screen.**

In the Grafana UI, click the plus button, and then click Import.

**Step 2: Click Upload JSON File.**

**Step 3: Copy over the `mongo-metrics.json` or the `hardware-metrics.json` file to create a dashboard.**

```json
{
 "__inputs": [
   {
     "name": "DS_PROMETHEUS",
     "label": "prometheus",
     "description": "",
     "type": "datasource",
     "pluginId": "prometheus",
     "pluginName": "Prometheus"
   }
 ],
 "__elements": [],
 "__requires": [
   {
     "type": "grafana",
     "id": "grafana",
     "name": "Grafana",
     "version": "8.5.6"
   },
   {
     "type": "panel",
     "id": "graph",
     "name": "Graph (old)",
     "version": ""
   },
   {
     "type": "datasource",
     "id": "prometheus",
     "name": "Prometheus",
     "version": "1.0.0"
   },
   {
     "type": "panel",
     "id": "table",
     "name": "Table",
     "version": ""
   }
 ],
 "annotations": {
   "list": [
     {
       "builtIn": 1,
       "datasource": {
         "type": "datasource",
         "uid": "grafana"
       },
       "enable": true,
       "hide": true,
       "iconColor": "rgba(0, 211, 255, 1)",
       "name": "Annotations & Alerts",
       "target": {
         "limit": 100,
         "matchAny": false,
         "tags": [],
         "type": "dashboard"
       },
       "type": "dashboard"
     }
   ]
 },
 "editable": true,
 "fiscalYearStartMonth": 0,
 "graphTooltip": 0,
 "id": null,
 "iteration": 1657202032408,
 "links": [],
 "liveNow": false,
 "panels": [
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 0
     },
     "id": 10,
     "panels": [],
     "title": "Overview",
     "type": "row"
   },
   {
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "thresholds"
         },
         "custom": {
           "align": "auto",
           "displayMode": "auto",
           "inspect": false
         },
         "decimals": 2,
         "displayName": "",
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "short"
       },
       "overrides": [
         {
           "matcher": {
             "id": "byName",
             "options": "Value"
           },
           "properties": [
             {
               "id": "unit",
               "value": "short"
             },
             {
               "id": "decimals",
               "value": 2
             },
             {
               "id": "custom.align"
             }
           ]
         }
       ]
     },
     "gridPos": {
       "h": 4,
       "w": 24,
       "x": 0,
       "y": 1
     },
     "id": 41,
     "options": {
       "footer": {
         "fields": "",
         "reducer": [
           "sum"
         ],
         "show": false
       },
       "showHeader": true
     },
     "pluginVersion": "8.5.6",
     "targets": [
       {
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         },
         "exemplar": false,
         "expr": "label_replace( sum(mongodb_info{group_id=~\"$group_id\", cl_name=~\"$cl_name\", instance=~\"$host.*\"}) by (group_id, org_id, rs_nm, cl_name), \"hostname\", \"$1\", \"instance\", \"(.*)\")\n",
         "format": "table",
         "instant": true,
         "interval": "",
         "legendFormat": "",
         "refId": "A"
       }
     ],
     "title": "Group Metadata",
     "transformations": [
       {
         "id": "organize",
         "options": {
           "excludeByName": {
             "Time": true,
             "Value #A": true,
             "instance": true,
             "rs_nm": false
           },
           "indexByName": {
             "": 2,
             "Time": 0,
             "Value #A": 6,
             "cl_name": 4,
             "group_id": 3,
             "org_id": 1,
             "rs_nm": 5
           },
           "renameByName": {
             "": "Group Name ",
             "Time": "",
             "cl_name": "Cluster Name",
             "group_id": "Group Id",
             "hostname": "Host",
             "instance": "",
             "org_id": "Org Id",
             "process_port": "Port",
             "replica_state": "ReplicaSet State",
             "rs_nm": "ReplicaSet Name"
           }
         }
       },
       {
         "id": "groupBy",
         "options": {
           "fields": {
             "Cluster Name": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Group Id": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Group Name ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Host": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Host ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Org Id": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Replica set state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "ReplicaSet Name": {
               "aggregations": [],
               "operation": "groupby"
             },
             "ReplicaSet State": {
               "aggregations": [],
               "operation": "groupby"
             },
             "host ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "hostname": {
               "aggregations": [],
               "operation": "groupby"
             },
             "instance": {
               "aggregations": [],
               "operation": "groupby"
             },
             "port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "process_port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica set": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica set state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica_state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "rs_nm": {
               "aggregations": [],
               "operation": "groupby"
             }
           }
         }
       },
       {
         "id": "merge",
         "options": {
           "reducers": []
         }
       }
     ],
     "type": "table"
   },
   {
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "thresholds"
         },
         "custom": {
           "align": "auto",
           "displayMode": "auto",
           "inspect": false
         },
         "decimals": 0,
         "displayName": "",
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "none"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 6,
       "w": 24,
       "x": 0,
       "y": 5
     },
     "id": 42,
     "options": {
       "footer": {
         "fields": "",
         "reducer": [
           "sum"
         ],
         "show": false
       },
       "showHeader": true
     },
     "pluginVersion": "8.5.6",
     "targets": [
       {
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         },
         "exemplar": false,
         "expr": "label_replace( sum(mongodb_info{group_id=~\"$group_id\", cl_name=~\"$cl_name\", instance=~\"$host.*\"}) by (instance, replica_state_name, process_port, rs_nm, process_type), \"hostname\", \"$1\", \"instance\", \"(.*):.*\")\n",
         "format": "table",
         "instant": true,
         "interval": "",
         "legendFormat": "",
         "refId": "A"
       }
     ],
     "title": "Cluster host list",
     "transformations": [
       {
         "id": "organize",
         "options": {
           "excludeByName": {
             "Time": true,
             "Value #A": true,
             "instance": false,
             "rs_nm": false
           },
           "indexByName": {
             "Time": 0,
             "Value": 6,
             "instance": 1,
             "process_port": 2,
             "process_type": 4,
             "replica_state_name": 5,
             "rs_nm": 3
           },
           "renameByName": {
             "Time": "",
             "Value": "",
             "hostname": "Host",
             "instance": "Hostname",
             "process_port": "Port",
             "process_type": "Process Type",
             "replica_state": "ReplicaSet State",
             "replica_state_name": "Replica State",
             "rs_nm": "ReplicaSet Name"
           }
         }
       },
       {
         "id": "groupBy",
         "options": {
           "fields": {
             "Host": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Host ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Hostname": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Process Type": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Replica State": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Replica set state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "ReplicaSet Name": {
               "aggregations": [],
               "operation": "groupby"
             },
             "ReplicaSet State": {
               "aggregations": [],
               "operation": "groupby"
             },
             "host ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "hostname": {
               "aggregations": [],
               "operation": "groupby"
             },
             "instance": {
               "aggregations": [],
               "operation": "groupby"
             },
             "port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "process_port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica set": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica set state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica_state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "rs_nm": {
               "aggregations": [],
               "operation": "groupby"
             }
           }
         }
       },
       {
         "id": "merge",
         "options": {
           "reducers": []
         }
       }
     ],
     "type": "table"
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 11
     },
     "id": 8,
     "panels": [],
     "title": "Memory",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of megabytes resident. MMAPv1: It is typical over time, on a dedicated database server, for this number to approach the amount of physical ram on the box. WiredTiger: In a standard deployment resident is the amount of memory used by the WiredTiger cache plus the memory dedicated to other in memory structures used by the mongod process. By default, mongod with WiredTiger reserves 50% of the total physical memory on the server for the cache and at steady state, WiredTiger tries to limit cache usage to 80% of that total. For example, if a server has 16GB of memory, WiredTiger will assume it can use 8GB for cache and at steady state should use about 6.5GB.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "decmbytes"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 12,
       "x": 0,
       "y": 12
     },
     "hiddenSeries": false,
     "id": 2,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_mem_resident{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Memory - Resident",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "decmbytes",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The virtual megabytes for the mongod process. MMAPv1: Generally virtual should be a little larger than mapped (or 2x with --journal), but if virtual is many gigabytes larger, it indicates that excessive memory is being used by other aspects than the memory mapping of files -- that would be bad/suboptimal. The most common case of usage of a high amount of memory for non-mapped is that there are very many connections to the database. Each connection has a thread stack and the memory for those stacks can add up to a considerable amount. WiredTiger: Generally virtual should be a little larger than mapped, but if virtual is many gigabytes larger, it indicates that excessive memory is being used by other aspects than the memory mapping of files -- that would be bad/suboptimal. The most common case of usage of a high amount of memory for non-mapped is that there are very many connections to the database. Each connection has a thread stack and the memory for those stacks can add up to a considerable amount.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "decmbytes"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 12,
       "x": 12,
       "y": 12
     },
     "hiddenSeries": false,
     "id": 72,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_mem_virtual{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Memory - Virtual",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "decmbytes",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 20
     },
     "id": 17,
     "panels": [],
     "title": "Asserts",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of regular asserts raised per second over the selected sample period\n",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 0,
       "y": 21
     },
     "hiddenSeries": false,
     "id": 73,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(mongodb_asserts_regular{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Asserts - Regular",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of warnings per second over the selected sample period",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 6,
       "y": 21
     },
     "hiddenSeries": false,
     "id": 74,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(mongodb_asserts_warning{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Asserts - Warning",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of message asserts per second over the selected sample period. These are internal server errors that have a well defined text string. Stack traces are logged for these",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 12,
       "y": 21
     },
     "hiddenSeries": false,
     "id": 75,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(mongodb_asserts_msg{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Asserts - Message",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of user asserts per second over the selected sample period. These are errors that can be generated by a user such as out of disk space or duplicate key",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 18,
       "y": 21
     },
     "hiddenSeries": false,
     "id": 76,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(mongodb_asserts_user{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Asserts - User",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 29
     },
     "id": 44,
     "panels": [],
     "title": "Cache",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of bytes per second read into WiredTiger's cache over the selected sample period.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "Bps"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 0,
       "y": 30
     },
     "hiddenSeries": false,
     "id": 77,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_wiredTiger_cache_bytes_read_into_cache{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Cache Activity - Read Into",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "Bps",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of bytes per second written from WiredTiger's cache over the selected sample period.\n",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "Bps"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 6,
       "y": 30
     },
     "hiddenSeries": false,
     "id": 78,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_wiredTiger_cache_bytes_written_from_cache{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Cache Activity - Write From",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "Bps",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of bytes currently in the WiredTiger cache.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "bytes"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 12,
       "y": 30
     },
     "hiddenSeries": false,
     "id": 79,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_wiredTiger_cache_bytes_currently_in_the_cache{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Cache Usage - Used",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "bytes",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of tracked dirty bytes currently in the WiredTiger cache.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "bytes"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 18,
       "y": 30
     },
     "hiddenSeries": false,
     "id": 80,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_wiredTiger_cache_tracked_dirty_bytes_in_the_cache{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Cache Usage - Dirty",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "bytes",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 38
     },
     "id": 28,
     "panels": [],
     "title": "Connections",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of currently active connections to this server. A stack is allocated per connection; thus very many connections can result in significant RAM usage.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "none"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 9,
       "w": 24,
       "x": 0,
       "y": 39
     },
     "hiddenSeries": false,
     "id": 81,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_connections_current{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Connections - Current",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "none",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 48
     },
     "id": 30,
     "panels": [],
     "title": "Cursors",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of cursors that the server is maintaining for clients. Because MongoDB exhausts unused cursors, typically this value is small or zero. However, if there is a queue, stale tailable cursors, or a large number of operations this value may rise.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "none"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 13,
       "x": 0,
       "y": 49
     },
     "hiddenSeries": false,
     "id": 82,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_metrics_cursor_open_total{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Cursors - Total Open",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "none",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of cursors that have timed out per second over the selected sample period",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "none"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 11,
       "x": 13,
       "y": 49
     },
     "hiddenSeries": false,
     "id": 83,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_metrics_cursor_timedOut{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Cursors - Timed Out",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "none",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 57
     },
     "id": 32,
     "panels": [],
     "title": "Document Metrics",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate per second of documents returned by queries over the selected sample period.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 0,
       "y": 58
     },
     "hiddenSeries": false,
     "id": 84,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_metrics_document_returned{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Document Metrics - Returned",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate per second of documents inserted over the selected sample period.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 6,
       "y": 58
     },
     "hiddenSeries": false,
     "id": 87,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_metrics_document_inserted{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Document Metrics - Inserted",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate per second of documents updated over the selected sample period.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 12,
       "y": 58
     },
     "hiddenSeries": false,
     "id": 86,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_metrics_document_updated{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Document Metrics - Updated",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate per second of documents deleted over the selected sample period.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 18,
       "y": 58
     },
     "hiddenSeries": false,
     "id": 85,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_metrics_document_deleted{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Document Metrics - Deleted",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 66
     },
     "id": 69,
     "panels": [],
     "title": "Network",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of requests sent to this database server per second over the selected sample period",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 0,
       "y": 67
     },
     "hiddenSeries": false,
     "id": 88,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_network_numRequests{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Network - Num Requests",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of physical (after any wire compression) bytes sent to this database server per second over the selected sample period",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "binBps"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 16,
       "x": 8,
       "y": 67
     },
     "hiddenSeries": false,
     "id": 90,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_network_bytesIn{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "rx - {{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       },
       {
         "expr": "label_replace(-1 * sum(irate(mongodb_network_bytesOut{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "legendFormat": "tx - {{hostname}}:{{process_port}}",
         "refId": "B",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Network - Bytes In",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "binBps",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 75
     },
     "id": 93,
     "panels": [],
     "title": "Opcounters",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of commands performed per second over the selected sample period",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 0,
       "y": 76
     },
     "hiddenSeries": false,
     "id": 96,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_opcounters_command{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Opcounters - Command",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of queries performed per second over the selected sample period",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 8,
       "y": 76
     },
     "hiddenSeries": false,
     "id": 101,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_opcounters_query{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Opcounters - Query",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of updates performed per second over the selected sample period",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 16,
       "y": 76
     },
     "hiddenSeries": false,
     "id": 100,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_opcounters_update{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Opcounters - Update",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of deletes performed per second over the selected sample period",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 0,
       "y": 84
     },
     "hiddenSeries": false,
     "id": 99,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_opcounters_delete{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Opcounters - Delete",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of getMores performed per second on any cursor over the selected sample period. On a primary, this number can be high even if the query count is low as the secondaries \"getMore\" from the primary often as part of replication.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 8,
       "y": 84
     },
     "hiddenSeries": false,
     "id": 97,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_opcounters_getmore{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Opcounters - Getmore",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of inserts performed per second over the selected sample period",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 16,
       "y": 84
     },
     "hiddenSeries": false,
     "id": 98,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_opcounters_insert{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Opcounters - Insert",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 92
     },
     "id": 95,
     "panels": [],
     "title": "Operation Execution Times",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average execution time in milliseconds per read operation over the selected sample period.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "µs"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 0,
       "y": 93
     },
     "hiddenSeries": false,
     "id": 102,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_opLatencies_reads_latency{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])/irate(mongodb_opLatencies_reads_ops{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Operation Execution Times - Avg Ms/Read",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "µs",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average execution time in milliseconds per write operation over the selected sample period.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "µs"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 8,
       "y": 93
     },
     "hiddenSeries": false,
     "id": 104,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_opLatencies_writes_latency{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])/irate(mongodb_opLatencies_writes_ops{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Operation Execution Times - Avg Ms/Write",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "µs",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average execution time in milliseconds per command operation over the selected sample period.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "µs"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 16,
       "y": 93
     },
     "hiddenSeries": false,
     "id": 103,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_opLatencies_commands_latency{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])/irate(mongodb_opLatencies_commands_ops{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Operation Execution Times - Avg Ms/Command",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "µs",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 101
     },
     "id": 106,
     "panels": [],
     "title": "Page Faults",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate of page faults on this process per second over the selected sample period. In non-Windows environments this is hard page faults only.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 24,
       "x": 0,
       "y": 102
     },
     "hiddenSeries": false,
     "id": 107,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_extra_info_page_faults{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Page Faults",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 110
     },
     "id": 111,
     "panels": [],
     "title": "Query Executor",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate per second over the selected sample period of index items scanned during queries and query-plan evaluation. This rate is driven by the same value as totalKeysExamined in the output of explain().",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 12,
       "x": 0,
       "y": 111
     },
     "hiddenSeries": false,
     "id": 108,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_metrics_queryExecutor_scanned{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Query Executor - Scanned",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate per second over the selected sample period of documents scanned during queries and query-plan evaluation. This rate is driven by the same value as totalDocsExamined in the output of explain().",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 12,
       "x": 12,
       "y": 111
     },
     "hiddenSeries": false,
     "id": 109,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_metrics_queryExecutor_scannedObjects{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Query Executor - Scanned Objects",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 119
     },
     "id": 113,
     "panels": [],
     "title": "Queues",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of operations queued waiting for any lock",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "none"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 0,
       "y": 120
     },
     "hiddenSeries": false,
     "id": 114,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_globalLock_currentQueue_total{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Queues - Total",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "none",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of operations queued waiting for a read lock",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "none"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 8,
       "y": 120
     },
     "hiddenSeries": false,
     "id": 115,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_globalLock_currentQueue_readers{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Queues - Readers",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "none",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of operations queued waiting for a write lock",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "none"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 8,
       "x": 16,
       "y": 120
     },
     "hiddenSeries": false,
     "id": 116,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_globalLock_currentQueue_writers{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Queues - Writers",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "none",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 128
     },
     "id": 118,
     "panels": [],
     "title": "Scan and Order",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The average rate per second over the selected sample period of queries that return sorted results that cannot perform the sort operation using an index.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "/s"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 24,
       "x": 0,
       "y": 129
     },
     "hiddenSeries": false,
     "id": 119,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(irate(mongodb_metrics_operation_scanAndOrder{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}[$Interval])) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Scan and Order",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "/s",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "collapsed": false,
     "datasource": {
       "type": "prometheus",
       "uid": "000000010"
     },
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 137
     },
     "id": 123,
     "panels": [],
     "title": "Tickets Available",
     "type": "row"
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of read tickets available to the WiredTiger storage engine. Read tickets represent the number of concurrent read operations allowed into the storage engine. When this value reaches zero new read requests may queue until a read ticket becomes available.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "none"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 12,
       "x": 0,
       "y": 138
     },
     "hiddenSeries": false,
     "id": 120,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_wiredTiger_concurrentTransactions_read_available{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Tickets Available - Reads",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "none",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   },
   {
     "aliasColors": {},
     "bars": false,
     "dashLength": 10,
     "dashes": false,
     "datasource": {
       "type": "prometheus",
       "uid": "${DS_PROMETHEUS}"
     },
     "description": "The number of write tickets available to the WiredTiger storage engine. Write tickets represent the number of concurrent write operations allowed into the storage engine. When this value reaches zero new write requests may queue until a write ticket becomes available.",
     "fieldConfig": {
       "defaults": {
         "links": [],
         "unit": "none"
       },
       "overrides": []
     },
     "fill": 1,
     "fillGradient": 0,
     "gridPos": {
       "h": 8,
       "w": 12,
       "x": 12,
       "y": 138
     },
     "hiddenSeries": false,
     "id": 121,
     "legend": {
       "avg": false,
       "current": false,
       "max": false,
       "min": false,
       "show": true,
       "total": false,
       "values": false
     },
     "lines": true,
     "linewidth": 1,
     "nullPointMode": "null",
     "options": {
       "alertThreshold": true,
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "percentage": false,
     "pluginVersion": "8.5.6",
     "pointradius": 2,
     "points": false,
     "renderer": "flot",
     "seriesOverrides": [],
     "spaceLength": 10,
     "stack": false,
     "steppedLine": false,
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(mongodb_wiredTiger_concurrentTransactions_write_available{group_id=~\"$group_id\", cl_name=~\"$cl_name\", rs_nm=~\"$rs_nm\", instance=~\"$host.*\",  process_port=~\"$process_port\"}) by (instance, process_port) , \"hostname\", \"$1\", \"instance\", \"(.*)\")",
         "interval": "",
         "legendFormat": "{{hostname}}:{{process_port}}",
         "refId": "A",
         "datasource": {
           "type": "prometheus",
           "uid": "${DS_PROMETHEUS}"
         }
       }
     ],
     "thresholds": [],
     "timeRegions": [],
     "title": "Tickets Available - Writes",
     "tooltip": {
       "shared": true,
       "sort": 0,
       "value_type": "individual"
     },
     "type": "graph",
     "xaxis": {
       "mode": "time",
       "show": true,
       "values": []
     },
     "yaxes": [
       {
         "format": "none",
         "logBase": 1,
         "show": true
       },
       {
         "format": "short",
         "logBase": 1,
         "show": true
       }
     ],
     "yaxis": {
       "align": false
     }
   }
 ],
 "schemaVersion": 36,
 "style": "dark",
 "tags": [],
 "templating": {
   "list": [
     {
       "auto": true,
       "auto_count": 30,
       "auto_min": "1m",
       "current": {
         "selected": false,
         "text": "1m",
         "value": "1m"
       },
       "hide": 0,
       "name": "Interval",
       "options": [
         {
           "selected": false,
           "text": "auto",
           "value": "$__auto_interval_Interval"
         },
         {
           "selected": false,
           "text": "30s",
           "value": "30s"
         },
         {
           "selected": true,
           "text": "1m",
           "value": "1m"
         },
         {
           "selected": false,
           "text": "5m",
           "value": "5m"
         },
         {
           "selected": false,
           "text": "1h",
           "value": "1h"
         },
         {
           "selected": false,
           "text": "1d",
           "value": "1d"
         }
       ],
       "query": "30s,1m,5m,1h,1d",
       "queryValue": "",
       "refresh": 2,
       "skipUrlSync": false,
       "type": "interval"
     },
     {
       "current": {
         "selected": false,
         "text": "thanos",
         "value": "thanos"
       },
       "hide": 0,
       "includeAll": false,
       "multi": false,
       "name": "Datasource",
       "options": [],
       "query": "prometheus",
       "queryValue": "",
       "refresh": 1,
       "regex": "/thanos.*/",
       "skipUrlSync": false,
       "type": "datasource"
     },
     {
       "current": {},
       "datasource": {
         "type": "prometheus",
         "uid": "$Datasource"
       },
       "definition": "label_values(mongodb_up, job)",
       "hide": 0,
       "includeAll": false,
       "multi": false,
       "name": "job",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up, job)",
         "refId": "thanos-job-Variable-Query"
       },
       "refresh": 2,
       "regex": "",
       "skipUrlSync": false,
       "sort": 0,
       "tagValuesQuery": "",
       "tagsQuery": "",
       "type": "query",
       "useTags": false
     },
     {
       "current": {},
       "datasource": {
         "type": "prometheus",
         "uid": "$Datasource"
       },
       "definition": "label_values(mongodb_up{job=\"$job\"}, group_id)",
       "hide": 0,
       "includeAll": false,
       "label": "Group Id",
       "multi": false,
       "name": "group_id",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up{job=\"$job\"}, group_id)",
         "refId": "thanos-group_id-Variable-Query"
       },
       "refresh": 1,
       "regex": "",
       "skipUrlSync": false,
       "sort": 5,
       "tagValuesQuery": "",
       "tagsQuery": "",
       "type": "query",
       "useTags": false
     },
     {
       "current": {},
       "datasource": {
         "type": "prometheus",
         "uid": "$Datasource"
       },
       "definition": "label_values(mongodb_up{group_id='$group_id'}, cl_name)",
       "hide": 0,
       "includeAll": false,
       "label": "Cluster Name",
       "multi": false,
       "name": "cl_name",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up{group_id='$group_id'}, cl_name)",
         "refId": "thanos-cl_name-Variable-Query"
       },
       "refresh": 2,
       "regex": "",
       "skipUrlSync": false,
       "sort": 5,
       "tagValuesQuery": "",
       "tagsQuery": "",
       "type": "query",
       "useTags": false
     },
     {
       "current": {},
       "datasource": {
         "type": "prometheus",
         "uid": "$Datasource"
       },
       "definition": "label_values(mongodb_up{group_id='$group_id', cl_name='$cl_name'}, rs_nm)",
       "hide": 0,
       "includeAll": true,
       "label": "ReplicaSet Name",
       "multi": true,
       "name": "rs_nm",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up{group_id='$group_id', cl_name='$cl_name'}, rs_nm)",
         "refId": "thanos-rs_nm-Variable-Query"
       },
       "refresh": 1,
       "regex": "",
       "skipUrlSync": false,
       "sort": 5,
       "tagValuesQuery": "",
       "tagsQuery": "",
       "type": "query",
       "useTags": false
     },
     {
       "current": {},
       "datasource": {
         "type": "prometheus",
         "uid": "$Datasource"
       },
       "definition": "label_values(mongodb_up{group_id='$group_id', cl_name='$cl_name',rs_nm='$rs_nm'},instance)",
       "hide": 0,
       "includeAll": true,
       "label": "Host",
       "multi": true,
       "name": "host",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up{group_id='$group_id', cl_name='$cl_name',rs_nm='$rs_nm'},instance)",
         "refId": "thanos-host-Variable-Query"
       },
       "refresh": 2,
       "regex": "",
       "skipUrlSync": false,
       "sort": 5,
       "tagValuesQuery": "",
       "tagsQuery": "",
       "type": "query",
       "useTags": false
     },
     {
       "current": {},
       "datasource": {
         "type": "prometheus",
         "uid": "$Datasource"
       },
       "definition": "label_values(mongodb_up{group_id='$group_id', cl_name='$cl_name',rs_nm='$rs_nm'},process_port)",
       "description": "Only applicable for process level metrics",
       "hide": 0,
       "includeAll": true,
       "label": "Process Port",
       "multi": true,
       "name": "process_port",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up{group_id='$group_id', cl_name='$cl_name',rs_nm='$rs_nm'},process_port)",
         "refId": "thanos-process_port-Variable-Query"
       },
       "refresh": 1,
       "regex": "",
       "skipUrlSync": false,
       "sort": 5,
       "tagValuesQuery": "",
       "tagsQuery": "",
       "type": "query",
       "useTags": false
     }
   ]
 },
 "time": {
   "from": "now-6h",
   "to": "now"
 },
 "timepicker": {
   "refresh_intervals": [
     "5s",
     "10s",
     "30s",
     "1m",
     "5m",
     "15m",
     "30m",
     "1h",
     "2h",
     "1d"
   ]
 },
 "timezone": "",
 "title": "Ops Manager Clusters - Mongo Metrics",
 "uid": "W0lo7Gx7z",
 "version": 17,
 "weekStart": ""
}
```

```json
{
 "annotations": {
   "list": [
     {
       "builtIn": 1,
       "datasource": "-- Grafana --",
       "enable": true,
       "hide": true,
       "iconColor": "rgba(0, 211, 255, 1)",
       "name": "Annotations & Alerts",
       "target": {
         "limit": 100,
         "matchAny": false,
         "tags": [],
         "type": "dashboard"
       },
       "type": "dashboard"
     }
   ]
 },
 "description": "",
 "editable": true,
 "fiscalYearStartMonth": 0,
 "gnetId": null,
 "graphTooltip": 0,
 "id": 8,
 "iteration": 1639495636182,
 "links": [],
 "liveNow": false,
 "panels": [
   {
     "collapsed": false,
     "datasource": null,
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 0
     },
     "id": 10,
     "panels": [],
     "title": "Overview",
     "type": "row"
   },
   {
     "datasource": null,
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "thresholds"
         },
         "custom": {
           "align": "auto",
           "displayMode": "color-text",
           "filterable": false
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         }
       },
       "overrides": [
         {
           "matcher": {
             "id": "byName",
             "options": "instance"
           },
           "properties": [
             {
               "id": "custom.width",
               "value": 409
             }
           ]
         }
       ]
     },
     "gridPos": {
       "h": 3,
       "w": 11,
       "x": 0,
       "y": 1
     },
     "id": 41,
     "options": {
       "frameIndex": 0,
       "showHeader": true,
       "sortBy": [
         {
           "desc": true,
           "displayName": "Value #A"
         }
       ]
     },
     "pluginVersion": "8.2.2",
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(mongodb_up{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (group_name, group_id, org_id, replica_set_name, cluster_name), \"hostname\", \"$1\", \"instance\", \"(.*):.*\")\n",
         "format": "table",
         "interval": "",
         "legendFormat": "",
         "refId": "A"
       }
     ],
     "title": "Group Metadata",
     "transformations": [
       {
         "id": "organize",
         "options": {
           "excludeByName": {
             "Time": true,
             "Value #A": true,
             "instance": true,
             "replica_set_name": false
           },
           "indexByName": {
             "Time": 0,
             "Value #A": 6,
             "cluster_name": 4,
             "group_id": 3,
             "group_name": 2,
             "org_id": 1,
             "replica_set_name": 5
           },
           "renameByName": {
             "Time": "",
             "cluster_name": "Cluster Name",
             "group_id": "Group Id",
             "group_name": "Group Name ",
             "hostname": "Host",
             "instance": "",
             "org_id": "Org Id",
             "process_port": "Port",
             "replica_set_name": "ReplicaSet Name",
             "replica_state": "ReplicaSet State"
           }
         }
       },
       {
         "id": "groupBy",
         "options": {
           "fields": {
             "Cluster Name": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Group Id": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Group Name ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Host": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Host ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Org Id": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Replica set state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "ReplicaSet Name": {
               "aggregations": [],
               "operation": "groupby"
             },
             "ReplicaSet State": {
               "aggregations": [],
               "operation": "groupby"
             },
             "host ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "hostname": {
               "aggregations": [],
               "operation": "groupby"
             },
             "instance": {
               "aggregations": [],
               "operation": "groupby"
             },
             "port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "process_port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica set": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica set state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica_set_name": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica_state": {
               "aggregations": [],
               "operation": "groupby"
             }
           }
         }
       }
     ],
     "type": "table"
   },
   {
     "datasource": null,
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "thresholds"
         },
         "custom": {
           "align": "auto",
           "displayMode": "color-text",
           "filterable": false
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         }
       },
       "overrides": [
         {
           "matcher": {
             "id": "byName",
             "options": "instance"
           },
           "properties": [
             {
               "id": "custom.width",
               "value": 409
             }
           ]
         },
         {
           "matcher": {
             "id": "byName",
             "options": "Port"
           },
           "properties": [
             {
               "id": "custom.width",
               "value": 80
             }
           ]
         },
         {
           "matcher": {
             "id": "byName",
             "options": "ReplicaSet State"
           },
           "properties": [
             {
               "id": "custom.width",
               "value": 135
             }
           ]
         },
         {
           "matcher": {
             "id": "byName",
             "options": "ReplicaSet Name"
           },
           "properties": [
             {
               "id": "custom.width",
               "value": 198
             }
           ]
         },
         {
           "matcher": {
             "id": "byName",
             "options": "Host"
           },
           "properties": [
             {
               "id": "custom.width",
               "value": 356
             }
           ]
         }
       ]
     },
     "gridPos": {
       "h": 5,
       "w": 13,
       "x": 11,
       "y": 1
     },
     "id": 42,
     "options": {
       "frameIndex": 0,
       "showHeader": true,
       "sortBy": []
     },
     "pluginVersion": "8.2.2",
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(mongodb_up{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance, replica_state, process_port, replica_set_name, process_type), \"hostname\", \"$1\", \"instance\", \"(.*):.*\")\n",
         "format": "table",
         "interval": "",
         "legendFormat": "",
         "refId": "A"
       }
     ],
     "title": "Cluster host list",
     "transformations": [
       {
         "id": "organize",
         "options": {
           "excludeByName": {
             "Time": true,
             "Value #A": true,
             "instance": true,
             "process_type": false,
             "replica_set_name": false
           },
           "indexByName": {
             "Time": 0,
             "Value #A": 6,
             "hostname": 1,
             "instance": 2,
             "process_port": 3,
             "replica_set_name": 5,
             "replica_state": 4
           },
           "renameByName": {
             "Time": "",
             "hostname": "Host",
             "instance": "",
             "process_port": "Port",
             "process_type": "Type",
             "replica_set_name": "ReplicaSet Name",
             "replica_state": "ReplicaSet State"
           }
         }
       },
       {
         "id": "groupBy",
         "options": {
           "fields": {
             "Host": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Host ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Replica set state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "ReplicaSet Name": {
               "aggregations": [],
               "operation": "groupby"
             },
             "ReplicaSet State": {
               "aggregations": [],
               "operation": "groupby"
             },
             "Type": {
               "aggregations": [],
               "operation": "groupby"
             },
             "host ": {
               "aggregations": [],
               "operation": "groupby"
             },
             "hostname": {
               "aggregations": [],
               "operation": "groupby"
             },
             "instance": {
               "aggregations": [],
               "operation": "groupby"
             },
             "port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "process_port": {
               "aggregations": [],
               "operation": "groupby"
             },
             "process_type": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica set": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica set state": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica_set_name": {
               "aggregations": [],
               "operation": "groupby"
             },
             "replica_state": {
               "aggregations": [],
               "operation": "groupby"
             }
           }
         }
       }
     ],
     "type": "table"
   },
   {
     "collapsed": false,
     "datasource": null,
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 6
     },
     "id": 8,
     "panels": [],
     "title": "System Memory",
     "type": "row"
   },
   {
     "datasource": null,
     "description": "The number of kilobytes of used shared memory (shared between several processes, thus including RAM disks, SYS-V-IPC and BSD like SHMEM)",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "deckbytes"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 0,
       "y": 7
     },
     "id": 2,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(hardware_system_memory_shared_mem_kilobytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System Memory - Shared",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The number of kilobytes of buffer cache, relatively temporary storage for raw disk blocks",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "deckbytes"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 6,
       "y": 7
     },
     "id": 6,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(hardware_system_memory_buffers_kilobytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System Memory - Buffers",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The number of kilobytes in the page cache.",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "deckbytes"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 12,
       "y": 7
     },
     "id": 11,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace (sum(hardware_system_memory_cached_kilobytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System Memory - Cached",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The number of kilobytes of physical memory in use\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "deckbytes"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 0,
       "y": 15
     },
     "id": 13,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(hardware_system_memory_mem_total_kilobytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance) - sum(hardware_system_memory_mem_free_kilobytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System Memory - Used",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The total amount of swap space in free and used, measured in kilobytes\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "deckbytes"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 6,
       "y": 15
     },
     "id": 37,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(hardware_system_memory_swap_total_kilobytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance) - sum(hardware_system_memory_swap_free_kilobytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "swap used for host - {{hostname}}",
         "refId": "A"
       },
       {
         "exemplar": true,
         "expr": "label_replace (sum(hardware_system_memory_swap_free_kilobytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "hide": false,
         "interval": "",
         "legendFormat": "swap free for host - {{hostname}}",
         "refId": "B"
       }
     ],
     "title": "System Memory - Swap",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "An estimate of the number of kilobytes of system memory available for running new applications, without swapping",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "deckbytes"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 12,
       "y": 15
     },
     "id": 15,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(hardware_system_memory_mem_available_kilobytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System Memory - Available",
     "type": "timeseries"
   },
   {
     "collapsed": false,
     "datasource": null,
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 23
     },
     "id": 17,
     "panels": [],
     "title": "System CPU",
     "type": "row"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU had something runnable, but the hypervisor chose to run something else. For servers with more than 1 CPU core, this value can exceed 100%.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": [
         {
           "__systemRef": "hideSeriesFrom",
           "matcher": {
             "id": "byNames",
             "options": {
               "mode": "exclude",
               "names": [
                 "host - banana-shard-00-01.faplr.mmscloudteam.com"
               ],
               "prefix": "All except:",
               "readOnly": true
             }
           },
           "properties": [
             {
               "id": "custom.hideFrom",
               "value": {
                 "legend": false,
                 "tooltip": false,
                 "viz": true
               }
             }
           ]
         }
       ]
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 0,
       "y": 24
     },
     "id": 19,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_steal_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / 10) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System cpu - steal",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing guest, which is included in user. For servers with more than 1 CPU core, this value can exceed 100%.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 5,
       "y": 24
     },
     "id": 20,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_guest_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / 10) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System cpu - guest",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent performing software interrupts. For servers with more than 1 CPU core, this value can exceed 100%.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 10,
       "y": 24
     },
     "id": 21,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_soft_irq_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / 10) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System cpu - softirq",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent performing hardware interrupts. For servers with more than 1 CPU core, this value can exceed 100%.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 15,
       "y": 24
     },
     "id": 22,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_irq_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / 10) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System cpu - irq",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent waiting for IO operations to complete. For servers with more than 1 CPU core, this value can exceed 100%\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 0,
       "y": 31
     },
     "id": 23,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(hardware_system_cpu_io_wait_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / 10) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System cpu - iowait",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent occupied by all processes with a positive nice value. For servers with more than 1 CPU core, this value can exceed 100%.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 5,
       "y": 31
     },
     "id": 24,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_nice_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / 10) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System cpu - nice",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing operating system calls from all processes. For servers with more than 1 CPU core, this value can exceed 100%.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 10,
       "y": 31
     },
     "id": 25,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_kernel_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / 10) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System cpu - kernel",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing all user applications (not just MongoDB processes). For servers with more than 1 CPU core, this value can exceed 100%.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 15,
       "y": 31
     },
     "id": 26,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_user_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / 10) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "System cpu - user",
     "type": "timeseries"
   },
   {
     "collapsed": false,
     "datasource": null,
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 38
     },
     "id": 44,
     "panels": [],
     "title": "Normalized System Cpu",
     "type": "row"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU had something runnable, but the hypervisor chose to run something else. It is scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": [
         {
           "__systemRef": "hideSeriesFrom",
           "matcher": {
             "id": "byNames",
             "options": {
               "mode": "exclude",
               "names": [
                 "host - banana-shard-00-01.faplr.mmscloudteam.com"
               ],
               "prefix": "All except:",
               "readOnly": true
             }
           },
           "properties": [
             {
               "id": "custom.hideFrom",
               "value": {
                 "legend": false,
                 "tooltip": false,
                 "viz": true
               }
             }
           ]
         }
       ]
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 0,
       "y": 39
     },
     "id": 46,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_steal_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / (10 * hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\"})) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Normalized System cpu - steal",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing guest, which is included in user. It is scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 5,
       "y": 39
     },
     "id": 47,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_guest_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / (10 * hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\"})) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Normalized System cpu - guest",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent performing software interrupts. It is scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 10,
       "y": 39
     },
     "id": 48,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_soft_irq_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / (10 * hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\"})) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Normalized System cpu - softirq",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent performing hardware interrupts. It is scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 15,
       "y": 39
     },
     "id": 49,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_irq_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / (10 * hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\"})) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Normalized System cpu - irq",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent waiting for IO operations to complete. It is scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 0,
       "y": 46
     },
     "id": 51,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(hardware_system_cpu_io_wait_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / (10 * hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\"})) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Normalized System cpu - iowait",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent occupied by all processes with a positive nice value. It is scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 5,
       "y": 46
     },
     "id": 52,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_nice_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / (10 * hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\"})) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Normalized System cpu - nice",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing operating system calls from all processes. It is scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 10,
       "y": 46
     },
     "id": 53,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_kernel_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / (10 * hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\"})) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Normalized System cpu - kernel",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing all user applications (not just MongoDB processes). It is scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 5,
       "x": 15,
       "y": 46
     },
     "id": 50,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_cpu_user_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / (10 * hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\"})) by (instance) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Normalized System cpu - user",
     "type": "timeseries"
   },
   {
     "collapsed": false,
     "datasource": null,
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 53
     },
     "id": 28,
     "panels": [],
     "title": "System Network",
     "type": "row"
   },
   {
     "datasource": null,
     "description": "The average rate of physical bytes received per second by the eth0 network interface\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "Bps"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 9,
       "w": 10,
       "x": 0,
       "y": 54
     },
     "id": 73,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_network_eth0_bytes_in_bytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval])) by (instance) + sum(rate(hardware_system_network_lo_bytes_in_bytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval])) by (instance), \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Network bytes In",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The average rate of physical bytes transmitted per second by the eth0 network interface",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "Bps"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 9,
       "w": 10,
       "x": 10,
       "y": 54
     },
     "id": 74,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_system_network_eth0_bytes_out_bytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval])) by (instance) + sum(rate(hardware_system_network_lo_bytes_out_bytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval])) by (instance), \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}}",
         "refId": "A"
       }
     ],
     "title": "Network bytes Out",
     "type": "timeseries"
   },
   {
     "collapsed": false,
     "datasource": null,
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 63
     },
     "id": 30,
     "panels": [],
     "title": "System Disk",
     "type": "row"
   },
   {
     "datasource": null,
     "description": "The total bytes of free disk space on the disk partition used by MongoDB.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "decbytes"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 0,
       "y": 64
     },
     "id": 14,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(hardware_disk_metrics_disk_space_free_bytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance, disk_name) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "disk - {{disk_name}}, host - {{hostname}} ",
         "refId": "A"
       }
     ],
     "title": "System Disk - Free",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percent of free disk space on the partition used by MongoDB.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 6,
       "y": 64
     },
     "id": 71,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(hardware_disk_metrics_disk_space_free_bytes{group_id=~\"$group_id\",  instance=~\"$host.*\"} / (hardware_disk_metrics_disk_space_used_bytes{group_id=~\"$group_id\",  instance=~\"$host.*\"} + hardware_disk_metrics_disk_space_free_bytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) * 100) by (instance, disk_name) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "disk - {{disk_name}}, host - {{hostname}} ",
         "refId": "A"
       }
     ],
     "title": "System Disk Percent Free",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The total bytes of used disk space on the partition that runs MongoDB.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "decbytes"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 12,
       "y": 64
     },
     "id": 36,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(hardware_disk_metrics_disk_space_used_bytes{group_id=~\"$group_id\",  instance=~\"$host.*\"}) by (instance, disk_name) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "disk - {{disk_name}} host - {{hostname}} ",
         "refId": "A"
       }
     ],
     "title": "System Disk - Used",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The write throughput of I/O operations per second for the disk partition used for MongoDB.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "/ sec"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 18,
       "y": 64
     },
     "id": 63,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_disk_metrics_write_count{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval])) by (instance, disk_name) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "hide": false,
         "interval": "",
         "legendFormat": "disk - {{disk_name}} host - {{hostname}} ",
         "refId": "B"
       }
     ],
     "title": "System Disk Write IOPS",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The write latency in milliseconds of the disk partition used by MongoDB.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "ms"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 0,
       "y": 72
     },
     "id": 64,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_disk_metrics_write_time_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / rate(hardware_disk_metrics_write_count{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval])) by (instance, disk_name), \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "hide": false,
         "interval": "",
         "legendFormat": "disk - {{disk_name}} host - {{hostname}} ",
         "refId": "B"
       }
     ],
     "title": "System Disk Write Latency",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The Read latency in milliseconds of the disk partition used by MongoDB.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "ms"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 6,
       "y": 72
     },
     "id": 65,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_disk_metrics_read_time_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) / rate(hardware_disk_metrics_read_count{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval])) by (instance, disk_name), \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "hide": false,
         "interval": "",
         "legendFormat": "disk - {{disk_name}} host - {{hostname}} ",
         "refId": "B"
       }
     ],
     "title": "System Disk Read Latency",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The read throughput of I/O operations per second for the disk partition used for MongoDB.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "/ sec"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 12,
       "y": 72
     },
     "id": 62,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_disk_metrics_read_count{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval])) by (instance, disk_name) , \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "disk - {{disk_name}} host - {{hostname}} ",
         "refId": "A"
       }
     ],
     "title": "System Disk Read IOPS",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time during which requests are being issued to and serviced by the partition. This includes requests from any process, not just MongoDB processes.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 18,
       "y": 72
     },
     "id": 67,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_disk_metrics_total_time_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) ) by (instance, disk_name) / 10, \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "hide": false,
         "interval": "",
         "legendFormat": "disk - {{disk_name}} host - {{hostname}} ",
         "refId": "B"
       }
     ],
     "title": "System Disk Util %",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The average length of queue of requests issued to the disk partition used by MongoDB.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "ms"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 8,
       "w": 6,
       "x": 0,
       "y": 80
     },
     "id": 66,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace( sum(rate(hardware_disk_metrics_weighted_time_io_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\"}[$interval]) ) by (instance, DiskName), \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "hide": false,
         "interval": "",
         "legendFormat": "disk - {{disk_name}} host - {{hostname}} ",
         "refId": "B"
       }
     ],
     "title": "System Disk Queue Depth",
     "type": "timeseries"
   },
   {
     "collapsed": false,
     "datasource": null,
     "gridPos": {
       "h": 1,
       "w": 24,
       "x": 0,
       "y": 88
     },
     "id": 32,
     "panels": [],
     "title": "Process CPU",
     "type": "row"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing this MongoDB process, scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 6,
       "x": 0,
       "y": 89
     },
     "id": 54,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace((sum(rate(hardware_process_cpu_user_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\", process_port=~\"$process_port\" } [$interval])) by (instance, process_port)  / on(instance) group_left  hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\" })/10, \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}} port - {{process_port}}",
         "refId": "A"
       }
     ],
     "title": "Normalized Process cpu - user",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 6,
       "x": 6,
       "y": 89
     },
     "id": 58,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace((sum(rate(hardware_process_cpu_children_user_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\", process_port=~\"$process_port\" } [$interval])) by (instance, process_port)  / on(instance) group_left  hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\" })/10, \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}} port - {{process_port}}",
         "refId": "A"
       }
     ],
     "title": "Normalized Process cpu - children user",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing operating system calls for this MongoDB process, scaled to a range of 0-100% by dividing by the number of CPU cores.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 6,
       "x": 12,
       "y": 89
     },
     "id": 55,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace((sum(rate(hardware_process_cpu_kernel_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\", process_port=~\"$process_port\" } [$interval])) by (instance, process_port)  / on(instance) group_left  hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\" })/10, \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}} port - {{process_port}}",
         "refId": "A"
       }
     ],
     "title": "Normalized Process cpu - kernel",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 6,
       "x": 18,
       "y": 89
     },
     "id": 57,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace((sum(rate(hardware_process_cpu_children_kernel_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\", process_port=~\"$process_port\" } [$interval])) by (instance, process_port)  / on(instance) group_left  hardware_platform_num_logical_cpus{group_id=~\"$group_id\",  instance=~\"$host.*\" })/10, \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}} port - {{process_port}}",
         "refId": "A"
       }
     ],
     "title": "Normalized Process cpu - children kernel",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing this MongoDB process. For servers with more than 1 CPU core, this value can exceed 100%.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 6,
       "x": 0,
       "y": 96
     },
     "id": 56,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(hardware_process_cpu_user_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\", process_port=~\"$process_port\" } [$interval])) by (instance, process_port)  / 10, \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}} port - {{process_port}}",
         "refId": "A"
       }
     ],
     "title": "Process cpu - user",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 6,
       "x": 6,
       "y": 96
     },
     "id": 59,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(hardware_process_cpu_children_user_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\", process_port=~\"$process_port\" } [$interval])) by (instance, process_port)  / 10, \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}} port - {{process_port}}",
         "refId": "A"
       }
     ],
     "title": "Process cpu - child user",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "The percentage of time the CPU spent servicing operating system calls for this MongoDB process. For servers with more than 1 CPU core, this value can exceed 100%.\n",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 6,
       "x": 12,
       "y": 96
     },
     "id": 60,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(hardware_process_cpu_kernel_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\", process_port=~\"$process_port\" } [$interval])) by (instance, process_port)  / 10, \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}} port - {{process_port}}",
         "refId": "A"
       }
     ],
     "title": "Process cpu - kernel",
     "type": "timeseries"
   },
   {
     "datasource": null,
     "description": "",
     "fieldConfig": {
       "defaults": {
         "color": {
           "mode": "palette-classic"
         },
         "custom": {
           "axisLabel": "",
           "axisPlacement": "auto",
           "barAlignment": 0,
           "drawStyle": "line",
           "fillOpacity": 0,
           "gradientMode": "none",
           "hideFrom": {
             "legend": false,
             "tooltip": false,
             "viz": false
           },
           "lineInterpolation": "linear",
           "lineWidth": 1,
           "pointSize": 5,
           "scaleDistribution": {
             "type": "linear"
           },
           "showPoints": "auto",
           "spanNulls": false,
           "stacking": {
             "group": "A",
             "mode": "none"
           },
           "thresholdsStyle": {
             "mode": "off"
           }
         },
         "mappings": [],
         "thresholds": {
           "mode": "absolute",
           "steps": [
             {
               "color": "green",
               "value": null
             },
             {
               "color": "red",
               "value": 80
             }
           ]
         },
         "unit": "percent"
       },
       "overrides": []
     },
     "gridPos": {
       "h": 7,
       "w": 6,
       "x": 18,
       "y": 96
     },
     "id": 61,
     "options": {
       "legend": {
         "calcs": [],
         "displayMode": "list",
         "placement": "bottom"
       },
       "tooltip": {
         "mode": "single"
       }
     },
     "targets": [
       {
         "exemplar": true,
         "expr": "label_replace(sum(rate(hardware_process_cpu_children_kernel_milliseconds{group_id=~\"$group_id\",  instance=~\"$host.*\", process_port=~\"$process_port\" } [$interval])) by (instance, process_port)  / 10, \"hostname\", \"$1\", \"instance\", \"(.*):.*\")",
         "interval": "",
         "legendFormat": "host - {{hostname}} port - {{process_port}}",
         "refId": "A"
       }
     ],
     "title": "Process cpu - children kernel",
     "type": "timeseries"
   }
 ],
 "refresh": false,
 "schemaVersion": 31,
 "style": "dark",
 "tags": [],
 "templating": {
   "list": [
     {
       "current": {
         "selected": false,
         "text": "Prometheus",
         "value": "Prometheus"
       },
       "description": null,
       "error": null,
       "hide": 0,
       "includeAll": false,
       "label": null,
       "multi": false,
       "name": "Datasource",
       "options": [],
       "query": "prometheus",
       "queryValue": "",
       "refresh": 1,
       "regex": "",
       "skipUrlSync": false,
       "type": "datasource"
     },
     {
       "allValue": null,
       "current": {
         "selected": false,
         "text": "611c15fc5851c22d37e3f351",
         "value": "611c15fc5851c22d37e3f351"
       },
       "datasource": null,
       "definition": "label_values(group_id)",
       "description": null,
       "error": null,
       "hide": 0,
       "includeAll": false,
       "label": "Group Id",
       "multi": false,
       "name": "group_id",
       "options": [],
       "query": {
         "query": "label_values(group_id)",
         "refId": "StandardVariableQuery"
       },
       "refresh": 1,
       "regex": "",
       "skipUrlSync": false,
       "sort": 0,
       "type": "query"
     },
     {
       "allValue": null,
       "current": {
         "selected": false,
         "text": "Cluster0",
         "value": "Cluster0"
       },
       "datasource": null,
       "definition": "label_values(mongodb_up{group_id='$group_id'}, cluster_name)",
       "description": null,
       "error": null,
       "hide": 0,
       "includeAll": false,
       "label": "Cluster Name",
       "multi": false,
       "name": "cluster_name",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up{group_id='$group_id'}, cluster_name)",
         "refId": "StandardVariableQuery"
       },
       "refresh": 2,
       "regex": "",
       "skipUrlSync": false,
       "sort": 0,
       "type": "query"
     },
     {
       "allValue": null,
       "current": {
         "selected": true,
         "text": [
           "All"
         ],
         "value": [
           "$__all"
         ]
       },
       "datasource": null,
       "definition": "label_values(mongodb_up{group_id='$group_id', cluster_name='$cluster_name'}, replica_set_name)",
       "description": null,
       "error": null,
       "hide": 0,
       "includeAll": true,
       "label": "Replica set name",
       "multi": true,
       "name": "replica_set_name",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up{group_id='$group_id', cluster_name='$cluster_name'}, replica_set_name)",
         "refId": "StandardVariableQuery"
       },
       "refresh": 2,
       "regex": "",
       "skipUrlSync": false,
       "sort": 0,
       "type": "query"
     },
     {
       "allValue": null,
       "current": {
         "selected": true,
         "text": [
           "All"
         ],
         "value": [
           "$__all"
         ]
       },
       "datasource": null,
       "definition": "label_values(mongodb_up{group_id='$group_id', cluster_name='$cluster_name',replica_set_name='$replica_set_name'},instance)",
       "description": null,
       "error": null,
       "hide": 0,
       "includeAll": true,
       "label": null,
       "multi": true,
       "name": "host",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up{group_id='$group_id', cluster_name='$cluster_name',replica_set_name='$replica_set_name'},instance)",
         "refId": "StandardVariableQuery"
       },
       "refresh": 2,
       "regex": "(.*):.*",
       "skipUrlSync": false,
       "sort": 0,
       "type": "query"
     },
     {
       "allValue": null,
       "current": {
         "selected": true,
         "text": [
           "All"
         ],
         "value": [
           "$__all"
         ]
       },
       "datasource": null,
       "definition": "label_values(mongodb_up{group_id='$group_id', cluster_name='$cluster_name',replica_set_name='$replica_set_name'},process_port)",
       "description": "Only applicable for process level metrics",
       "error": null,
       "hide": 0,
       "includeAll": true,
       "label": "Process Port",
       "multi": true,
       "name": "process_port",
       "options": [],
       "query": {
         "query": "label_values(mongodb_up{group_id='$group_id', cluster_name='$cluster_name',replica_set_name='$replica_set_name'},process_port)",
         "refId": "StandardVariableQuery"
       },
       "refresh": 1,
       "regex": "",
       "skipUrlSync": false,
       "sort": 0,
       "type": "query"
     },
     {
       "auto": true,
       "auto_count": 30,
       "auto_min": "10s",
       "current": {
         "selected": false,
         "text": "1m",
         "value": "1m"
       },
       "description": null,
       "error": null,
       "hide": 0,
       "label": "Interval",
       "name": "interval",
       "options": [
         {
           "selected": false,
           "text": "auto",
           "value": "$__auto_interval_interval"
         },
         {
           "selected": false,
           "text": "30s",
           "value": "30s"
         },
         {
           "selected": true,
           "text": "1m",
           "value": "1m"
         },
         {
           "selected": false,
           "text": "5m",
           "value": "5m"
         },
         {
           "selected": false,
           "text": "30m",
           "value": "30m"
         },
         {
           "selected": false,
           "text": "1h",
           "value": "1h"
         },
         {
           "selected": false,
           "text": "1d",
           "value": "1d"
         }
       ],
       "query": "30s,1m,5m,30m,1h,1d",
       "queryValue": "",
       "refresh": 2,
       "skipUrlSync": false,
       "type": "interval"
     }
   ]
 },
 "time": {
   "from": "now-30m",
   "to": "now"
 },
 "timepicker": {},
 "timezone": "",
 "title": "Hardware Metrics - Ops Manager",
 "uid": "7LTNNcpnzsasddsd",
 "version": 1
}
```

To learn more about importing Grafana dashboards, see [the Grafana documentation](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/import-dashboards/).

## Performance Metrics Available to Prometheus

The following metrics are available when you use the [Prometheus](https://prometheus.io/)
integration with your MongoDB Atlas cluster:

- prometheus-metric-labels-mms

  - serverStatus metrics
  - replSetStatus metrics

- prometheus-hardware-metrics-mms

## MongoDB Metric Labels

Each MongoDB metric contains the following labels:

| Label | Description |
|---|---|
| `group_id` | Unique hexadecimal digit string that identifies the project. |
| `org_id` | Unique hexadecimal digit string that identifies the organization. |
| `cl_role` | Human readable label that defines the cluster role. |
| `cl_name` | Human-readable label that identifies the cluster. |
| `rs_nm` | Human-readable label that identifies the replica set. |
| `rs_state` | Number that indicates the replica set state. |
| `process_port` | Port on which the process runs. |

## MongoDB Information Metrics

`mongodb_info` is a gauge that always has the value of `1`. This
metric contains all the prometheus-metric-labels-mms and
also the following labels:

| Label | Description |
|---|---|
| `mongodb_version` | String that represents the major, minor, and patch versions. |
| `replica_state_name` | String that indicates the replica set member status. |
| `process_type` | String that indicates the process running. Its values can be `mongod`, `mongos`, or `config`. |

## Hardware Metrics

**Note:**

You can also view descriptions of each hardware metric in the
[Prometheus expression browser](https://prometheus.io/docs/visualization/browser/).

| Name | Operating System | Type | Description |
|---|---|---|---|
| `hardware_system_cpu_nice` | Unix, Darwin | Counter | Time spent in user mode with low priority. |
| `hardware_system_cpu_io_wait` | Unix | Counter | Time waiting for I/O to complete. |
| `hardware_system_cpu_irq` | Unix | Counter | Time spent servicing interrupts. |
| `hardware_system_cpu_soft_irq` | Unix | Counter | Time spent servicing softirq's. |
| `hardware_system_cpu_steal` | Unix | Counter | Time spent in other operating systems when running in a virtual environment. |
| `hardware_system_cpu_guest` | Unix | Counter | Time spent running a virtual CPU for the guest operating systems under the control of the Linux kernel. |
| `hardware_system_cpu_guest_nice` | Unix | Counter | Time spent running a guest with an adjusted niceness. |
| `hardware_system_cpu_kernel_milliseconds` | All | Counter | Time spent in system mode. |
| `hardware_system_cpu_user_milliseconds` | All | Counter | Time spent in user mode. |
| `hardware_disk_metrics_weighted_time_io` | Unix | Counter | Weighted time spent doing I/O's. |
| `hardware_disk_metrics_physical_write_count` | Unix | Counter | Number of physical write I/O's processed. |
| `hardware_disk_metrics_physical_read_count` | Unix | Counter | Number of physical read I/O's processed. |
| `hardware_disk_metrics_total_time` | Unix | Counter | Total time this block device is active. |
| `hardware_disk_metrics_idle_time` | Windows | Counter | Time spent in the idle task. |
| `hardware_disk_metrics_disk_space_free_bytes` | All | Gauge | Disk space available in the mounted file system. |
| `hardware_disk_metrics_disk_space_used_bytes` | All | Gauge | Disk space used in the mounted file system. |
| `hardware_disk_metrics_read_count` | All | Counter | Number of read I/O's processed. |
| `hardware_disk_metrics_read_time_milliseconds` | All | Counter | Total wait time for read requests. |
| `hardware_disk_metrics_write_count` | All | Counter | Number of write I/O's processed. |
| `hardware_disk_metrics_write_time_milliseconds` | All | Counter | Total wait time for write requests. |
| `hardware_process_cpu_children_user` | Unix | Counter | Amount of time scheduled in user mode for this process to wait for children. |
| `hardware_process_cpu_children_kernel` | Unix | Counter | Amount of time scheduled in kernel mode for this process to wait for children. |
| `hardware_process_cpu_kernel_milliseconds` | All | Counter | Amount of time scheduled in kernel mode for this process. |
| `hardware_process_cpu_user_milliseconds` | All | Counter | Amount of time scheduled in user mode for this process. |
| `hardware_system_vm_page_swap_in` | Unix | Counter | Number of pages the system has swapped in from disk. |
| `hardware_system_vm_page_swap_out` | Unix | Counter | Number of pages the system has swapped out to disk. |
| `hardware_system_memory_mem_total` | Unix | Gauge | Total usable RAM (physical RAM minus a few reserved bits and the kernel binary code). |
| `hardware_system_memory_mem_free` | Unix | Gauge | Sum of `LowFree` + `HighFree`. |
| `hardware_system_memory_mem_available` | Unix | Gauge | An estimate of how much memory is available for starting new applications, without swapping. |
| `hardware_system_memory_buffers` | Unix | Gauge | Temporary storage for raw disk blocks that shouldn't get tremendously large. |
| `hardware_system_memory_cached` | Unix | Gauge | In-memory cache for files read from the disk. This doesn't include `SwapCached`. |
| `hardware_system_memory_swap_total` | Unix | Gauge | Total amount of swap space available. |
| `hardware_system_memory_swap_free` | Unix | Gauge | Total amount of swap space unused. |
| `hardware_system_memory_shared_mem` | Unix | Gauge | Amount of memory consumed in file systems whose contents reside in virtual memory. |
| `hardware_system_memory_swap_free_kilobytes` | All | Gauge | Total amount of swap space unused. |
| `hardware_system_memory_swap_total_kilobytes` | All | Gauge | Total amount of swap space available. |
| `hardware_platform_num_logical_cpus` | All | Gauge | Number of logical CPUs usable by the current process. |
| `hardware_system_network_eth0_bytes_in_bytes` | All | Counter | Number of bytes of data received by the interface. |
| `hardware_system_network_eth0_bytes_out_bytes` | All | Counter | Number of bytes of data transmitted by the interface. |
| `hardware_system_network_lo_bytes_in_bytes` | All | Counter | Number of bytes of data received by the interface. |
| `hardware_system_network_lo_bytes_out_bytes` | All | Counter | Number of bytes of data transmitted by the interface. |

## Hardware Metric Labels

Each hardware metric contains the following labels:

| Label | Description |
|---|---|
| `group_id` | Unique hexadecimal digit string that identifies the project. |
| `org_id` | Unique hexadecimal digit string that identifies the organization. |
| `process_port` | Port on which the process runs. |
| `disk_name` | Human-readable label that identifies the disk. |
