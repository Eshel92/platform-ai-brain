<!-- Part 6 of 6 of osquery/exported-fields-reference.md (split because the page is big). -->

* _time.timestamp_ - Current timestamp (log format) in UTC
* _unified_log.timestamp_ - unix timestamp associated with the entry
* _windows_eventlog.timestamp_ - Timestamp to selectively filter the events

*timestamp_ms* - keyword, number.long

* _prometheus_metrics.timestamp_ms_ - Unix timestamp of collected data in MS

*timezone* - keyword, text.text

* _time.timezone_ - Timezone for reported time (hardcoded to UTC)

*title* - keyword, text.text

* _cups_jobs.title_ - Title of the printed job
* _windows_update_history.title_ - Title of an update

*token_elevation_status* - keyword, number.long

* _process_etw_events.token_elevation_status_ - Primary token elevation status - Present only on ProcessStart events

*token_elevation_type* - keyword, text.text

* _process_etw_events.token_elevation_type_ - Primary token elevation type - Present only on ProcessStart events

*total_seconds* - keyword, number.long

* _uptime.total_seconds_ - Total uptime seconds

*total_size* - keyword, number.long

* _docker_container_processes.total_size_ - Total virtual memory size
* _processes.total_size_ - Total virtual memory size (Linux, Windows) or 'footprint' (macOS)

*total_width* - keyword, number.long

* _memory_devices.total_width_ - Total width, in bits, of this memory device, including any check or error-correction bits

*transaction_id* - keyword, number.long

* _file_events.transaction_id_ - ID used during bulk update
* _yara_events.transaction_id_ - ID used during bulk update

*translated* - keyword, number.long

* _processes.translated_ - Indicates whether the process is running under the Rosetta Translation Environment, yes=1, no=0, error=-1.

*transmit_rate* - keyword, text.text

* _wifi_status.transmit_rate_ - The current transmit rate

*tries* - keyword, text.text

* _authorizations.tries_ - Label top-level key

*tty* - keyword, text.text

* _last.tty_ - Entry terminal
* _logged_in_users.tty_ - Device name

*turbo_disabled* - keyword, number.long

* _msr.turbo_disabled_ - Whether the turbo feature is disabled.

*turbo_ratio_limit* - keyword, number.long

* _msr.turbo_ratio_limit_ - The turbo feature ratio limit.

*type* - keyword, text.text

* _apparmor_events.type_ - Event type
* _appcompat_shims.type_ - Type of the SDB database.
* _block_devices.type_ - Block device type string
* _bpf_socket_events.type_ - The socket type
* _crashes.type_ - Type of crash log
* _device_file.type_ - File status
* _device_firmware.type_ - Type of device
* _device_partitions.type_ - Filesystem type if recognized, otherwise, 'meta', 'normal', or 'unallocated'
* _disk_encryption.type_ - Description of cipher type and mode if available
* _disk_info.type_ - The interface type of the disk.
* _dns_cache.type_ - DNS record type
* _dns_resolvers.type_ - Address type: sortlist, nameserver, search
* _docker_container_mounts.type_ - Type of mount (bind, volume)
* _docker_container_ports.type_ - Protocol (tcp, udp)
* _docker_volumes.type_ - Volume type
* _file.type_ - File status
* _firefox_addons.type_ - Extension, addon, webapp
* _hardware_events.type_ - Type of hardware and hardware event
* _homebrew_packages.type_ - Package type ('formula' or 'cask')
* _interface_addresses.type_ - Type of address. One of dhcp, manual, auto, other, unknown
* _interface_details.type_ - Interface type (includes virtual)
* _kernel_keys.type_ - The key type.
* _keychain_items.type_ - Keychain item type (class)
* _last.type_ - Entry type, according to ut_type types (utmp.h)
* _logged_in_users.type_ - Login type
* _logical_drives.type_ - Deprecated (always 'Unknown').
* _lxd_certificates.type_ - Type of the certificate
* _lxd_networks.type_ - Type of network
* _mounts.type_ - Mounted device type
* _ntfs_acl_permissions.type_ - Type of access mode for the access control entry.
* _nvram.type_ - Data type (CFData, CFString, etc)
* _osquery_events.type_ - Either publisher or subscriber
* _osquery_extensions.type_ - SDK extension type: core, extension, or module
* _osquery_flags.type_ - Flag type
* _process_etw_events.type_ - Event Type (ProcessStart, ProcessStop)
* _process_open_pipes.type_ - Pipe Type: named vs unnamed/anonymous
* _registry.type_ - Type of the registry value, or 'subkey' if item is a subkey
* _routes.type_ - Type of route
* _selinux_events.type_ - Event type
* _shared_resources.type_ - Type of resource being shared. Types include: disk drives, print queues, interprocess communications (IPC), and general devices.
* _smbios_tables.type_ - Table entry type
* _smc_keys.type_ - SMC-reported type literal type
* _startup_items.type_ - Startup Item or Login Item
* _system_controls.type_ - Data type
* _ulimit_info.type_ - System resource to be limited
* _user_events.type_ - The file description for the process socket
* _users.type_ - Whether the account is roaming (domain), local, or a system profile
* _windows_crashes.type_ - Type of crash log
* _windows_search.type_ - The item type
* _windows_security_products.type_ - Type of security product
* _xprotect_meta.type_ - Either plugin or extension

