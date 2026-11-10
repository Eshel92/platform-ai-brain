<!-- Converted from user/dashboard/create-dashboards.asciidoc (AsciiDoc). Includes are inlined. -->

# Build dashboards

Kibana offers many ways to build powerful dashboards that will help you visualize and keep track of the most important information contained in your Elasticsearch data.

* Create and assemble visualizations such as charts or maps, and enrich them with helpful legends containing key data.
* Extract and show key indicators and metrics to keep them visible and highlighted at all times.
* Add text, images, and links to help viewers make the most of your dashboard.
* Include additional controls to facilitate filtering and browsing the data.

To create or edit dashboards, you first need to:

* have [data indexed into Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/getting-started-index.html) and a data view. A data view is a subset of your Elasticsearch data, and allows you to load just the right data when building a visualization or exploring it. 
**Tip:** If you don't have data at hand and still want to explore dashboards, you can import one of the sample data sets available.

* have sufficient permissions on the **Dashboard** feature. If that's not the case, you might get a read-only indicator. A Kibana administrator can grant you the required privileges.

## Create a dashboard

. Open the *Dashboards* page in Kibana.

. Select *Create dashboard* to start with an empty dashboard.
When you create a dashboard, you are automatically in edit mode and can make changes to the dashboard. 
. Add content to the dashboard. You have several options covered in more detail in the Visualizations section:
** **Create visualization**. This option is a shortcut to create a chart using **Lens**, the default visualization editor in Kibana.
** **Add panel**. Choose one of the available panels to add and configure content to your dashboard.
** **Add from library**. Select existing content that has already been configured and saved to the **Visualize Library**.
** **Controls**. Add controls to help filter the content of your dashboard.
(Figure: images/add_content_to_dashboard_8.15.0.png)
. Organize your dashboard by organizing the various panels. 
. Define the main settings of your dashboard from the *Settings* menu located in the toolbar.
.. A meaningful title, description, and tags allow you to find the dashboard quickly later when browsing your list of dashboards or using the Kibana search bar.
.. Additional display options allow you unify the look and feel of the dashboard's panels:

*** *Store time with dashboard* &mdash; Saves the specified time filter.
*** *Use margins between panels* &mdash; Adds a margin of space between each panel.
*** *Show panel titles* &mdash; Displays the titles in the panel headers.
*** *Sync color palettes across panels* &mdash; Applies the same color palette to all panels on the dashboard.
*** *Sync cursor across panels* &mdash; When you hover your cursor over a time series chart or a heatmap, the cursor on all other related dashboard charts automatically appears.
*** *Sync tooltips across panels* &mdash; When you hover your cursor over a *Lens* chart, the tooltips on all other related dashboard charts automatically appear.

.. Click *Apply*.
(Figure: https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt4a6e9807f1fac9f8/6750ee9cef6d5a250c229e50/dashboard-settings-8.17.0.gif)

. Click **Save**  to save the dashboard.

## Edit a dashboard

. Open the *Dashboards* page in Kibana.

. Locate the dashboard you want to edit.
**Tip:** When looking for a specific dashboard, you can filter them by tag or by creator, or search the list based on their name and description. Note that the creator information is only available for dashboards created on or after version 8.14.

. Click the dashboard *Title* you want to open.

. Make sure that you are in **Edit** mode to be able to make changes to the dashboard. You can switch between **Edit** and **View** modes from the toolbar.
(Figure: https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt619b284e92c2be27/6750f3a512a5eae780936fe3/switch-to-view-mode-8.17.0.gif)
. Make the changes that you need to the dashboard:

** Adjust the dashboard's settings
** Add, remove, move, or edit panels
** Change the available controls
. **Save** the dashboard. You automatically switch to *View* mode upon saving. 

**Note:** Managed dashboards can't be edited directly, but you can duplicate them and edit these duplicates.

### Reset dashboard changes

When editing a dashboard, you can revert any changes you've made since the last save using **Reset dashboards**.

**Note:** Once changes are saved, you can no longer revert them in one click, and instead have to edit the dashboard manually.

. In the toolbar, click *Reset*.

. On the *Reset dashboard?* window, click *Reset dashboard*.

(Figure: https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blte0c08bede75b3874/6750f5566cdeea14b273b048/reset-dashboard-8.17.0.gif)

