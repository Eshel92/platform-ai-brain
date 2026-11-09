<!-- Converted from tutorial/start-and-stop-application.txt (reStructuredText). Includes are inlined. -->

# Start and Stop Ops Manager Application

## Start the Ops Manager Server

**Note:**

If you installed from a `tar.gz` or `.zip` archive, you must create
a symlink located at the path `/etc/init.d/mongodb-mms` that points
to the `<install_dir>/bin/mongodb-mms`.

After configuring your Ops Manager deployment, you can start the Ops Manager Application
with this command:

```sh
sudo /etc/init.d/mongodb-mms start
```

In some situations, starting MongoDB *may* take several minutes to pre-allocate
the journal files. This is normal behavior.

To open Ops Manager, enter the URL specified in the `URL to Access Ops
Manager` setting in the Ops Manager UI. If you are opening Ops Manager for the first
time, enter the following URL, where `<host>` is the fully qualified domain
name of the Ops Manager server. Ops Manager prompts you to register a new user when
you login for the first time.

```none
http://<host>:8080
```

## Stop the Ops Manager Application

Enter the following command:

```sh
sudo /etc/init.d/mongodb-mms stop
```

## Startup Log File Output

The Ops Manager Application logs its startup output
to a `logs` directory of each Ops Manager host.

The log file for each Ops Manager instance is named `mms#-startup.log`, 
where `#` is a zero-based index of the Ops Manager instance. The log 
file for the `Backup Daemon` is named `daemon-startup.log`.

If the Ops Manager Application starts successfully, the `init.d` daemon 
creates log entries in this log file that resemble the following:

```none
[main] INFO  ServerMain:202 - Starting mms...
[main] WARN  AbstractConnector:294 - Acceptors should be <=2*availableProcessors: SelectChannelConnector@0.0.0.0:0
[null] LoginService=HashLoginService identityService=org.eclipse.jetty.security.DefaultIdentityService@1eb3319f
[main] INFO  AppConfig:46 - Starting app for env: hosted
[main] INFO  MmsAppConfig:67 - Not loading backup components
[main] INFO  GraphiteSvcImpl:67 - Graphite service not configured, events will be ignored.
[main] INFO  TwilioSvcImpl:48 - Twilio service not configured, SMS events will be ignored.
[main] INFO  ServerMain:266 - Started in: 24979 (ms)
```

**Note:**

The startup log is rotated and retains the full
history of all startup events. You can
change its retention policy.

## Optional: Run as Different User

#. Edit `<install_dir>/conf/mms.conf`:

   ```ini
   MMS_USER=foo_user
   ```

#. Change Ownership of `<install_dir>` for new user:

   ```sh
   sudo chown -R foo_user:foo_group <install_dir>
   ```

#. Change Ownership of head directory for new user:

   ```sh
   sudo chown foo_user:foo_user -R <head_directory_filepath>
   ```

#. Restart the Ops Manager Application:

   ```sh
   sudo <install_dir>/bin/mongodb-mms restart
   ```

## Optional: Ops Manager Application Server Port Number

#. Edit `<install_dir>/conf/conf-mms.properties`:

   ```ini
   mms.centralUrl=http://mms.example.com:<newport>
   ```

#. Edit `<install_dir>/conf/mms.conf`

   ```ini
   BASE_PORT=<newport>
   ```

#. Restart the Ops Manager Application:

   ```sh
   sudo <install_dir>/bin/mongodb-mms restart
   ```