*type_name* - keyword, text.text

* _last.type_name_ - Entry type name, according to ut_type types (utmp.h)
* _shared_resources.type_name_ - Human readable value for the 'type' column

*uid* - keyword

* _account_policy_data.uid_ - User ID
* _asl.uid_ - UID that sent the log message (set by the server).
* _authorized_keys.uid_ - The local owner of authorized_keys file
* _bpf_process_events.uid_ - User ID
* _bpf_socket_events.uid_ - User ID
* _browser_plugins.uid_ - The local user that owns the plugin
* _chrome_extension_content_scripts.uid_ - The local user that owns the extension
* _chrome_extensions.uid_ - The local user that owns the extension
* _crashes.uid_ - User ID of the crashed process
* _device_file.uid_ - Owning user ID
* _disk_encryption.uid_ - Currently authenticated user if available
* _docker_container_processes.uid_ - User ID
* _es_process_events.uid_ - User ID of the process
* _file.uid_ - Owning user ID
* _file_events.uid_ - Owning user ID
* _firefox_addons.uid_ - The local user that owns the addon
* _kernel_keys.uid_ - The user ID of the key owner.
* _known_hosts.uid_ - The local user that owns the known_hosts file
* _launchd_overrides.uid_ - User ID applied to the override, 0 applies to all
* _package_bom.uid_ - Expected user of file or directory
* _password_policy.uid_ - User ID for the policy, -1 for policies that are global
* _process_events.uid_ - User ID at process start
* _process_file_events.uid_ - The uid of the process performing the action
* _processes.uid_ - Unsigned user ID
* _safari_extensions.uid_ - The local user that owns the extension
* _seccomp_events.uid_ - User ID of the user who started the analyzed process
* _shell_history.uid_ - Shell history owner
* _ssh_configs.uid_ - The local owner of the ssh_config file
* _user_events.uid_ - User ID
* _user_groups.uid_ - User ID
* _user_ssh_keys.uid_ - The local user that owns the key file
* _users.uid_ - User ID
* _vscode_extensions.uid_ - The local user that owns the plugin

*uid_signed* - keyword, number.long

* _users.uid_signed_ - User ID as int64 signed (Apple)

*umci_policy_status* - keyword, text.text

* _hvci_status.umci_policy_status_ - The status of the User Mode Code Integrity security settings. Returns UNKNOWN if an error is encountered.

*uncompressed* - keyword, number.long

