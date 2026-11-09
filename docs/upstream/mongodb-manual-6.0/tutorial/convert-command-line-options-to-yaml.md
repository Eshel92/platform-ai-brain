<!-- Converted from tutorial/convert-command-line-options-to-yaml.txt (reStructuredText). Includes are inlined. -->

# Convert Self-Managed Command-Line Options to YAML

`mongod` and `mongos` accept `--outputConfig` 
command-line option to output the configuration used by the
`mongod` / `mongos` instance. 

You can use this option to convert command-line options to YAML
configuration.
   

## Examples

### Convert `mongod` Command-Line Options to YAML

Consider the following `mongod` invocation that uses the
command-line options:

```bash
mongod --shardsvr --replSet myShard  --dbpath /var/lib/mongodb --bind_ip localhost,My-Example-Hostname --fork --logpath /var/log/mongodb/mongod.log --clusterAuthMode x509 --tlsMode requireTLS  --tlsCAFile /path/to/my/CA/file  --tlsCertificateKeyFile /path/to/my/certificate/file --tlsClusterFile /path/to/my/cluster/membership/file
```

Include the `--outputConfig`
command-line option to generate the corresponding YAML file.

```bash
mongod --shardsvr --replSet myShard  --dbpath /var/lib/mongodb --bind_ip localhost,My-Example-Hostname --fork --logpath /var/log/mongodb/mongod.log --clusterAuthMode x509 --tlsMode requireTLS  --tlsCAFile /path/to/my/CA/file  --tlsCertificateKeyFile /path/to/my/certificate/file --tlsClusterFile /path/to/my/cluster/membership/file --outputConfig
```

The `mongod` outputs the following YAML to `stdout` and
exits:

```yaml
net:
  bindIp: localhost,My-Example-Hostname
  tls:
    CAFile: /path/to/my/CA/file
    certificateKeyFile: /path/to/my/certificate/file
    clusterFile: /path/to/my/cluster/membership/file
    mode: requireTLS
outputConfig: true
processManagement:
  fork: true
replication:
  replSet: myShard
security:
  clusterAuthMode: x509
sharding:
  clusterRole: shardsvr
storage:
  dbPath: /var/lib/mongodb
systemLog:
  destination: file
  path: /var/log/mongodb/mongod.log
```

To create a configuration file, copy the generated content into a
file and delete the `outputConfig` setting from the YAML.

### Convert `mongos` Command-Line Options to YAML

Consider the following `mongos` invocation that uses the
command-line options:

```bash
mongos --configdb myCSRS/cfg1.example.net:27019,cfg2.example.net:27019 --bind_ip localhost,My-Example-MONGOS-Hostname --fork --logpath /var/log/mongodb/mongos.log --clusterAuthMode x509 --tlsMode requireTLS  --tlsCAFile /path/to/my/CA/file  --tlsCertificateKeyFile /path/to/my/certificate/file --tlsClusterFile /path/to/my/cluster/membership/file
```

Include the `--outputConfig`
command-line option to generate the corresponding YAML for the
`mongos` instance:

```bash
mongos --configdb myCSRS/cfg1.example.net:27019,cfg2.example.net:27019 --bind_ip localhost,My-Example-MONGOS-Hostname --fork --logpath /var/log/mongodb/mongos.log --clusterAuthMode x509 --tlsMode requireTLS  --tlsCAFile /path/to/my/CA/file  --tlsCertificateKeyFile /path/to/my/certificate/file --tlsClusterFile /path/to/my/cluster/membership/file --outputConfig
```

The `mongos` outputs the following YAML to `stdout` and exits:

```yaml
net:
  bindIp: localhost,My-Example-MONGOS-Hostname
  tls:
    CAFile: /path/to/my/CA/file
    certificateKeyFile: /path/to/my/certificate/file
    clusterFile: /path/to/my/cluster/membership/file
    mode: requireTLS
outputConfig: true
processManagement:
  fork: true
security:
  clusterAuthMode: x509
sharding:
  configDB: myCSRS/cfg1.example.net:27019,cfg2.example.net:27019
systemLog:
  destination: file
  path: /var/log/mongodb/mongos.log
```

To create a configuration file, copy the generated content into a
file and delete the `outputConfig` setting from the YAML.
