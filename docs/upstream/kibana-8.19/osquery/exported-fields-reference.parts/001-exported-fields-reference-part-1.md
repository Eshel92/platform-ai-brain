<!-- Part 1 of 6 of osquery/exported-fields-reference.md (split because the page is big). -->

<!-- Converted from osquery/exported-fields-reference.asciidoc (AsciiDoc). Includes are inlined. -->

## Exported fields reference

The following fields can be returned in osquery results. Note the following about osquery fields:

* Some fields list multiple descriptions because the one that applies depends on which table was queried. For example, a result stored in the `osquery.autoupdate` field may represent a response from the `firefox_addons` table or the `windows_security_center` table. 
* In the cases where a field name is associated with more than one osquery table, we have made a best guess at what the data `type` should be. In the cases where it is unknown, the data type is set as a `keyword` object. 

For more information about osquery tables, see the [osquery schema documentation](https://osquery.io/schema).

### Fields

*UUID* - keyword, text.text

* _system_extensions.UUID_ - Extension unique id

*access* - keyword, text.text

* _ntfs_acl_permissions.access_ - Specific permissions that indicate the rights described by the ACE.

*accessed_directories* - keyword, text.text

* _prefetch.accessed_directories_ - Directories accessed by application within ten seconds of launch.

*accessed_directories_count* - keyword, number.long

* _prefetch.accessed_directories_count_ - Number of directories accessed.

*accessed_files* - keyword, text.text

* _prefetch.accessed_files_ - Files accessed by application within ten seconds of launch.

*accessed_files_count* - keyword, number.long

* _prefetch.accessed_files_count_ - Number of files accessed.

*accessed_time* - keyword, number.long

* _shellbags.accessed_time_ - Directory Accessed time.

*account* - keyword, text.text

* _keychain_items.account_ - Optional item account

*account_id* - keyword, text.text

* _ec2_instance_metadata.account_id_ - AWS account ID which owns this EC2 instance

*action* - keyword, text.text

* _disk_events.action_ - Appear or disappear
* _file_events.action_ - Change action (UPDATE, REMOVE, etc)
* _hardware_events.action_ - Remove, insert, change properties, etc
* _ntfs_journal_events.action_ - Change action (Write, Delete, etc)
* _scheduled_tasks.action_ - Actions executed by the scheduled task
* _socket_events.action_ - The socket action (bind, listen, close)
* _windows_firewall_rules.action_ - Action for the rule or default setting
* _yara_events.action_ - Change action (UPDATE, REMOVE, etc)

*activated* - keyword, number.long

* _tpm_info.activated_ - TPM is activated

*active* - keyword, number.long

* _firefox_addons.active_ - 1 If the addon is active else 0
* _memory_info.active_ - The total amount of buffer or page cache memory, in bytes, that is in active use
* _osquery_events.active_ - 1 if the publisher or subscriber is active else 0
* _osquery_packs.active_ - Whether this pack is active (the version, platform and discovery queries match) yes=1, no=0.
* _osquery_registry.active_ - 1 If this plugin is active else 0
* _virtual_memory_info.active_ - Total number of active pages.

*active_disks* - keyword, number.long

* _md_devices.active_disks_ - Number of active disks in array

*active_state* - keyword, text.text

* _systemd_units.active_state_ - The high-level unit activation state, i.e. generalization of SUB

*activity* - keyword, number.long

* _unified_log.activity_ - the activity ID associate with the entry

*actual* - keyword, number.long

* _fan_speed_sensors.actual_ - Actual speed

*add_reason* - keyword, text.text

* _wifi_networks.add_reason_ - Shows why this network was added, via menubar or command line or something else 

*added_at* - keyword, number.long

* _wifi_networks.added_at_ - Time this network was added as a unix_time

*additional_properties* - keyword, text.text

* _windows_search.additional_properties_ - Comma separated list of columns to include in properties JSON

*address* - keyword, text.text

* _arp_cache.address_ - IPv4 address target
* _dns_resolvers.address_ - Resolver IP/IPv6 address
* _etc_hosts.address_ - IP address mapping
* _interface_addresses.address_ - Specific address for interface
* _kernel_modules.address_ - Kernel module address
* _listening_ports.address_ - Specific address for bind
* _platform_info.address_ - Relative address of firmware mapping
* _user_events.address_ - The Internet protocol address or family ID

*address_width* - keyword, text.text

* _cpu_info.address_width_ - The width of the CPU address bus.

*admindir* - keyword, text.text

* _deb_packages.admindir_ - libdpkg admindir. Defaults to /var/lib/dpkg

*algorithm* - keyword, text.text

* _authorized_keys.algorithm_ - Key type

*alias* - keyword, text.text

* _etc_protocols.alias_ - Protocol alias
* _time_machine_destinations.alias_ - Human readable name of drive

*aliases* - keyword, text.text

* _etc_services.aliases_ - Optional space separated list of other names for a service
* _lxd_images.aliases_ - Comma-separated list of image aliases

*allow_maximum* - keyword, number.long

* _shared_resources.allow_maximum_ - Number of concurrent users for this resource has been limited. If True, the value in the MaximumAllowed property is ignored.

*allow_root* - keyword, text.text

* _authorizations.allow_root_ - Label top-level key

*allow_signed_enabled* - keyword, number.long

* _alf.allow_signed_enabled_ - 1 If allow signed mode is enabled else 0

*ambient_brightness_enabled* - keyword, text.text

* _connected_displays.ambient_brightness_enabled_ - The ambient brightness setting associated with the display. This will be 1 if enabled and is 0 if disabled or not supported.

*ami_id* - keyword, text.text

* _ec2_instance_metadata.ami_id_ - AMI ID used to launch this EC2 instance

*amperage* - keyword, number.long

* _battery.amperage_ - The current amperage in/out of the battery in mA (positive means charging, negative means discharging)

*anonymous* - keyword, number.long

* _virtual_memory_info.anonymous_ - Total number of anonymous pages.

*antispyware* - keyword, text.text

* _windows_security_center.antispyware_ - Deprecated (always 'Good').

*antivirus* - keyword, text.text

* _windows_security_center.antivirus_ - The health of the monitored Antivirus solution (see windows_security_products)

*api_version* - keyword, text.text

* _docker_version.api_version_ - API version

*app_name* - keyword, text.text

* _windows_firewall_rules.app_name_ - Friendly name of the application to which the rule applies

*apparmor* - keyword, text.text

* _apparmor_events.apparmor_ - Apparmor Status like ALLOWED, DENIED etc.

*applescript_enabled* - keyword, text.text

* _apps.applescript_enabled_ - Info properties NSAppleScriptEnabled label

*application* - keyword, text.text

* _office_mru.application_ - Associated Office application

*arch* - keyword, text.text

* _deb_packages.arch_ - Package architecture
* _docker_version.arch_ - Hardware architecture
* _os_version.arch_ - OS Architecture
* _rpm_packages.arch_ - Architecture(s) supported
* _seccomp_events.arch_ - Information about the CPU architecture
* _signature.arch_ - If applicable, the arch of the signed code

*architecture* - keyword, text.text

* _docker_info.architecture_ - Hardware architecture
* _ec2_instance_metadata.architecture_ - Hardware architecture of this EC2 instance
* _lxd_images.architecture_ - Target architecture for the image
* _lxd_instances.architecture_ - Instance architecture

*architectures* - keyword, text.text

* _apt_sources.architectures_ - Repository architectures

*args* - keyword, text.text

* _startup_items.args_ - Arguments provided to startup executable

*arguments* - keyword, text.text

* _kernel_info.arguments_ - Kernel arguments

*array_handle* - keyword, text.text

* _memory_devices.array_handle_ - The memory array that the device is attached to

*assessments_enabled* - keyword, number.long

* _gatekeeper.assessments_enabled_ - 1 If a Gatekeeper is enabled else 0

*asset_tag* - keyword, text.text

* _memory_devices.asset_tag_ - Manufacturer specific asset tag of memory device

*atime* - keyword, number.long

* _device_file.atime_ - Last access time
* _file.atime_ - Last access time
* _file_events.atime_ - Last access time
* _process_events.atime_ - File last access in UNIX time
* _shared_memory.atime_ - Attached time

*attach* - keyword, text.text

* _apparmor_profiles.attach_ - Which executable(s) a profile will attach to.

*attached* - keyword, number.long

* _shared_memory.attached_ - Number of attached processes

*attributes* - keyword, text.text

* _file.attributes_ - File attrib string. See: https://ss64.com/nt/attrib.html

*audible_alarm* - keyword, text.text

* _chassis_info.audible_alarm_ - If TRUE, the frame is equipped with an audible alarm.

*audit_account_logon* - keyword, number.long

* _security_profile_info.audit_account_logon_ - Determines whether the operating system MUST audit each time this computer validates the credentials of an account

*audit_account_manage* - keyword, number.long

* _security_profile_info.audit_account_manage_ - Determines whether the operating system MUST audit each event of account management on a computer

*audit_ds_access* - keyword, number.long

* _security_profile_info.audit_ds_access_ - Determines whether the operating system MUST audit each instance of user attempts to access an Active Directory object that has its own system access control list (SACL) specified

*audit_logon_events* - keyword, number.long

* _security_profile_info.audit_logon_events_ - Determines whether the operating system MUST audit each instance of a user attempt to log on or log off this computer

*audit_object_access* - keyword, number.long

* _security_profile_info.audit_object_access_ - Determines whether the operating system MUST audit each instance of user attempts to access a non-Active Directory object that has its own SACL specified

*audit_policy_change* - keyword, number.long

* _security_profile_info.audit_policy_change_ - Determines whether the operating system MUST audit each instance of user attempts to change user rights assignment policy, audit policy, account policy, or trust policy

*audit_privilege_use* - keyword, number.long

* _security_profile_info.audit_privilege_use_ - Determines whether the operating system MUST audit each instance of user attempts to exercise a user right

*audit_process_tracking* - keyword, number.long

* _security_profile_info.audit_process_tracking_ - Determines whether the operating system MUST audit process-related events

*audit_system_events* - keyword, number.long

* _security_profile_info.audit_system_events_ - Determines whether the operating system MUST audit System Change, System Startup, System Shutdown, Authentication Component Load, and Loss or Excess of Security events

*auid* - keyword

* _process_events.auid_ - Audit User ID at process start
* _process_file_events.auid_ - Audit user ID of the process using the file
* _seccomp_events.auid_ - Audit user ID (loginuid) of the user who started the analyzed process
* _socket_events.auid_ - Audit User ID
* _user_events.auid_ - Audit User ID

*authenticate_user* - keyword, text.text

* _authorizations.authenticate_user_ - Label top-level key

*authentication_package* - keyword, text.text

* _logon_sessions.authentication_package_ - The authentication package used to authenticate the owner of the logon session.

*author* - keyword, text.text

* _chocolatey_packages.author_ - Optional package author
* _chrome_extensions.author_ - Optional extension author
* _npm_packages.author_ - Package-supplied author
* _python_packages.author_ - Optional package author
* _safari_extensions.author_ - Optional extension author

*authority* - keyword, text.text

* _signature.authority_ - Certificate Common Name

*authority_key_id* - keyword, text.text

* _certificates.authority_key_id_ - AKID an optionally included SHA1

*authority_key_identifier* - keyword, text.text

* _curl_certificate.authority_key_identifier_ - Authority Key Identifier

*authorizations* - keyword, text.text

* _keychain_acls.authorizations_ - A space delimited set of authorization attributes

*auto_join* - keyword, number.long

* _wifi_networks.auto_join_ - 1 if this network set to join automatically, 0 otherwise

*auto_login* - keyword, number.long

* _wifi_networks.auto_login_ - 1 if auto login is enabled, 0 otherwise

*auto_update* - keyword, number.long

* _lxd_images.auto_update_ - Whether the image auto-updates (1) or not (0)

*autoupdate* - keyword

* _firefox_addons.autoupdate_ - 1 If the addon applies background updates else 0
* _windows_security_center.autoupdate_ - The health of the Windows Autoupdate feature

*availability* - keyword, text.text

* _cpu_info.availability_ - The availability and status of the CPU.

*availability_zone* - keyword, text.text

* _ec2_instance_metadata.availability_zone_ - Availability zone in which this instance launched

*average* - keyword, text.text

* _load_average.average_ - Load average over the specified period.

*average_memory* - keyword, number.long

* _osquery_schedule.average_memory_ - Average of the bytes of resident memory left allocated after collecting results

*avg_disk_bytes_per_read* - keyword, number.long

* _physical_disk_performance.avg_disk_bytes_per_read_ - Average number of bytes transferred from the disk during read operations

*avg_disk_bytes_per_write* - keyword, number.long

* _physical_disk_performance.avg_disk_bytes_per_write_ - Average number of bytes transferred to the disk during write operations

*avg_disk_read_queue_length* - keyword, number.long

* _physical_disk_performance.avg_disk_read_queue_length_ - Average number of read requests that were queued for the selected disk during the sample interval

*avg_disk_sec_per_read* - keyword, number.long

* _physical_disk_performance.avg_disk_sec_per_read_ - Average time, in seconds, of a read operation of data from the disk

*avg_disk_sec_per_write* - keyword, number.long

* _physical_disk_performance.avg_disk_sec_per_write_ - Average time, in seconds, of a write operation of data to the disk

*avg_disk_write_queue_length* - keyword, number.long

* _physical_disk_performance.avg_disk_write_queue_length_ - Average number of write requests that were queued for the selected disk during the sample interval

*backup_date* - keyword, number.long

* _time_machine_backups.backup_date_ - Backup Date

*bank_locator* - keyword, text.text

* _memory_devices.bank_locator_ - String number of the string that identifies the physically-labeled bank where the memory device is located

*base64* - keyword, number.long

* _extended_attributes.base64_ - 1 if the value is base64 encoded else 0

*base_image* - keyword, text.text

* _lxd_instances.base_image_ - ID of image used to launch this instance

*base_uri* - keyword, text.text

* _apt_sources.base_uri_ - Repository base URI

*baseurl* - keyword, text.text

* _yum_sources.baseurl_ - Repository base URL

*basic_constraint* - keyword, text.text

* _curl_certificate.basic_constraint_ - Basic Constraints

*binary_queue* - keyword, number.long

* _carbon_black_info.binary_queue_ - Size in bytes of binaries waiting to be sent to Carbon Black server

*bitmap_chunk_size* - keyword, text.text

* _md_devices.bitmap_chunk_size_ - Bitmap chunk size

*bitmap_external_file* - keyword, text.text

* _md_devices.bitmap_external_file_ - External referenced bitmap file

*bitmap_on_mem* - keyword, text.text

* _md_devices.bitmap_on_mem_ - Pages allocated in in-memory bitmap, if enabled

*block* - keyword, text.text

* _ssh_configs.block_ - The host or match block

*block_size* - keyword, number.long

* _block_devices.block_size_ - Block size in bytes
* _device_file.block_size_ - Block size of filesystem
* _file.block_size_ - Block size of filesystem

*blocks* - keyword, number.long

* _device_partitions.blocks_ - Number of blocks
* _mounts.blocks_ - Mounted device used blocks

*blocks_available* - keyword, number.long

* _mounts.blocks_available_ - Mounted device available blocks

*blocks_free* - keyword, number.long

* _mounts.blocks_free_ - Mounted device free blocks

*blocks_size* - keyword, number.long

* _device_partitions.blocks_size_ - Byte size of each block
* _mounts.blocks_size_ - Block size in bytes

*bluetooth_sharing* - keyword, number.long

* _sharing_preferences.bluetooth_sharing_ - 1 If bluetooth sharing is enabled for any user else 0

*board_model* - keyword, text.text

* _system_info.board_model_ - Board model

*board_serial* - keyword, text.text

* _system_info.board_serial_ - Board serial number

*board_vendor* - keyword, text.text

* _system_info.board_vendor_ - Board vendor

*board_version* - keyword, text.text

* _system_info.board_version_ - Board version

*boot_partition* - keyword, number.long

* _logical_drives.boot_partition_ - True if Windows booted from this drive.

*boot_uuid* - keyword, text.text

* _ibridge_info.boot_uuid_ - Boot UUID of the iBridge controller

*bp_microcode_disabled* - keyword, number.long

* _kva_speculative_info.bp_microcode_disabled_ - Branch Predictions are disabled due to lack of microcode update.

*bp_mitigations* - keyword, number.long

* _kva_speculative_info.bp_mitigations_ - Branch Prediction mitigations are enabled.

*bp_system_pol_disabled* - keyword, number.long

* _kva_speculative_info.bp_system_pol_disabled_ - Branch Predictions are disabled via system policy.

*breach_description* - keyword, text.text

* _chassis_info.breach_description_ - If provided, gives a more detailed description of a detected security breach.

*bridge_nf_ip6tables* - keyword, number.long

* _docker_info.bridge_nf_ip6tables_ - 1 if bridge netfilter ip6tables is enabled. 0 otherwise

*bridge_nf_iptables* - keyword, number.long

* _docker_info.bridge_nf_iptables_ - 1 if bridge netfilter iptables is enabled. 0 otherwise

*broadcast* - keyword, text.text

* _interface_addresses.broadcast_ - Broadcast address for the interface

*browser_type* - keyword, text.text

* _chrome_extension_content_scripts.browser_type_ - The browser type (Valid values: chrome, chromium, opera, yandex, brave)
* _chrome_extensions.browser_type_ - The browser type (Valid values: chrome, chromium, opera, yandex, brave, edge, edge_beta)

*bsd_flags* - keyword, text.text

* _file.bsd_flags_ - The BSD file flags (chflags). Possible values: NODUMP, UF_IMMUTABLE, UF_APPEND, OPAQUE, HIDDEN, ARCHIVED, SF_IMMUTABLE, SF_APPEND

*bssid* - keyword, text.text

* _wifi_status.bssid_ - The current basic service set identifier
* _wifi_survey.bssid_ - The current basic service set identifier

*btime* - keyword, number.long

* _file.btime_ - (B)irth or (cr)eate time
* _process_events.btime_ - File creation in UNIX time

*buffers* - keyword, number.long

* _memory_info.buffers_ - The amount of physical RAM, in bytes, used for file buffers

*build* - keyword, text.text

* _os_version.build_ - Optional build-specific or variant string

*build_distro* - keyword, text.text

* _osquery_info.build_distro_ - osquery toolkit platform distribution name (os version)

*build_id* - keyword, text.text

* _sandboxes.build_id_ - Sandbox-specific identifier

*build_number* - keyword, number.long

* _windows_crashes.build_number_ - Windows build number of the crashing machine

*build_platform* - keyword, text.text

* _osquery_info.build_platform_ - osquery toolkit build platform

*build_time* - keyword, text.text

* _docker_version.build_time_ - Build time
* _portage_packages.build_time_ - Unix time when package was built

*bundle_executable* - keyword, text.text

* _apps.bundle_executable_ - Info properties CFBundleExecutable label

*bundle_identifier* - keyword, text.text

* _apps.bundle_identifier_ - Info properties CFBundleIdentifier label
* _running_apps.bundle_identifier_ - The bundle identifier of the application

*bundle_name* - keyword, text.text

* _apps.bundle_name_ - Info properties CFBundleName label

*bundle_package_type* - keyword, text.text

* _apps.bundle_package_type_ - Info properties CFBundlePackageType label

*bundle_path* - keyword, text.text

* _sandboxes.bundle_path_ - Application bundle used by the sandbox
* _system_extensions.bundle_path_ - System extension bundle path

*bundle_short_version* - keyword, text.text

* _apps.bundle_short_version_ - Info properties CFBundleShortVersionString label

*bundle_version* - keyword, text.text

* _apps.bundle_version_ - Info properties CFBundleVersion label
* _safari_extensions.bundle_version_ - The version of the build that identifies an iteration of the bundle

*busy_state* - keyword, number.long

* _iokit_devicetree.busy_state_ - 1 if the device is in a busy state else 0
* _iokit_registry.busy_state_ - 1 if the node is in a busy state else 0

*bytes* - keyword, number.long

* _curl.bytes_ - Number of bytes in the response
* _iptables.bytes_ - Number of matching bytes for this rule.

*bytes_available* - keyword, number.long

* _time_machine_destinations.bytes_available_ - Bytes available on volume

*bytes_received* - keyword, number.long

* _lxd_networks.bytes_received_ - Number of bytes received on this network

*bytes_sent* - keyword, number.long

* _lxd_networks.bytes_sent_ - Number of bytes sent on this network

*bytes_used* - keyword, number.long

* _time_machine_destinations.bytes_used_ - Bytes used on volume

*ca* - keyword, number.long

* _certificates.ca_ - 1 if CA: true (certificate is an authority) else 0

*cache_path* - keyword, text.text

* _quicklook_cache.cache_path_ - Path to cache data

*cached* - keyword, number.long

* _lxd_images.cached_ - Whether image is cached (1) or not (0)
* _memory_info.cached_ - The amount of physical RAM, in bytes, used as cache memory

*capability* - keyword, number.long

* _apparmor_events.capability_ - Capability number

*capname* - keyword, text.text

* _apparmor_events.capname_ - Capability requested by the process

*caption* - keyword, text.text

* _patches.caption_ - Short description of the patch.
* _windows_optional_features.caption_ - Caption of feature in settings UI

*captive_login_date* - keyword, number.long

* _wifi_networks.captive_login_date_ - Time this network logged in to a captive portal as unix_time

*captive_portal* - keyword, number.long

* _wifi_networks.captive_portal_ - 1 if this network has a captive portal, 0 otherwise

*carve* - keyword, number.long

* _carves.carve_ - Set this value to '1' to start a file carve

*carve_guid* - keyword, text.text

* _carves.carve_guid_ - Identifying value of the carve session

*category* - keyword, text.text

* _apps.category_ - The UTI that categorizes the app for the App Store
* _file_events.category_ - The category of the file defined in the config
* _ntfs_journal_events.category_ - The category that the event originated from
* _power_sensors.category_ - The sensor category: currents, voltage, wattage
* _system_extensions.category_ - System extension category
* _unified_log.category_ - the category of the os_log_t used
* _yara_events.category_ - The category of the file

*cdhash* - keyword, text.text

* _es_process_events.cdhash_ - Codesigning hash of the process
* _signature.cdhash_ - Hash of the application Code Directory

*celsius* - keyword, number.double

* _temperature_sensors.celsius_ - Temperature in Celsius

*certificate* - keyword, text.text

* _lxd_certificates.certificate_ - Certificate content

*cgroup_driver* - keyword, text.text

* _docker_info.cgroup_driver_ - Control groups driver

*cgroup_namespace* - keyword, text.text

* _docker_containers.cgroup_namespace_ - cgroup namespace
* _process_namespaces.cgroup_namespace_ - cgroup namespace inode

*cgroup_path* - keyword, text.text

* _processes.cgroup_path_ - The full hierarchical path of the process's control group

*chain* - keyword, text.text

* _iptables.chain_ - Size of module content.

*change_type* - keyword, text.text

* _docker_container_fs_changes.change_type_ - Type of change: C:Modified, A:Added, D:Deleted

*channel* - keyword

* _wifi_status.channel_ - Channel number
* _wifi_survey.channel_ - Channel number
* _windows_eventlog.channel_ - Source or channel of the event

*channel_band* - keyword, number.long

* _wifi_status.channel_band_ - Channel band
* _wifi_survey.channel_band_ - Channel band

*channel_width* - keyword, number.long

* _wifi_status.channel_width_ - Channel width
* _wifi_survey.channel_width_ - Channel width

*charged* - keyword, number.long

* _battery.charged_ - 1 if the battery is currently completely charged. 0 otherwise

*charging* - keyword, number.long

* _battery.charging_ - 1 if the battery is currently being charged by a power source. 0 otherwise

*chassis_types* - keyword, text.text

* _chassis_info.chassis_types_ - A comma-separated list of chassis types, such as Desktop or Laptop.

*check_array_finish* - keyword, text.text

* _md_devices.check_array_finish_ - Estimated duration of the check array activity

*check_array_progress* - keyword, text.text

* _md_devices.check_array_progress_ - Progress of the check array activity

*check_array_speed* - keyword, text.text

* _md_devices.check_array_speed_ - Speed of the check array activity

*checksum* - keyword, text.text

* _disk_events.checksum_ - UDIF Master checksum if available (CRC32)

*chemistry* - keyword, text.text

* _battery.chemistry_ - The battery chemistry type (eg. LiP). Some possible values are documented in https://learn.microsoft.com/en-us/windows/win32/power/battery-information-str.

*child_pid* - keyword, number.long

* _es_process_events.child_pid_ - Process ID of a child process in case of a fork event

*chunk_size* - keyword, number.long

* _md_devices.chunk_size_ - chunk size in bytes

*cid* - keyword, number.long

* _bpf_process_events.cid_ - Cgroup ID
* _bpf_socket_events.cid_ - Cgroup ID

*class* - keyword, text.text

* _authorizations.class_ - Label top-level key
* _drivers.class_ - Device/driver class name
* _iokit_devicetree.class_ - Best matching device class (most-specific category)
* _iokit_registry.class_ - Best matching device class (most-specific category)
* _usb_devices.class_ - USB Device class
* _wmi_cli_event_consumers.class_ - The name of the class.
* _wmi_event_filters.class_ - The name of the class.
* _wmi_filter_consumer_binding.class_ - The name of the class.
* _wmi_script_event_consumers.class_ - The name of the class.

*clear_text_password* - keyword, number.long

* _security_profile_info.clear_text_password_ - Determines whether passwords MUST be stored by using reversible encryption

*client_app_id* - keyword, text.text

* _windows_update_history.client_app_id_ - Identifier of the client application that processed an update

*client_site_name* - keyword, text.text

* _ntdomains.client_site_name_ - The name of the site where the domain controller is configured.

*cloud_id* - keyword, text.text

* _ycloud_instance_metadata.cloud_id_ - Cloud identifier for the VM

*cmdline* - keyword, text.text

* _bpf_process_events.cmdline_ - Command line arguments
* _docker_container_processes.cmdline_ - Complete argv
* _es_process_events.cmdline_ - Command line arguments (argv)
* _process_etw_events.cmdline_ - Command Line
* _process_events.cmdline_ - Command line arguments (argv)
* _processes.cmdline_ - Complete argv

*cmdline_count* - keyword, number.long

* _es_process_events.cmdline_count_ - Number of command line arguments

*cmdline_size* - keyword, number.long

* _process_events.cmdline_size_ - Actual size (bytes) of command line arguments

*code* - keyword, text.text

* _seccomp_events.code_ - The seccomp action

*code_integrity_policy_enforcement_status* - keyword, text.text

* _hvci_status.code_integrity_policy_enforcement_status_ - The status of the code integrity policy enforcement settings. Returns UNKNOWN if an error is encountered.

*codename* - keyword, text.text

* _os_version.codename_ - OS version codename

*codesigning_flags* - keyword, text.text

* _es_process_events.codesigning_flags_ - Codesigning flags matching one of these options, in a comma separated list: NOT_VALID, ADHOC, NOT_RUNTIME, INSTALLER. See kern/cs_blobs.h in XNU for descriptions.

*collect_cross_processes* - keyword, number.long

* _carbon_black_info.collect_cross_processes_ - If the sensor is configured to cross process events

*collect_data_file_writes* - keyword, number.long

* _carbon_black_info.collect_data_file_writes_ - If the sensor is configured to collect non binary file writes

*collect_emet_events* - keyword, number.long

* _carbon_black_info.collect_emet_events_ - If the sensor is configured to EMET events

*collect_file_mods* - keyword, number.long

* _carbon_black_info.collect_file_mods_ - If the sensor is configured to collect file modification events

*collect_module_info* - keyword, number.long

* _carbon_black_info.collect_module_info_ - If the sensor is configured to collect metadata of binaries

*collect_module_loads* - keyword, number.long

* _carbon_black_info.collect_module_loads_ - If the sensor is configured to capture module loads

*collect_net_conns* - keyword, number.long

* _carbon_black_info.collect_net_conns_ - If the sensor is configured to collect network connections

*collect_process_user_context* - keyword, number.long

* _carbon_black_info.collect_process_user_context_ - If the sensor is configured to collect the user running a process

*collect_processes* - keyword, number.long

* _carbon_black_info.collect_processes_ - If the sensor is configured to process events

*collect_reg_mods* - keyword, number.long

* _carbon_black_info.collect_reg_mods_ - If the sensor is configured to collect registry modification events

*collect_sensor_operations* - keyword, number.long

* _carbon_black_info.collect_sensor_operations_ - Unknown

*collect_store_files* - keyword, number.long

* _carbon_black_info.collect_store_files_ - If the sensor is configured to send back binaries to the Carbon Black server

*collisions* - keyword, number.long

* _interface_details.collisions_ - Packet Collisions detected

*color_depth* - keyword, number.long

* _video_info.color_depth_ - The amount of bits per pixel to represent color.

*comm* - keyword, text.text

* _apparmor_events.comm_ - Command-line name of the command that was used to invoke the analyzed process
* _seccomp_events.comm_ - Command-line name of the command that was used to invoke the analyzed process

*command* - keyword, text.text

* _crontab.command_ - Raw command string
* _docker_containers.command_ - Command with arguments
* _shell_history.command_ - Unparsed date/line/command history line

*command_line* - keyword, text.text

* _windows_crashes.command_line_ - Command-line string passed to the crashed process

*command_line_template* - keyword, text.text

* _wmi_cli_event_consumers.command_line_template_ - Standard string template that specifies the process to be started. This property can be NULL, and the ExecutablePath property is used as the command line.

*comment* - keyword, text.text

* _authorizations.comment_ - Label top-level key
* _authorized_keys.comment_ - Optional comment
* _docker_image_history.comment_ - Instruction comment
* _etc_protocols.comment_ - Comment with protocol description
* _etc_services.comment_ - Optional comment for a service.
* _groups.comment_ - Remarks or comments associated with the group
* _keychain_items.comment_ - Optional keychain comment

*common_name* - keyword, text.text

* _certificates.common_name_ - Certificate CommonName
* _curl_certificate.common_name_ - Common name of company issued to

*compat* - keyword, number.long

* _seccomp_events.compat_ - Is system call in compatibility mode

*compiler* - keyword, text.text

* _apps.compiler_ - Info properties DTCompiler label

*completed_time* - keyword, number.long

* _cups_jobs.completed_time_ - When the job completed printing

*components* - keyword, text.text

* _apt_sources.components_ - Repository components

*compressed* - keyword, number.long

* _virtual_memory_info.compressed_ - The total number of pages that have been compressed by the VM compressor.

*compressor* - keyword, number.long

* _virtual_memory_info.compressor_ - The number of pages used to store compressed VM pages.

*computer_name* - keyword, text.text

* _system_info.computer_name_ - Friendly computer name (optional)
* _windows_eventlog.computer_name_ - Hostname of system where event was generated
* _windows_events.computer_name_ - Hostname of system where event was generated

*condition* - keyword, text.text

* _battery.condition_ - One of the following: "Normal" indicates the condition of the battery is within normal tolerances, "Service Needed" indicates that the battery should be checked out by a licensed Mac repair service, "Permanent Failure" indicates the battery needs replacement

*config_entrypoint* - keyword, text.text

* _docker_containers.config_entrypoint_ - Container entrypoint(s)

*config_flag* - keyword, text.text

* _sip_config.config_flag_ - The System Integrity Protection config flag

*config_hash* - keyword, text.text

* _osquery_info.config_hash_ - Hash of the working configuration state

*config_name* - keyword, text.text

* _carbon_black_info.config_name_ - Sensor group

*config_valid* - keyword, number.long

* _osquery_info.config_valid_ - 1 if the config was loaded and considered valid, else 0

*config_value* - keyword, text.text

* _system_controls.config_value_ - The MIB value set in /etc/sysctl.conf

*configured_clock_speed* - keyword, number.long

* _memory_devices.configured_clock_speed_ - Configured speed of memory device in megatransfers per second (MT/s)

*configured_voltage* - keyword, number.long

* _memory_devices.configured_voltage_ - Configured operating voltage of device in millivolts

*connection_id* - keyword, text.text

* _interface_details.connection_id_ - Name of the network connection as it appears in the Network Connections Control Panel program.

*connection_status* - keyword, text.text

* _interface_details.connection_status_ - State of the network adapter connection to the network.

*connection_type* - keyword, text.text

* _connected_displays.connection_type_ - The connection type associated with the display.

*consistency_scan_date* - keyword, number.long

* _time_machine_destinations.consistency_scan_date_ - Consistency scan date

*consumer* - keyword, text.text

* _wmi_filter_consumer_binding.consumer_ - Reference to an instance of __EventConsumer that represents the object path to a logical consumer, the recipient of an event.

*containers* - keyword, number.long

* _docker_info.containers_ - Total number of containers

*containers_paused* - keyword, number.long

* _docker_info.containers_paused_ - Number of containers in paused state

*containers_running* - keyword, number.long

* _docker_info.containers_running_ - Number of containers currently running

*containers_stopped* - keyword, number.long

* _docker_info.containers_stopped_ - Number of containers in stopped state

*content* - keyword, text.text

* _disk_events.content_ - Disk event content

*content_caching* - keyword, number.long

* _sharing_preferences.content_caching_ - 1 If content caching is enabled else 0

*content_type* - keyword, text.text

* _package_install_history.content_type_ - Package content_type (optional)

*conversion_status* - keyword, number.long

* _bitlocker_info.conversion_status_ - The bitlocker conversion status of the drive.

*coprocessor_version* - keyword, text.text

* _ibridge_info.coprocessor_version_ - The manufacturer and chip version

*copy* - keyword, number.long

* _virtual_memory_info.copy_ - Total number of copy-on-write pages.

*copyright* - keyword, text.text

* _apps.copyright_ - Info properties NSHumanReadableCopyright label
* _safari_extensions.copyright_ - A human-readable copyright notice for the bundle

*core* - keyword, number.long

* _cpu_time.core_ - Name of the cpu (core)

*cosine_similarity* - keyword, number.double

* _powershell_events.cosine_similarity_ - How similar the Powershell script is to a provided 'normal' character frequency

*count* - keyword, number.long

* _userassist.count_ - Number of times the application has been executed.
* _yara.count_ - Number of YARA matches
* _yara_events.count_ - Number of YARA matches

*country_code* - keyword, text.text

* _wifi_status.country_code_ - The country code (ISO/IEC 3166-1:1997) for the network
* _wifi_survey.country_code_ - The country code (ISO/IEC 3166-1:1997) for the network

*cpu* - keyword, number.double

* _docker_container_processes.cpu_ - CPU utilization as percentage

*cpu_brand* - keyword, text.text

* _system_info.cpu_brand_ - CPU brand string, contains vendor and model

*cpu_cfs_period* - keyword, number.long

* _docker_info.cpu_cfs_period_ - 1 if CPU Completely Fair Scheduler (CFS) period support is enabled. 0 otherwise

*cpu_cfs_quota* - keyword, number.long

* _docker_info.cpu_cfs_quota_ - 1 if CPU Completely Fair Scheduler (CFS) quota support is enabled. 0 otherwise

*cpu_kernelmode_usage* - keyword, number.long

* _docker_container_stats.cpu_kernelmode_usage_ - CPU kernel mode usage

*cpu_logical_cores* - keyword, number.long

* _system_info.cpu_logical_cores_ - Number of logical CPU cores available to the system

*cpu_microcode* - keyword, text.text

* _system_info.cpu_microcode_ - Microcode version

*cpu_physical_cores* - keyword, number.long

* _system_info.cpu_physical_cores_ - Number of physical CPU cores in to the system

*cpu_pred_cmd_supported* - keyword, number.long

* _kva_speculative_info.cpu_pred_cmd_supported_ - PRED_CMD MSR supported by CPU Microcode.

*cpu_set* - keyword, number.long

* _docker_info.cpu_set_ - 1 if CPU set selection support is enabled. 0 otherwise

*cpu_shares* - keyword, number.long

* _docker_info.cpu_shares_ - 1 if CPU share weighting support is enabled. 0 otherwise

*cpu_sockets* - keyword, number.long

* _system_info.cpu_sockets_ - Number of processor sockets in the system

*cpu_spec_ctrl_supported* - keyword, number.long

* _kva_speculative_info.cpu_spec_ctrl_supported_ - SPEC_CTRL MSR supported by CPU Microcode.

*cpu_status* - keyword, number.long

* _cpu_info.cpu_status_ - The current operating status of the CPU.

*cpu_subtype* - keyword

* _processes.cpu_subtype_ - Indicates the specific processor on which an entry may be used.
* _system_info.cpu_subtype_ - CPU subtype

*cpu_total_usage* - keyword, number.long

* _docker_container_stats.cpu_total_usage_ - Total CPU usage

*cpu_type* - keyword

* _processes.cpu_type_ - Indicates the specific processor designed for installation.
* _system_info.cpu_type_ - CPU type

*cpu_usermode_usage* - keyword, number.long

* _docker_container_stats.cpu_usermode_usage_ - CPU user mode usage

*cpus* - keyword, number.long

* _docker_info.cpus_ - Number of CPUs

*crash_path* - keyword, text.text

* _crashes.crash_path_ - Location of log file
* _windows_crashes.crash_path_ - Path of the log file

*crashed_thread* - keyword, number.long

* _crashes.crashed_thread_ - Thread ID which crashed

*created* - keyword, text.text

* _authorizations.created_ - Label top-level key
* _docker_containers.created_ - Time of creation as UNIX time
* _docker_image_history.created_ - Time of creation as UNIX time
* _docker_images.created_ - Time of creation as UNIX time
* _docker_networks.created_ - Time of creation as UNIX time
* _keychain_items.created_ - Date item was created

*created_at* - keyword, text.text

* _lxd_images.created_at_ - ISO time of image creation
* _lxd_instances.created_at_ - ISO time of creation

*created_by* - keyword, text.text

* _docker_image_history.created_by_ - Created by instruction

*created_time* - keyword, number.long

* _shellbags.created_time_ - Directory Created time.

*creation_time* - keyword

* _account_policy_data.creation_time_ - When the account was first created
* _cups_jobs.creation_time_ - When the print request was initiated

*creator* - keyword, text.text

* _firefox_addons.creator_ - Addon-supported creator string

*creator_pid* - keyword, number.long

* _shared_memory.creator_pid_ - Process ID that created the segment
