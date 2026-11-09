<!-- Converted from tutorial/transparent-huge-pages.txt (reStructuredText). Includes are inlined. -->

# Disable Transparent Huge Pages (THP)

Transparent Huge Pages (THP) is a Linux memory management system
that reduces the overhead of Translation Lookaside Buffer (TLB) lookups
on machines with large amounts of memory by using larger memory pages.

However, database workloads often perform poorly with THP enabled,
because they tend to have sparse rather than contiguous memory access
patterns. When running MongoDB on Linux, THP should be disabled for
best performance.

To ensure that THP is disabled before `mongod` starts,
you should create a service file for your platform's initialization
system that disables THP at boot. Instructions are provided below for
both the **systemd** and the **System V init** initialization systems.

Additionally, for RHEL (Red Hat Enterprise Linux) / CentOS
systems that make use of `ktune` and `tuned` performance profiles,
you must create a custom `tuned` profile as well.

## Create a Service File

To create a service file that disables THP, you will use the
built-in initialization system for your platform. Recent versions
of Linux tend to use **systemd** (which uses the `systemctl` command),
while older versions of Linux tend to use **System V init** (which uses
the `service` command). Refer to the documentation for your operating
system for more information.

Use the initialization system appropriate for your platform:

**systemd-systemctl:**

**Step 1: Create the `systemd` unit file**

Create the following file and save it at 
`/etc/systemd/system/disable-transparent-huge-pages.service`:

```sh
[Unit]
Description=Disable Transparent Hugepages (THP)
DefaultDependencies=no
After=sysinit.target local-fs.target
Before=mongod.service

[Service]
Type=oneshot
ExecStart=/bin/sh -c 'echo never | tee /sys/kernel/mm/transparent_hugepage/enabled > /dev/null && echo never | tee /sys/kernel/mm/transparent_hugepage/defrag > /dev/null'

[Install]
WantedBy=basic.target
```

**Note:**

Some versions of Red Hat Enterprise Linux, and potentially other Red 
Hat-based derivatives, use a different path for the THP `enabled` 
file:

```bash
/sys/kernel/mm/redhat_transparent_hugepage/enabled 
```

Verify which path is in use on your system and update the 
`disable-transparent-huge-pages.service` file accordingly.

**Step 2: Reload `systemd` unit files**

To reload the `systemd` unit files and make 
`disable-transparent-huge-pages.service` available for use, run the 
following command :

```sh
sudo systemctl daemon-reload
```

**Step 3: Start the service**

Run:

```sh
sudo systemctl start disable-transparent-huge-pages
```

To verify that the relevant THP settings have changed, run the
following command:

```sh
cat /sys/kernel/mm/transparent_hugepage/enabled && cat /sys/kernel/mm/transparent_hugepage/defrag
```

On Red Hat Enterprise Linux and potentially other Red Hat-based 
derivatives, you may instead need to use the following:

```sh
cat /sys/kernel/mm/redhat_transparent_hugepage/enabled && cat /sys/kernel/mm/redhat_transparent_hugepage/defrag 
```

The output should resemble the following: 

```bash
never
never
```

**Step 4: Configure your operating system to run it on boot**

To ensure that this setting is applied each time the operating system 
starts, run the following command:

```sh
sudo systemctl enable disable-transparent-huge-pages
```

**Step 5: (*Optional*) Customize tuned or ktune profile**

If you use `tuned` or `ktune` profiles on 
RHEL (Red Hat Enterprise Linux)/ CentOS, you must also create 
a custom `tuned` profile.

**initd-service:**

**Step 1: Create the `init.d` script**

Create the following file and save it at 
`/etc/init.d/disable-transparent-hugepages`:

