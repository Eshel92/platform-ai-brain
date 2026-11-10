<!-- Converted from user/dashboard/share-dashboards.asciidoc (AsciiDoc). Includes are inlined. -->

# Share dashboards

To share a dashboard with a larger audience, click *Share* in the toolbar. For detailed information about the sharing options and time ranges, refer to Reporting and sharing.

(Figure: https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/bltc45bb05c1fab3e60/68826ffb4f04ad6e224c2248/share-dashboard.gif)

**Tip:** When sharing a dashboard with a link while a panel is in maximized view, the generated link will also open the dashboard on the same maximized panel view.

## Export dashboards

You can export dashboards from **Stack Management** > **Saved Objects**. To configure and start the export: 

. Select the dashboard that you want, then click **Export**.
. Enable **Include related objects** if you want that objects associated to the selected dashboard, such as data views and visualizations, also get exported. This option is enabled by default and recommended if you plan to import that dashboard again in a different space or cluster.
. Select **Export**.

image:images/dashboard-export-saved-object.png[Option to export a dashboard]

To automate Kibana, you can export dashboards as NDJSON using the [Export saved objects API](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-saved-objects). It is important to export dashboards with all necessary references.