* _virtual_memory_info.uncompressed_ - Total number of uncompressed pages.

*uninstall_string* - keyword, text.text

* _programs.uninstall_string_ - Path and filename of the uninstaller.

*unique_chip_id* - keyword, text.text

* _ibridge_info.unique_chip_id_ - Unique id of the iBridge controller

*unit_file_state* - keyword, text.text

* _systemd_units.unit_file_state_ - Whether the unit file is enabled, e.g. `enabled`, `masked`, `disabled`, etc

*unix_time* - keyword, number.long

* _time.unix_time_ - Current UNIX time in UTC

*unmask* - keyword, number.long

* _portage_keywords.unmask_ - If the package is unmasked

*unused_devices* - keyword, text.text

* _md_devices.unused_devices_ - Unused devices

*update_id* - keyword, text.text

* _windows_update_history.update_id_ - Revision-independent identifier of an update

*update_revision* - keyword, number.long

* _windows_update_history.update_revision_ - Revision number of an update

*update_source_alias* - keyword, text.text

* _lxd_images.update_source_alias_ - Alias of image at update source server

*update_source_certificate* - keyword, text.text

* _lxd_images.update_source_certificate_ - Certificate for update source server

*update_source_protocol* - keyword, text.text

* _lxd_images.update_source_protocol_ - Protocol used for image information update and image import from source server

*update_source_server* - keyword, text.text

* _lxd_images.update_source_server_ - Server for image update

*update_url* - keyword, text.text

* _chrome_extensions.update_url_ - Extension-supplied update URI
* _safari_extensions.update_url_ - Extension-supplied update URI

*upid* - keyword, number.long

* _processes.upid_ - A 64bit pid that is never reused. Returns -1 if we couldn't gather them from the system.

*uploaded_at* - keyword, text.text

* _lxd_images.uploaded_at_ - ISO time of image upload

*upn* - keyword, text.text

* _logon_sessions.upn_ - The user principal name (UPN) for the owner of the logon session.

*uppid* - keyword, number.long

* _processes.uppid_ - The 64bit parent pid that is never reused. Returns -1 if we couldn't gather them from the system.

*uptime* - keyword, number.long

* _apparmor_events.uptime_ - Time of execution in system uptime
* _kernel_panics.uptime_ - System uptime at kernel panic in nanoseconds
* _process_events.uptime_ - Time of execution in system uptime
* _process_file_events.uptime_ - Time of execution in system uptime
* _seccomp_events.uptime_ - Time of execution in system uptime
* _selinux_events.uptime_ - Time of execution in system uptime
* _socket_events.uptime_ - Time of execution in system uptime
* _user_events.uptime_ - Time of execution in system uptime

*url* - keyword, text.text

* _curl.url_ - The url for the request
* _lxd_cluster_members.url_ - URL of the node

*usage* - keyword, number.long

* _kernel_keys.usage_ - the number of threads and open file references that refer to this key.

*usb_address* - keyword, number.long

* _usb_devices.usb_address_ - USB Device used address

*usb_port* - keyword, number.long

* _usb_devices.usb_port_ - USB Device used port

*use* - keyword, text.text

* _memory_arrays.use_ - Function for which the array is used
* _portage_use.use_ - USE flag which has been enabled for package

*used_by* - keyword, text.text

* _kernel_modules.used_by_ - Module reverse dependencies
* _lxd_networks.used_by_ - URLs for containers using this network

*user* - keyword

* _cpu_time.user_ - Time spent in user mode
* _cups_jobs.user_ - The user who printed the job
* _docker_container_processes.user_ - User name
* _logged_in_users.user_ - User login name
* _logon_sessions.user_ - The account name of the security principal that owns the logon session.
* _sandboxes.user_ - Sandbox owner
* _systemd_units.user_ - The configured user, if any

*user_account* - keyword, text.text

