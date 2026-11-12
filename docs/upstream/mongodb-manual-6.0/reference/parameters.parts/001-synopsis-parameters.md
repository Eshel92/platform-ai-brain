<!-- Part 1 of 8 of reference/parameters.md (split because the page is big). -->

## Synopsis

MongoDB provides a number of configuration options that you can set
using:

- the `setParameter` command:

  ```javascript
  db.adminCommand( { setParameter: 1, <parameter>: <value>  } )
  ```

- the `setParameter` configuration setting:

  ```yaml
  setParameter:
     <parameter1>: <value1>
     ...
  ```

- the `--setParameter` command-line option for `mongod`
  and `mongos`:

  ```bash
  mongod --setParameter <parameter>=<value>
  mongos --setParameter <parameter>=<value>
  ```

For additional configuration options, see
/reference/configuration-options, `mongod` and
`mongos`.


## Parameters
