<!-- Converted from upgrade/shut-down-node.asciidoc (AsciiDoc). Includes are inlined. -->

* If you are running Elasticsearch with `systemd`:
```sh
sudo systemctl stop elasticsearch.service
```

* If you are running Elasticsearch with SysV `init`:
```sh
sudo -i service elasticsearch stop
```

* If you are running Elasticsearch as a daemon:
```sh
kill $(cat pid)
```
