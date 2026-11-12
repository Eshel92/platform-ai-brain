<!-- Part 2 of 6 of osquery/exported-fields-reference.md (split because the page is big). -->

*creator_uid* - keyword, number.long

* _shared_memory.creator_uid_ - User ID of creator process

*csname* - keyword, text.text

* _patches.csname_ - The name of the host the patch is installed on.

*ctime* - keyword

* _device_file.ctime_ - Creation time
* _file.ctime_ - Last status change time
* _file_events.ctime_ - Last status change time
* _gatekeeper_approved_apps.ctime_ - Last change time
* _process_events.ctime_ - File last metadata change in UNIX time
* _shared_memory.ctime_ - Changed time

*current_capacity* - keyword, number.long

* _battery.current_capacity_ - The battery's current capacity (level of charge) in mAh

*current_clock_speed* - keyword, number.long

* _cpu_info.current_clock_speed_ - The current frequency of the CPU.

*current_directory* - keyword, text.text

* _windows_crashes.current_directory_ - Current working directory of the crashed process

*current_disk_queue_length* - keyword, number.long

* _physical_disk_performance.current_disk_queue_length_ - Number of requests outstanding on the disk at the time the performance data is collected

*current_locale* - keyword, text.text

* _chrome_extensions.current_locale_ - Current locale supported by extension

*current_value* - keyword, text.text

* _system_controls.current_value_ - Value of setting

*cwd* - keyword, text.text

* _bpf_process_events.cwd_ - Current working directory
* _es_process_events.cwd_ - The process current working directory
* _process_events.cwd_ - The process current working directory
* _process_file_events.cwd_ - The current working directory of the process
* _processes.cwd_ - Process current working directory

*cycle_count* - keyword, number.long

* _battery.cycle_count_ - The number of charge/discharge cycles

*data* - keyword, text.text

* _magic.data_ - Magic number data from libmagic
* _registry.data_ - Data content of registry value
* _windows_eventlog.data_ - Data associated with the event
* _windows_events.data_ - Data associated with the event

*data_width* - keyword, number.long

* _memory_devices.data_width_ - Data width, in bits, of this memory device

*database* - keyword, number.long

* _lxd_cluster_members.database_ - Whether the server is a database node (1) or not (0)

*date* - keyword

* _drivers.date_ - Driver date
* _platform_info.date_ - Self-reported platform code update date
* _windows_update_history.date_ - Date and the time an update was applied

*date_created* - keyword, number.long

* _windows_search.date_created_ - The unix timestamp of when the item was created.

*date_modified* - keyword, number.long

* _windows_search.date_modified_ - The unix timestamp of when the item was last modified

*datetime* - keyword, text.text

* _crashes.datetime_ - Date/Time at which the crash occurred
* _powershell_events.datetime_ - System time at which the Powershell script event occurred
* _process_etw_events.datetime_ - Event timestamp in DATETIME format
* _syslog_events.datetime_ - Time known to syslog
* _time.datetime_ - Current date and time (ISO format) in UTC
* _windows_crashes.datetime_ - Timestamp (log format) of the crash
* _windows_eventlog.datetime_ - System time at which the event occurred
* _windows_events.datetime_ - System time at which the event occurred

*day* - keyword, number.long

* _time.day_ - Current day in UTC

*day_of_month* - keyword, text.text

* _crontab.day_of_month_ - The day of the month for the job

*day_of_week* - keyword, text.text

* _crontab.day_of_week_ - The day of the week for the job

*days* - keyword, number.long

* _uptime.days_ - Days of uptime

*dc_site_name* - keyword, text.text

* _ntdomains.dc_site_name_ - The name of the site where the domain controller is located.

*decompressed* - keyword, number.long

* _virtual_memory_info.decompressed_ - The total number of pages that have been decompressed by the VM compressor.

*default_locale* - keyword, text.text

* _chrome_extensions.default_locale_ - Default locale supported by extension

*default_value* - keyword, text.text

* _osquery_flags.default_value_ - Flag default value

*denied_mask* - keyword, text.text

* _apparmor_events.denied_mask_ - Denied permissions for the process

*denylisted* - keyword, number.long

* _osquery_schedule.denylisted_ - 1 if the query is denylisted else 0

*dependencies* - keyword, text.text

* _kernel_panics.dependencies_ - Module dependencies existing in crashed module's backtrace

*depth* - keyword, number.long

* _iokit_devicetree.depth_ - Device nested depth
* _iokit_registry.depth_ - Node nested depth

*description* - keyword, text.text

