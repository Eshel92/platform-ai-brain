<!-- Part 7 of 8 of tutorial/prometheus-integration.md (split because the page is big). -->

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