* _services.user_account_ - The name of the account that the service process will be logged on as when it runs. This name can be of the form Domain\UserName. If the account belongs to the built-in domain, the name can be of the form .\UserName.

*user_account_control* - keyword, text.text

* _windows_security_center.user_account_control_ - The health of the User Account Control (UAC) capability in Windows

*user_action* - keyword, text.text

* _xprotect_reports.user_action_ - Action taken by user after prompted

*user_agent* - keyword, text.text

* _curl.user_agent_ - The user-agent string to use for the request

*user_namespace* - keyword, text.text

* _docker_containers.user_namespace_ - User namespace
* _process_namespaces.user_namespace_ - user namespace inode

*user_time* - keyword, number.long

* _osquery_schedule.user_time_ - Total user time in milliseconds spent executing
* _processes.user_time_ - CPU time in milliseconds spent in user space

*user_uuid* - keyword, text.text

* _disk_encryption.user_uuid_ - UUID of authenticated user if available

*username* - keyword, text.text

* _certificates.username_ - Username
* _es_process_events.username_ - Username
* _last.username_ - Entry username
* _launchd.username_ - Run this daemon or agent as this username
* _managed_policies.username_ - Policy applies only this user
* _preferences.username_ - (optional) read preferences for a specific user
* _process_etw_events.username_ - User rights - primary token username
* _rpm_package_files.username_ - File default username from info DB
* _shadow.username_ - Username
* _startup_items.username_ - The user associated with the startup item
* _suid_bin.username_ - Binary owner username
* _users.username_ - Username
* _windows_crashes.username_ - Username of the user who ran the crashed process

*uses_pattern* - keyword, number.long

* _xprotect_entries.uses_pattern_ - Uses a match pattern instead of identity

*uts_namespace* - keyword, text.text

* _docker_containers.uts_namespace_ - UTS namespace
* _process_namespaces.uts_namespace_ - uts namespace inode

*uuid* - keyword, text.text

* _block_devices.uuid_ - Block device Universally Unique Identifier
* _disk_encryption.uuid_ - Disk Universally Unique Identifier
* _disk_events.uuid_ - UUID of the volume inside DMG if available
* _managed_policies.uuid_ - Optional UUID assigned to policy set
* _osquery_extensions.uuid_ - The transient ID assigned for communication
* _osquery_info.uuid_ - Unique ID provided by the system
* _system_info.uuid_ - Unique ID provided by the system
* _users.uuid_ - User's UUID (Apple) or SID (Windows)
* _vscode_extensions.uuid_ - Extension UUID

*valid_from* - keyword, text.text

* _curl_certificate.valid_from_ - Period of validity start date

*valid_to* - keyword, text.text

* _curl_certificate.valid_to_ - Period of validity end date

*value* - keyword, text.text

* _ad_config.value_ - Variable typed option value
* _augeas.value_ - The value of the configuration item
* _azure_instance_tags.value_ - The tag value
* _cpuid.value_ - Bit value or string
* _default_environment.value_ - Value of the environment variable
* _docker_container_envs.value_ - Environment variable value
* _docker_container_labels.value_ - Optional label value
* _docker_image_labels.value_ - Optional label value
* _docker_network_labels.value_ - Optional label value
* _docker_volume_labels.value_ - Optional label value
* _ec2_instance_tags.value_ - Tag value
* _extended_attributes.value_ - The parsed information from the attribute
* _launchd_overrides.value_ - Overridden value
* _lxd_instance_config.value_ - Configuration parameter value
* _lxd_instance_devices.value_ - Device info param value
* _managed_policies.value_ - Policy value
* _mdls.value_ - Value stored in the metadata key
* _nvram.value_ - Raw variable data
* _oem_strings.value_ - The value of the OEM string
* _osquery_flags.value_ - Flag value
* _plist.value_ - String value of most CF types
* _power_sensors.value_ - Power in Watts
* _preferences.value_ - String value of most CF types
* _process_envs.value_ - Environment variable value
* _selinux_settings.value_ - Active value.
* _smc_keys.value_ - A type-encoded representation of the key value
* _wmi_bios_info.value_ - Value of the Bios setting

