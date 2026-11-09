<!-- Converted from tutorial/fts-vs-quickstart.txt (reStructuredText). Includes are inlined. -->

:noprevnext:

# Use MongoDB Search and Vector Search

If you installed MongoDBSearch resource successfully, you can create
MongoDB Search and Vector Search indexes as the `mdb-user` and run
MongoDB Search and Vector Search queries using the indexes. This page
describes how to load sample data, create MongoDB Search and
Vector Search indexes for the data, and run MongoDB Search and
Vector Search queries against the data. 

## Prerequisites

To use MongoDB Search and Vector Search, you must have the following:

- Successful deployment of `MongoDB` and MongoDBSearch.

  To learn more, see: 

  - k8s-fts-vs-install-enterprise
  - k8s-fts-vs-install-external-enterprise

- User with permissions to create MongoDB Search and Vector Search and
  run MongoDB Search and Vector Search queries.

  To learn more, see k8s-search-create-role-user.

- Kubernetes command-line tool, `kubectl`, configured to communicate with
  your cluster.
- Bash v5.1 or higher for running the commands in this tutorial. 

## Procedure

**Step 1: Set the environment variables.**

a. To set the environment variables for use in the subsequent steps
   in this procedure, copy the following, set the values for the
   environment variables, and then load the environment variables: 

   ```yaml
   # The env vars here are all commented out because this snippets module
   # is reusable across different MongoDB deployments and all the necessary variables
   # should be already defined there.

   # set it to the context name of the k8s cluster
   #export K8S_CTX="<local cluster context>"
   # the following namespace will be used to deploy mongodb tools pod
   #export MDB_NS="mongodb"

   # regular user performing restore and search queries on sample mflix database
   # the user should be able to restore database using mongorestore
   #export MDB_USER_PASSWORD="mdb-user-password-CHANGE-ME"

   # name of MongoDB or MongoDBCommunity resource in case it's deployed in the same cluster
   # user only for the connection string in MDB_CONNECTION_STRING env var below
   #export MDB_RESOURCE_NAME="mdbc-rs"

   # TLS-related resources used by the snippets in this module
   #export MDB_TLS_CA_SECRET_NAME="${MDB_RESOURCE_NAME}-ca"
   #export MDB_TLS_CA_CONFIGMAP="${MDB_RESOURCE_NAME}-ca-configmap"
   #export MDB_TLS_SERVER_CERT_SECRET_NAME="${MDB_RESOURCE_NAME}-tls"
   #export MDB_SEARCH_TLS_SECRET_NAME="${MDB_RESOURCE_NAME}-search-tls"

   # default connection string if MongoDB database is deployed using the operator
   #export MDB_CONNECTION_STRING="mongodb://mdb-user:${MDB_USER_PASSWORD}@${MDB_RESOURCE_NAME}-0.${MDB_RESOURCE_NAME}-svc.${MDB_NS}.svc.cluster.local:27017/?replicaSet=${MDB_RESOURCE_NAME}"
   # To enable TLS for the shared snippets, append driver options directly to the connection string, for example:
   #export MDB_CONNECTION_STRING="mongodb://mdb-user:${MDB_USER_PASSWORD}@${MDB_RESOURCE_NAME}-0.${MDB_RESOURCE_NAME}-svc.${MDB_NS}.svc.cluster.local:27017/?replicaSet=${MDB_RESOURCE_NAME}&tls=true&tlsCAFile=/tls/ca.crt"
   ```

#. To connect using the TLS-enabled connection string, as shown
   (on line 27) in the `env_variables.sh` file, download the
   public CA certificate for the MongoDBSearch service so that the 
   `mongosh` client can reference it.   

**Step 2: Deploy a MongoDB tools pod.**

Deploy a pod named `mongodb-tools-pod` to run MongoDB client
tools like `mongosh` and `mongorestore` from within the Kubernetes
cluster. Running a pod inside the cluster simplifies connectivity
to mongodb without neeeding to expose the database externally. 

The following command deploys a pod named `mongodb-tools-pod`
that runs a MongoDB Community Server image. The pod is kept
running with a `sleep infinity` command to allow you to use
`kubectl exec` to run MongoDB client tools. 

