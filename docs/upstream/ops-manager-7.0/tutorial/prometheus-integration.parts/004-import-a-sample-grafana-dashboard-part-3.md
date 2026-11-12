<!-- Part 4 of 8 of tutorial/prometheus-integration.md (split because the page is big). -->

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
