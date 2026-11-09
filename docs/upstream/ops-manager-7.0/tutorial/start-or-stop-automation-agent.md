<!-- Converted from tutorial/start-or-stop-automation-agent.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Start or Stop the Automation Agent

**Important:** Legacy Automation Agent is EoL for Ops Manager 4.4

Update
from the legacy Automation Agent to the
MongoDB Agent.

For maintenance or troubleshooting purposes, you may want to
temporarily shut down or restart the Automation Agent.

## Start the Automation Agent

tabs:
  - id: linux-rpm
    name: RPM
    content: |

      If you installed the Automation Agent using an `rpm` package,
      such as on RHEL, CentOS, or SUSE, issue the following command to
      start the agent:

      ```sh
      sudo service mongodb-mms-automation-agent start
      ```

  - id: linux-deb
    name: DEB
    content: |

      If you installed the Automation Agent using a `deb` package,
      as on Ubuntu, issue the following command to start the agent:

      ```sh
      sudo start mongodb-mms-automation-agent
      ```

  - id: linux-tar
    name: TAR
    content: |

      Use this command if you installed to Linux or macOS using a
      `tar` file. Issue the following command from the directory to
      which you installed the Automation Agent:

      ```sh
      nohup ./mongodb-mms-automation-agent >> automation-agent.log 2>&1 &
      ```

  - id: windows
    name: Windows
    content: |

      1. Click the `windows` button.
      #. Click Control Panel.
      #. Click Administrative Tools.
      #. Click Services.
      #. Click MongoDB Automation Agent.
      #. From the Action menu, select Start.

## Stop the Automation Agent

tabs:
  - id: linux-rpm
    name: RPM
    content: |

      If you installed the Automation Agent using an `rpm` package,
      such as on RHEL, CentOS, or SUSE, issue the following command
      to stop the agent:

      ```sh
      sudo service mongodb-mms-automation-agent stop
      ```

  - id: linux-deb
    name: DEB
    content: |

      If you installed the Automation Agent using a `deb` package,
      as on Ubuntu, issue the following command to stop the agent:

      ```sh
      sudo stop mongodb-mms-automation-agent
      ```

  - id: linux-tar
    name: TAR
    content: |

      If you installed to a Linux system or macOS using a `tar` file,
      issue the following command to stop the Automation Agent:

      ```sh
      pkill -f mongodb-mms-automation-agent
      ```

  - id: windows
    name: Windows
    content: |

      1. Click the `windows` button.
      #. Click Control Panel.
      #. Click Administrative Tools.
      #. Click Services.
      #. Click MongoDB Automation Agent.
      #. From the Action menu, select Stop.
