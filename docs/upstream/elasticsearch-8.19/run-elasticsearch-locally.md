<!-- Converted from run-elasticsearch-locally.asciidoc (AsciiDoc). Includes are inlined. -->

## Run Elasticsearch locally

**Warning:**
*DO NOT USE THESE INSTRUCTIONS FOR PRODUCTION DEPLOYMENTS*

The instructions on this page are for *local development only*. Do not use this configuration for production deployments, because it is not secure.
Refer to deployment options for a list of production deployment options.

Quickly set up Elasticsearch and Kibana in Docker for local development or testing, using the [`start-local` script](https://github.com/elastic/start-local?tab=readme-ov-file#-try-elasticsearch-and-kibana-locally).

This setup comes with a one-month trial of the Elastic *Platinum* license.
After the trial period, the license reverts to *Free and open - Basic*.
Refer to [Elastic subscriptions](https://www.elastic.co/subscriptions) for more information.

### Prerequisites

- If you don't have Docker installed, [download and install Docker Desktop](https://www.docker.com/products/docker-desktop) for your operating system.
- If you're using Microsoft Windows, then install [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install).

### Run `start-local`

To set up Elasticsearch and Kibana locally, run the `start-local` script:

```sh
curl -fsSL https://elastic.co/start-local | sh
```

This script creates an `elastic-start-local` folder containing configuration files and starts both Elasticsearch and Kibana using Docker.

After running the script, you can access Elastic services at the following endpoints:

* *Elasticsearch*: http://localhost:9200
* *Kibana*: http://localhost:5601

The script generates a random password for the `elastic` user, and an API key, stored in the `.env` file.

**Caution:**
This setup is for local testing only. HTTPS is disabled, and Basic authentication is used for Elasticsearch. For security, Elasticsearch and Kibana are accessible only through `localhost`.

### Learn more

For more detailed information about the `start-local` setup, refer to the [README on GitHub](https://github.com/elastic/start-local).
Learn about customizing the setup, logging, and more.

### Next steps

Use our quick start guides to learn the basics of Elasticsearch.
