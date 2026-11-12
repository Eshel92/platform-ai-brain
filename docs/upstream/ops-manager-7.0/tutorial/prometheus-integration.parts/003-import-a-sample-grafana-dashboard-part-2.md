<!-- Part 3 of 8 of tutorial/prometheus-integration.md (split because the page is big). -->

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
