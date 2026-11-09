<!-- Converted from tutorial/nav/start-or-stop-mongodb-agent.txt (reStructuredText). Includes are inlined. -->

# Restart the MongoDB  Agent

For maintenance or troubleshooting purposes, you may want to
temporarily shut down or restart the MongoDB Agent.

## Restart the MongoDB Agent

tabs:
  - id: linux-rpm
    name: RPM
    content: |

      If you installed the MongoDB Agent using an `rpm` package,
      such as on RHEL, CentOS, or SUSE, issue the following command to
      restart the MongoDB Agent:

      ```sh
      sudo service mongodb-mms-automation-agent restart
      ```

  - id: linux-deb
    name: DEB
    content: |

      If you installed the MongoDB Agent using a `deb` package,
      as on Ubuntu, issue the following command to restart the
      MongoDB Agent:

      ```sh
      sudo restart mongodb-mms-automation-agent
      ```

  - id: linux-tar
    name: TAR
    content: |

      Use these commands if you installed to Linux using a
      `tar` file. Issue the following commands from the directory to
      which you installed the MongoDB Agent:

      ```sh
      pkill -f mongodb-mms-automation-agent
      nohup ./mongodb-mms-automation-agent >> automation-agent.log 2>&1 &
      ```

## Start the MongoDB Agent

tabs:
  - id: linux-rpm
    name: RPM
    content: |

      If you installed the MongoDB Agent using an `rpm` package,
      such as on RHEL, CentOS, or SUSE, issue the following command to
      start the MongoDB Agent:

      ```sh
      sudo service mongodb-mms-automation-agent start
      ```

  - id: linux-deb
    name: DEB
    content: |

      If you installed the MongoDB Agent using a `deb` package,
      as on Ubuntu, issue the following command to start the
      MongoDB Agent:

      ```sh
      sudo start mongodb-mms-automation-agent
      ```

  - id: linux-tar
    name: TAR
    content: |

      Use this command if you installed to Linux using a
      `tar` file. Issue the following command from the directory to
      which you installed the MongoDB Agent:

      ```sh
      nohup ./mongodb-mms-automation-agent >> automation-agent.log 2>&1 &
      ```

## Stop the MongoDB Agent

tabs:
  - id: linux-rpm
    name: RPM
    content: |

      If you installed the MongoDB Agent using an `rpm` package,
      such as on RHEL, CentOS, or SUSE, issue the following command
      to stop the MongoDB Agent:

      ```sh
      sudo service mongodb-mms-automation-agent stop
      ```

  - id: linux-deb
    name: DEB
    content: |

      If you installed the MongoDB Agent using a `deb` package,
      as on Ubuntu, issue the following command to stop the MongoDB Agent:

      ```sh
      sudo stop mongodb-mms-automation-agent
      ```

  - id: linux-tar
    name: TAR
    content: |

      If you installed to a Linux system using a `tar` file,
      issue the following command to stop the MongoDB Agent:

      ```sh
      pkill -f mongodb-mms-automation-agent
      ```