*valuetype* - keyword, text.text

* _mdls.valuetype_ - CoreFoundation type of data stored in value

*variable* - keyword, text.text

* _default_environment.variable_ - Name of the environment variable

*vbs_status* - keyword, text.text

* _hvci_status.vbs_status_ - The status of the virtualization based security settings. Returns UNKNOWN if an error is encountered.

*vendor* - keyword, text.text

* _block_devices.vendor_ - Block device vendor string
* _disk_events.vendor_ - Disk event vendor string
* _hardware_events.vendor_ - Hardware device vendor
* _pci_devices.vendor_ - PCI Device vendor
* _platform_info.vendor_ - Platform code vendor
* _rpm_packages.vendor_ - Package vendor
* _usb_devices.vendor_ - USB Device vendor string

*vendor_id* - keyword, text.text

* _connected_displays.vendor_id_ - The vendor ID of the display.
* _hardware_events.vendor_id_ - Hex encoded Hardware vendor identifier
* _pci_devices.vendor_id_ - Hex encoded PCI Device vendor identifier
* _usb_devices.vendor_id_ - Hex encoded USB Device vendor identifier

*vendor_syndrome* - keyword, text.text

* _memory_error_info.vendor_syndrome_ - Vendor specific ECC syndrome or CRC data associated with the erroneous access

*version* - keyword, text.text

* _alf.version_ - Application Layer Firewall version
* _apt_sources.version_ - Repository source version
* _authorizations.version_ - Label top-level key
* _azure_instance_metadata.version_ - Version of the VM image
* _bitlocker_info.version_ - The FVE metadata version of the drive.
* _browser_plugins.version_ - Plugin short version
* _chocolatey_packages.version_ - Package-supplied version
* _chrome_extension_content_scripts.version_ - Extension-supplied version
* _chrome_extensions.version_ - Extension-supplied version
* _crashes.version_ - Version info of the crashed process
* _curl_certificate.version_ - Version Number
* _deb_packages.version_ - Package version
* _device_firmware.version_ - Firmware version
* _docker_version.version_ - Docker version
* _drivers.version_ - Driver version
* _es_process_events.version_ - Version of EndpointSecurity event
* _es_process_file_events.version_ - Version of EndpointSecurity event
* _firefox_addons.version_ - Addon-supplied version string
* _gatekeeper.version_ - Version of Gatekeeper's gke.bundle
* _homebrew_packages.version_ - Current 'linked' version
* _hvci_status.version_ - The version number of the Device Guard build.
* _ie_extensions.version_ - Version of the executable
* _intel_me_info.version_ - Intel ME version
* _kernel_extensions.version_ - Extension version
* _kernel_info.version_ - Kernel version
* _npm_packages.version_ - Package-supplied version
* _office_mru.version_ - Office application version number
* _os_version.version_ - Pretty, suitable for presentation, OS version
* _osquery_extensions.version_ - Extension's version
* _osquery_info.version_ - osquery toolkit version
* _osquery_packs.version_ - Minimum osquery version that this query will run on
* _package_install_history.version_ - Package display version
* _package_receipts.version_ - Installed package version
* _platform_info.version_ - Platform code version
* _portage_keywords.version_ - The version which are affected by the use flags, empty means all
* _portage_packages.version_ - The version which are affected by the use flags, empty means all
* _portage_use.version_ - The version of the installed package
* _programs.version_ - Product version information.
* _python_packages.version_ - Package-supplied version
* _rpm_packages.version_ - Package version
* _safari_extensions.version_ - Extension long version
* _system_extensions.version_ - System extension version
* _usb_devices.version_ - USB Device version number
* _vscode_extensions.version_ - Extension version
* _windows_crashes.version_ - File version info of the crashed process

