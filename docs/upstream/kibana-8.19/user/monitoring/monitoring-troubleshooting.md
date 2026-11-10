<!-- Converted from user/monitoring/monitoring-troubleshooting.asciidoc (AsciiDoc). Includes are inlined. -->

# Troubleshooting monitoring in Kibana

Use the information in this section to troubleshoot common problems and find 
answers for frequently asked questions related to the Kibana {monitor-features}.

## Cannot view the cluster because the license information is invalid

*Symptoms:*

The following error appears in a banner at the top of the screen in Kibana on the 
*Stack Monitoring > Clusters* page:
`You can't view the "<my_cluster>" cluster because the license information is invalid.`

*Resolution:*

You cannot monitor a version 6.3 or later cluster from Kibana version 6.2 or earlier. 
To resolve this issue, upgrade Kibana to 6.3 or later. See 
{stack-ref}/upgrading-elastic-stack.html[Upgrading the Elastic Stack]. 

## {filebeat} index is corrupt

*Symptoms:*

The *Stack Monitoring* application displays a Monitoring Request error indicating
that an illegal argument exception has occurred because fielddata is disabled on
text fields by default.

*Resolution*

 . Stop all your {filebeat} instances.
 . Delete indices beginning with `filebeat-$VERSION`, where `VERSION` corresponds
   to the version of {filebeat} running.
. Restart all your {filebeat} instances.

## No monitoring data is visible in Kibana

*Symptoms:*

The *Stack Monitoring* page in Kibana is empty. 

*Resolution:*

. Confirm that Kibana is seeking monitoring data from the appropriate Elasticsearch URL.
By default, data is retrieved from the cluster specified in the 
`elasticsearch.hosts` setting in the `kibana.yml` file. If you want to retrieve it
from a different monitoring cluster, set `monitoring.ui.elasticsearch.hosts`.
See monitoring-settings-kb.

. Confirm that there is monitoring data available at that URL. It is stored in
indices such as `.monitoring-kibana-*` and `.monitoring-es-*` or
`metrics-kibana.stack_monitoring.*`, depending on which method is
used to collect monitoring data. At a minimum, you must have monitoring data
for the Elasticsearch production cluster. Once that data exists, Kibana can display
monitoring data for other products in the cluster.

. Set the time filter to “Last 1 hour”.  When monitoring data appears in your
cluster, the page automatically refreshes with the monitoring summary.

. If using Elastic Agent, ensure that all integration assets have been installed in
the monitoring cluster.
