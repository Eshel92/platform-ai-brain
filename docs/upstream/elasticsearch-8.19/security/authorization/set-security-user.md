<!-- Converted from security/authorization/set-security-user.asciidoc (AsciiDoc). Includes are inlined. -->

#### Pre-processing documents to add security details

To guarantee that a user reads only their own documents, it makes sense to set up
document level security. In this scenario, each document must have the username
or role name associated with it, so that this information can be used by the
role query for document level security. This is a situation where the
set security user processor ingest processor can help.

**Note:** Document level security doesn't apply to write APIs. You must use unique
ids for each user that uses the same data stream or index, otherwise they might overwrite other
users' documents. The ingest processor just adds properties for the current
authenticated user to the documents that are being indexed.

The set security user processor attaches user-related details (such as
`username`,  `roles`, `email`, `full_name` and `metadata` ) from the current
authenticated user to the current document by pre-processing the ingest. When
you index data with an ingest pipeline, user details are automatically attached
to the document. If the authenticating credential is an API key, the API key
`id`, `name` and `metadata` (if it exists and is non-empty) are also attached to
the document.

For more information see ingest and
ingest-node-set-security-user-processor
