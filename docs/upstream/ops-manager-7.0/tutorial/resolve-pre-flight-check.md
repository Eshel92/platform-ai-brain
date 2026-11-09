<!-- Converted from tutorial/resolve-pre-flight-check.txt (reStructuredText). Includes are inlined. -->

# Resolve Pre-flight Check Failure

When you start Ops Manager in Local Mode, Ops Manager performs a
*pre-flight check*. This check verifies if you downloaded all the
MongoDB binary archives for at least one platform of the needed MongoDB
versions to the `Versions Directory` on the Ops Manager server.
If these binaries were not downloaded, Ops Manager fails this check and
stops.

To pass the pre-flight check, you can either:

- Install all of the binaries for every version of MongoDB you need in
  the `Versions Directory` or

- Reconfigure Ops Manager temporarily so it can start, then change the
  versions of MongoDB your Ops Manager server supports.

This tutorial outlines the steps to configure Ops Manager temporarily to
resolve the pre-flight check failure and return to Local
Mode setting.

## Change Configuration File to Allow Ops Manager to Start

To reconfigure Ops Manager temporarily:

**Step 1: Open the Ops Manager configuration properties file.**

On your Ops Manager host, open the Ops Manager configuration properties
file. The configuration properties file is located in the following
path:

tabs:

  - id: debian
    content: |

      ```sh
      /opt/mongodb/mms/conf/conf-mms.properties
      ```

  - id: rhel
    content: |

      ```sh
      /opt/mongodb/mms/conf/conf-mms.properties
      ```

  - id: linux
    content: |

      ```sh
      <path>/conf/conf-mms.properties
      ```

**Step 2: Update the configuration file to change the source for MongoDB binaries.**

Add the following line to change the source for the MongoDB binaries
to be via the internet.

```ini
automation.versions.source=remote
```

Save and close the file.

**Step 3: Repeat for each Ops Manager host. (Optional)**

If you run Ops Manager with
high availability,
you must repeat the previous step on each Ops Manager host.

**Step 4: Start the Ops Manager service on each Ops Manager host.**

tabs:

  - id: debian
    content: |

      ```sh
      sudo service mongodb-mms start
      ```

  - id: rhel
    content: |

      ```sh
      sudo service mongodb-mms start
      ```

  - id: linux
    content: |

      ```sh
      <path>/bin/mongodb-mms start
      ```

If you run Ops Manager with high availability, you must repeat this
step on each Ops Manager host.

**Step 5: Ensure you have downloaded MongoDB binaries in your Versions Directory.**

For the selected versions, ensure that you have downloaded and placed
the archived binaries in the `Versions Directory` for every
project in Ops Manager.

Once you have changed which versions you want to support, continue
to the return-to-local-mode procedure.

## Return to Local Mode

Once you have resolved the pre-flight check errors, proceed with the
following steps to run Ops Manager in Local Mode.

If these steps are not completed, Ops Manager remains in Internet mode and
displays a notice in the configuration page notifying you that the
Local Mode setting in your `conf-mms.properties`
overrides this setting.

To revert to Local Mode:

**Step 1: Open the Ops Manager configuration properties file.**

On your Ops Manager host, open the Ops Manager configuration properties
file. The configuration properties file is located in the following
path:

tabs:

  - id: debian
    content: |

      ```sh
      /opt/mongodb/mms/conf/conf-mms.properties
      ```

  - id: rhel
    content: |

      ```sh
      /opt/mongodb/mms/conf/conf-mms.properties
      ```

  - id: linux
    content: |

      ```sh
      <path>/conf/conf-mms.properties
      ```

**Step 2: Delete the `automation.versions.source` line.**

Remove the following line to revert the change you made in the
previous procedure and re-enables Local Mode.

```ini
automation.versions.source=remote
```

Save and close the file.

**Step 3: Repeat the previous steps on each Ops Manager host. (Optional)**

If you run Ops Manager with
high availability,
you must repeat the previous steps on each Ops Manager host.

**Step 4: Restart the Ops Manager service on each Ops Manager host.**

tabs:

  - id: debian
    content: |

      ```sh
      sudo service mongodb-mms restart
      ```

  - id: rhel
    content: |

      ```sh
      sudo service mongodb-mms restart
      ```

  - id: linux
    content: |

      ```sh
      <path>/bin/mongodb-mms restart
      ```