(See `user/dashboard/dashboard-controls.md`)
(See `user/dashboard/drilldowns.md`)

## Organize dashboard panels

### Arrange panels in collapsible sections

Organize your dashboard panels into collapsible sections to improve readability and navigation, especially for dashboards with many panels. Collapsible sections also help dashboards load faster by only loading the content from expanded sections.

To add a collapsible section:

. Open the dashboard and make sure that you are in **Edit** mode.

. Select **Add panel** and select **Collapsible section**. The collapsible section is added at the end of the dashboard.

. Optionally, edit the label of the section.

. Drag and drop any panels you want into the section. +
**Note:** The section must be expanded in order to place panels into it.

. Just like any other panel, you can drag an drop the collapsible section to a different position in the dashboard.

. Save the dashboard. 

Users viewing the dashboard will find the section in the same state as when you saved the dashboard. If you saved it with the section collapsed, then it will also be collapsed by default for users.

(Figure: https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt8c368aecdd095010/685e8fcb9c34ed3c353812a5/collapsible_panels.gif)

### Move and resize panels

Compare the data in your panels side-by-side, organize panels by priority, resize the panels so they all appear immediately on the dashboard, and more.

In the toolbar, click *Edit*, then use the following options:

* To move, hover over the panel, click and hold image:images/move-control.png[The move control icon, width=4%] and drag to the new location. Your screen scrolls automatically when you drag above or below the visible parts of the dashboard.

* To resize, click and hold the bottom right corner of the panel and drag to the new dimensions.

* To maximize to full screen, open the panel menu and click *Maximize*.
**Tip:** If you share a dashboard while viewing a full screen panel, the generated link will directly open the same panel in full screen mode.

#### Move and resize panels using a keyboard

To move a panel:

1. Using `Tab`, browse to the `move` icon panel action and press `Enter` or `Space` to lock the action.
2. Use `Arrow` keys to move the panel to the new location.
3. Press `Enter` or `Space` again to release the panel.
4. Save the dashboard.

To resize a panel:

1. Using `Tab`, browse to the `scale` icon panel action and press `Enter` or `Space` to lock the action.
2. Use `Arrow` keys to resize the panel to the new dimensions.
3. Press `Enter` or `Space` again to release the panel.
4. Save the dashboard.

**Tip:** While moving or resizing a panel, you can cancel the action at any time by pressing `Escape`.

### Copy and duplicate panels

To duplicate a panel and its configured functionality, use the clone and copy panel options. Cloned and copied panels replicate all of the functionality from the original panel, 
including renaming, editing, and cloning. 

#### Duplicate panels

Duplicated panels appear next to the original panel, and move the other panels to provide a space on the dashboard.

. In the toolbar, click *Edit*.

. Open the panel menu and select *Duplicate*.

#### Copy panels

Copy panels from one dashboard to another dashboard.

. Open the panel menu and select *Copy to dashboard*.

. On the *Copy to dashboard* window, select the dashboard, then click *Copy and go to dashboard*.
image:[Copy a panel to another dashboard, width 30%](https://images.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt48304cb3cd1ee2e6/6753879eb7c4663812148d47/copy-to-dashboard-8.17.0.gif)

## Duplicate dashboards

. Open the dashboard you want to duplicate.

. In *View* mode, click *Duplicate* in the toolbar.

. In the *Duplicate dashboard* window, enter a title and optional description and tags.

. Click *Save*.

You will be redirected to the duplicated dashboard.

To duplicate a managed dashboard, follow the instructions above or click the *Managed* badge in the toolbar. Then click *Duplicate* in the dialogue that appears. 

(Figure: images/managed-dashboard-popover-8.16.0.png)

## Import dashboards

You can import dashboards from the **Saved Objects** page under **Stack Management**. Refer to Manage saved objects.

When importing dashboards, you also import their related objects, such as data views and visualizations. Import options allow you to define how the import should behave with these related objects.

* **Check for existing objects**: When selected, objects are not imported when another object with the same ID already exists in this space or cluster. For example, if you import a dashboard that uses a data view which already exists, the data view is not imported and the dashboard uses the existing data view instead. You can also chose to select manually which of the imported or the existing objects are kept by selecting **Request action on conflict**.

* **Create new objects with random IDs**: All related objects are imported and are assigned a new ID to avoid conflicts.

image:images/dashboard-import-saved-object.png[Import panel]