```shell
kubectl apply -n "${MDB_NS}" --context "${K8S_CTX}" -f - <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: mongodb-tools-pod
  labels:
    app: mongodb-tools
spec:
  containers:
  - name: mongodb-tools
    image: mongodb/mongodb-community-server:${MDB_VERSION%-ent}-ubi8
    command: ["/bin/bash", "-c"]
    args: ["sleep infinity"]
    volumeMounts:
    - name: mongo-ca
      mountPath: /tls
      readOnly: true
  restartPolicy: Never
  volumes:
  - name: mongo-ca
    configMap:
      name: ${MDB_TLS_CA_CONFIGMAP:-"${MDB_RESOURCE_NAME}-ca-configmap"}
      optional: true
      items:
      - key: ca.crt
        path: ca.crt
EOF

echo "Waiting for the mongodb-tools to be ready..."
kubectl --context "${K8S_CTX}" -n "${MDB_NS}" wait --for=condition=Ready pod/mongodb-tools-pod --timeout=60s
```

**Step 3: Import the sample data.**

Import the `sample_mflix` database, which contains the following
collections: 

* - Collection Name
  - Description

* - `comments`
  - Contains comments associated with specific movies.

* - `embedded_movies`
  - Contains details on movies in the `Western`, 
    `Action`, and `Fantasy` genres from the `movies`
    collection with the following additional fields: 

    - `plot_embedding_voyage_3_large` - Contains 2048d embeddings
      created from the `plot` field using Voyage AI's
      `voyage-3-large` embedding model and converted to
      `binData` for efficient storage and retrieval.  

    - `plot_embedding` - Contains 1536d embeddings created from the
      `plot` field using OpenAI's `text-embedding-ada-002`
      embedding model and converted to `binData` for efficient
      storage and retrieval. 

* - `movies`
  - Contains movie information, including release year, director,
    and reviews.

