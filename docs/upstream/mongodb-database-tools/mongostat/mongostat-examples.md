<!-- Converted from mongostat/mongostat-examples.txt (reStructuredText). Includes are inlined. -->

# mongostat Examples

This page shows examples for `mongostat`.

Run `mongostat` from the system command line, not the 
`mongo` shell.

## Specify `mongostat` Collection Period and Frequency

In the first example, `mongostat` will return data every
second for 20 seconds. `mongostat` collects data from the
`mongod` instance running on the localhost interface on
port 27017. All of the following invocations produce identical
behavior:

```sh
mongostat --rowcount=20 1
mongostat --rowcount=20
mongostat -n=20 1
mongostat -n=20
```

In the next example, `mongostat` returns data every 5 minutes
(or 300 seconds) for as long as the program runs. `mongostat`
collects data from the `mongod` instance running on the
localhost interface on port `27017`. The following
invocations produce identical behavior:

```sh
mongostat --rowcount=0 300
mongostat -n=0 300
mongostat 300
```

In the following example, `mongostat` returns data every 5
minutes for an hour (12 times.) `mongostat` collects data
from the `mongod` instance running on the localhost interface
on port 27017. The following invocations produce identical
behavior:

```sh
mongostat --rowcount=12 300
mongostat -n=12 300
```

## Add Fields to `mongostat` Output

`-O` allows you to specify fields from the
`serverStatus` output to add to the default
`mongostat` output. If you include a space in your
custom filed name, do not put additional quotes around the field name. 

The following example adds fields to the default
`mongostat` output:

```sh
mongostat -O='host,version,network.numRequests=network requests'
```

The `mongostat` output resembles:

```sh
insert query update delete getmore command dirty used flushes vsize   res qrw arw net_in net_out conn                time            host version network requests
    *0    *0     *0     *0       0     2|0  0.0% 0.0%       0 2.51G 19.0M 0|0 0|0   158b   39.4k    2 Oct 11 12:14:45.878 localhost:37017  3.3.14               91
    *0    *0     *0     *0       0     1|0  0.0% 0.0%       0 2.51G 19.0M 0|0 0|0   157b   39.3k    2 Oct 11 12:14:46.879 localhost:37017  3.3.14               95
    *0    *0     *0     *0       0     1|0  0.0% 0.0%       0 2.51G 19.0M 0|0 0|0   157b   39.2k    2 Oct 11 12:14:47.884 localhost:37017  3.3.14               99
```

The following fields are added to the default output:

- `host`
- `version`
- `network.numRequests`

The `network.numRequests` field has a custom field name,
"network requests".

## Specify `mongostat` Output Fields

`-o` specifies the columns
`mongostat` includes in its output. You can specify any
`serverStatus` field as a `mongostat` output
column.

The following example uses custom fields for `mongostat`:

```sh
mongostat --port 27500 -o='host,opcounters.insert.rate()=Insert Rate,opcounters.query.rate()=Query Rate,opcounters.command.rate()=Command Rate,wiredTiger.cache.pages requested from the cache=Pages Req,metrics.document.inserted=inserted rate'
```

The `mongostat` output resembles:

```sh
           host Insert Rate Query Rate Command Rate Pages Req Inserted Rate
localhost:27500         180          1            8   2999446          9638
localhost:27500          40          3           12   2999601          9678
localhost:27500         181          2            9   3000207          9859
localhost:27500          39          2           12   3000362          9899
localhost:27500         181          2           11   3000969         10080
localhost:27500          39          2           10   3001124         10120
```

The counters and corresponding custom field names are: 

| Counter | Custom Field Name |
|---|---|
| opcounters.insert.rate | Insert Rate |
| opcounters.query.rate | Query Rate |
| opcounters.command.rate | Command Rate |
| wiredTiger.cache.pages requested from the cache | Pages Req |
| metrics.document.inserted | Inserted Rate |

## View Rate of Change for a Field with `.rate()`

`.rate()` enables you to view the rate per second at which a
numerical field has changed from one `mongostat` call to the
next. For example, you can view the rate at which documents have been
inserted during an insert operation. `.rate()` can therefore
help you view the performance of your `mongod` instance.

The following example reports on the rate of change of the
`metrics.document.inserted` `serverStatus` field. The
invocation uses `-o`'s ability to specify the name of an column
to label `metrics.document.inserted.rate()` as "inserted rate" and
`metrics.document.inserted` as "inserted":

```sh
mongostat -o='host,mem,bits,metrics.document.inserted.rate()=inserted rate,metrics.document.inserted=inserted' --rowcount=5
```

The output would then resemble:

```sh
           host mem.bits inserted rate inserted
localhost:37017       64           501     3455
localhost:37017       64           967    13128
localhost:37017       64           972    22851
localhost:37017       64           214    25000
localhost:37017       64             0    25000
```

## View Field Changes with `.diff()`

`.diff()` returns the difference between the current
`serverStatus` field value and the value from the previous
`mongostat` call. The following example returns statistics on
the number of documents being inserted into a collection: ``inserted
diff`` is the difference in the
`metrics.document.inserted` field between subsequent
calls, while `inserted` is the value of
`metrics.document.inserted`:

```sh
mongostat -o='host,mem.bits,metrics.document.inserted.diff()=inserted diff,metrics.document.inserted=inserted' --rowcount=5
```

