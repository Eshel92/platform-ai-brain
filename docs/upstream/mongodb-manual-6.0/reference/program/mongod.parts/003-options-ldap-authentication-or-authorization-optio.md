<!-- Part 3 of 6 of reference/program/mongod.md (split because the page is big). -->

### LDAP Authentication or Authorization Options

**`--ldapServers <host1>:<port>,<host2>:<port>,...,<hostN>:<port>`**

*Available in MongoDB Enterprise only.*

The LDAP server against which the `mongod` authenticates users or
determines what actions a user is authorized to perform on a given
database. If the LDAP server specified has any replicated instances,
you may specify the host and port of each replicated server in a
comma-delimited list.

If your LDAP infrastructure partitions the LDAP directory over multiple LDAP
servers, specify *one* LDAP server or any of its replicated instances to
`--ldapServers`. MongoDB supports following LDAP referrals as defined in [RFC 4511 4.1.10](https://www.rfc-editor.org/rfc/rfc4511.txt). Do not use `--ldapServers`
for listing every LDAP server in your infrastructure.

This setting can be configured on a running `mongod` using
`setParameter`.

If unset, `mongod` cannot use LDAP authentication or authorization.

**`--ldapValidateLDAPServerConfig <boolean>`**

*Available in MongoDB Enterprise*

A flag that determines if the `mongod` instance checks
the availability of the `LDAP server(s)` as part of its startup:

- If `true`, the `mongod` instance performs the
  availability check and only continues to start up if the LDAP
  server is available.

- If `false`, the `mongod` instance skips the
  availability check; i.e. the instance starts up even if the LDAP
  server is unavailable.

**`--ldapQueryUser <string>`**

*Available in MongoDB Enterprise only.*

The identity with which `mongod` binds as, when connecting to or
performing queries on an LDAP server.

Only required if any of the following are true:

- Using LDAP authorization.
- Using an LDAP query for `username transformation`.
- The LDAP server disallows anonymous binds

You must use `--ldapQueryUser` with `--ldapQueryPassword`.

If unset, `mongod` doesn't attempt to bind to the LDAP server.

This setting can be configured on a running `mongod` using
`setParameter`.

**Note:**

Windows MongoDB deployments can use `--ldapBindWithOSDefaults`
instead of `--ldapQueryUser` and `--ldapQueryPassword`. You cannot specify
both `--ldapQueryUser` and `--ldapBindWithOSDefaults` at the same time.

**`--ldapQueryPassword <string | array>`**

*Type*: string or array

*Available in MongoDB Enterprise only.*

The password used to bind to an LDAP server when using
`queryUser`. You must use 
`queryPassword` with
`queryUser`.

If not set, `mongod` or `mongos` does not attempt to
bind to the LDAP server.

You can configure this setting on a running `mongod` or 
`mongos` using `setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a 
string or an array of strings. If `ldapQueryPassword` is set to an array, 
MongoDB tries each password in order until one succeeds. Use a password array 
to roll over the LDAP account password without downtime.

**Note:**

Windows MongoDB deployments can use `useOSDefaults`
instead of `queryUser` and 
`queryPassword`. You cannot specify both 
`queryPassword` and 
`useOSDefaults` at the same time.

*Available in MongoDB Enterprise only.*

The password used to bind to an LDAP server when using
`--ldapQueryUser`. You must use `--ldapQueryPassword` with
`--ldapQueryUser`.

If not set, `mongod` does not attempt to bind to the LDAP server.

You can configure this setting on a running `mongod` using
`setParameter`.

The `ldapQueryPassword` `setParameter` command accepts either a 
string or an array of strings. If `ldapQueryPassword` is set to an array, 
MongoDB tries each password in order until one succeeds. Use a password array 
to roll over the LDAP account password without downtime.

**Note:**

Windows MongoDB deployments can use `--ldapBindWithOSDefaults`
instead of `--ldapQueryUser` and `--ldapQueryPassword`. 
You cannot specify both `--ldapQueryPassword` and 
`--ldapBindWithOSDefaults` at the same time.

*Available in MongoDB Enterprise only.*

The password used to bind to an LDAP server when using
`--ldapQueryUser`. You must use `--ldapQueryPassword` with
`--ldapQueryUser`.

If not set, `mongoldap` does not attempt to bind to the LDAP server.

You can configure this setting on a running `mongoldap` using
`setParameter`.

The `ldapQueryPassword``setParameter` command accepts either a 
string or an array of strings. If `ldapQueryPassword` is set to an array, 
MongoDB tries each password in order until one succeeds. Use a password array 
to roll over the LDAP account password without downtime.

**Note:**

Windows MongoDB deployments can use `--ldapBindWithOSDefaults`
instead of `--ldapQueryUser` and `--ldapQueryPassword`. 
You cannot specify both `--ldapQueryPassword` and 
`--ldapBindWithOSDefaults` at the same time.

**`--ldapBindWithOSDefaults <bool>`**

*Default*: false

Available in MongoDB Enterprise for the Windows platform only.

Allows `mongod` to authenticate, or bind, using your Windows login
credentials when connecting to the LDAP server.

Only required if:

- Using LDAP authorization.
- Using an LDAP query for `username transformation`.
- The LDAP server disallows anonymous binds

Use `--ldapBindWithOSDefaults` to replace `--ldapQueryUser` and
`--ldapQueryPassword`.

**`--ldapBindMethod <string>`**

*Default*: simple

*Available in MongoDB Enterprise only.*

The method `mongod` uses to authenticate to an LDAP server.
Use with `--ldapQueryUser` and `--ldapQueryPassword` to
connect to the LDAP server.

`--ldapBindMethod` supports the following values:

* `simple` - `mongod` uses simple authentication.

* `sasl` - `mongod` uses SASL protocol for authentication

If you specify `sasl`, you can configure the available SASL mechanisms
using `--ldapBindSaslMechanisms`. `mongod` defaults to
using `DIGEST-MD5` mechanism.

**`--ldapBindSaslMechanisms <string>`**

*Default*: DIGEST-MD5

*Available in MongoDB Enterprise only.*

A comma-separated list of SASL mechanisms `mongod` can
use when authenticating to the LDAP server. The `mongod` and the
LDAP server must agree on at least one mechanism. The `mongod`
dynamically loads any SASL mechanism libraries installed on the host
machine at runtime.

Install and configure the appropriate libraries for the selected
SASL mechanism(s) on both the `mongod` host and the remote
LDAP server host. Your operating system may include certain SASL
libraries by default. Defer to the documentation associated with each
SASL mechanism for guidance on installation and configuration.

If using the `GSSAPI` SASL mechanism for use with
security-kerberos, verify the following for the
`mongod` host machine:

`Linux`
  - The `KRB5_CLIENT_KTNAME` environment
    variable resolves to the name of the client keytab-files
    for the host machine. For more on Kerberos environment
    variables, please defer to the
    [Kerberos documentation](https://web.mit.edu/kerberos/krb5-1.13/doc/admin/env_variables.html).
  - The client keytab includes a
    kerberos-user-principal for the `mongod` to use when
    connecting to the LDAP server and execute LDAP queries.

`Windows`
  If connecting to an Active Directory server, the Windows
  Kerberos configuration automatically generates a
  [Ticket-Granting-Ticket](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380510(v=vs.85).aspx)
  when the user logs onto the system. Set `--ldapBindWithOSDefaults` to
  `true` to allow `mongod` to use the generated credentials when
  connecting to the Active Directory server and execute queries.

Set `--ldapBindMethod` to `sasl` to use this option.

**Note:**

For a complete list of SASL mechanisms see the
[IANA listing](http://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml).
Defer to the documentation for your LDAP or Active Directory
service for identifying the SASL mechanisms compatible with the
service.

MongoDB is not a source of SASL mechanism libraries, nor
is the MongoDB documentation a definitive source for
installing or configuring any given SASL mechanism. For
documentation and support, defer to the SASL mechanism
library vendor or owner.

For more information on SASL, defer to the following resources:

- For Linux, please see the [Cyrus SASL documentation](https://www.cyrusimap.org/sasl/).
- For Windows, please see the [Windows SASL documentation](https://msdn.microsoft.com/en-us/library/cc223500.aspx).

**`--ldapTransportSecurity <string>`**

*Default*: tls

*Available in MongoDB Enterprise only.*

By default, `mongod` creates a TLS/SSL secured connection to the LDAP
server.

For Linux deployments, you must configure the appropriate TLS Options in
`/etc/openldap/ldap.conf` file. Your operating system's package manager
creates this file as part of the MongoDB Enterprise installation, via the
`libldap` dependency. See the documentation for `TLS Options` in the
[ldap.conf OpenLDAP documentation](http://www.openldap.org/software/man.cgi?query=ldap.conf&manpath=OpenLDAP+2.4-Release)
for more complete instructions.

For Windows deployment, you must add the LDAP server CA certificates to the
Windows certificate management tool. The exact name and functionality of the
tool may vary depending on operating system version. Please see the
documentation for your version of Windows for more information on
certificate management.

Set `--ldapTransportSecurity` to `none` to disable TLS/SSL between `mongod` and the LDAP
server.

**Warning:**

Setting `--ldapTransportSecurity` to `none` transmits plaintext information and possibly
credentials between `mongod` and the LDAP server.

**`--ldapTimeoutMS <long>`**

*Default*: 10000

*Available in MongoDB Enterprise only.*

The amount of time in milliseconds `mongod` should wait for an LDAP server
to respond to a request.

Increasing the value of `--ldapTimeoutMS` may prevent connection failure between the
MongoDB server and the LDAP server, if the source of the failure is a
connection timeout. Decreasing the value of `--ldapTimeoutMS` reduces the time
MongoDB waits for a response from the LDAP server.

This setting can be configured on a running `mongod` using
`setParameter`.

**`--ldapUserToDNMapping <string>`**

*Available in MongoDB Enterprise only.*

Maps the username provided to `mongod` for authentication to a LDAP
Distinguished Name (DN). You may need to use `--ldapUserToDNMapping` to transform a
username into an LDAP DN in the following scenarios:

- Performing LDAP authentication with simple LDAP binding, where users
  authenticate to MongoDB with usernames that are not full LDAP DNs.

- Using an `LDAP authorization query template` that requires a DN.

- Transforming the usernames of clients authenticating to Mongo DB 
  using different authentication mechanisms, such as x.509 or
  kerberos, to a full LDAP DN for authorization.

`--ldapUserToDNMapping` expects a quote-enclosed JSON-string representing an ordered array
of documents. Each document contains a regular expression `match` and
either a `substitution` or `ldapQuery` template used for transforming the
incoming username.

Each document in the array has the following form:

```javascript
{
  match: "<regex>"
  substitution: "<LDAP DN>" | ldapQuery: "<LDAP Query>"
}
```

| Field | Description | Example |
|---|---|---|
| `match` | An ECMAScript-formatted regular expression (regex) to match against a provided username. Each parenthesis-enclosed section represents a regex capture group used by `substitution` or `ldapQuery`. | `"(.+)ENGINEERING"` `"(.+)DBA"` |
| `substitution` | An LDAP distinguished name (DN) formatting template that converts the authentication name matched by the `match` regex into a LDAP DN. Each curly bracket-enclosed numeric value is replaced by the corresponding [regex capture group](http://www.regular-expressions.info/refcapture.html) extracted from the authentication username via the `match` regex. The result of the substitution must be an [RFC4514](https://www.ietf.org/rfc/rfc4514.txt) escaped string. | `"cn={0},ou=engineering, dc=example,dc=com"` |
| `ldapQuery` | A LDAP query formatting template that inserts the authentication name matched by the `match` regex into an LDAP query URI encoded respecting RFC4515 and RFC4516. Each curly bracket-enclosed numeric value is replaced by the corresponding [regex capture group](http://www.regular-expressions.info/refcapture.html) extracted from the authentication username via the `match` expression. `mongod` executes the query against the LDAP server to retrieve the LDAP DN for the authenticated user. `mongod` requires exactly one returned result for the transformation to be successful, or `mongod` skips this transformation. | `"ou=engineering,dc=example, dc=com??one?(user={0})"` |

**Note:**

An explanation of  [RFC4514](https://www.ietf.org/rfc/rfc4514.txt),
[RFC4515](https://tools.ietf.org/rfc/rfc4515),
[RFC4516](https://tools.ietf.org/html/rfc4516), or LDAP queries is out
of scope for the MongoDB Documentation. Please review the RFC directly or
use your preferred LDAP resource.

For each document in the array, you must use either `substitution` or
`ldapQuery`. You *cannot* specify both in the same document.

When performing authentication or authorization, `mongod` steps through
each document in the array in the given order, checking the authentication
username against the `match` filter.  If a match is found,
`mongod` applies the transformation and uses the output for
authenticating the user. `mongod` does not check the remaining documents
in the array.

If the given document does not match the provided authentication
name, `mongod` continues through the list of documents
to find additional matches. If no matches are found in any document,
or the transformation the document describes fails,
`mongod` returns an error. 

`mongod` also returns an error if one of the transformations cannot be 
evaluated due to networking or authentication failures to the LDAP server. 
`mongod` rejects the connection request and does not check the remaining
documents in the array.

Starting in MongoDB 5.0, `--ldapUserToDNMapping`
accepts an empty string `""` or empty array `[ ]` in place of a
mapping documnent. If providing an empty string or empty array to
`--ldapUserToDNMapping`, MongoDB maps the
authenticated username as the LDAP DN. In earlier versions, providing
an empty mapping document causes mapping to fail.

**Example:**

The following shows two transformation documents. The first
document matches against any string ending in `@ENGINEERING`, placing
anything preceeding the suffix into a regex capture group. The
second document matches against any string ending in `@DBA`, placing
anything preceeding the suffix into a regex capture group.

**Important:** You must pass the array to `--ldapUserToDNMapping` as a string.

```text
"[
   {
      match: "(.+)@ENGINEERING.EXAMPLE.COM",
      substitution: "cn={0},ou=engineering,dc=example,dc=com"
   },
   {
      match: "(.+)@DBA.EXAMPLE.COM",
      ldapQuery: "ou=dba,dc=example,dc=com??one?(user={0})"

   }

]"
```

A user with username `alice@ENGINEERING.EXAMPLE.COM` matches the first
document. The regex capture group `{0}` corresponds to the string
`alice`. The resulting output is the DN
`"cn=alice,ou=engineering,dc=example,dc=com"`.

A user with username `bob@DBA.EXAMPLE.COM` matches the second document.
The regex capture group `{0}` corresponds to the string `bob`.  The
resulting output is the LDAP query
`"ou=dba,dc=example,dc=com??one?(user=bob)"`. `mongod` executes this
query against the LDAP server, returning the result
`"cn=bob,ou=dba,dc=example,dc=com"`.

If `--ldapUserToDNMapping` is unset, `mongod` applies no transformations to the username
when attempting to authenticate or authorize a user against the LDAP server.

This setting can be configured on a running `mongod` using the
`setParameter` database command.

**`--ldapAuthzQueryTemplate <string>`**

*Available in MongoDB Enterprise only.*

A relative LDAP query URL formatted conforming to [RFC4515](https://tools.ietf.org/rfc/rfc4515) and [RFC4516](https://tools.ietf.org/html/rfc4516) that `mongod` executes to obtain
the LDAP groups to which the authenticated user belongs to. The query is
relative to the host or hosts specified in `--ldapServers`.

In the URL, you can use the following substituion tokens:

| Substitution Token | Description |
|---|---|
| `{USER}` | Substitutes the authenticated username, or the `transformed` username if a `username mapping` is specified. |
| `{PROVIDED_USER}` | Substitutes the supplied username, i.e. before either authentication or `LDAP transformation`. |

When constructing the query URL, ensure that the order of LDAP parameters
respects RFC4516:

```bash
[ dn  [ ? [attributes] [ ? [scope] [ ? [filter] [ ? [Extensions] ] ] ] ] ]
```

If your query includes an attribute, `mongod` assumes that the query
retrieves a the DNs which this entity is member of.

If your query does not include an attribute, `mongod` assumes
the query retrieves all entities which the user is member of.

For each LDAP DN returned by the query, `mongod` assigns the authorized
user a corresponding role on the `admin` database. If a role on the on the
`admin` database exactly matches the DN, `mongod` grants the user the
roles and privileges assigned to that role. See the
`db.createRole()` method for more information on creating roles.

**Example:**

This LDAP query returns any groups listed in the LDAP user object's
`memberOf` attribute.

```bash
"{USER}?memberOf?base"
```

Your LDAP configuration may not include the `memberOf` attribute as part
of the user schema, may possess a different attribute for reporting group
membership, or may not track group membership through attributes.
Configure your query with respect to your own unique LDAP configuration.

If unset, `mongod` cannot authorize users using LDAP.

This setting can be configured on a running `mongod` using the
`setParameter` database command.

**Note:**

An explanation of [RFC4515](https://tools.ietf.org/rfc/rfc4515),
[RFC4516](https://tools.ietf.org/html/rfc4516) or LDAP queries is out
of scope for the MongoDB Documentation. Please review the RFC directly or
use your preferred LDAP resource.
