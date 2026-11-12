<!-- Converted from spaces/index.asciidoc (AsciiDoc). Includes are inlined. -->

## Spaces

You can define multiple spaces in a single Kibana instance from the **Spaces** menu. Each space has its own navigation and saved objects, and users can only access the spaces that they have been granted access to. This access is based on user roles, and a given role can have different permissions per space.

Kibana creates a default space for you.
When you create more spaces, users are asked to choose a space when they log in to Kibana, and can change their
current space at any time from the top menu.

(Figure: images/change-space.png)

To go to **Spaces**, find **Stack Management** in the navigation menu or use the global search bar.

### Required privileges

The `kibana_admin` role or equivalent is required to manage **Spaces**.

### Create a space

You can have up to 1,000 spaces by default. The maximum number of spaces can be configured by the `xpack.spaces.maxSpaces` setting (refer to Spaces settings in Kibana).

. Select *Create space* and provide a name, description, and URL identifier.
The URL identifier is a short text string that becomes part of the
Kibana URL when you are inside that space. Kibana suggests a URL identifier based
on the name of your space, but you can customize the identifier to your liking.
You cannot change the space identifier once you create the space.

. Select a **Solution view**. This setting controls the navigation that all users of the space will get:

** **Search**: A light navigation menu focused on analytics and Search use cases. Features specific to Observability and Security are hidden.
** **Observability**: A light navigation menu focused on analytics and Observability use cases. Features specific to Search and Security are hidden.
** **Security**: A light navigation menu focused on analytics and Security use cases. Features specific to Observability and Search are hidden.
** **Classic**: All features from all solutions are visible by default using the classic, multilayered navigation menus. You can customize which features are visible individually. 

. If you selected the **Classic** solution view, you can customize the **Feature visibility** as you need it to be for that space.
**Note:** Even when disabled in this menu, some Management features can remain visible to some users depending on their privileges. Additionally, controlling feature visibility is not a security feature. To secure access
to specific features on a per-user basis, you must configure Kibana Security.

. Customize the avatar of the space to your liking.

. Save your new space by selecting **Create space**.

You can edit all of the space settings you just defined at any time, except for the URL identifier.

Kibana also has an API
if you prefer to create spaces programmatically.

### Define access to a space

Users can access spaces based on the roles that they have. 

* Certain reserved roles can view and access all spaces by default. You can't prevent those roles from accessing a space. Instead, you can grant different roles to your users.
* When creating or editing a role, you can define which existing spaces that role can access, and with which permissions.
* When editing a space, you can assign roles to the space and define the permissions within the space for these roles. To do that, go to the **Permissions** tab of the space you're editing.
When a role is assigned to _All Spaces_, you can't remove its access from the space settings. You must instead edit the role to give it more granular access to individual spaces.

### Delete a space

Deleting a space permanently removes the space and all of its contents.
Find the space on the *Spaces* overview page and click the trash icon in the Actions column.
You can't delete the default space, but you can customize it to your liking.

### Move saved objects between spaces

To move saved objects between spaces, you can copy objects, or export and import objects.

### Configure a space-level landing page

You can create a custom experience for users by configuring the Kibana landing page on a per-space basis.
The landing page can route users to a specific dashboard, application, or saved object as they enter each space.

To configure the landing page, use the default route setting in
<<kibana-general-settings, Stack Management > Kibana > Advanced settings>>.
For example, you might set the default route to `/app/dashboards`.

(Figure: images/spaces-configure-landing-page.png)

### Disable spaces

Since Kibana 8.0, the Spaces feature cannot be disabled.