* _appcompat_shims.description_ - Description of the SDB.
* _browser_plugins.description_ - Plugin description text
* _chassis_info.description_ - An extended description of the chassis if available.
* _chrome_extensions.description_ - Extension-optional description
* _disk_info.description_ - The OS's description of the disk.
* _drivers.description_ - Driver description
* _firefox_addons.description_ - Addon-supplied description string
* _interface_details.description_ - Short description of the object a one-line string.
* _kernel_keys.description_ - The key description.
* _keychain_acls.description_ - The description included with the ACL entry
* _keychain_items.description_ - Optional item description
* _logical_drives.description_ - The canonical description of the drive, e.g. 'Logical Fixed Disk', 'CD-ROM Disk'.
* _lxd_images.description_ - Image description
* _lxd_instances.description_ - Instance description
* _npm_packages.description_ - Package-supplied description
* _osquery_flags.description_ - Flag description
* _patches.description_ - Fuller description of the patch.
* _safari_extensions.description_ - Optional extension description text
* _secureboot.description_ - (Apple Silicon) Human-readable description: 'Full Security', 'Reduced Security', or 'Permissive Security'
* _services.description_ - Service Description
* _shared_resources.description_ - A textual description of the object
* _smbios_tables.description_ - Table entry description
* _systemd_units.description_ - Unit description
* _users.description_ - Optional user description
* _windows_update_history.description_ - Description of an update
* _ycloud_instance_metadata.description_ - Description of the VM

*designed_capacity* - keyword, number.long

* _battery.designed_capacity_ - The battery's designed capacity in mAh

*dest_filename* - keyword, text.text

* _es_process_file_events.dest_filename_ - Destination filename for the event

*dest_path* - keyword, text.text

* _process_file_events.dest_path_ - The canonical path associated with the event

*destination* - keyword, text.text

* _cups_jobs.destination_ - The printer the job was sent to
* _docker_container_mounts.destination_ - Destination path inside container
* _routes.destination_ - Destination IP address

*destination_id* - keyword, text.text

* _time_machine_backups.destination_id_ - Time Machine destination ID
* _time_machine_destinations.destination_id_ - Time Machine destination ID

*dev_id_enabled* - keyword, number.long

* _gatekeeper.dev_id_enabled_ - 1 If a Gatekeeper allows execution from identified developers else 0

*developer_id* - keyword, text.text

* _safari_extensions.developer_id_ - Optional developer identifier
* _xprotect_meta.developer_id_ - Developer identity (SHA1) of extension

*development_region* - keyword, text.text

* _apps.development_region_ - Info properties CFBundleDevelopmentRegion label
* _browser_plugins.development_region_ - Plugin language-localization

*device* - keyword, text.text

* _device_file.device_ - Absolute file path to device node
* _device_firmware.device_ - The device name
* _device_hash.device_ - Absolute file path to device node
* _device_partitions.device_ - Absolute file path to device node
* _disk_events.device_ - Disk event BSD name
* _file.device_ - Device ID (optional)
* _kernel_info.device_ - Kernel device identifier
* _lxd_instance_devices.device_ - Name of the device
* _mounts.device_ - Mounted device
* _process_memory_map.device_ - MA:MI Major/minor device ID

*device_alias* - keyword, text.text

* _mounts.device_alias_ - Mounted device alias

*device_error_address* - keyword, text.text

* _memory_error_info.device_error_address_ - 32 bit physical address of the error relative to the start of the failing memory address, in bytes

*device_id* - keyword, text.text

* _bitlocker_info.device_id_ - ID of the encrypted drive.
* _cpu_info.device_id_ - The DeviceID of the CPU.
* _drivers.device_id_ - Device ID
* _logical_drives.device_id_ - The drive id, usually the drive name, e.g., 'C:'.

*device_locator* - keyword, text.text

* _memory_devices.device_locator_ - String number of the string that identifies the physically-labeled socket or board position where the memory device is located

*device_name* - keyword, text.text

* _drivers.device_name_ - Device name
* _md_devices.device_name_ - md device name

*device_path* - keyword, text.text

* _iokit_devicetree.device_path_ - Device tree path

*device_type* - keyword, text.text

* _lxd_instance_devices.device_type_ - Device type

*dhcp_enabled* - keyword, number.long

* _interface_details.dhcp_enabled_ - If TRUE, the dynamic host configuration protocol (DHCP) server automatically assigns an IP address to the computer system when establishing a network connection.

*dhcp_lease_expires* - keyword, text.text

* _interface_details.dhcp_lease_expires_ - Expiration date and time for a leased IP address that was assigned to the computer by the dynamic host configuration protocol (DHCP) server.

*dhcp_lease_obtained* - keyword, text.text

* _interface_details.dhcp_lease_obtained_ - Date and time the lease was obtained for the IP address assigned to the computer by the dynamic host configuration protocol (DHCP) server.

*dhcp_server* - keyword, text.text

* _interface_details.dhcp_server_ - IP address of the dynamic host configuration protocol (DHCP) server.

*direction* - keyword, text.text

* _windows_firewall_rules.direction_ - Direction of traffic for which the rule applies

*directory* - keyword, text.text

* _extended_attributes.directory_ - Directory of file(s)
* _file.directory_ - Directory of file(s)
* _hash.directory_ - Must provide a path or directory
* _npm_packages.directory_ - Directory where node_modules are located
* _python_packages.directory_ - Directory where Python modules are located
* _users.directory_ - User's home directory

