<!-- Converted from setup/docker.asciidoc (AsciiDoc). Includes are inlined. -->

### Install Kibana with Docker

Docker images for Kibana are available from the Elastic Docker registry. The
base image is [ubuntu:20.04](https://hub.docker.com/_/ubuntu).

A list of all published Docker images and tags is available at
[www.docker.elastic.co](https://www.docker.elastic.co). The source code is in
[GitHub](https://github.com/elastic/dockerfiles/tree/{branch}/kibana).

These images contain both free and subscription features.
Start a 30-day trial to try out all of the features.

### Run Kibana in Docker for development

Use Docker commands to run Kibana on a single-node Elasticsearch cluster for development or
testing.

**Tip:** This setup doesn't run multiple Elasticsearch nodes by default. To create a
multi-node cluster with Kibana, use Docker Compose instead. Refer to
https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docker.html#docker-compose-file[Start a multi-node cluster with Docker
Compose] in the Elasticsearch documentation.

#### Hardened Docker images

You can also use the hardened [Wolfi](https://wolfi.dev/) image for additional security. Using Wolfi images requires Docker version 20.10.10 or higher.

To use the Wolfi image, append `-wolfi` to the image tag in the Docker command.

For example:

```sh
docker pull docker.elastic.co/elasticsearch/elasticsearch-wolfi:{version}
```

#### Start a single node cluster

. Install Docker. Visit [Get Docker](https://docs.docker.com/get-docker/) to
install Docker for your environment.
**Important:** If using Docker Desktop, make sure to allocate at least 4GB of
memory. You can adjust memory usage in Docker Desktop by going to **Settings >
Resources**.

. Create a new Docker network for Elasticsearch and Kibana.
```sh
docker network create elastic
```

. Pull the Elasticsearch Docker image.
**Warning:** Version {version} has not yet been released.
No Docker image is currently available for Elasticsearch {version}.

```sh
docker pull {es-docker-image}
```

. Optional: Install
[Cosign](https://docs.sigstore.dev/system_config/installation/) for your
environment. Then use Cosign to verify the Elasticsearch image's signature.
```sh
wget https://artifacts.elastic.co/cosign.pub
cosign verify --key cosign.pub {es-docker-image}
```
The `cosign` command prints the check results and the signature payload in JSON format:
```sh
Verification for {es-docker-image} --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - Existence of the claims in the transparency log was verified offline
  - The signatures were verified against the specified public key
```

. Start an Elasticsearch container.
```sh
docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB {es-docker-image}
```
**Tip:** Use the `-m` flag to set a memory limit for the container. This removes the
need to [manually set the JVM size](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/docker.html#docker-set-heap-size).
The command prints the `elastic` user password and an enrollment token for Kibana.

. Copy the generated `elastic` password and enrollment token. These credentials
are only shown when you start Elasticsearch for the first time. You can regenerate the
credentials using the following commands.
```sh
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
```

. Pull the Kibana Docker image.
**Warning:** Version {version} has not yet been released.
No Docker image is currently available for Kibana {version}.

```sh
docker pull {kib-docker-image}
```

. Optional: Verify the Kibana image's signature.
```sh
wget https://artifacts.elastic.co/cosign.pub
cosign verify --key cosign.pub {kib-docker-image}
```

. Start a Kibana container.
```sh
docker run --name kib01 --net elastic -p 5601:5601 {kib-docker-image}
```

. When Kibana starts, it outputs a unique generated link to the terminal. To
access Kibana, open this link in a web browser.

. In your browser, enter the enrollment token that was generated when you started Elasticsearch.
To regenerate the token, run:
```sh
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
```

. Log in to Kibana as the `elastic` user with the password that was generated
when you started Elasticsearch.
To regenerate the password, run:
```sh
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
```

#### Remove Docker containers

To remove the containers and their network, run:

```sh
# Remove the Elastic network
docker network rm elastic

# Remove the {es} container
docker rm es01

# Remove the {kib} container
docker rm kib01
```

### Configure Kibana on Docker

The Docker images provide several methods for configuring Kibana. The
conventional approach is to provide a `kibana.yml` file as described in
[Configuring Kibana](https://www.elastic.co/guide/en/kibana/8.19/settings.html), but it's also possible to use
environment variables to define settings.

#### Bind-mounted configuration

One way to configure Kibana on Docker is to provide `kibana.yml` via bind-mounting.
With `docker-compose`, the bind-mount can be specified like this:

```
version: '2'
services:
  kibana:
    image: {kib-docker-image}
    volumes:
      - ./kibana.yml:/usr/share/kibana/config/kibana.yml
```

#### Persist the Kibana keystore

By default, Kibana auto-generates a keystore file for secure settings at startup. To persist your [secure settings](https://www.elastic.co/guide/en/kibana/8.19/secure-settings.html), use the `kibana-keystore` utility to bind-mount the parent directory of the keystore to the container. For example:

```
docker run -it --rm -v full_path_to/config:/usr/share/kibana/config -v full_path_to/data:/usr/share/kibana/data {kib-docker-image} bin/kibana-keystore create
docker run -it --rm -v full_path_to/config:/usr/share/kibana/config -v full_path_to/data:/usr/share/kibana/data {kib-docker-image} bin/kibana-keystore add test_keystore_setting
```

#### Environment variable configuration

Under Docker, Kibana can be configured via environment variables. When
the container starts, a helper process checks the environment for variables that
can be mapped to Kibana command-line arguments.

For compatibility with container orchestration systems, these
environment variables are written in all capitals, with underscores as
word separators. The helper translates these names to valid
Kibana setting names.

**Warning:** All information that you include in environment variables is visible through the `ps` command, including sensitive information.

Some example translations are shown here:

**Example Docker Environment Variables**
**Environment Variable**:: **Kibana Setting**
`SERVER_NAME`:: `server.name`
`SERVER_BASEPATH`:: `server.basePath`
`ELASTICSEARCH_HOSTS`:: `elasticsearch.hosts`

In general, any setting listed in settings can be configured with this technique.

Supplying array options can be tricky. The following example shows the syntax for providing an array to `ELASTICSEARCH_HOSTS`.

These variables can be set with docker-compose like this:

```
version: '2'
services:
  kibana:
    image: {kib-docker-image}
    environment:
      SERVER_NAME: kibana.example.org
      ELASTICSEARCH_HOSTS: '["<HOST_1>:9200","<HOST_2>:9200","<HOST_3>:9200"]'
```

Since environment variables are translated to CLI arguments, they take
precedence over settings configured in `kibana.yml`.

#### Docker defaults

The following settings have different default values when using the Docker
images:

`server.host`:: `"0.0.0.0"`
`server.shutdownTimeout`:: `"5s"`
`elasticsearch.hosts`:: `http://elasticsearch:9200`
`monitoring.ui.container.elasticsearch.enabled`:: `true`

These settings are defined in the default `kibana.yml`. They can be overridden
with a custom `kibana.yml` or via
environment variables.

**Important:** If replacing `kibana.yml` with a custom version, be sure to copy the
defaults to the custom file if you want to retain them. If not, they will
be "masked" by the new file.
