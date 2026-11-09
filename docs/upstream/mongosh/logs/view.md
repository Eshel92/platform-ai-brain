<!-- Converted from logs/view.txt (reStructuredText). Includes are inlined. -->

# View Shell Logs

The MongoDB Shell stores logs for each session. The default log location
depends on your operating system.

**Step 1: Find your Log ID.**

**Example:**

MongoDB Shell displays the log ID each time you open the shell.

```javascript
$ mongosh

Current Mongosh Log ID: c2961dbd6b73b052671d9df0
Connecting to: mongodb://127.0.0.1:27017
Using MongoDB: 4.2.8
Using Mongosh: 2.14.1
```

**Step 2: View the log for the session.**

**macOS and Linux:**

MongoDB Shell saves the log for each session to your user's
`.mongodb/mongosh` directory:

```sh
~/.mongodb/mongosh/<LogID>_log
```

Run the following command to view the log for a session:

```sh
cat ~/.mongodb/mongosh/<LogID>_log
```

Run the following command to tail the log for a session:

```sh
tail -f ~/.mongodb/mongosh/<LogID>_log
```

**Windows:**

MongoDB Shell saves the log for each session to your user's
`C:\Users\<username>\AppData\Local\` directory:

```sh
%UserProfile%/AppData/Local/mongodb/mongosh/<LogID>_log
```

Run the following PowerShell command to view the log for a session:

```sh
Get-Content %UserProfile%/AppData/Local/mongodb/mongosh/<LogID>_log
```

Run the following PowerShell command to tail the log for a
session:

```sh
Get-Content %UserProfile%/AppData/Local/mongodb/mongosh/<LogID>_log
```

**Tip:**

To change where MongoDB Shell writes logs, see
mongosh-log-location.

Starting in MongoDB Shell 2.4.0, you can use the `log.getPath()`
command to view the current log file location. For example:

```javascript
log.getPath()
```

Example output:

```javascript
/Users/jane.doe/.mongodb/mongosh/c2961dbd6b73b052671d9df0_log
```

The hexadecimal value in the path is the MongoDB Shell log identifier for
the current session.
