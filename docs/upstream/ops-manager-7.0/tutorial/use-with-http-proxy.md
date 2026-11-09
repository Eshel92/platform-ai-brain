<!-- Converted from tutorial/use-with-http-proxy.txt (reStructuredText). Includes are inlined. -->

# Configure Ops Manager to Use an HTTP Proxy for Outgoing Traffic

In restricted network environments, you can configure Ops Manager to use a
proxy to make outbound network requests. 

You can use an HTTP proxy to:

- fetch MongoDB server and Agent binaries and the Ops Manager
  `version manifest` from MongoDB
- contact any third-party services you have integrated with Ops Manager.

## Prerequsites

### Add Allow List of Sites for Version Manifest Source

Ops Manager, the `Backup Daemon`, and MongoDB Agents need direct
outbound access to certain MongoDB, Inc.-hosted URL (Uniform Resource Locator)\s over HTTPS (Hypertext Transfer Protocol Secure) to
download the MongoDB Agent and MongoDB versions.

If you want Ops Manager, the Backup Daemon, and the MongoDB Agents to
use a proxy to limit internet access, you can configure your
firewall to allow access to MongoDB URL (Uniform Resource Locator)\s.

The URL (Uniform Resource Locator)\s you add to the firewall's allow list depend upon what you
have set as your `Installer Download Source`. This setting has two
subsettings: Ops Manager gets installers from: and
Agents get the installers from:. The Agents' installer
source is also the Backup Daemon's source.

* - Ops Manager Source
  - Agent/Daemon Source
  - Domains to Allow

* - MongoDB
  - MongoDB
  -
    - downloads.mongodb.com, downloads.mongodb.org for MongoDB Enterprise Builds
    - opsmanager.mongodb.com for `version manifest`
    - fastdl.mongodb.org for MongoDB Community Builds

* - MongoDB
  - Ops Manager
  -
    - downloads.mongodb.com, downloads.mongodb.org for MongoDB Enterprise Builds
    - opsmanager.mongodb.com for `version manifest`
    - fastdl.mongodb.org for MongoDB Community Builds
    - `URL to Access Ops Manager` for Agents to download MongoDB installers from Ops Manager

* - Ops Manager
  - Ops Manager
  - `URL to Access Ops Manager` for Agents to download MongoDB installers from Ops Manager

### Exclude Internal Hosts from HTTP Proxy

If you configure an HTTP proxy, you can use the
following procedure and the `Non Proxy Hosts`
property to allow the Ops Manager Application Server to
bypass the proxy when accessing specific hosts. The
hosts that you exclude are typically internal.

**See also:**

To learn more about maintaining MongoDB versions in Ops Manager with
limited internet access, see
/tutorial/configure-local-mode.

## Procedure

**Step 1: Configure the proxy settings.**

a. Click the Admin link at the top left.
#. Click Ops Manager Config.
#. Click Miscellaneous.
#. Set the options for the proxy under the
   HTTP/HTTPS Proxy section:

   | Field | Action |
   |---|---|
   | `Proxy Host` | Specify the hostname of the proxy server. |
   | `Proxy Port` | Specify the port of the proxy server. |
   | `Non Proxy Hosts` | Specify a pipe-separated (`\|`) list of internal hosts to bypass the outgoing proxy you configured. |
   | `Proxy Username` | If the proxy server requires authentication, specify the username with which to authenticate. |
   | `Proxy Password` | If the proxy server requires authentication, specify the password with which to authenticate. |

**Important:**

Ops Manager doesn't support NTLM (Windows NT LAN Manager)
protocol authentication for proxies.

**Step 2: Restart Ops Manager.**

Use the command appropriate to your platform.

* - Platform

  - Restart Service Command

* - RHEL, CentOS, Amazon Linux and Ubuntu

  -

    ```sh
    sudo service mongodb-mms restart
    ```

* - Other Linux distributions

  -

    ```sh
    <install_dir>/bin/mongodb-mms restart
    ```