The output would then resemble:

```sh
           host mem.bits inserted diff inserted
localhost:27017       64             0    25359
localhost:27017       64            94    25453
localhost:27017       64           938    26391
localhost:27017       64           964    27355
localhost:27017       64           978    28333
```

## View Statistics for a Replica Set or Sharded Cluster

In many cases, using the `--discover` option
will help provide a more complete snapshot of the state of an entire
group of machines. If a `mongos` process connected to a
sharded cluster is running on port `27017` of the local
machine, you can use the following form to return statistics from all
members of the cluster:

```sh
mongostat --discover
```

## View Statistics in an Interactive Interface

Use the `--interactive` option to
view statistics in a non-scrolling [ncurses](https://www.gnu.org/software/ncurses/) -style
interactive output. The `--interactive` option lets you highlight specific
hosts, columns, or fields to view. When combined with `--discover`,
`--interactive` displays statistics for all members of a
replica set or sharded cluster, as in the following example:

```sh
mongostat --discover --interactive
```

The output for a sharded cluster would then resemble:

```sh
                  host insert query update delete getmore command dirty used flushes mapped vsize   res faults qrw arw net_in net_out conn set repl                time
hostname.local:27018     *0    *0     *0     *0       0     1|0  0.0% 0.0%       0        3.25G 25.0M    n/a 0|0 1|0   157b   43.9k   19 tic  PRI Nov  2 11:44:46.439
hostname.local:27019     *0    *0     *0     *0       0     2|0  0.0% 0.0%       0        3.18G 26.0M    n/a 0|0 1|0   322b   44.4k   12 tic  SEC Nov  2 11:44:46.439
hostname.local:27020     *0    *0     *0     *0       0     2|0  0.0% 0.0%       0        3.18G 26.0M    n/a 0|0 1|0   322b   44.4k   12 tic  SEC Nov  2 11:44:46.439
hostname.local:27021   2017    *0     *0     *0     826  1029|0  0.0% 0.0%       0        3.25G 31.0M    n/a 0|0 1|0  1.74m   1.60m   20 tac  PRI Nov  2 11:44:46.439
hostname.local:27022  *2021    *0     *0     *0       0     2|0  0.0% 0.0%       0        3.19G 32.0M    n/a 0|0 1|0   322b   44.6k   12 tac  SEC Nov  2 11:44:46.438
hostname.local:27023  *2022    *0     *0     *0       0     3|0  0.0% 0.0%       0        3.19G 33.0M    n/a 0|0 1|0   323b   44.7k   12 tac  SEC Nov  2 11:44:46.438
     localhost:27017   2071    *0     *0     *0       0  2073|0                  0     0B 2.43G 9.00M      0 0|0 0|0   249k    130k    4      RTR Nov  2 11:44:47.429

Press '?' to toggle help
```

## Connect to a MongoDB Atlas Cluster using AWS IAM Credentials

**New in version:** 100.1.0

To connect to a MongoDB Atlas cluster which
has been configured to support authentication via [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html),
provide a `connection string` to
`mongostat` similar to the following:

```none
mongostat 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' <other options>
```

Connecting to Atlas using AWS IAM credentials in this manner uses the
`MONGODB-AWS` `authentication mechanism`
and the `$external` `authSource`, as shown in this example.

If using an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html),
as well, provide it with the `AWS_SESSION_TOKEN`
`authMechanismProperties` value, as follows:

```none
mongostat 'mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>' <other options>
```

**Note:**

If the AWS access key ID, secret access key, or session token
include the following characters:

```none
: / ? # [ ] @
```

those characters must be converted using [percent encoding](https://tools.ietf.org/html/rfc3986#section-2.1).

Alternatively, the AWS access key ID, secret access key, and optionally
session token can each be provided outside of the connection string
using the `--username`, `--password`, and
`--awsSessionToken` options instead, like so:

```none
mongostat 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS' --username <aws access key id> --password <aws secret access key> --awsSessionToken <aws session token> <other options>
```

When provided as command line parameters, these three options do not
require percent encoding.

You may also set these credentials on your platform using standard
[AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list).
`mongostat` checks for the following environment variables when you
use the `MONGODB-AWS`
`authentication mechanism`:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN`

If set, these credentials do not need to be specified in the connection
string or via their explicit options.

**Note:**

If you chose to use the AWS environment variables to specify these
values, you cannot mix and match with the corresponding explicit or 
connection string options for these credentials. Either use the
environment variables for access key ID *and* secret access key
(*and* session token if used), **or** specify each of these using the
explicit or connection string options instead.

The following example sets these environment variables in the `bash`
shell:

```none
export AWS_ACCESS_KEY_ID='<aws access key id>'
export AWS_SECRET_ACCESS_KEY='<aws secret access key>'
export AWS_SESSION_TOKEN='<aws session token>'
```

Syntax for setting environment variables in other shells will be
different. Consult the documentation for your platform for more
information.

You can verify that these environment variables have been set with the
following command:

```none
env | grep AWS
```

Once set, the following example connects to a MongoDB Atlas cluster
using these environment variables:

```none
mongostat 'mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS'  <other options>
```

## Learn More

- mongostat
- mongostat-compatibility-and-installation
- mongostat Behavior
