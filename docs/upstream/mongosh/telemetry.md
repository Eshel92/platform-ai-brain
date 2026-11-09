<!-- Converted from telemetry.txt (reStructuredText). Includes are inlined. -->

# Configure Telemetry Options

`mongosh` collects pseudo-anonymous aggregated usage data to improve
MongoDB products. `mongosh` collects this data by default. `mongosh`
collects data during interactive and agentic sessions only, not
scripted sessions. You can disable this data collection at any time.

## Data Tracked by `mongosh`

`mongosh` tracks the following data:

- The type of MongoDB `mongosh` is connected to. For example,
  Enterprise Edition or Community Edition.

- The methods run in `mongosh`. `mongosh` only tracks the names of
  the methods, and does not track any arguments supplied to methods.

- Whether you run scripts with `mongosh`.

- Errors.

- Your IP address. When `mongosh` sends telemetry data, your IP
  address is visible to the endpoint, but `mongosh` does not store it
  with your telemetry data.

`mongosh` *does not* track:

- Usernames or credentials.

- Queries run in `mongosh`.

- Any data stored in your MongoDB deployment.

## Toggle Telemetry Collection

Use the following methods in `mongosh` to toggle telemetry data
collection.

**`disableTelemetry()`**

Disable telemetry for `mongosh`.

```javascript
disableTelemetry()
```

The command response confirms that telemetry is disabled:

```javascript
Telemetry is now disabled.
```

**Tip:**

You can also disable telemetry at startup by using the
`--eval` startup option.

The following command starts `mongosh` with telemetry disabled:

```javascript
mongosh --nodb --eval "disableTelemetry()"
```

**`enableTelemetry()`**

Enable telemetry for `mongosh`.

```javascript
enableTelemetry()
```

The command response confirms that telemetry is enabled:

```javascript
Telemetry is now enabled.
```