*disabled* - keyword

* _browser_plugins.disabled_ - Is the plugin disabled. 1 = Disabled
* _firefox_addons.disabled_ - 1 If the addon is application-disabled else 0
* _launchd.disabled_ - Skip loading this daemon or agent on boot
* _wifi_networks.disabled_ - 1 if this network is disabled, 0 otherwise

*disc_sharing* - keyword, number.long

* _sharing_preferences.disc_sharing_ - 1 If CD or DVD sharing is enabled else 0

*disconnected* - keyword, number.long

* _connectivity.disconnected_ - True if the all interfaces are not connected to any network

*discovery_cache_hits* - keyword, number.long

* _osquery_packs.discovery_cache_hits_ - The number of times that the discovery query used cached values since the last time the config was reloaded

*discovery_executions* - keyword, number.long

* _osquery_packs.discovery_executions_ - The number of times that the discovery queries have been executed since the last time the config was reloaded

*disk_bytes_read* - keyword, number.long

* _processes.disk_bytes_read_ - Bytes read from disk

*disk_bytes_written* - keyword, number.long

* _processes.disk_bytes_written_ - Bytes written to disk

*disk_index* - keyword, number.long

* _disk_info.disk_index_ - Physical drive number of the disk.

*disk_read* - keyword, number.long

* _docker_container_stats.disk_read_ - Total disk read bytes

*disk_size* - keyword, number.long

* _disk_info.disk_size_ - Size of the disk.

*disk_write* - keyword, number.long

* _docker_container_stats.disk_write_ - Total disk write bytes

*display_id* - keyword, text.text

* _connected_displays.display_id_ - The display ID.

*display_name* - keyword, text.text

* _apps.display_name_ - Info properties CFBundleDisplayName label
* _services.display_name_ - Service Display name

*display_type* - keyword, text.text

* _connected_displays.display_type_ - The type of display.

*dns_domain* - keyword, text.text

* _interface_details.dns_domain_ - Organization name followed by a period and an extension that indicates the type of organization, such as 'microsoft.com'.

*dns_domain_name* - keyword, text.text

* _logon_sessions.dns_domain_name_ - The DNS name for the owner of the logon session.

*dns_domain_suffix_search_order* - keyword, text.text

* _interface_details.dns_domain_suffix_search_order_ - Array of DNS domain suffixes to be appended to the end of host names during name resolution.

*dns_forest_name* - keyword, text.text

* _ntdomains.dns_forest_name_ - The name of the root of the DNS tree.

*dns_host_name* - keyword, text.text

* _interface_details.dns_host_name_ - Host name used to identify the local computer for authentication by some utilities.

*dns_server_search_order* - keyword, text.text

* _interface_details.dns_server_search_order_ - Array of server IP addresses to be used in querying for DNS servers.

*domain* - keyword, text.text

* _ad_config.domain_ - Active Directory trust domain
* _managed_policies.domain_ - System or manager-chosen domain key
* _preferences.domain_ - Application ID usually in com.name.product format

*domain_controller_address* - keyword, text.text

* _ntdomains.domain_controller_address_ - The IP Address of the discovered domain controller..

*domain_controller_name* - keyword, text.text

* _ntdomains.domain_controller_name_ - The name of the discovered domain controller.

*domain_name* - keyword, text.text

* _ntdomains.domain_name_ - The name of the domain.

*drive_letter* - keyword, text.text

* _bitlocker_info.drive_letter_ - Drive letter of the encrypted drive.
* _ntfs_journal_events.drive_letter_ - The drive letter identifying the source journal

*drive_name* - keyword, text.text

* _md_drives.drive_name_ - Drive device name

*driver* - keyword, text.text

* _docker_container_mounts.driver_ - Driver providing the mount
* _docker_networks.driver_ - Network driver
* _docker_volumes.driver_ - Volume driver
* _hardware_events.driver_ - Driver claiming the device
* _lxd_storage_pools.driver_ - Storage driver
* _pci_devices.driver_ - PCI Device used driver
* _video_info.driver_ - The driver of the device.

*driver_date* - keyword, number.long

* _video_info.driver_date_ - The date listed on the installed driver.

*driver_key* - keyword, text.text

* _drivers.driver_key_ - Driver key

*driver_version* - keyword, text.text

* _video_info.driver_version_ - The version of the installed driver.

*dst_ip* - keyword, text.text

* _iptables.dst_ip_ - Destination IP address.

*dst_mask* - keyword, text.text

* _iptables.dst_mask_ - Destination IP address mask.

*dst_port* - keyword, text.text

* _iptables.dst_port_ - Protocol destination port(s).

*dtime* - keyword, number.long

* _shared_memory.dtime_ - Detached time

*dump_certificate* - keyword, number.long

* _curl_certificate.dump_certificate_ - Set this value to '1' to dump certificate

*duration* - keyword, number.long