```sh
#!/bin/bash
### BEGIN INIT INFO
# Provides:          disable-transparent-hugepages
# Required-Start:    $local_fs
# Required-Stop:
# X-Start-Before:    mongod mongodb-mms-automation-agent
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Disable Linux Transparent Hugepages
# Description:       Disable Linux Transparent Hugepages, to improve
#                    database performance.
### END INIT INFO

case $1 in
  start)
    if [ -d /sys/kernel/mm/transparent_hugepage ]; then
      thp_path=/sys/kernel/mm/transparent_hugepage
    elif [ -d /sys/kernel/mm/redhat_transparent_hugepage ]; then
      thp_path=/sys/kernel/mm/redhat_transparent_hugepage
    else
      exit 0
    fi

    echo 'never' | tee ${thp_path}/enabled > /dev/null && echo 'never' | tee ${thp_path}/defrag > /dev/null

    unset thp_path
    ;;
esac
```

**Step 2: Make the script executable**

Run:

```sh
sudo chmod 755 /etc/init.d/disable-transparent-hugepages
```

**Step 3: Run the script**

Run:

```sh
sudo /etc/init.d/disable-transparent-hugepages start
```

To verify that the relevant THP settings have changed, run the
following command:

```sh
cat /sys/kernel/mm/transparent_hugepage/enabled && cat /sys/kernel/mm/transparent_hugepage/defrag
```

On Red Hat Enterprise Linux and potentially other Red Hat-based
derivatives, you may instead need to use the following:

```sh
cat /sys/kernel/mm/redhat_transparent_hugepage/enabled && cat /sys/kernel/mm/redhat_transparent_hugepage/defrag
```

The output should resemble the following: 

```bash
never 
never
```

**Step 4: Configure your operating system to run it on boot**

To ensure that this setting is applied each time the operating system 
starts, run the following command for your Linux distribution:

| Distribution | Command |
|---|---|
| Ubuntu and Debian | .. code:: sh sudo update-rc.d disable-transparent-hugepages defaults |
| SUSE | .. code:: sh sudo insserv /etc/init.d/disable-transparent-hugepages |
| Red Hat, CentOS, Amazon Linux, and derivatives | .. code:: sh sudo chkconfig --add disable-transparent-hugepages |

**Step 5: (*Optional*) Customize tuned or ktune profile**

If you are using `tuned` or `ktune` profiles on 
RHEL (Red Hat Enterprise Linux)/ CentOS, you must also create 
a custom `tuned` profile.

## Using `tuned` and `ktune`

**Important:**

If using `tuned` or `ktune`, you must also perform the steps in
this section after creating the service file above.

`tuned` and `ktune` are dynamic kernel tuning tools that can affect
the transparent huge pages setting on your system. If you are using
`tuned` / `ktune` on your RHEL (Red Hat Enterprise Linux)
/ CentOS system while running `mongod`, you must create a custom
`tuned` profile to ensure that THP remains disabled.

### Red Hat/CentOS 6

**Step 1: Create a new profile.**

Create a new profile from an existing profile by copying the
relevant directory. This example uses the
`virtual-guest` profile as the base, and uses
`virtual-guest-no-thp` as the new profile:

```sh
sudo cp -r /etc/tune-profiles/virtual-guest /etc/tune-profiles/virtual-guest-no-thp
```

**Step 2: Edit `ktune.sh`.**

Edit `/etc/tune-profiles/virtual-guest-no-thp/ktune.sh`
and change the `set_transparent_hugepages` setting to the
following:

```cfg
set_transparent_hugepages never
```

**Step 3: Enable the new profile.**

Enable the new profile:

```sh
sudo tuned-adm profile virtual-guest-no-thp
```

### Red Hat/CentOS 7 and 8

**Step 1: Create a new profile.**

Create a new directory to hold the custom `tuned` profile.
This example inherits from the existing `virtual-guest`
profile, and uses `virtual-guest-no-thp` as the new profile:

```sh
sudo mkdir /etc/tuned/virtual-guest-no-thp
```

**Step 2: Edit `tuned.conf`.**

Create and edit `/etc/tuned/virtual-guest-no-thp/tuned.conf` so that it contains the
following:

```ini
[main]
include=virtual-guest

[vm]
transparent_hugepages=never
```

This example inherits from the existing `virtual-guest`
profile. Select the profile most appropriate for your system.

**Step 5: Enable the new profile.**

Enable the new profile:

```sh
sudo tuned-adm profile virtual-guest-no-thp
```
