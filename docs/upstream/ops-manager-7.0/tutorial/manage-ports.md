<!-- Converted from tutorial/manage-ports.txt (reStructuredText). Includes are inlined. -->

# Manage Ops Manager Hostname and Ports

Ops Manager must provide a consistent hostname and consistent ports.
Follow these procedures to:

- Override the default hostname for Ops Manager
- Change the default ports for Ops Manager
- Enable the health-check endpoints

**Note:**

All of these procedures are *optional*. You shouldn't need to change
these settings unless your Ops Manager Backup Daemons or Ops Manager Application
doesn't appear with the correct hostname, or you need to change
ports to meet local security concerns.

## Override the Ops Manager Hostname

Ops Manager tries to detect its host's FQDN (fully qualified domain name). There might be times when
the Ops Manager hosts select the wrong hostname. If you need to override
the hostname that Ops Manager selected, you can set Ops Manager to use a
hostname that you specify.

**Important:**

If Ops Manager works as expected from the URL (Uniform Resource Locator) you wanted, you can
skip this procedure.

**linux:**

To set the hostname on Linux hosts:

**Step 1: Log in to the host running Ops Manager.**

**Step 2: Open `mms.conf` for editing.**

a. Navigate to the `<install_dir>/conf/` directory.

b. Open the `mms.conf` file as `root` in your preferred text
   editor.

   **Example:**

   ```sh
   sudo -H vi /opt/mongodb/mms/conf/mms.conf
   ```

**Step 3: Set the hostname values to the FQDN (fully qualified domain name) for the Ops Manager Application and Backup Daemon.**

Add two options with the `mms.system.hostname` value:

- `JAVA_MMS_UI_OPTS` for the Ops Manager Application
- `JAVA_DAEMON_OPTS` for the Backup Daemon

**Example:**

These Java options should look similar to this example:

```ini
JAVA_MMS_UI_OPTS="${JAVA_MMS_UI_OPTS} -Dmms.system.hostname=opsmanager.example.com"
JAVA_DAEMON_OPTS="${JAVA_DAEMON_OPTS} -Dmms.system.hostname=opsmanager-bkp.example.com"
```

You can use environment variables on Linux systems to set this
value:

```ini
JAVA_MMS_UI_OPTS="${JAVA_MMS_UI_OPTS} -Dmms.system.hostname=$(hostname -f)"
JAVA_DAEMON_OPTS="${JAVA_DAEMON_OPTS} -Dmms.system.hostname=$(hostname -f)"
```

**Step 4: Update the Ops Manager URL (Uniform Resource Locator).**

a. In the Ops Manager Application, click the Admin link in the
   upper right corner of the page.

b. Click the General tab and then click
   Ops Manager Config.

c. Update the URL to Access Ops Manager field to use the
   value you specified in the Java Options registry value.

   For example:

   ```sh
   https://opsmanager.example.com:11800
   ```

d. Click Save.

**Step 5: Restart Ops Manager.**

**debian:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**rhel:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**linux:**

Invoke the following command:

```sh
sudo /etc/init.d/mongodb-mms restart
```

You can access the Ops Manager Application from the new URL (Uniform Resource Locator) after
Ops Manager restarts.

**debian:**

To set the hostname on Ubuntu or Debian hosts:

**Step 1: Log in to the host running Ops Manager.**

**Step 2: Open `mms.conf` for editing.**

a. Navigate to the `<install_dir>/conf/` directory.

b. Open the `mms.conf` file as `root` in your preferred text
   editor.

   **Example:**

   ```sh
   sudo -H vi /opt/mongodb/mms/conf/mms.conf
   ```

**Step 3: Set the hostname values to the FQDN (fully qualified domain name) for the Ops Manager Application and Backup Daemon.**

Add two options with the `mms.system.hostname` value:

- `JAVA_MMS_UI_OPTS` for the Ops Manager Application
- `JAVA_DAEMON_OPTS` for the Backup Daemon

**Example:**

These Java options should look similar to this example:

```ini
JAVA_MMS_UI_OPTS="${JAVA_MMS_UI_OPTS} -Dmms.system.hostname=opsmanager.example.com"
JAVA_DAEMON_OPTS="${JAVA_DAEMON_OPTS} -Dmms.system.hostname=opsmanager-bkp.example.com"
```

You can use environment variables on Linux systems to set this
value:

