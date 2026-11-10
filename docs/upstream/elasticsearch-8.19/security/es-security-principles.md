<!-- Converted from security/es-security-principles.asciidoc (AsciiDoc). Includes are inlined. -->

## Elasticsearch security principles

Protecting your Elasticsearch cluster and the data it contains is of utmost importance.
Implementing a defense in depth strategy provides multiple layers of security
to help safeguard your system. The following principles provide a foundation
for running Elasticsearch in a secure manner that helps to mitigate attacks on your
system at multiple levels.

### Run Elasticsearch with security enabled

Never run an Elasticsearch cluster without security enabled. This principle cannot be
overstated. Running Elasticsearch without security leaves your cluster exposed to anyone
who can send network traffic to Elasticsearch, permitting these individuals to download,
modify, or delete any data in your cluster.
Start the Elastic Stack with security enabled or
manually configure security to prevent
unauthorized access to your clusters and ensure that internode communication
is secure. 

### Run Elasticsearch with a dedicated non-root user

Never try to run Elasticsearch as the `root` user, which would invalidate any defense 
strategy and permit a malicious user to do *anything* on your server. You must 
create a dedicated, unprivileged user to run Elasticsearch. By default, the `rpm`, `deb`, 
`docker`, and Windows packages of Elasticsearch contain an `elasticsearch` user with
this scope.

### Protect Elasticsearch from public internet traffic

Even with security enabled, never expose Elasticsearch to public internet traffic.
Using an application to sanitize requests to Elasticsearch still poses risks, such as
a malicious user writing `_search` requests that could overwhelm an
Elasticsearch cluster and bring it down. Keep Elasticsearch as isolated as possible, preferably
behind a firewall and a VPN. Any internet-facing applications should run 
pre-canned aggregations, or not run aggregations at all.

While you absolutely shouldn't expose Elasticsearch directly to the internet, you also
shouldn't expose Elasticsearch directly to users. Instead, use an intermediary
application to make requests on behalf of users. This implementation allows you 
to track user behaviors, such as can submit requests, and to which specific
nodes in the cluster. For example, you can implement an application that accepts
a search term from a user and funnels it through a
`simple_query_string` query. 

### Implement role based access control

Define roles for your users and
assign appropriate privileges to ensure that users have
access only to the resources that they need. This process determines whether the 
user behind an incoming request is allowed to run that request.