* _bpf_process_events.duration_ - How much time was spent inside the syscall (nsecs)
* _bpf_socket_events.duration_ - How much time was spent inside the syscall (nsecs)

*eapi* - keyword, number.long

* _portage_packages.eapi_ - The eapi for the ebuild

*egid* - keyword

* _docker_container_processes.egid_ - Effective group ID
* _es_process_events.egid_ - Effective Group ID of the process
* _process_events.egid_ - Effective group ID at process start
* _process_file_events.egid_ - Effective group ID of the process using the file
* _processes.egid_ - Unsigned effective group ID

*eid* - keyword, text.text

* _apparmor_events.eid_ - Event ID
* _bpf_process_events.eid_ - Event ID
* _bpf_socket_events.eid_ - Event ID
* _disk_events.eid_ - Event ID
* _es_process_events.eid_ - Event ID
* _es_process_file_events.eid_ - Event ID
* _file_events.eid_ - Event ID
* _hardware_events.eid_ - Event ID
* _ntfs_journal_events.eid_ - Event ID
* _process_etw_events.eid_ - Event ID
* _process_events.eid_ - Event ID
* _process_file_events.eid_ - Event ID
* _selinux_events.eid_ - Event ID
* _socket_events.eid_ - Event ID
* _syslog_events.eid_ - Event ID
* _user_events.eid_ - Event ID
* _windows_events.eid_ - Event ID
* _yara_events.eid_ - Event ID

*ejectable* - keyword, number.long

* _disk_events.ejectable_ - 1 if ejectable, 0 if not

*elapsed_time* - keyword, number.long

* _processes.elapsed_time_ - Elapsed time in seconds this process has been running.

*element* - keyword, text.text

* _apps.element_ - Does the app identify as a background agent

*elevated_token* - keyword, number.long

* _processes.elevated_token_ - Process uses elevated token yes=1, no=0

*enable_admin_account* - keyword, number.long

* _security_profile_info.enable_admin_account_ - Determines whether the Administrator account on the local computer is enabled

*enable_guest_account* - keyword, number.long

* _security_profile_info.enable_guest_account_ - Determines whether the Guest account on the local computer is enabled

*enable_ipv6* - keyword, number.long

* _docker_networks.enable_ipv6_ - 1 if IPv6 is enabled on this network. 0 otherwise

*enabled* - keyword

* _app_schemes.enabled_ - 1 if this handler is the OS default, else 0
* _event_taps.enabled_ - Is the Event Tap enabled
* _interface_details.enabled_ - Indicates whether the adapter is enabled or not.
* _location_services.enabled_ - 1 if Location Services are enabled, else 0
* _lxd_cluster.enabled_ - Whether clustering enabled (1) or not (0) on this node
* _sandboxes.enabled_ - Application sandboxings enabled on container
* _scheduled_tasks.enabled_ - Whether or not the scheduled task is enabled
* _screenlock.enabled_ - 1 If a password is required after sleep or the screensaver begins; else 0
* _sip_config.enabled_ - 1 if this configuration is enabled, otherwise 0
* _tpm_info.enabled_ - TPM is enabled
* _windows_firewall_rules.enabled_ - 1 if the rule is enabled
* _yum_sources.enabled_ - Whether the repository is used

*enabled_nvram* - keyword, number.long

* _sip_config.enabled_nvram_ - 1 if this configuration is enabled, otherwise 0

*encrypted* - keyword, number.long

* _disk_encryption.encrypted_ - 1 If encrypted: true (disk is encrypted), else 0
* _user_ssh_keys.encrypted_ - 1 if key is encrypted, 0 otherwise

*encryption* - keyword, text.text

* _time_machine_destinations.encryption_ - Last known encrypted state

*encryption_method* - keyword, text.text

* _bitlocker_info.encryption_method_ - The encryption type of the device.

*encryption_status* - keyword, text.text

* _disk_encryption.encryption_status_ - Disk encryption status with one of following values: encrypted | not encrypted | undefined

*end* - keyword, text.text

* _memory_map.end_ - End address of memory region
* _process_memory_map.end_ - Virtual end address (hex)

*ending_address* - keyword, text.text

* _memory_array_mapped_addresses.ending_address_ - Physical ending address of last kilobyte of a range of memory mapped to physical memory array
* _memory_device_mapped_addresses.ending_address_ - Physical ending address of last kilobyte of a range of memory mapped to physical memory array

*endpoint_id* - keyword, text.text

* _docker_container_networks.endpoint_id_ - Endpoint ID

*entry* - keyword, text.text

* _authorization_mechanisms.entry_ - The whole string entry
* _shimcache.entry_ - Execution order.

*env* - keyword, text.text

* _es_process_events.env_ - Environment variables delimited by spaces
* _process_events.env_ - Environment variables delimited by spaces

*env_count* - keyword, number.long

* _es_process_events.env_count_ - Number of environment variables
* _process_events.env_count_ - Number of environment variables

*env_size* - keyword, number.long

