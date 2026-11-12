<!-- Converted from user/security/authorization/index.asciidoc (AsciiDoc). Includes are inlined. -->

### Granting access to Kibana

The Elastic Stack comes with the `kibana_admin` [built-in role](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/built-in-roles.html), which you can use to grant access to all Kibana features in all spaces. To grant users access to a subset of spaces or features, you can create a custom role that grants the desired Kibana privileges.

When you assign a user multiple roles, the user receives a union of the roles’ privileges. Therefore, assigning the `kibana_admin` role in addition to a custom role that grants Kibana privileges is ineffective because `kibana_admin` has access to all the features in all spaces.

### Kibana role management

Roles are a collection of privileges that allow you to perform actions in Kibana and Elasticsearch. Users are not directly granted privileges, but are instead assigned one or more roles that describe the desired level of access. When you assign a user multiple roles, the user receives a union of the roles’ privileges. This means that you cannot reduce the privileges of a user by assigning them an additional role. You must instead remove or edit one of their existing roles.

To create a role, open the menu, then click *Stack Management > Roles* and click **Create role**.

#### Required permissions

The `manage_security` [cluster privilege](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-privileges.html#privileges-list-cluster) is required to access role management.

#### Cluster privileges

Cluster privileges grant access to monitoring and management features in Elasticsearch. They also enable Stack Management capabilities in Kibana.

Refer to [cluster privileges](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-privileges.html#privileges-list-cluster) for a complete description of available options.

#### Index privileges

Each role can grant access to multiple data indices, and each index can have a different set of privileges.
We recommend granting the `read` and `view_index_metadata` privileges to each index that you expect your users to work with in Kibana.

Refer to [index privileges](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/security-privileges.html#privileges-list-indices) for a complete description of available options.

Document-level and field-level security affords you even more granularity when it comes to granting access to your data.
With document-level security (DLS), you can write an Elasticsearch query to describe which documents this role grants access to.
With field-level security (FLS), you can instruct Elasticsearch to grant or deny access to specific fields within each document.

##### Example: Grant access to indices that match the `filebeat-*` pattern

. Go to **Stack Management > Roles**, and then click **Create role**.
. In **Index privileges**, enter:
.. `filebeat-*` in the **Index** field.
.. `read` and `view_index_metadata` in the **Privileges** field.

(Figure: security/images/create-role-index-example.png)

##### Example: Grant read access to specific documents in indices that match the `filebeat-*` pattern

[Document-level security](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/document-level-security.html) is a [subscription feature](https://www.elastic.co/subscriptions).

. Go to **Stack Management > Roles**, and then click **Create role**.
. In **Index privileges**, enter:
.. `filebeat-*` in the **Indices** field.
.. `read` and `view_index_metadata` in the **Privileges** field.
. Select **Grant read privileges to specific documents**.
. Enter an Elasticsearch query that matches the documents your users should access. This example writes a query that allows access to documents that have a `category` field equal to `click`:
```sh
{
  "match": {
    "category": "click"
  }
}
```
**Note:** Kibana automatically surrounds your DLS query with a `query` block, so you don't have to provide your own.

(Figure: security/images/create-role-dls-example.png)

#### Remote index privileges

If you have at least a platinum license, you can manage access to indices in remote clusters. 

You can assign the same privileges, document-level, and field-level as for local index privileges. 

##### Example: Grant access to indices in remote clusters

. Go to **Stack Management > Roles**, and then click **Create role**.
. In **Remote index privileges**, enter:
.. The name of your remote cluster in the **Remote clusters** field.
.. The name of the index in your remote cluster in the **Remote indices** field.
.. The allowed actions in the **Privileges** field. (e.g. `read` and `view_index_metadata`)

(Figure: security/images/create-role-remote-index-example.png)

#### Kibana privileges

To assign Kibana privileges to the role, click **Add Kibana privilege** in the Kibana section.

(Figure: spaces/images/spaces-roles.png)

Open the **Spaces** selection control to specify whether to grant the role access to all spaces **All Spaces** or one or more individual spaces. If you select **All Spaces**, you can’t select individual spaces until you clear your selection.

Use the **Privilege** menu to grant access to features. The default is **Custom**, which you can use to grant access to individual features. Otherwise, you can grant read and write access to all current and future features by selecting **All**, or grant read access to all current and future features by selecting **Read**.

When using the **Customize by feature** option, you can choose either **All**, **Read** or **None** for access to each feature. As new features are added to Kibana, roles that use the custom option do not automatically get access to the new features. You must manually update the roles.

**Note:** *{stack-monitor-app}* relies on built-in roles to grant access. When a
user is assigned the appropriate roles, the *{stack-monitor-app}* application is
available; otherwise, it is not visible.

To apply your changes, click **Add Kibana privilege**. The privilege shows up under the Kibana privileges section of the role.

(Figure: security/images/create-space-privilege.png)

#### Feature availability

Features are available to users when their roles grant access to the features, **and** those features are visible in their current space. The following matrix explains when features are available to users when controlling access via spaces and role-based access control:

|===
|**Spaces config** |**Role config** |**Result**

|Feature hidden
|Feature disabled
|Feature not available

|Feature hidden
|Feature enabled
|Feature not available

|Feature visible
|Feature disabled
|Feature not available

|Feature visible
|Feature enabled
|**Feature available**
|===

#### Assigning different privileges to different spaces

Using the same role, it’s possible to assign different privileges to different spaces. After you’ve added privileges, click **Add Kibana privilege**. If you’ve already added privileges for either **All Spaces** or an individual space, you will not be able to select these in the **Spaces** selection control.

Additionally, if you’ve already assigned privileges at **All Spaces**, you are only able to assign additional privileges to individual spaces. Similar to the behavior of multiple roles granting the union of all privileges, Kibana privileges are also a union. If you’ve already granted the user the **All** privilege at **All Spaces**, you’re not able to restrict the role to only the **Read** privilege at an individual space.

#### Privilege summary

To view a summary of the privileges granted, click **View privilege summary**.

(Figure: security/images/view-privilege-summary.png)

#### Example 1: Grant all access to Dashboard at an individual space

. Click **Add Kibana privilege**.
. For **Spaces**, select an individual space.
. For **Privilege**, leave the default selection of **Custom**.
. For the Dashboard feature, select **All**
. Click **Add Kibana privilege**.

(Figure: security/images/privilege-example-1.png)

#### Example 2: Grant all access to one space and read access to another

. Click **Add Kibana privilege**.
. For **Spaces**, select the first space.
. For **Privilege**, select **All**.
. Click **Add Kibana privilege**.
. For **Spaces**, select the second space.
. For **Privilege**, select **Read**.
. Click **Add Kibana privilege**.

(Figure: security/images/privilege-example-2.png)

#### Example 3: Grant read access to all spaces and write access to an individual space

. Click **Add Kibana privilege**.
. For **Spaces**, select **All Spaces**.
. For **Privilege**, select **Read**.
. Click **Add Kibana privilege**.
. For **Spaces**, select the individual space.
. For **Privilege**, select **All**.
. Click **Add Kibana privilege**.

(Figure: security/images/privilege-example-3.png)
