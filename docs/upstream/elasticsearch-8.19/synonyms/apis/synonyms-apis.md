<!-- Converted from synonyms/apis/synonyms-apis.asciidoc (AsciiDoc). Includes are inlined. -->

## Synonyms APIs

---

**New API reference**
For the most up-to-date API details, refer to [Synonyms APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-synonyms).

The synonyms management API provides a convenient way to define and manage synonyms in an internal system index. Related synonyms can be grouped in a "synonyms set".
Create as many synonym sets as you need.

This provides an alternative to:

- Defining inline synonyms in an analyzer definition, which impacts mapping size and can lead to performance issues.
- Using synonyms files, which implies uploading and managing file consistency on all cluster nodes.

Synonyms sets can be used to configure synonym graph token filters and synonym token filters.
These filters are applied as part of the analysis process by the search analyzer.

**Note:** Synonyms sets are limited to a maximum of 10,000 synonym rules per set.
If you need to manage more synonym rules, you can create multiple synonyms sets.

**Warning:** Synonyms sets must exist before they can be added to indices.
If an index is created referencing a nonexistent synonyms set, the index will remain in a partially created and inoperable state.
The only way to recover from this scenario is to ensure the synonyms set exists then either delete and re-create the index, or close and re-open the index.

**Warning:**
Invalid synonym rules can cause errors when applying analyzer changes.
For reloadable analyzers, this prevents reloading and applying changes.
You must correct errors in the synonym rules and reload the analyzer.

An index with invalid synonym rules cannot be reopened, making it inoperable when:

* A node containing the index starts
* The index is opened from a closed state
* A node restart occurs (which reopens the node assigned shards)

### Synonyms sets APIs

You can use these APIs to dynamically update synonyms sets used at search time.
Your search results will immediately reflect the synonyms set changes.

Use the following APIs to manage synonyms sets:

* put-synonyms-set
* get-synonyms-set
* list-synonyms-sets
* delete-synonyms-set

### Synonym rules APIs

Synonyms sets are composed of synonym rules.
Each synonym rule defines a group of words that act as synonyms.
You can update individual synonym rules for a specific synonyms set instead of updating the complete synonyms set.

Use the following APIs to manage individual synonym rules in a synonyms set:

* put-synonym-rule
* get-synonym-rule
* delete-synonym-rule

(See `synonyms/apis/put-synonyms-set.md`)
(See `synonyms/apis/get-synonyms-set.md`)
(See `synonyms/apis/list-synonyms-sets.md`)
(See `synonyms/apis/delete-synonyms-set.md`)
(See `synonyms/apis/put-synonym-rule.md`)
(See `synonyms/apis/get-synonym-rule.md`)
(See `synonyms/apis/delete-synonym-rule.md`)
