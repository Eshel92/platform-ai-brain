<!-- Converted from setup/install/targz-running.asciidoc (AsciiDoc). Includes are inlined. -->

#### Run Kibana from the command line

Kibana can be started from the command line as follows:

```sh
./bin/kibana
```

By default, Kibana runs in the foreground, prints its logs to the
standard output (`stdout`), and can be stopped by pressing *Ctrl-C*.

If this is the first time you're starting Kibana, this command generates a 
unique link in your terminal to enroll your Kibana instance with Elasticsearch.

. In your terminal, click the generated link to open Kibana in your browser.

. In your browser, paste the enrollment token that was generated in the terminal 
when you started Elasticsearch, and then click the button to connect your Kibana instance with Elasticsearch.

. Log in to Kibana as the `elastic` user with the password that was 
generated when you started Elasticsearch.

**Note:**
If you need to reset the password for the `elastic` user or other
built-in users, run the [`elasticsearch-reset-password`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/reset-password.html) tool. To generate new enrollment tokens for 
Kibana or Elasticsearch nodes, run the
[`elasticsearch-create-enrollment-token`](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/create-enrollment-token.html) tool.
These tools are available in the Elasticsearch `bin` directory.
