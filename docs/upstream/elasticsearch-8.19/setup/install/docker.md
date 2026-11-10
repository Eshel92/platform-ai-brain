<!-- Converted from setup/install/docker.asciidoc (AsciiDoc). Includes are inlined. -->

### Install Elasticsearch with Docker

Docker images for Elasticsearch are available from the Elastic Docker registry. A list of
all published Docker images and tags is available at
[www.docker.elastic.co](https://www.docker.elastic.co). The source code is in
[GitHub](https://github.com/elastic/elasticsearch/blob/{branch}/distribution/docker).

This package contains both free and subscription features.
Start a 30-day trial to try out all of the features.

**Tip:**
If you just want to test Elasticsearch in local development, refer to run-elasticsearch-locally.
Please note that this setup is not suitable for production environments.

#### Run Elasticsearch in Docker

Use Docker commands to start a single-node Elasticsearch cluster for development or
testing. You can then run additional Docker commands to add nodes to the test
cluster or run Kibana.

**Tip:** This setup doesn't run multiple Elasticsearch nodes or Kibana by default. To create a
multi-node cluster with Kibana, use Docker Compose instead. See
docker-compose-file.

##### Hardened Docker images

You can also use the hardened [Wolfi](https://wolfi.dev/) image for additional security.
Using Wolfi images requires Docker version 20.10.10 or higher.

To use the Wolfi image, append `-wolfi` to the image tag in the Docker command.

For example:

```sh
docker pull {docker-wolfi-image}
```

##### Start a single-node cluster

. Install Docker. Visit [Get Docker](https://docs.docker.com/get-docker/) to
install Docker for your environment.
If using Docker Desktop, make sure to allocate at least 4GB of memory. You can
adjust memory usage in Docker Desktop by going to **Settings > Resources**.

. Create a new docker network.
```sh
docker network create elastic
```
. Pull the Elasticsearch Docker image.
**Warning:** Version {version} has not yet been released.
No Docker image is currently available for Elasticsearch {version}.

```sh
docker pull {docker-image}
```

. Optional: Install
[Cosign](https://docs.sigstore.dev/cosign/system_config/installation/) for your
environment. Then use Cosign to verify the Elasticsearch image's signature.
```sh
wget https://artifacts.elastic.co/cosign.pub
cosign verify --key cosign.pub {docker-image}
```
The `cosign` command prints the check results and the signature payload in JSON format:
```sh
Verification for {docker-image} --
The following checks were performed on each of these signatures:
  - The cosign claims were validated
  - Existence of the claims in the transparency log was verified offline
  - The signatures were verified against the specified public key
```

. Start an Elasticsearch container.
```sh
docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB {docker-image}
```
**Tip:** Use the `-m` flag to set a memory limit for the container. This removes the
need to manually set the JVM size.

Machine learning features such as semantic search with ELSER
require a larger container with more than 1GB of memory.
If you intend to use the machine learning capabilities, then start the container with this command:
```sh
docker run --name es01 --net elastic -p 9200:9200 -it -m 6GB -e "xpack.ml.use_auto_machine_memory_percent=true" {docker-image}
```
The command prints the `elastic` user password and an enrollment token for Kibana.

. Copy the generated `elastic` password and enrollment token. These credentials
are only shown when you start Elasticsearch for the first time. You can regenerate the
credentials using the following commands.
```sh
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
```
We recommend storing the `elastic` password as an environment variable in your shell. Example:
```sh
export ELASTIC_PASSWORD="your_password"
```

. Copy the `http_ca.crt` SSL certificate from the container to your local machine.
```sh
docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
```

. Make a REST API call to Elasticsearch to ensure the Elasticsearch container is running.
```sh
curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200
```

##### Add more nodes

. Use an existing node to generate a enrollment token for the new node.
```sh
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node
```
The enrollment token is valid for 30 minutes.

. Start a new Elasticsearch container. Include the enrollment token as an environment variable.
```sh
docker run -e ENROLLMENT_TOKEN="<token>" --name es02 --net elastic -it -m 1GB {docker-image}
```

. Call the cat nodes API to verify the node was added to the cluster.
```sh
curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200/_cat/nodes
```

##### Run Kibana

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

##### Remove containers

To remove the containers and their network, run:

```sh
# Remove the Elastic network
docker network rm elastic

# Remove {es} containers
docker rm es01
docker rm es02

# Remove the {kib} container
docker rm kib01
```

##### Next steps

You now have a test Elasticsearch environment set up. Before you start
serious development or go into production with Elasticsearch, review the
requirements and recommendations to apply when running Elasticsearch in Docker in production.

#### Start a multi-node cluster with Docker Compose

Use Docker Compose to start a three-node Elasticsearch cluster with Kibana. Docker Compose
lets you start multiple containers with a single command.

##### Configure and start the cluster

. Install Docker Compose. Visit the
[Docker Compose docs](https://docs.docker.com/compose/install/) to install Docker
Compose for your environment.
If you're using Docker Desktop, Docker Compose is installed automatically. Make
sure to allocate at least 4GB of memory to Docker Desktop. You can adjust memory
usage in Docker Desktop by going to **Settings > Resources**.

. Create or navigate to an empty directory for the project.

. Download and save the following files in the project directory:
- [`.env`](https://github.com/elastic/elasticsearch/blob/{branch}/docs/reference/setup/install/docker/.env)
- [`docker-compose.yml`](https://github.com/elastic/elasticsearch/blob/{branch}/docs/reference/setup/install/docker/docker-compose.yml)

. In the `.env` file, specify a password for the `ELASTIC_PASSWORD` and
`KIBANA_PASSWORD` variables.
The passwords must be alphanumeric and can't contain special characters, such as
`!` or `@`. The bash script included in the `docker-compose.yml` file only
works with alphanumeric characters. Example:
```txt
# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=changeme

# Password for the 'kibana_system' user (at least 6 characters)
KIBANA_PASSWORD=changeme
...
```

. In the `.env` file, set `STACK_VERSION` to the current Elastic Stack version.
```txt
...
# Version of Elastic products
STACK_VERSION={version}
...
```

. By default, the Docker Compose configuration exposes port `9200` on all network interfaces.
To avoid exposing port `9200` to external hosts, set `ES_PORT` to `127.0.0.1:9200`
in the `.env` file. This ensures Elasticsearch is only accessible from the host
machine.
```txt
...
# Port to expose Elasticsearch HTTP API to the host
#ES_PORT=9200
ES_PORT=127.0.0.1:9200
...
```

. To start the cluster, run the following command from the project directory.
```sh
docker-compose up -d
```

. After the cluster has started, open http://localhost:5601 in a web browser to
access Kibana.

. Log in to Kibana as the `elastic` user using the `ELASTIC_PASSWORD` you set
earlier.

##### Stop and remove the cluster

To stop the cluster, run `docker-compose down`. The data in the Docker volumes
is preserved and loaded when you restart the cluster with `docker-compose up`.

```sh
docker-compose down
```

To delete the network, containers, and volumes when you stop the cluster,
specify the `-v` option:

```sh
docker-compose down -v
```

##### Next steps

You now have a test Elasticsearch environment set up. Before you start
serious development or go into production with Elasticsearch, review the
requirements and recommendations to apply when running Elasticsearch in Docker in production.

#### Using the Docker images in production

The following requirements and recommendations apply when running Elasticsearch in Docker in production.

##### Set `vm.max_map_count`

The `vm.max_map_count` kernel setting must be set to `1048576`.

How you set `vm.max_map_count` depends on your platform.

###### Linux

To view the current value for the `vm.max_map_count` setting, run:

```sh
grep vm.max_map_count /etc/sysctl.conf
vm.max_map_count=1048576
```

To apply the setting on a live system, run:

```sh
sysctl -w vm.max_map_count=1048576
```

To permanently change the value for the `vm.max_map_count` setting, update the
value in `/etc/sysctl.conf`.

###### macOS with [Docker for Mac](https://docs.docker.com/docker-for-mac)

The `vm.max_map_count` setting must be set within the xhyve virtual machine:

. From the command line, run:
```sh
screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty
```

. Press enter and use `sysctl` to configure `vm.max_map_count`:
```sh
sysctl -w vm.max_map_count=1048576
```

. To exit the `screen` session, type `Ctrl a d`.

###### Windows and macOS with [Docker Desktop](https://www.docker.com/products/docker-desktop)

The `vm.max_map_count` setting must be set via docker-machine:

```sh
docker-machine ssh
sudo sysctl -w vm.max_map_count=1048576
```

###### Windows with [Docker Desktop WSL 2 backend](https://docs.docker.com/docker-for-windows/wsl)

The `vm.max_map_count` setting must be set in the "docker-desktop" WSL instance before the
Elasticsearch container will properly start. There are several ways to do this, depending
on your version of Windows and your version of WSL.

If you are on Windows 10 before version 22H2, or if you are on Windows 10 version 22H2 using the
built-in version of WSL, you must either manually set it every time you restart Docker before starting
your Elasticsearch container, or (if you do not wish to do so on every restart) you must globally set
every WSL2 instance to have the `vm.max_map_count` changed. This is because these versions of WSL
do not properly process the /etc/sysctl.conf file.

To manually set it every time you reboot, you must run the following commands in a command prompt
or PowerShell window every time you restart Docker:

```sh
wsl -d docker-desktop -u root
sysctl -w vm.max_map_count=1048576
```

If you are on these versions of WSL and you do not want to have to run those commands every
time you restart Docker, you can globally change every WSL distribution with this setting
by modifying your %USERPROFILE%\.wslconfig as follows:

```text
[wsl2]
kernelCommandLine = "sysctl.vm.max_map_count=1048576"
```

This will cause all WSL2 VMs to have that setting assigned when they start.

If you are on Windows 11, or Windows 10 version 22H2 and have installed the Microsoft Store
version of WSL, you can modify the /etc/sysctl.conf within the "docker-desktop" WSL
distribution, perhaps with commands like this:

```sh
wsl -d docker-desktop -u root
vi /etc/sysctl.conf
```

and appending a line which reads:
```text
vm.max_map_count = 1048576
```

##### Configuration files must be readable by the `elasticsearch` user

By default, Elasticsearch runs inside the container as user `elasticsearch` using
uid:gid `1000:0`.

**Important:** One exception is [Openshift](https://docs.openshift.com/container-platform/3.6/creating_images/guidelines.html#openshift-specific-guidelines),
which runs containers using an arbitrarily assigned user ID.
Openshift presents persistent volumes with the gid set to `0`, which works without any adjustments.

If you are bind-mounting a local directory or file, it must be readable by the `elasticsearch` user.
In addition, this user must have write access to the config, data and log dirs
(Elasticsearch needs write access to the `config` directory so that it can generate a keystore).
A good strategy is to grant group access to gid `0` for the local directory.

For example, to prepare a local directory for storing data through a bind-mount:

```sh
mkdir esdatadir
chmod g+rwx esdatadir
chgrp 0 esdatadir
```

You can also run an Elasticsearch container using both a custom UID and GID. You
must ensure that file permissions will not prevent Elasticsearch from executing. You
can use one of two options:

* Bind-mount the `config`, `data` and `logs`
  directories. If you intend to install plugins and prefer not to
  create a custom Docker image, you must also
  bind-mount the `plugins` directory.
* Pass the `--group-add 0` command line option to `docker run`. This
  ensures that the user under which Elasticsearch is running is also a member of the
  `root` (GID 0) group inside the container.

##### Increase ulimits for nofile and nproc

Increased ulimits for nofile and nproc
must be available for the Elasticsearch containers.
Verify the [init system](https://github.com/moby/moby/tree/ea4d1243953e6b652082305a9c3cda8656edab26/contrib/init)
for the Docker daemon sets them to acceptable values.

To check the Docker daemon defaults for ulimits, run:

```sh
docker run --rm {docker-image} /bin/bash -c 'ulimit -Hn && ulimit -Sn && ulimit -Hu && ulimit -Su'
```

If needed, adjust them in the Daemon or override them per container.
For example, when using `docker run`, set:

```sh
--ulimit nofile=65535:65535
```

##### Disable swapping

Swapping needs to be disabled for performance and node stability.
For information about ways to do this, see setup-configuration-memory.

If you opt for the `bootstrap.memory_lock: true` approach,
you also need to define the `memlock: true` ulimit in the
[Docker Daemon](https://docs.docker.com/engine/reference/commandline/dockerd/#default-ulimits),
or explicitly set for the container as shown in the  sample compose file.
When using `docker run`, you can specify:

```sh
-e "bootstrap.memory_lock=true" --ulimit memlock=-1:-1
```

##### Randomize published ports

The image [exposes](https://docs.docker.com/engine/reference/builder/#/expose)
TCP ports 9200 and 9300. For production clusters, randomizing the
published ports with `--publish-all` is recommended,
unless you are pinning one container per host.

##### Manually set the heap size

By default, Elasticsearch automatically sizes JVM heap based on a nodes's
roles and the total memory available to the node's container. We
recommend this default sizing for most production environments. If needed, you
can override default sizing by manually setting JVM heap size.

To manually set the heap size in production, bind mount a <<set-jvm-options,JVM
options>> file under `/usr/share/elasticsearch/config/jvm.options.d` that
includes your desired heap size settings.

For testing, you can also manually set the heap size using the `ES_JAVA_OPTS`
environment variable. For example, to use 1GB, use the following command.

```sh
docker run -e ES_JAVA_OPTS="-Xms1g -Xmx1g" -e ENROLLMENT_TOKEN="<token>" --name es01 -p 9200:9200 --net elastic -it {docker-image}
```

The `ES_JAVA_OPTS` variable overrides all other JVM options.
We do not recommend using `ES_JAVA_OPTS` in production.

##### Pin deployments to a specific image version

Pin your deployments to a specific version of the Elasticsearch Docker image. For
example {docker-image}.

##### Always bind data volumes

You should use a volume bound on `/usr/share/elasticsearch/data` for the following reasons:

. The data of your Elasticsearch node won't be lost if the container is killed

. Elasticsearch is I/O sensitive and the Docker storage driver is not ideal for fast I/O

. It allows the use of advanced
[Docker volume plugins](https://docs.docker.com/engine/extend/plugins/#volume-plugins)

##### Avoid using `loop-lvm` mode

If you are using the devicemapper storage driver, do not use the default `loop-lvm` mode.
Configure docker-engine to use
[direct-lvm](https://docs.docker.com/engine/userguide/storagedriver/device-mapper-driver/#configure-docker-with-devicemapper).

##### Centralize your logs

Consider centralizing your logs by using a different
[logging driver](https://docs.docker.com/engine/admin/logging/overview/). Also
note that the default json-file logging driver is not ideally suited for
production use.

#### Configuring Elasticsearch with Docker

When you run in Docker, the Elasticsearch configuration files are loaded from
`/usr/share/elasticsearch/config/`.

To use custom configuration files, you bind-mount the files
over the configuration files in the image.

You can set individual Elasticsearch configuration parameters using Docker environment variables.
The sample compose file and the
single-node example use this method. You can
use the setting name directly as the environment variable name. If
you cannot do this, for example because your orchestration platform forbids
periods in environment variable names, then you can use an alternative
style by converting the setting name as follows.

. Change the setting name to uppercase
. Prefix it with `ES_SETTING_`
. Escape any underscores (`_`) by duplicating them
. Convert all periods (`.`) to underscores (`_`)

For example, `-e bootstrap.memory_lock=true` becomes
`-e ES_SETTING_BOOTSTRAP_MEMORY__LOCK=true`.

You can use the contents of a file to set the value of the
`ELASTIC_PASSWORD` or `KEYSTORE_PASSWORD` environment variables, by
suffixing the environment variable name with `_FILE`. This is useful for
passing secrets such as passwords to Elasticsearch without specifying them directly.

For example, to set the Elasticsearch bootstrap password from a file, you can bind mount the
file and set the `ELASTIC_PASSWORD_FILE` environment variable to the mount location.
If you mount the password file to `/run/secrets/bootstrapPassword.txt`, specify:

```sh
-e ELASTIC_PASSWORD_FILE=/run/secrets/bootstrapPassword.txt
```

You can override the default command for the image to pass Elasticsearch configuration
parameters as command line options. For example:

```sh
docker run <various parameters> bin/elasticsearch -Ecluster.name=mynewclustername
```

While bind-mounting your configuration files is usually the preferred method in production,
you can also create a custom Docker image
that contains your configuration.

##### Mounting Elasticsearch configuration files

Create custom config files and bind-mount them over the corresponding files in the Docker image.
For example, to bind-mount `custom_elasticsearch.yml` with `docker run`, specify:

```sh
-v full_path_to/custom_elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml
```

If you bind-mount a custom `elasticsearch.yml` file, ensure it includes the
`network.host: 0.0.0.0` setting. This setting ensures the node is reachable for
HTTP and transport traffic, provided its ports are exposed. The Docker image's
built-in `elasticsearch.yml` file includes this setting by default.

**Important:** The container **runs Elasticsearch as user `elasticsearch` using
uid:gid `1000:0`**. Bind mounted host directories and files must be accessible by this user,
and the data and log directories must be writable by this user.

##### Create an encrypted Elasticsearch keystore

By default, Elasticsearch will auto-generate a keystore file for <<secure-settings,secure
settings>>. This file is obfuscated but not encrypted.

To encrypt your secure settings with a password and have them persist outside
the container, use a `docker run` command to manually create the keystore
instead. The command must:

* Bind-mount the `config` directory. The command will create an
  `elasticsearch.keystore` file in this directory. To avoid errors, do
  not directly bind-mount the `elasticsearch.keystore` file.
* Use the `elasticsearch-keystore` tool with the `create -p` option. You'll be
  prompted to enter a password for the keystore.

For example:

```sh
docker run -it --rm \
-v full_path_to/config:/usr/share/elasticsearch/config \
{docker-image} \
bin/elasticsearch-keystore create -p
```

You can also use a `docker run` command to add or update secure settings in the
keystore. You'll be prompted to enter the setting values. If the keystore is
encrypted, you'll also be prompted to enter the keystore password.

```sh
docker run -it --rm \
-v full_path_to/config:/usr/share/elasticsearch/config \
{docker-image} \
bin/elasticsearch-keystore \
add my.secure.setting \
my.other.secure.setting
```

If you've already created the keystore and don't need to update it, you can
bind-mount the `elasticsearch.keystore` file directly. You can use the
`KEYSTORE_PASSWORD` environment variable to provide the keystore password to the
container at startup. For example, a `docker run` command might have the
following options:

```sh
-v full_path_to/config/elasticsearch.keystore:/usr/share/elasticsearch/config/elasticsearch.keystore
-e KEYSTORE_PASSWORD=mypassword
```

##### Using custom Docker images

In some environments, it might make more sense to prepare a custom image that contains
your configuration. A `Dockerfile` to achieve this might be as simple as:

```sh
FROM {docker-image}
COPY --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config/
```

You could then build and run the image with:

```sh
docker build --tag=elasticsearch-custom .
docker run -ti -v /usr/share/elasticsearch/data elasticsearch-custom
```

Some plugins require additional security permissions.
You must explicitly accept them either by:

* Attaching a `tty` when you run the Docker image and allowing the permissions when prompted.
* Inspecting the security permissions and accepting them (if appropriate) by adding the `--batch` flag to the plugin install command.

See {plugins}/_other_command_line_parameters.html[Plugin management]
for more information.

#### Troubleshoot Docker errors for Elasticsearch

Here’s how to resolve common errors when running Elasticsearch with Docker.

##### elasticsearch.keystore is a directory

```txt
Exception in thread "main" org.elasticsearch.bootstrap.BootstrapException: java.io.IOException: Is a directory: SimpleFSIndexInput(path="/usr/share/elasticsearch/config/elasticsearch.keystore") Likely root cause: java.io.IOException: Is a directory
```

A keystore-related `docker run` command attempted
to directly bind-mount an `elasticsearch.keystore` file that doesn't exist. If
you use the `-v` or `--volume` flag to mount a file that doesn't exist, Docker
instead creates a directory with the same name.

To resolve this error:

. Delete the `elasticsearch.keystore` directory in the `config` directory.
. Update the `-v` or `--volume` flag to point to the `config` directory path
  rather than the keystore file's path. For an example, see
  docker-keystore-bind-mount.
. Retry the command.

##### elasticsearch.keystore: Device or resource busy

```txt
Exception in thread "main" java.nio.file.FileSystemException: /usr/share/elasticsearch/config/elasticsearch.keystore.tmp -> /usr/share/elasticsearch/config/elasticsearch.keystore: Device or resource busy
```

A `docker run` command attempted to <<docker-keystore-bind-mount,update the
keystore>> while directly bind-mounting the `elasticsearch.keystore` file. To
update the keystore, the container requires access to other files in the
`config` directory, such as `keystore.tmp`.

To resolve this error:

. Update the `-v` or `--volume` flag to point to the `config` directory
  path rather than the keystore file's path. For an example, see
  docker-keystore-bind-mount.
. Retry the command.