* _process_events.env_size_ - Actual size (bytes) of environment list

*env_variables* - keyword, text.text

* _docker_containers.env_variables_ - Container environmental variables

*environment* - keyword, text.text

* _apps.environment_ - Application-set environment variables

*ephemeral* - keyword, number.long

* _lxd_instances.ephemeral_ - Whether the instance is ephemeral(1) or not(0)

*epoch* - keyword, number.long

* _rpm_packages.epoch_ - Package epoch value

*error* - keyword, text.text

* _apparmor_events.error_ - Error information

*error_granularity* - keyword, text.text

* _memory_error_info.error_granularity_ - Granularity to which the error can be resolved

*error_operation* - keyword, text.text

* _memory_error_info.error_operation_ - Memory access operation that caused the error

*error_resolution* - keyword, text.text

* _memory_error_info.error_resolution_ - Range, in bytes, within which this error can be determined, when an error address is given

*error_type* - keyword, text.text

* _memory_error_info.error_type_ - type of error associated with current error status for array or device

*euid* - keyword

* _docker_container_processes.euid_ - Effective user ID
* _es_process_events.euid_ - Effective User ID of the process
* _process_events.euid_ - Effective user ID at process start
* _process_file_events.euid_ - Effective user ID of the process using the file
* _processes.euid_ - Unsigned effective user ID

*event* - keyword, text.text

* _crontab.event_ - The job @event name (rare)

*event_queue* - keyword, number.long

* _carbon_black_info.event_queue_ - Size in bytes of Carbon Black event files on disk

*event_tap_id* - keyword, number.long

* _event_taps.event_tap_id_ - Unique ID for the Tap

*event_tapped* - keyword, text.text

* _event_taps.event_tapped_ - The mask that identifies the set of events to be observed.

*event_type* - keyword, text.text

* _es_process_events.event_type_ - Type of EndpointSecurity event
* _es_process_file_events.event_type_ - Type of EndpointSecurity event

*eventid* - keyword, number.long

* _windows_eventlog.eventid_ - Event ID of the event
* _windows_events.eventid_ - Event ID of the event

*events* - keyword, number.long

* _osquery_events.events_ - Number of events emitted or received since osquery started

*exception_address* - keyword, text.text

* _windows_crashes.exception_address_ - Address (in hex) where the exception occurred

*exception_code* - keyword, text.text

* _windows_crashes.exception_code_ - The Windows exception code

*exception_codes* - keyword, text.text

* _crashes.exception_codes_ - Exception codes from the crash

*exception_message* - keyword, text.text

* _windows_crashes.exception_message_ - The NTSTATUS error message associated with the exception code

*exception_notes* - keyword, text.text

* _crashes.exception_notes_ - Exception notes from the crash

*exception_type* - keyword, text.text

* _crashes.exception_type_ - Exception type of the crash

*exe* - keyword, text.text

* _seccomp_events.exe_ - The path to the executable that was used to invoke the analyzed process

*executable* - keyword, text.text

* _appcompat_shims.executable_ - Name of the executable that is being shimmed. This is pulled from the registry.
* _process_file_events.executable_ - The executable path

*executable_path* - keyword, text.text

* _wmi_cli_event_consumers.executable_path_ - Module to execute. The string can specify the full path and file name of the module to execute, or it can specify a partial name. If a partial name is specified, the current drive and current directory are assumed.

*execution_flag* - keyword, number.long

* _shimcache.execution_flag_ - Boolean Execution flag, 1 for execution, 0 for no execution, -1 for missing (this flag does not exist on Windows 10 and higher).

*executions* - keyword, number.long

* _osquery_schedule.executions_ - Number of times the query was executed

*exit_code* - keyword, text.text

* _bpf_process_events.exit_code_ - Exit code of the system call
* _bpf_socket_events.exit_code_ - Exit code of the system call
* _es_process_events.exit_code_ - Exit code of a process in case of an exit event
* _process_etw_events.exit_code_ - Exit Code - Present only on ProcessStop events

*expand* - keyword, number.long

* _default_environment.expand_ - 1 if the variable needs expanding, 0 otherwise

*expire* - keyword, number.long

* _shadow.expire_ - Number of days since UNIX epoch date until account is disabled

*expires_at* - keyword, text.text

* _lxd_images.expires_at_ - ISO time of image expiration

*extended_key_usage* - keyword, text.text

* _curl_certificate.extended_key_usage_ - Extended usage of key in certificate

*extension_type* - keyword, text.text

* _safari_extensions.extension_type_ - Extension Type: WebOrAppExtension or LegacyExtension

*extensions* - keyword, text.text

* _osquery_info.extensions_ - osquery extensions status

*external* - keyword, number.long

* _app_schemes.external_ - 1 if this handler does NOT exist on macOS by default, else 0

*extra* - keyword, text.text

* _asl.extra_ - Extra columns, in JSON format. Queries against this column are performed entirely in SQLite, so do not benefit from efficient querying via asl.h.
* _os_version.extra_ - Optional extra release specification
* _platform_info.extra_ - Platform-specific additional information