* - `sessions`
  - Metadata field. Contains users'
    [JSON Web Tokens](https://en.wikipedia.org/wiki/JSON_Web_Token).

* - `theaters`
  - Contains locations of movie theaters.

* - `users`
  - Contains user information.

The following command downloads the sample dataset and uses
`mongorestore` to load the data into the `sample_mflix`
database in your MongoDB deployment, connecting as the
`mdb-user`.  

```shell
# Restore sample_mflix database. Provide any TLS parameters directly within MDB_CONNECTION_STRING.
kubectl exec -n "${MDB_NS}" --context "${K8S_CTX}" \
  mongodb-tools-pod -- env MDB_CONNECTION_STRING="${MDB_CONNECTION_STRING}" /bin/bash -eu -c "$(cat <<'EOF'
echo "Downloading sample database archive..."
curl -fSL https://atlas-education.s3.amazonaws.com/sample_mflix.archive -o /tmp/sample_mflix.archive

echo "Restoring sample database"
mongorestore \
  --archive=/tmp/sample_mflix.archive \
  --verbose=1 \
  --drop \
  --nsInclude 'sample_mflix.*' \
  --uri="${MDB_CONNECTION_STRING}"
EOF
)"
```

**Step 4: Create an index.**

You can create a MongoDB Search or a Vector Search index. You
must create a MongoDB Search index to run `$search` and
`$searchMeta` queries and Vector Search index to run
`$vectorSearch` queries. 

- MongoDB Search provides flexible index definitions that support
  dynamic and static field mappings, various analyzers (standard,
  language-specific, custom), and features like synonyms and
  faceted search. To learn more, see fts-define-index.
- Vector Search provides simple index definition that supports
  querying vector embeddings or text (if you enabled `mongot` 
  for Automated Embedding) in your data based on semantic 
  similarity by using ANN (Approximate Nearest Neighbor) 
  and ENN (Exact Nearest Neighbor) search algorithm. To 
  learn more, see Define Vector Search Index. 

a. Copy, paste, and run the following command in your terminal to
   create a MongoDB Search or a Vector Search index. 

   The command uses `kubectl exec` to run `mongosh` in the
   `mongodb-tools-pod`. It connects to the `sample_mflix`
   `db.<collection>.createSearchIndex()` method to create an index. 

   **fts:**

   The following command creates a MongoDB Search index named
   `default` with dynamic mappings on the `movies`
   collection. Dynamic mapping automatically indexes all
   dynamically indexable field types.

   ```shell
   kubectl exec --context "${K8S_CTX}" -n "${MDB_NS}" mongodb-tools-pod -- \
     mongosh --quiet "${MDB_CONNECTION_STRING}" \
       --eval "use sample_mflix" \
       --eval 'db.movies.createSearchIndex("default", { mappings: { dynamic: true } });'
   ```

   **vs:**

   The following command creates a Vector Search index named
   `vector_index` on the `plot_embedding_voyage_3_large`
   field with `2048` number of dimensions in the
   `embedded_movies` collection for running ANN
   (Approximate Nearest Neighbor) queries. 

   ```shell
   kubectl exec --context "${K8S_CTX}" -n "${MDB_NS}" mongodb-tools-pod -- \
     mongosh --quiet "${MDB_CONNECTION_STRING}" \
       --eval "use sample_mflix" \
       --eval 'db.embedded_movies.createSearchIndex("vector_index", "vectorSearch",
       { "fields": [ {
         "type": "vector",
         "path": "plot_embedding_voyage_3_large",
         "numDimensions": 2048,
         "similarity":
         "dotProduct",
         "quantization": "scalar"
       } ] });'
   ```

   **vs-auto-embed:**

   You can create the following index only if you configured `mongot` for Automated Embedding. 
   Automated Embedding is available as a Preview feature for 
   MongoDB Community Edition.

   The following command creates a Vector Search index named
   `vector_auto_embed_index` on the `plot` field in the `movies` 
   collection. The index definition uses the embedding model set in 
   the environment variable for generating embeddings for the data 
   in the `plot` field. 

   ```shell
   kubectl exec --context "${K8S_CTX}" -n "${MDB_NS}" mongodb-tools-pod -- \
     mongosh --quiet "${MDB_CONNECTION_STRING}" \
       --eval "use sample_mflix" \
       --eval 'db.movies.createSearchIndex("vector_auto_embed_index", "vectorSearch",
         { "fields": [ {
           "type": "autoEmbed",
           "modality": "text",
           "path": "plot",
           "model": "'"${EMBEDDING_MODEL}"'"
         } ] });'
   ```

#. Wait for index creation to complete. 

   Index creation is an asynchronous process. Run the following
   script to wait for 60 seconds for the index creation to
   complete. 

   ```shell
   # Currently it's not possible to check the status of search indexes, we need to just wait
   echo "Sleeping to wait for search indexes to be created"
   sleep 60
   ```

   Alternatively, run the following command to retrieve the list of
   indexes for the collection.

   **fts:**

   ```shell
   kubectl exec --context "${K8S_CTX}" -n "${MDB_NS}" mongodb-tools-pod -- \
     mongosh --quiet "${MDB_CONNECTION_STRING}" \
       --eval "use sample_mflix" \
       --eval 'db.runCommand({"listSearchIndexes": "movies"});'
   ```

   **vs:**

   ```shell
   kubectl exec --context "${K8S_CTX}" -n "${MDB_NS}" mongodb-tools-pod -- \
     mongosh --quiet "${MDB_CONNECTION_STRING}" \
       --eval "use sample_mflix" \
       --eval 'db.runCommand({"listSearchIndexes": "embedded_movies"});'
   ```

   **vs-auto-embed:**

   ```shell
   ```

   Output:

   ```shell
   ```

**Step 5: Query the data using the index.**

After the index creation is successful, you can run MongoDB Search
or Vector Search queries using the index. You can also combine
MongoDB Search with Vector Search. To learn more about running
MongoDB Search queries, see fts-define-query. To learn more
about Vector Search queries, see return-vector-search-results. 

The following script defines the aggregation pipeline query
criteria and uses the `kubectl exec` command to load `mongosh`
to execute the query. 

**fts:**

The following query searches the `plot` field for movie
plots that contain the term `baseball`. It excludes movies
in the `comedy` and `romance` genres. 

```shell
```

Output:

```shell
```

**vs:**

The following query searches the
`plot_embedding_voyage_3_large` field using 2048 dimension 
vector embeddings for the string `time travel`, generated
using Voyage AI's `voyage-3-large` model. 

```shell
```

Output:

```shell
```

**vs-auto-embed:**

The following query searches the `plot` field for movies with plots 
that are semantically similar to `spy thriller`, for which 
Vector Search automatically generated embeddings using the model 
specified in the index for the `plot` field (`voyage-4`). The 
query specifies up to `150` neighbors to consider and returns only 
the top `10` documents in the results.

```shell
```

Output:

```shell
```

## Resources

To learn more about creating indexes and running search queries, see:

- atlas-search
- avs-overview
