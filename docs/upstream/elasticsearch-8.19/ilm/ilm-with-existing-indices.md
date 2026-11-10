<!-- Converted from ilm/ilm-with-existing-indices.asciidoc (AsciiDoc). Includes are inlined. -->

## Manage existing indices

If you've been using Curator or some other mechanism to manage periodic indices,
you have a couple options when migrating to ILM:

* Set up your index templates to use an ILM policy to manage your new indices.
Once ILM is managing your current write index, you can apply an appropriate policy to your old indices.

* Reindex into an ILM-managed index.

**Note:** Starting in Curator version 5.7, Curator ignores ILM managed indices.

### Apply policies to existing time series indices

The simplest way to transition to managing your periodic indices with ILM is
to configure an index template to apply a lifecycle policy to new indices.
Once the index you are writing to is being managed by ILM,
you can manually apply a policy to your older indices.

Define a separate policy for your older indices that omits the rollover action.
Rollover is used to manage where new data goes, so isn't applicable.

Keep in mind that policies applied to existing indices compare the `min_age` for each phase to
the original creation date of the index, and might proceed through multiple phases immediately.
If your policy performs resource-intensive operations like force merge,
you don't want to have a lot of indices performing those operations all at once
when you switch over to ILM.

You can specify different `min_age` values in the policy you use for existing indices,
or set `index.lifecycle.origination_date`
to control how the index age is calculated.

Once all pre-ILM indices have been aged out and removed,
you can delete the policy you used to manage them.

**Note:** If you are using Beats or Logstash, enabling ILM in version 7.0 and onward
sets up ILM to manage new indices automatically.
If you are using Beats through Logstash,
you might need to change your Logstash output configuration and invoke the Beats setup
to use ILM for new data.

### Reindex into a managed index

An alternative to applying policies to existing indices is to
reindex your data into an ILM-managed index.
You might want to do this if creating periodic indices with very small amounts of data
has led to excessive shard counts, or if continually indexing into the same index has led to large shards
and performance issues.

First, you need to set up the new ILM-managed index:

. Update your index template to include the necessary ILM settings.
. Bootstrap an initial index as the write index.
. Stop writing to the old indices and index new documents using the alias that points to bootstrapped index.

To reindex into the managed index:

. Pause indexing new documents if you do not want to mix new and old data in the ILM-managed index.
Mixing old and new data in one index is safe,
but a combined index needs to be retained until you are ready to delete the new data.

. Reduce the ILM poll interval to ensure that the index doesn't
grow too large while waiting for the rollover check.
By default, ILM checks to see what actions need to be taken every 10 minutes.
```console
PUT _cluster/settings
{
  "persistent": {
    "indices.lifecycle.poll_interval": "1m" <1>
  }
}
```
<1> Check once a minute to see if ILM actions such as rollover need to be performed.

. Reindex your data using the reindex API.
If you want to partition the data in the order in which it was originally indexed,
you can run separate reindex requests.
**Important:** Documents retain their original IDs. If you don't use automatically generated document IDs,
and are reindexing from multiple source indices, you might need to do additional processing to
ensure that document IDs don't conflict. One way to do this is to use a
script in the reindex call to append the original index name
to the document ID.

```console
PUT _index_template/mylogs_template
{
  "index_patterns": [
    "mylogs-*"
  ],
  "template": {
    "settings": {
      "number_of_shards": 1,
      "number_of_replicas": 1,
      "index": {
        "lifecycle": {
          "name": "mylogs_condensed_policy", <2>
          "rollover_alias": "mylogs" <3>
        }
      }
    },
    "mappings": {
      "properties": {
        "message": {
          "type": "text"
        },
        "@timestamp": {
          "type": "date"
        }
      }
    }
  }
}
```

```console
POST mylogs-pre-ilm-2019.06.24/_doc
{
  "@timestamp": "2019-06-24T10:34:00",
  "message": "this is one log message"
}
```

```console
POST mylogs-pre-ilm-2019.06.25/_doc
{
  "@timestamp": "2019-06-25T17:42:00",
  "message": "this is another log message"
}
```

```console
DELETE _index_template/mylogs_template
```

```console
POST _reindex
{
  "source": {
    "index": "mylogs-*" <1>
  },
  "dest": {
    "index": "mylogs", <2>
    "op_type": "create" <3>
  }
}
```

<1> Matches your existing indices. Using the prefix for
    the new indices makes using this index pattern much easier.
<2> The alias that points to your bootstrapped index.
<3> Halts reindexing if multiple documents have the same ID.
    This is recommended to prevent accidentally overwriting documents
    if documents in different source indices have the same ID.

. When reindexing is complete, set the ILM poll interval back to its default value to
prevent unnecessary load on the master node:
```console
PUT _cluster/settings
{
  "persistent": {
    "indices.lifecycle.poll_interval": null
  }
}

```

. Resume indexing new data using the same alias.
Querying using this alias will now search your new data and all of the reindexed data.

. Once you have verified that all of the reindexed data is available in the new managed indices,
you can safely remove the old indices.