*facility* - keyword, text.text

* _asl.facility_ - Sender's facility.  Default is 'user'.
* _syslog_events.facility_ - Syslog facility

*fahrenheit* - keyword, number.double

* _temperature_sensors.fahrenheit_ - Temperature in Fahrenheit

*failed_disks* - keyword, number.long

* _md_devices.failed_disks_ - Number of failed disks in array

*failed_login_count* - keyword, number.long

* _account_policy_data.failed_login_count_ - The number of failed login attempts using an incorrect password. Count resets after a correct password is entered.

*failed_login_timestamp* - keyword, number.double

* _account_policy_data.failed_login_timestamp_ - The time of the last failed login attempt. Resets after a correct password is entered

*family* - keyword, number.long

* _bpf_socket_events.family_ - The Internet protocol family ID
* _listening_ports.family_ - Network protocol (IPv4, IPv6)
* _process_open_sockets.family_ - Network protocol (IPv4, IPv6)
* _socket_events.family_ - The Internet protocol family ID

*fan* - keyword, text.text

* _fan_speed_sensors.fan_ - Fan number

*faults* - keyword, number.long

* _virtual_memory_info.faults_ - Total number of calls to vm_faults.

*fd* - keyword, text.text

* _bpf_socket_events.fd_ - The file description for the process socket
* _listening_ports.fd_ - Socket file descriptor number
* _process_open_files.fd_ - Process-specific file descriptor number
* _process_open_pipes.fd_ - File descriptor
* _process_open_sockets.fd_ - Socket file descriptor number
* _socket_events.fd_ - The file description for the process socket

*feature* - keyword, text.text

* _cpuid.feature_ - Present feature flags

*feature_control* - keyword, number.long

* _msr.feature_control_ - Bitfield controlling enabled features.

*field_name* - keyword, text.text

* _system_controls.field_name_ - Specific attribute of opaque type

*file_attributes* - keyword, text.text

* _ntfs_journal_events.file_attributes_ - File attributes

*file_backed* - keyword, number.long

* _virtual_memory_info.file_backed_ - Total number of file backed pages.

*file_id* - keyword, text.text

* _file.file_id_ - file ID

*file_sharing* - keyword, number.long

* _sharing_preferences.file_sharing_ - 1 If file sharing is enabled else 0

*file_system* - keyword, text.text

* _logical_drives.file_system_ - The file system of the drive.

*file_version* - keyword, text.text

* _file.file_version_ - File version

*filename* - keyword, text.text

* _device_file.filename_ - Name portion of file path
* _es_process_file_events.filename_ - The source or target filename for the event
* _file.filename_ - Name portion of file path
* _lxd_images.filename_ - Filename of the image file
* _prefetch.filename_ - Executable filename.
* _xprotect_entries.filename_ - Use this file name to match

*filepath* - keyword, text.text

* _package_bom.filepath_ - Package file or directory

*filesystem* - keyword, text.text

* _disk_events.filesystem_ - Filesystem if available

*filetype* - keyword, text.text

* _xprotect_entries.filetype_ - Use this file type to match

*filevault_status* - keyword, text.text

* _disk_encryption.filevault_status_ - FileVault status with one of following values: on | off | unknown

*filter* - keyword, text.text

* _wmi_filter_consumer_binding.filter_ - Reference to an instance of __EventFilter that represents the object path to an event filter which is a query that specifies the type of event to be received.

*filter_name* - keyword, text.text

* _iptables.filter_name_ - Packet matching filter table name.

*fingerprint* - keyword, text.text

* _lxd_certificates.fingerprint_ - SHA256 hash of the certificate

*finished_at* - keyword, text.text

* _docker_containers.finished_at_ - Container finish time as string

*firewall* - keyword, text.text

* _windows_security_center.firewall_ - The health of the monitored Firewall (see windows_security_products)

*firewall_unload* - keyword, number.long

* _alf.firewall_unload_ - 1 If firewall unloading enabled else 0

*firmware_type* - keyword, text.text

* _platform_info.firmware_type_ - The type of firmware (uefi, bios, iboot, openfirmware, unknown).

*firmware_version* - keyword, text.text

* _ibridge_info.firmware_version_ - The build version of the firmware

*fix_comments* - keyword, text.text

* _patches.fix_comments_ - Additional comments about the patch.

*flag* - keyword, number.long

* _shadow.flag_ - Reserved

*flags* - keyword

* _device_partitions.flags_ - Value that describes the partition (TSK_VS_PART_FLAG_ENUM)
* _dns_cache.flags_ - DNS record flags
* _interface_details.flags_ - Flags (netdevice) for the device
* _kernel_keys.flags_ - A set of flags describing the state of the key.
* _mounts.flags_ - Mounted device flags
* _pipes.flags_ - The flags indicating whether this pipe connection is a server or client end, and if the pipe for sending messages or bytes
* _process_etw_events.flags_ - Process Flags
* _routes.flags_ - Flags to describe route