*video_mode* - keyword, text.text

* _video_info.video_mode_ - The current resolution of the display.

*virtual_process* - keyword, number.long

* _processes.virtual_process_ - Process is virtual (e.g. System, Registry, vmmem) yes=1, no=0

*visible* - keyword, number.long

* _firefox_addons.visible_ - 1 If the addon is shown in browser else 0

*visible_alarm* - keyword, text.text

* _chassis_info.visible_alarm_ - If TRUE, the frame is equipped with a visual alarm.

*vm_id* - keyword, text.text

* _azure_instance_metadata.vm_id_ - Unique identifier for the VM
* _azure_instance_tags.vm_id_ - Unique identifier for the VM

*vm_scale_set_name* - keyword, text.text

* _azure_instance_metadata.vm_scale_set_name_ - VM scale set name

*vm_size* - keyword, text.text

* _azure_instance_metadata.vm_size_ - VM size

*voltage* - keyword, number.long

* _battery.voltage_ - The battery's current voltage in mV

*volume_creation* - keyword, text.text

* _prefetch.volume_creation_ - Volume creation time.

*volume_id* - keyword, number.long

* _quicklook_cache.volume_id_ - Parsed volume ID from fs_id

*volume_serial* - keyword, text.text

* _file.volume_serial_ - Volume serial number
* _prefetch.volume_serial_ - Volume serial number.

*volume_size* - keyword, number.long

* _platform_info.volume_size_ - (Optional) size of firmware volume

*wall_time* - keyword, number.long

* _osquery_schedule.wall_time_ - Total wall time in seconds spent executing (deprecated), hidden=True

*wall_time_ms* - keyword, number.long

* _osquery_schedule.wall_time_ms_ - Total wall time in milliseconds spent executing

*warning* - keyword, number.long

* _shadow.warning_ - Number of days before password expires to warn user about it

*was_captive_network* - keyword, number.long

* _wifi_networks.was_captive_network_ - 1 if this network was previously a captive network, 0 otherwise

*watch_paths* - keyword, text.text

* _launchd.watch_paths_ - Key that launches daemon or agent if path is modified

*watcher* - keyword, number.long

* _osquery_info.watcher_ - Process (or thread/handle) ID of optional watcher process

*weekday* - keyword, text.text

* _time.weekday_ - Current weekday in UTC

*win32_exit_code* - keyword, number.long

* _services.win32_exit_code_ - The error code that the service uses to report an error that occurs when it is starting or stopping

*win_timestamp* - keyword, number.long

* _time.win_timestamp_ - Timestamp value in 100 nanosecond units

*windows_security_center_service* - keyword, text.text

* _windows_security_center.windows_security_center_service_ - The health of the Windows Security Center Service

*wired* - keyword, number.long

* _virtual_memory_info.wired_ - Total number of wired down pages.

*wired_size* - keyword, number.long

* _docker_container_processes.wired_size_ - Bytes of unpageable memory used by process
* _processes.wired_size_ - Bytes of unpageable memory used by process

*working_directory* - keyword, text.text

* _launchd.working_directory_ - Key used to specify a directory to chdir to before launch

*working_disks* - keyword, number.long

* _md_devices.working_disks_ - Number of working disks in array

*world* - keyword, number.long

* _portage_packages.world_ - If package is in the world file

*writable* - keyword, number.long

* _disk_events.writable_ - 1 if writable, 0 if not

*xpath* - keyword, text.text

* _windows_eventlog.xpath_ - The custom query to filter events

*year* - keyword, number.long

* _time.year_ - Current year in UTC

*zero_fill* - keyword, number.long

* _virtual_memory_info.zero_fill_ - Total number of zero filled pages.

*zone* - keyword, text.text

* _azure_instance_metadata.zone_ - Availability zone of the VM
* _ycloud_instance_metadata.zone_ - Availability zone of the VM
