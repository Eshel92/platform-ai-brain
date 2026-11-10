<!-- Converted from setup/install/systemd.asciidoc (AsciiDoc). Includes are inlined. -->

#### Run Kibana with `systemd`

To configure Kibana to start automatically when the system starts,
run the following commands:

```sh
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable kibana.service
```

Kibana can be started and stopped as follows:

```sh
sudo systemctl start kibana.service
sudo systemctl stop kibana.service
```

These commands provide no feedback as to whether Kibana was started
successfully or not. Log information can be accessed via
`journalctl -u kibana.service`.
