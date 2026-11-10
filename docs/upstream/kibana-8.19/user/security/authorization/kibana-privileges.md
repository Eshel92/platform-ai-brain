<!-- Converted from user/security/authorization/kibana-privileges.asciidoc (AsciiDoc). Includes are inlined. -->

# Kibana privileges

Kibana privileges grant users access to features within Kibana. Roles have privileges to determine whether users have write or read access.

## Base privileges

Assigning a base privilege grants access to all Kibana features, such as *Discover*, *Dashboard*, *Visualize Library*, and *Canvas*.
`all`:: Grants full read-write access.
`read`:: Grants read-only access.

### Assigning base privileges

From the role management screen:

(Figure: security/images/assign-base-privilege.png)

Using the [role APIs](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-roles):
```js
PUT /api/security/role/my_kibana_role
{
  "elasticsearch": {
    "cluster" : [ ],
    "indices" : [ ]
  },
  "kibana": [
    {
      "base": ["all"],
      "feature": {},
      "spaces": ["marketing"]
    }
  ]
}
```

## Feature privileges

Assigning a feature privilege grants access to a specific feature.

`all`:: Grants full read-write access.
`read`:: Grants read-only access.

### Sub-feature privileges

Some features allow for finer access control than the `all` and `read` privileges.
This additional level of control is a {subscriptions}[subscription feature].

### Assigning feature privileges

From the role management screen:

(Figure: security/images/assign-subfeature-privilege.png)

Using the [role APIs](https://www.elastic.co/docs/api/doc/kibana/group/endpoint-roles):
```js
PUT /api/security/role/my_kibana_role
{
  "elasticsearch": {
    "cluster" : [ ],
    "indices" : [ ]
  },
  "kibana": [
    {
      "base": [],
      "feature": {
        "visualize": ["all"],
        "dashboard": ["read", "url_create"]
      },
      "spaces": ["marketing"]
    }
  ]
}
```
