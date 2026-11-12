<!-- Part 6 of 8 of tutorial/prometheus-integration.md (split because the page is big). -->

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
