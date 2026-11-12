<!-- Part 2 of 8 of tutorial/prometheus-integration.md (split because the page is big). -->

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