```ini
JAVA_MMS_UI_OPTS="${JAVA_MMS_UI_OPTS} -Dmms.system.hostname=$(hostname -f)"
JAVA_DAEMON_OPTS="${JAVA_DAEMON_OPTS} -Dmms.system.hostname=$(hostname -f)"
```

**Step 4: Update the Ops Manager URL (Uniform Resource Locator).**

a. In the Ops Manager Application, click the Admin link in the
   upper right corner of the page.

b. Click the General tab and then click
   Ops Manager Config.

c. Update the URL to Access Ops Manager field to use the
   value you specified in the Java Options registry value.

   For example:

   ```sh
   https://opsmanager.example.com:11800
   ```

d. Click Save.

**Step 5: Restart Ops Manager.**

**debian:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**rhel:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**linux:**

Invoke the following command:

```sh
sudo /etc/init.d/mongodb-mms restart
```

You can access the Ops Manager Application from the new URL (Uniform Resource Locator) after
Ops Manager restarts.

**rhel:**

To set the hostname on Red Hat or CentOS  hosts:

**Step 1: Log in to the host running Ops Manager.**

**Step 2: Open `mms.conf` for editing.**

a. Navigate to the `<install_dir>/conf/` directory.

b. Open the `mms.conf` file as `root` in your preferred text
   editor.

   **Example:**

   ```sh
   sudo -H vi /opt/mongodb/mms/conf/mms.conf
   ```

**Step 3: Set the hostname values to the FQDN (fully qualified domain name) for the Ops Manager Application and Backup Daemon.**

Add two options with the `mms.system.hostname` value:

- `JAVA_MMS_UI_OPTS` for the Ops Manager Application
- `JAVA_DAEMON_OPTS` for the Backup Daemon

**Example:**

These Java options should look similar to this example:

```ini
JAVA_MMS_UI_OPTS="${JAVA_MMS_UI_OPTS} -Dmms.system.hostname=opsmanager.example.com"
JAVA_DAEMON_OPTS="${JAVA_DAEMON_OPTS} -Dmms.system.hostname=opsmanager-bkp.example.com"
```

You can use environment variables on Linux systems to set this
value:

```ini
JAVA_MMS_UI_OPTS="${JAVA_MMS_UI_OPTS} -Dmms.system.hostname=$(hostname -f)"
JAVA_DAEMON_OPTS="${JAVA_DAEMON_OPTS} -Dmms.system.hostname=$(hostname -f)"
```

**Step 4: Update the Ops Manager URL (Uniform Resource Locator).**

a. In the Ops Manager Application, click the Admin link in the
   upper right corner of the page.

b. Click the General tab and then click
   Ops Manager Config.

c. Update the URL to Access Ops Manager field to use the
   value you specified in the Java Options registry value.

   For example:

   ```sh
   https://opsmanager.example.com:11800
   ```

d. Click Save.

**Step 5: Restart Ops Manager.**

**debian:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**rhel:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**linux:**

Invoke the following command:

```sh
sudo /etc/init.d/mongodb-mms restart
```

You can access the Ops Manager Application from the new URL (Uniform Resource Locator) after
Ops Manager restarts.

## Change the Default Port

Ops Manager uses the ports and health-check endpoints described in
/reference/firewall-configuration. The endpoints default to
`disabled`.

**linux:**

To change the ports on Linux hosts:

**Step 1: Log in to the host running Ops Manager.**

**Step 2: Open `mms.conf` for editing.**

a. Navigate to the `<install_dir>/conf/` directory.

b. Open the `mms.conf` file as `root` in your preferred text
   editor.

   **Example:**

   ```sh
   sudo -H vi /opt/mongodb/mms/conf/mms.conf
   ```

**Step 3: Set the `BASE_PORT` value to the desired Ops Manager port.**

When changing the port, ensure that the chosen port is available for
use.

By default, Ops Manager uses port `8080`. Change the `BASE_PORT`
value to the desired port number.

For example:

```sh
BASE_PORT=11800
```

If you want to change the port for Ops Manager connections over TLS (Transport Layer Security),
update `BASE_SSL_PORT`.

**Step 4: Update the Ops Manager URL (Uniform Resource Locator).**

a. In the Ops Manager Application, click the Admin link in the
   upper right corner of the page.

b. Click the General tab and then click
   Ops Manager Config.

