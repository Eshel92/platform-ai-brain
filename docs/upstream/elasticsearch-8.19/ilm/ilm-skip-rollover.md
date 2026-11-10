<!-- Converted from ilm/ilm-skip-rollover.asciidoc (AsciiDoc). Includes are inlined. -->

## Skip rollover

When `index.lifecycle.indexing_complete` is set to `true`, 
ILM won't perform the rollover action on an index, 
even if it otherwise meets the rollover criteria. 
It's set automatically by ILM when the rollover action completes successfully.

You can set it manually to skip rollover if you need to make an exception
to your normal lifecycle policy and update the alias to force a roll over, 
but want ILM to continue to manage the index. 
If you use the rollover API, it is not necessary to configure this setting manually. 

If an index's lifecycle policy is removed, this setting is also removed.

**Important:** When `index.lifecycle.indexing_complete` is `true`, 
ILM verifies that the index is no longer the write index 
for the alias specified by `index.lifecycle.rollover_alias`.
If the index is still the write index or the rollover alias is not set,
the index is moved to the `ERROR` step.

For example, if you need to change the name of new indices in a series while retaining
previously-indexed data in accordance with your configured policy, you can:

. Create a template for the new index pattern that uses the same policy. 
. Bootstrap the initial index.
. Change the write index for the alias to the bootstrapped index 
using the aliases API.
. Set `index.lifecycle.indexing_complete` to `true` on the old index to indicate 
that it does not need to be rolled over.

ILM continues to manage the old index in accordance with your existing policy. 
New indices are named according to the new template and 
managed according to the same policy without interruption.