*folder_id* - keyword, text.text

* _ycloud_instance_metadata.folder_id_ - Folder identifier for the VM

*following* - keyword, text.text

* _systemd_units.following_ - The name of another unit that this unit follows in state

*force_logoff_when_expire* - keyword, number.long

* _security_profile_info.force_logoff_when_expire_ - Determines whether SMB client sessions with the SMB server will be forcibly disconnected when the client's logon hours expire

*forced* - keyword, number.long

* _preferences.forced_ - 1 if the value is forced/managed, else 0

*form_factor* - keyword, text.text

* _memory_devices.form_factor_ - Implementation form factor for this memory device

*format* - keyword, text.text

* _cups_jobs.format_ - The format of the print job

*forwarding_enabled* - keyword, number.long

* _interface_ipv6.forwarding_enabled_ - Enable IP forwarding

*fragment_path* - keyword, text.text

* _systemd_units.fragment_path_ - The unit file path this unit was read from, if there is any

*frame_backtrace* - keyword, text.text

* _kernel_panics.frame_backtrace_ - Backtrace of the crashed module

*free* - keyword, number.long

* _virtual_memory_info.free_ - Total number of free pages.

*free_space* - keyword, number.long

* _logical_drives.free_space_ - The amount of free space, in bytes, of the drive (-1 on failure).

*friendly_name* - keyword, text.text

* _interface_addresses.friendly_name_ - The friendly display name of the interface.
* _interface_details.friendly_name_ - The friendly display name of the interface.

*from_webstore* - keyword, text.text

* _chrome_extensions.from_webstore_ - True if this extension was installed from the web store

*fs_id* - keyword, text.text

* _quicklook_cache.fs_id_ - Quicklook file fs_id key

*fsgid* - keyword

* _process_events.fsgid_ - Filesystem group ID at process start
* _process_file_events.fsgid_ - Filesystem group ID of the process using the file

*fsuid* - keyword

* _apparmor_events.fsuid_ - Filesystem user ID
* _process_events.fsuid_ - Filesystem user ID at process start
* _process_file_events.fsuid_ - Filesystem user ID of the process using the file

*gateway* - keyword, text.text

* _docker_container_networks.gateway_ - Gateway
* _docker_networks.gateway_ - Network gateway
* _routes.gateway_ - Route gateway

*gid* - keyword

* _asl.gid_ - GID that sent the log message (set by the server).
* _bpf_process_events.gid_ - Group ID
* _bpf_socket_events.gid_ - Group ID
* _device_file.gid_ - Owning group ID
* _docker_container_processes.gid_ - Group ID
* _es_process_events.gid_ - Group ID of the process
* _file.gid_ - Owning group ID
* _file_events.gid_ - Owning group ID
* _groups.gid_ - Unsigned int64 group ID
* _kernel_keys.gid_ - The group ID of the key.
* _package_bom.gid_ - Expected group of file or directory
* _process_events.gid_ - Group ID at process start
* _process_file_events.gid_ - The gid of the process performing the action
* _processes.gid_ - Unsigned group ID
* _seccomp_events.gid_ - Group ID of the user who started the analyzed process
* _user_groups.gid_ - Group ID
* _users.gid_ - Group ID (unsigned)

*gid_signed* - keyword, number.long

* _groups.gid_signed_ - A signed int64 version of gid
* _users.gid_signed_ - Default group ID as int64 signed (Apple)

*git_commit* - keyword, text.text

* _docker_version.git_commit_ - Docker build git commit

*global_seq_num* - keyword, number.long

* _es_process_events.global_seq_num_ - Global sequence number
* _es_process_file_events.global_seq_num_ - Global sequence number

*global_state* - keyword, number.long

* _alf.global_state_ - 1 If the firewall is enabled with exceptions, 2 if the firewall is configured to block all incoming connections, else 0

*go_version* - keyword, text.text

* _docker_version.go_version_ - Go version

*gpgcheck* - keyword, text.text

* _yum_sources.gpgcheck_ - Whether packages are GPG checked

*gpgkey* - keyword, text.text

* _yum_sources.gpgkey_ - URL to GPG key

*grace_period* - keyword, number.long

* _screenlock.grace_period_ - The amount of time in seconds the screen must be asleep or the screensaver on before a password is required on-wake. 0 = immediately; -1 = no password is required on-wake

*group_sid* - keyword, text.text

* _groups.group_sid_ - Unique group ID

*grouping* - keyword, text.text

* _windows_firewall_rules.grouping_ - Group to which an individual rule belongs

*groupname* - keyword, text.text

* _groups.groupname_ - Canonical local group name
* _launchd.groupname_ - Run this daemon or agent as this group
* _rpm_package_files.groupname_ - File default groupname from info DB
* _suid_bin.groupname_ - Binary owner group

*guest* - keyword, number.long