c. Update the URL to Access Ops Manager field to use the
   value you specified in the Java Options registry value.

   For example:

   ```sh
   https://opsmanager.example.com:11800
   ```

d. Click Save.

**Step 5: Restart Ops Manager.**

**debian:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**rhel:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**linux:**

Invoke the following command:

```sh
sudo /etc/init.d/mongodb-mms restart
```

You can access the Ops Manager Application from the new URL (Uniform Resource Locator) after
Ops Manager restarts.

**debian:**

To change the ports on Ubuntu or Debian hosts:

**Step 1: Log in to the host running Ops Manager.**

**Step 2: Open `mms.conf` for editing.**

a. Navigate to the `<install_dir>/conf/` directory.

b. Open the `mms.conf` file as `root` in your preferred text
   editor.

   **Example:**

   ```sh
   sudo -H vi /opt/mongodb/mms/conf/mms.conf
   ```

**Step 3: Set the `BASE_PORT` value to the desired Ops Manager port.**

When changing the port, ensure that the chosen port is available for
use.

By default, Ops Manager uses port `8080`. Change the `BASE_PORT`
value to the desired port number.

For example:

```sh
BASE_PORT=11800
```

If you want to change the port for Ops Manager connections over TLS (Transport Layer Security),
update `BASE_SSL_PORT`.

**Step 4: Update the Ops Manager URL (Uniform Resource Locator).**

a. In the Ops Manager Application, click the Admin link in the
   upper right corner of the page.

b. Click the General tab and then click
   Ops Manager Config.

c. Update the URL to Access Ops Manager field to use the
   value you specified in the Java Options registry value.

   For example:

   ```sh
   https://opsmanager.example.com:11800
   ```

d. Click Save.

**Step 5: Restart Ops Manager.**

**debian:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**rhel:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**linux:**

Invoke the following command:

```sh
sudo /etc/init.d/mongodb-mms restart
```

You can access the Ops Manager Application from the new URL (Uniform Resource Locator) after
Ops Manager restarts.

**rhel:**

To change the ports on Red Hat or CentOS hosts:

**Step 1: Log in to the host running Ops Manager.**

**Step 2: Open `mms.conf` for editing.**

a. Navigate to the `<install_dir>/conf/` directory.

b. Open the `mms.conf` file as `root` in your preferred text
   editor.

   **Example:**

   ```sh
   sudo -H vi /opt/mongodb/mms/conf/mms.conf
   ```

**Step 3: Set the `BASE_PORT` value to the desired Ops Manager port.**

When changing the port, ensure that the chosen port is available for
use.

By default, Ops Manager uses port `8080`. Change the `BASE_PORT`
value to the desired port number.

For example:

```sh
BASE_PORT=11800
```

If you want to change the port for Ops Manager connections over TLS (Transport Layer Security),
update `BASE_SSL_PORT`.

**Step 4: Update the Ops Manager URL (Uniform Resource Locator).**

a. In the Ops Manager Application, click the Admin link in the
   upper right corner of the page.

b. Click the General tab and then click
   Ops Manager Config.

c. Update the URL to Access Ops Manager field to use the
   value you specified in the Java Options registry value.

   For example:

   ```sh
   https://opsmanager.example.com:11800
   ```

d. Click Save.

**Step 5: Restart Ops Manager.**

**debian:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**rhel:**

Invoke the following command:

```sh
sudo service mongodb-mms restart
```

**linux:**

Invoke the following command:

```sh
sudo /etc/init.d/mongodb-mms restart
```

You can access the Ops Manager Application from the new URL (Uniform Resource Locator) after
Ops Manager restarts.

## Enable the Health Check Endpoint

Ops Manager provides an HTTP (Hypertext Transfer Protocol) health-check endpoint. This endpoint is
accessed on port `8090` and is disabled by default. Before you enable
the endpoint, make sure that another application or process isn't using
port `8090` .

To enable the endpoint:

**Step 1: Open `mms.conf` for editing.**

Open the `mms.conf` file with root access. `mms.conf` is located in the
`<install_dir>/conf/` directory.

**Step 2: Uncomment `DEBUG.PORT`.**

To enable the endpoint, remove the `#` symbol so that the line
reads:

```ini
DEBUG.PORT=8090
```

**Important:**

This port is only accessible from `localhost` (or
`127.0.0.1`). The port number *can* be changed from `8090` to
another value.

**Step 3: Save the changes.**

**Step 4: Restart Ops Manager.**
