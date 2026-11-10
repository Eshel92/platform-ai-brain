<!-- Converted from management/managing-tags.asciidoc (AsciiDoc). Includes are inlined. -->

## Tags

Use tags to categorize your saved objects,
then filter for related objects based on shared tags.

To get started, go to the *Tags* management page using the navigation menu or the 
global search field.

(Figure: images/tags/tag-management-section.png)

### Required permissions

To create tags, you must meet the minimum requirements.

* Access to *Tags* requires the `Tag Management` Kibana privilege. To add the privilege, go to the *Roles* page using the navigation menu or the 
global search field.
* The `read` privilege allows you to assign tags to the saved objects for which you have write permission.
* The `write` privilege enables you to create, edit, and delete tags.

**Note:** Having the `Tag Management` Kibana privilege is not required to
view tags assigned on objects you have `read` access to, or to filter objects by tags
from the global search.

### Create a tag

Create a tag to assign to your saved objects.

. Click *Create tag*.

. Enter a name and select a color for the new tag.
The name cannot be longer than 50 characters.
. Click *Create tag*.

### Assign a tag to an object

To assign and remove tags, you must have `write` permission
on the objects to which you assign the tags.

. Find the tag you want to assign.
. Click the actions icon
image:images/actions_icon.png[Actions icon],
and then select *Manage assignments*.

. Select the objects to which you want to assign or remove tags.
(Figure: images/tags/manage-assignments-flyout.png)

. Click *Save tag assignments*.

### Delete a tag

When you delete a tag, you remove it from all saved objects that use it.

. Click the actions icon
image:images/actions_icon.png[Actions icon], and then select *Delete*.

. Click *Delete tag*.

**Tip:** To assign, delete, or clear multiple tags,
select them in the *Tags* view, and then select
the action from the *selected tags* menu.