* _cpu_time.guest_ - Time spent running a virtual CPU for a guest OS under the control of the Linux kernel

*guest_nice* - keyword, number.long

* _cpu_time.guest_nice_ - Time spent running a niced guest 

*handle* - keyword, text.text

* _memory_array_mapped_addresses.handle_ - Handle, or instance number, associated with the structure
* _memory_arrays.handle_ - Handle, or instance number, associated with the array
* _memory_device_mapped_addresses.handle_ - Handle, or instance number, associated with the structure
* _memory_devices.handle_ - Handle, or instance number, associated with the structure in SMBIOS
* _memory_error_info.handle_ - Handle, or instance number, associated with the structure
* _oem_strings.handle_ - Handle, or instance number, associated with the Type 11 structure
* _smbios_tables.handle_ - Table entry handle

*handle_count* - keyword, number.long

* _processes.handle_count_ - Total number of handles that the process has open. This number is the sum of the handles currently opened by each thread in the process.

*handler* - keyword, text.text

* _app_schemes.handler_ - Application label for the handler

*hard_limit* - keyword, text.text

* _ulimit_info.hard_limit_ - Maximum limit value

*hard_links* - keyword, number.long

* _device_file.hard_links_ - Number of hard links
* _file.hard_links_ - Number of hard links

*hardware_model* - keyword, text.text

* _disk_info.hardware_model_ - Hard drive model.
* _system_info.hardware_model_ - Hardware model

*hardware_serial* - keyword, text.text

* _system_info.hardware_serial_ - Device serial number

*hardware_vendor* - keyword, text.text

* _system_info.hardware_vendor_ - Hardware vendor

*hardware_version* - keyword, text.text

* _system_info.hardware_version_ - Hardware version

*has_expired* - keyword, number.long

* _curl_certificate.has_expired_ - 1 if the certificate has expired, 0 otherwise

*hash* - keyword, text.text

* _prefetch.hash_ - Prefetch CRC hash.

*hash_alg* - keyword, text.text

* _shadow.hash_alg_ - Password hashing algorithm

*hash_resources* - keyword, number.long

* _signature.hash_resources_ - Set to 1 to also hash resources, or 0 otherwise. Default is 1

*hashed* - keyword, number.long

* _file_events.hashed_ - 1 if the file was hashed, 0 if not, -1 if hashing failed

*header* - keyword, text.text

* _sudoers.header_ - Symbol for given rule

*header_pid* - keyword, number.long

* _process_etw_events.header_pid_ - Process ID of the process reporting the event

*header_size* - keyword, number.long

* _smbios_tables.header_size_ - Header size in bytes

*health* - keyword, text.text

* _battery.health_ - One of the following: "Good" describes a well-performing battery, "Fair" describes a functional battery with limited capacity, or "Poor" describes a battery that's not capable of providing power

*hidden* - keyword, number.long

* _scheduled_tasks.hidden_ - Whether or not the task is visible in the UI
* _smc_keys.hidden_ - 1 if this key is normally hidden, otherwise 0

*history_file* - keyword, text.text

* _shell_history.history_file_ - Path to the .*_history for this user

*hit_count* - keyword, text.text

* _quicklook_cache.hit_count_ - Number of cache hits on thumbnail

*home_directory* - keyword, text.text

* _logon_sessions.home_directory_ - The home directory for the logon session.

*home_directory_drive* - keyword, text.text

* _logon_sessions.home_directory_drive_ - The drive location of the home directory of the logon session.

*homepage* - keyword, text.text

* _npm_packages.homepage_ - Package supplied homepage

*hop_limit* - keyword, number.long

* _interface_ipv6.hop_limit_ - Current Hop Limit

*hopcount* - keyword, number.long

* _routes.hopcount_ - Max hops expected

*host* - keyword, text.text

* _asl.host_ - Sender's address (set by the server).
* _last.host_ - Entry hostname
* _logged_in_users.host_ - Remote hostname
* _preferences.host_ - 'current' or 'any' host, where 'current' takes precedence
* _syslog_events.host_ - Hostname configured for syslog

*host_ip* - keyword, text.text

* _docker_container_ports.host_ip_ - Host IP address on which public port is listening

*host_port* - keyword, number.long

* _docker_container_ports.host_port_ - Host port

*hostname* - keyword, text.text

* _curl_certificate.hostname_ - Hostname to CURL (domain[:port], e.g. osquery.io)
* _system_info.hostname_ - Network hostname including domain
* _ycloud_instance_metadata.hostname_ - Hostname of the VM

*hostnames* - keyword, text.text

* _etc_hosts.hostnames_ - Raw hosts mapping

*hotfix_id* - keyword, text.text

* _patches.hotfix_id_ - The KB ID of the patch.

*hour* - keyword, text.text

* _crontab.hour_ - The hour of the day for the job
* _time.hour_ - Current hour in UTC

*hours* - keyword, number.long

* _uptime.hours_ - Hours of uptime

*hresult* - keyword, number.long
