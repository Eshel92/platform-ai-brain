<!-- Part 4 of 6 of osquery/exported-fields-reference.md (split because the page is big). -->

* _hash.mount_namespace_id_ - Mount namespace id
* _npm_packages.mount_namespace_id_ - Mount namespace id
* _os_version.mount_namespace_id_ - Mount namespace id
* _rpm_packages.mount_namespace_id_ - Mount namespace id

*mount_point* - keyword, text.text

* _docker_volumes.mount_point_ - Mount point

*mountable* - keyword, number.long

* _disk_events.mountable_ - 1 if mountable, 0 if not

*mtime* - keyword

* _device_file.mtime_ - Last modification time
* _file.mtime_ - Last modification time
* _file_events.mtime_ - Last modification time
* _gatekeeper_approved_apps.mtime_ - Last modification time
* _process_events.mtime_ - File modification in UNIX time
* _quicklook_cache.mtime_ - Parsed version date field
* _registry.mtime_ - timestamp of the most recent registry write

*mtu* - keyword, number.long

* _interface_details.mtu_ - Network MTU
* _lxd_networks.mtu_ - MTU size
* _routes.mtu_ - Maximum Transmission Unit for the route

*name* - keyword, text.text

* _acpi_tables.name_ - ACPI table name
* _ad_config.name_ - The macOS-specific configuration name
* _apparmor_events.name_ - Process name
* _apparmor_profiles.name_ - Policy name.
* _apps.name_ - Name of the Name.app folder
* _apt_sources.name_ - Repository name
* _autoexec.name_ - Name of the program
* _azure_instance_metadata.name_ - Name of the VM
* _block_devices.name_ - Block device name
* _browser_plugins.name_ - Plugin display name
* _chocolatey_packages.name_ - Package display name
* _chrome_extensions.name_ - Extension display name
* _connected_displays.name_ - The name of the display.
* _cups_destinations.name_ - Name of the printer
* _deb_packages.name_ - Package name
* _disk_encryption.name_ - Disk name
* _disk_events.name_ - Disk event name
* _disk_info.name_ - The label of the disk object.
* _dns_cache.name_ - DNS record name
* _docker_container_mounts.name_ - Optional mount name
* _docker_container_networks.name_ - Network name
* _docker_container_processes.name_ - The process path or shorthand argv[0]
* _docker_container_stats.name_ - Container name
* _docker_containers.name_ - Container name
* _docker_info.name_ - Name of the docker host
* _docker_networks.name_ - Network name
* _docker_volume_labels.name_ - Volume name
* _docker_volumes.name_ - Volume name
* _etc_protocols.name_ - Protocol name
* _etc_services.name_ - Service name
* _fan_speed_sensors.name_ - Fan name
* _firefox_addons.name_ - Addon display name
* _homebrew_packages.name_ - Package name
* _ie_extensions.name_ - Extension display name
* _iokit_devicetree.name_ - Device node name
* _iokit_registry.name_ - Default name of the node
* _kernel_extensions.name_ - Extension label
* _kernel_modules.name_ - Module name
* _kernel_panics.name_ - Process name corresponding to crashed thread
* _launchd.name_ - File name of plist (used by launchd)
* _lxd_certificates.name_ - Name of the certificate
* _lxd_instance_config.name_ - Instance name
* _lxd_instance_devices.name_ - Instance name
* _lxd_instances.name_ - Instance name
* _lxd_networks.name_ - Name of the network
* _lxd_storage_pools.name_ - Name of the storage pool
* _managed_policies.name_ - Policy key name
* _md_personalities.name_ - Name of personality supported by kernel
* _memory_map.name_ - Region name
* _npm_packages.name_ - Package display name
* _ntdomains.name_ - The label by which the object is known.
* _nvram.name_ - Variable name
* _os_version.name_ - Distribution or product name
* _osquery_events.name_ - Event publisher or subscriber name
* _osquery_extensions.name_ - Extension's name
* _osquery_flags.name_ - Flag name
* _osquery_packs.name_ - The given name for this query pack
* _osquery_registry.name_ - Name of the plugin item
* _osquery_schedule.name_ - The given name for this query
* _package_install_history.name_ - Package display name
* _physical_disk_performance.name_ - Name of the physical disk
* _pipes.name_ - Name of the pipe
* _power_sensors.name_ - Name of power source
* _processes.name_ - The process path or shorthand argv[0]
* _programs.name_ - Commonly used product name.
* _python_packages.name_ - Package display name
* _registry.name_ - Name of the registry value entry
* _rpm_packages.name_ - RPM package name
* _safari_extensions.name_ - Extension display name
* _scheduled_tasks.name_ - Name of the scheduled task
* _services.name_ - Service name
* _shared_folders.name_ - The shared name of the folder as it appears to other users
* _shared_resources.name_ - Alias given to a path set up as a share on a computer system running Windows.
* _startup_items.name_ - Name of startup item
* _system_controls.name_ - Full sysctl MIB name
* _temperature_sensors.name_ - Name of temperature source
* _vscode_extensions.name_ - Extension Name
* _windows_firewall_rules.name_ - Friendly name of the rule
* _windows_optional_features.name_ - Name of the feature
* _windows_search.name_ - The name of the item
* _windows_security_products.name_ - Name of product
* _wmi_bios_info.name_ - Name of the Bios setting
* _wmi_cli_event_consumers.name_ - Unique name of a consumer.
* _wmi_event_filters.name_ - Unique identifier of an event filter.
* _wmi_script_event_consumers.name_ - Unique identifier for the event consumer. 
* _xprotect_entries.name_ - Description of XProtected malware
* _xprotect_reports.name_ - Description of XProtected malware
* _ycloud_instance_metadata.name_ - Name of the VM
* _yum_sources.name_ - Repository name

*name_constraints* - keyword, text.text

* _curl_certificate.name_constraints_ - Name Constraints

*namespace* - keyword, text.text

* _apparmor_events.namespace_ - AppArmor namespace

*native* - keyword, number.long

* _browser_plugins.native_ - Plugin requires native execution

*net_namespace* - keyword, text.text

* _docker_containers.net_namespace_ - Network namespace
* _listening_ports.net_namespace_ - The inode number of the network namespace
* _process_namespaces.net_namespace_ - net namespace inode
* _process_open_sockets.net_namespace_ - The inode number of the network namespace

*netmask* - keyword, text.text

* _dns_resolvers.netmask_ - Address (sortlist) netmask length
* _routes.netmask_ - Netmask length

*network_id* - keyword, text.text

* _docker_container_networks.network_id_ - Network ID

*network_name* - keyword, text.text

* _wifi_networks.network_name_ - Name of the network
* _wifi_status.network_name_ - Name of the network
* _wifi_survey.network_name_ - Name of the network

*network_rx_bytes* - keyword, number.long

* _docker_container_stats.network_rx_bytes_ - Total network bytes read

*network_tx_bytes* - keyword, number.long

* _docker_container_stats.network_tx_bytes_ - Total network bytes transmitted

*new_administrator_name* - keyword, text.text

* _security_profile_info.new_administrator_name_ - Determines the name of the Administrator account on the local computer

*new_guest_name* - keyword, text.text

* _security_profile_info.new_guest_name_ - Determines the name of the Guest account on the local computer

*next_run_time* - keyword, number.long

* _scheduled_tasks.next_run_time_ - Timestamp the task is scheduled to run next

*nice* - keyword, number.long

* _cpu_time.nice_ - Time spent in user mode with low priority (nice)
* _docker_container_processes.nice_ - Process nice level (-20 to 20, default 0)
* _processes.nice_ - Process nice level (-20 to 20, default 0)

*no_proxy* - keyword, text.text

* _docker_info.no_proxy_ - Comma-separated list of domain extensions proxy should not be used for

*node* - keyword, text.text

* _augeas.node_ - The node path of the configuration item

*node_ref_number* - keyword, text.text

* _ntfs_journal_events.node_ref_number_ - The ordinal that associates a journal record with a filename

*noise* - keyword, number.long

* _wifi_status.noise_ - The current noise measurement (dBm)
* _wifi_survey.noise_ - The current noise measurement (dBm)

*not_valid_after* - keyword, text.text

* _certificates.not_valid_after_ - Certificate expiration data

*not_valid_before* - keyword, text.text

* _certificates.not_valid_before_ - Lower bound of valid date

*nr_raid_disks* - keyword, number.long

* _md_devices.nr_raid_disks_ - Number of partitions or disk devices to comprise the array

*ntime* - keyword, text.text

* _bpf_process_events.ntime_ - The nsecs uptime timestamp as obtained from BPF
* _bpf_socket_events.ntime_ - The nsecs uptime timestamp as obtained from BPF

*num_procs* - keyword, number.long

* _docker_container_stats.num_procs_ - Number of processors

*number* - keyword, number.long

* _etc_protocols.number_ - Protocol number
* _oem_strings.number_ - The string index of the structure
* _smbios_tables.number_ - Table entry number

*number_memory_devices* - keyword, number.long

* _memory_arrays.number_memory_devices_ - Number of memory devices on array

*number_of_cores* - keyword, text.text

* _cpu_info.number_of_cores_ - The number of cores of the CPU.

*number_of_efficiency_cores* - keyword, number.long

* _cpu_info.number_of_efficiency_cores_ - The number of efficiency cores of the CPU. Only available on Apple Silicon

*number_of_performance_cores* - keyword, number.long

* _cpu_info.number_of_performance_cores_ - The number of performance cores of the CPU. Only available on Apple Silicon

*object_name* - keyword, text.text

* _winbaseobj.object_name_ - Object Name

*object_path* - keyword, text.text

* _systemd_units.object_path_ - The object path for this unit

*object_type* - keyword, text.text

* _winbaseobj.object_type_ - Object Type

*obytes* - keyword, number.long

* _interface_details.obytes_ - Output bytes

*odrops* - keyword, number.long

* _interface_details.odrops_ - Output drops

*oerrors* - keyword, number.long

* _interface_details.oerrors_ - Output errors

*offer* - keyword, text.text

* _azure_instance_metadata.offer_ - Offer information for the VM image (Azure image gallery VMs only)

*offset* - keyword, number.long

* _device_partitions.offset_ - Byte offset from the start of the volume
* _process_memory_map.offset_ - Offset into mapped path

*oid* - keyword, text.text

* _system_controls.oid_ - Control MIB

*old_path* - keyword, text.text

* _ntfs_journal_events.old_path_ - Old path (renames only)

*on_demand* - keyword, text.text

* _launchd.on_demand_ - Deprecated key, replaced by keep_alive

*on_disk* - keyword, number.long

* _processes.on_disk_ - The process path exists yes=1, no=0, unknown=-1

*online* - keyword, number.long

* _connected_displays.online_ - The online status of the display. This field is 1 if the display is online and 0 if it is offline.

*online_cpus* - keyword, number.long

* _docker_container_stats.online_cpus_ - Online CPUs

*oom_kill_disable* - keyword, number.long

* _docker_info.oom_kill_disable_ - 1 if Out-of-memory kill is disabled. 0 otherwise

*opackets* - keyword, number.long

* _interface_details.opackets_ - Output packets

*opaque_version* - keyword, text.text

* _gatekeeper.opaque_version_ - Version of Gatekeeper's gkopaque.bundle

*operation* - keyword, text.text

* _apparmor_events.operation_ - Permission requested by the process
* _process_file_events.operation_ - Operation type
* _windows_update_history.operation_ - Operation on an update

*option* - keyword, text.text

* _ad_config.option_ - Canonical name of option
* _ssh_configs.option_ - The option and value

*option_name* - keyword, text.text

* _cups_destinations.option_name_ - Option name

*option_value* - keyword, text.text

* _cups_destinations.option_value_ - Option value

*optional* - keyword, number.long

* _xprotect_entries.optional_ - Match any of the identities/patterns for this XProtect name

*optional_permissions* - keyword, text.text

* _chrome_extensions.optional_permissions_ - The permissions optionally required by the extensions

*optional_permissions_json* - keyword, text.text

* _chrome_extensions.optional_permissions_json_ - The JSON-encoded permissions optionally required by the extensions

*options* - keyword, text.text

* _authorized_keys.options_ - Optional list of login options
* _dns_resolvers.options_ - Resolver options
* _nfs_shares.options_ - Options string set on the export share

*organization* - keyword, text.text

* _curl_certificate.organization_ - Organization issued to

*organization_unit* - keyword, text.text

* _curl_certificate.organization_unit_ - Organization unit issued to

*original_filename* - keyword, text.text

* _file.original_filename_ - (Executable files only) Original filename

*original_parent* - keyword, number.long

* _es_process_events.original_parent_ - Original parent process ID in case of reparenting

*original_program_name* - keyword, text.text

* _authenticode.original_program_name_ - The original program name that the publisher has signed

*os* - keyword, text.text

* _docker_info.os_ - Operating system
* _docker_version.os_ - Operating system
* _lxd_images.os_ - OS on which image is based
* _lxd_instances.os_ - The OS of this instance

*os_type* - keyword, text.text

* _azure_instance_metadata.os_type_ - Linux or Windows
* _docker_info.os_type_ - Operating system type

*os_version* - keyword, text.text

* _kernel_panics.os_version_ - Version of the operating system

*other* - keyword, text.text

* _md_devices.other_ - Other information associated with array from /proc/mdstat

*other_run_times* - keyword, text.text

* _prefetch.other_run_times_ - Other execution times in prefetch file.

*ouid* - keyword, number.long

* _apparmor_events.ouid_ - Object owner's user ID

*outiface* - keyword, text.text

* _iptables.outiface_ - Output interface for the rule.

*outiface_mask* - keyword, text.text

* _iptables.outiface_mask_ - Output interface mask for the rule.

*output_bit* - keyword, number.long

* _cpuid.output_bit_ - Bit in register value for feature value

*output_register* - keyword, text.text

* _cpuid.output_register_ - Register used to for feature value

*output_size* - keyword, number.long

* _osquery_schedule.output_size_ - Cumulative total number of bytes generated by the resultant rows of the query

*overflows* - keyword, text.text

* _process_events.overflows_ - List of structures that overflowed

*owned* - keyword, number.long

* _tpm_info.owned_ - TPM is owned

*owner* - keyword, text.text

* _windows_search.owner_ - The owner of the item

*owner_gid* - keyword, number.long

* _process_events.owner_gid_ - File owner group ID

*owner_uid* - keyword, number.long

* _process_events.owner_uid_ - File owner user ID
* _shared_memory.owner_uid_ - User ID of owning process

*owner_uuid* - keyword, number.long

* _osquery_registry.owner_uuid_ - Extension route UUID (0 for core)

*package* - keyword, text.text

* _portage_keywords.package_ - Package name
* _portage_packages.package_ - Package name
* _portage_use.package_ - Package name
* _rpm_package_files.package_ - RPM package name

*package_filename* - keyword, text.text

* _package_receipts.package_filename_ - Filename of original .pkg file

*package_group* - keyword, text.text

* _rpm_packages.package_group_ - Package group

*package_id* - keyword, text.text

* _package_install_history.package_id_ - Label packageIdentifiers
* _package_receipts.package_id_ - Package domain identifier

*packets* - keyword, number.long

* _iptables.packets_ - Number of matching packets for this rule.

*packets_received* - keyword, number.long

* _lxd_networks.packets_received_ - Number of packets received on this network

*packets_sent* - keyword, number.long

* _lxd_networks.packets_sent_ - Number of packets sent on this network

*page_ins* - keyword, number.long

* _virtual_memory_info.page_ins_ - The total number of requests for pages from a pager.

*page_outs* - keyword, number.long

* _virtual_memory_info.page_outs_ - Total number of pages paged out.

*parent* - keyword

* _apparmor_events.parent_ - Parent process PID
* _block_devices.parent_ - Block device parent name
* _bpf_process_events.parent_ - Parent process ID
* _bpf_socket_events.parent_ - Parent process ID
* _crashes.parent_ - Parent PID of the crashed process
* _docker_container_processes.parent_ - Process parent's PID
* _es_process_events.parent_ - Parent process ID
* _es_process_file_events.parent_ - Parent process ID
* _iokit_devicetree.parent_ - Parent device registry ID
* _iokit_registry.parent_ - Parent registry ID
* _process_events.parent_ - Process parent's PID, or -1 if cannot be determined.
* _processes.parent_ - Process parent's PID

*parent_process_sequence_number* - keyword, number.long

* _process_etw_events.parent_process_sequence_number_ - Parent Process Sequence Number - Present only on ProcessStart events

*parent_ref_number* - keyword, text.text

* _ntfs_journal_events.parent_ref_number_ - The ordinal that associates a journal record with a filename's parent directory

*part_number* - keyword, text.text

* _memory_devices.part_number_ - Manufacturer specific serial number of memory device

*partial* - keyword

* _ntfs_journal_events.partial_ - Set to 1 if either path or old_path only contains the file or folder name
* _process_file_events.partial_ - True if this is a partial event (i.e.: this process existed before we started osquery)

*partition* - keyword, text.text

* _device_file.partition_ - A partition number
* _device_hash.partition_ - A partition number
* _device_partitions.partition_ - A partition number or description

*partition_row_position* - keyword, number.long

* _memory_device_mapped_addresses.partition_row_position_ - Identifies the position of the referenced memory device in a row of the address partition

*partition_width* - keyword, number.long

* _memory_array_mapped_addresses.partition_width_ - Number of memory devices that form a single row of memory for the address partition of this structure

*partitions* - keyword, number.long

* _disk_info.partitions_ - Number of detected partitions on disk.

*partner_fd* - keyword, number.long

* _process_open_pipes.partner_fd_ - File descriptor of shared pipe at partner's end

*partner_mode* - keyword, text.text

* _process_open_pipes.partner_mode_ - Mode of shared pipe at partner's end

*partner_pid* - keyword, number.long

* _process_open_pipes.partner_pid_ - Process ID of partner process sharing a particular pipe

*passpoint* - keyword, number.long

* _wifi_networks.passpoint_ - 1 if Passpoint is supported, 0 otherwise

*password_complexity* - keyword, number.long

* _security_profile_info.password_complexity_ - Determines whether passwords must meet a series of strong-password guidelines

*password_history_size* - keyword, number.long

* _security_profile_info.password_history_size_ - Number of unique new passwords that must be associated with a user account before an old password can be reused

*password_last_set_time* - keyword, number.double

* _account_policy_data.password_last_set_time_ - The time the password was last changed

*password_status* - keyword, text.text

* _shadow.password_status_ - Password status

*patch* - keyword, number.long

* _os_version.patch_ - Optional patch release

*path* - keyword, text.text

* _alf_exceptions.path_ - Path to the executable that is excepted
* _apparmor_profiles.path_ - Unique, aa-status compatible, policy identifier.
* _appcompat_shims.path_ - This is the path to the SDB database.
* _apps.path_ - Absolute and full Name.app path
* _augeas.path_ - The path to the configuration file
* _authenticode.path_ - Must provide a path or directory
* _autoexec.path_ - Path to the executable
* _background_activities_moderator.path_ - Application file path.
* _bpf_process_events.path_ - Binary path
* _bpf_socket_events.path_ - Path of executed file
* _browser_plugins.path_ - Path to plugin bundle
* _carves.path_ - The path of the requested carve
* _certificates.path_ - Path to Keychain or PEM bundle
* _chocolatey_packages.path_ - Path at which this package resides
* _chrome_extension_content_scripts.path_ - Path to extension folder
* _chrome_extensions.path_ - Path to extension folder
* _crashes.path_ - Path to the crashed process
* _crontab.path_ - File parsed
* _device_file.path_ - A logical path within the device node
* _disk_events.path_ - Path of the DMG file accessed
* _docker_container_fs_changes.path_ - FIle or directory path relative to rootfs
* _docker_containers.path_ - Container path
* _es_process_events.path_ - Path of executed file
* _es_process_file_events.path_ - Path of executed file
* _extended_attributes.path_ - Absolute file path
* _file.path_ - Absolute file path
* _firefox_addons.path_ - Path to plugin bundle
* _gatekeeper_approved_apps.path_ - Path of executable allowed to run
* _hardware_events.path_ - Local device path assigned (optional)
* _hash.path_ - Must provide a path or directory
* _homebrew_packages.path_ - Package install path
* _ie_extensions.path_ - Path to executable
* _kernel_extensions.path_ - Optional path to extension bundle
* _kernel_info.path_ - Kernel path
* _kernel_panics.path_ - Location of log file
* _keychain_acls.path_ - The path of the authorized application
* _keychain_items.path_ - Path to keychain containing item
* _launchd.path_ - Path to daemon or agent plist
* _launchd_overrides.path_ - Path to daemon or agent plist
* _listening_ports.path_ - Path for UNIX domain sockets
* _magic.path_ - Absolute path to target file
* _mdfind.path_ - Path of the file returned from spotlight
* _mdls.path_ - Path of the file
* _mounts.path_ - Mounted device path
* _npm_packages.path_ - Path at which this module resides
* _ntfs_acl_permissions.path_ - Path to the file or directory.
* _ntfs_journal_events.path_ - Path
* _office_mru.path_ - File path
* _osquery_extensions.path_ - Path of the extension's Thrift connection or library path
* _package_bom.path_ - Path of package bom
* _package_receipts.path_ - Path of receipt plist
* _plist.path_ - (required) read preferences from a plist
* _prefetch.path_ - Prefetch file path.
* _process_etw_events.path_ - Path of executed binary
* _process_events.path_ - Path of executed file
* _process_file_events.path_ - The path associated with the event
* _process_memory_map.path_ - Path to mapped file or mapped type
* _process_open_files.path_ - Filesystem path of descriptor
* _process_open_sockets.path_ - For UNIX sockets (family=AF_UNIX), the domain path
* _processes.path_ - Path to executed binary
* _python_packages.path_ - Path at which this module resides
* _quicklook_cache.path_ - Path of file
* _registry.path_ - Full path to the value
* _rpm_package_files.path_ - File path within the package
* _safari_extensions.path_ - Path to extension XAR bundle
* _sandboxes.path_ - Path to sandbox container directory
* _scheduled_tasks.path_ - Path to the executable to be run
* _services.path_ - Path to Service Executable
* _shared_folders.path_ - Absolute path of shared folder on the local system
* _shared_resources.path_ - Local path of the Windows share.
* _shellbags.path_ - Directory name.
* _shimcache.path_ - This is the path to the executed file.
* _signature.path_ - Must provide a path or directory
* _socket_events.path_ - Path of executed file
* _startup_items.path_ - Path of startup item
* _suid_bin.path_ - Binary path
* _system_extensions.path_ - Original path of system extension
* _user_events.path_ - Supplied path from event
* _user_ssh_keys.path_ - Path to key file
* _userassist.path_ - Application file path.
* _vscode_extensions.path_ - Extension path
* _windows_crashes.path_ - Path of the executable file for the crashed process
* _windows_search.path_ - The full path of the item.
* _yara.path_ - The path scanned

*pci_class* - keyword, text.text

* _pci_devices.pci_class_ - PCI Device class

*pci_class_id* - keyword, text.text

* _pci_devices.pci_class_id_ - PCI Device class ID in hex format

*pci_slot* - keyword, text.text

* _interface_details.pci_slot_ - PCI slot number
* _pci_devices.pci_slot_ - PCI Device used slot

*pci_subclass* - keyword, text.text

* _pci_devices.pci_subclass_ - PCI Device subclass

*pci_subclass_id* - keyword, text.text

* _pci_devices.pci_subclass_id_ - PCI Device  subclass in hex format

*pem* - keyword, text.text

* _curl_certificate.pem_ - Certificate PEM format

*percent_disk_read_time* - keyword, number.long

* _physical_disk_performance.percent_disk_read_time_ - Percentage of elapsed time that the selected disk drive is busy servicing read requests

*percent_disk_time* - keyword, number.long

* _physical_disk_performance.percent_disk_time_ - Percentage of elapsed time that the selected disk drive is busy servicing read or write requests

*percent_disk_write_time* - keyword, number.long

* _physical_disk_performance.percent_disk_write_time_ - Percentage of elapsed time that the selected disk drive is busy servicing write requests

*percent_idle_time* - keyword, number.long

* _physical_disk_performance.percent_idle_time_ - Percentage of time during the sample interval that the disk was idle

*percent_processor_time* - keyword, number.long

* _processes.percent_processor_time_ - Returns elapsed time that all of the threads of this process used the processor to execute instructions in 100 nanoseconds ticks.

*percent_remaining* - keyword, number.long

* _battery.percent_remaining_ - The percentage of battery remaining before it is drained

*percentage_encrypted* - keyword, number.long

* _bitlocker_info.percentage_encrypted_ - The percentage of the drive that is encrypted.

*perf_ctl* - keyword, number.long

* _msr.perf_ctl_ - Performance setting for the processor.

*perf_status* - keyword, number.long

* _msr.perf_status_ - Performance status for the processor.

*period* - keyword, text.text

* _load_average.period_ - Period over which the average is calculated.

*permanent* - keyword, text.text

* _arp_cache.permanent_ - 1 for true, 0 for false

*permissions* - keyword, text.text

* _chrome_extensions.permissions_ - The permissions required by the extension
* _kernel_keys.permissions_ - The key permissions, expressed as four hexadecimal bytes containing, from left to right, the possessor, user, group, and other permissions.
* _process_memory_map.permissions_ - r=read, w=write, x=execute, p=private (cow)
* _shared_memory.permissions_ - Memory segment permissions
* _suid_bin.permissions_ - Binary permissions

*permissions_json* - keyword, text.text

* _chrome_extensions.permissions_json_ - The JSON-encoded permissions required by the extension

*persistent* - keyword, number.long

* _chrome_extensions.persistent_ - 1 If extension is persistent across all tabs else 0

*persistent_volume_id* - keyword, text.text

* _bitlocker_info.persistent_volume_id_ - Persistent ID of the drive.

*personal_hotspot* - keyword, number.long

* _wifi_networks.personal_hotspot_ - 1 if this network is a personal hotspot, 0 otherwise

*pgroup* - keyword, number.long

* _docker_container_processes.pgroup_ - Process group
* _processes.pgroup_ - Process group

*physical_adapter* - keyword, number.long

* _interface_details.physical_adapter_ - Indicates whether the adapter is a physical or a logical adapter.

*physical_memory* - keyword, number.long

* _system_info.physical_memory_ - Total physical memory in bytes

*physical_presence_version* - keyword, text.text

* _tpm_info.physical_presence_version_ - Version of the Physical Presence Interface

*pid* - keyword, number.long

* _apparmor_events.pid_ - Process ID
* _asl.pid_ - Sending process ID encoded as a string.  Set automatically.
* _bpf_process_events.pid_ - Process ID
* _bpf_socket_events.pid_ - Process ID
* _crashes.pid_ - Process (or thread) ID of the crashed process
* _docker_container_processes.pid_ - Process ID
* _docker_containers.pid_ - Identifier of the initial process
* _es_process_events.pid_ - Process (or thread) ID
* _es_process_file_events.pid_ - Process (or thread) ID
* _last.pid_ - Process (or thread) ID
* _listening_ports.pid_ - Process (or thread) ID
* _logged_in_users.pid_ - Process (or thread) ID
* _lxd_instances.pid_ - Instance's process ID
* _osquery_info.pid_ - Process (or thread/handle) ID
* _pipes.pid_ - Process ID of the process to which the pipe belongs
* _process_envs.pid_ - Process (or thread) ID
* _process_etw_events.pid_ - Process ID
* _process_events.pid_ - Process (or thread) ID
* _process_file_events.pid_ - Process ID
* _process_memory_map.pid_ - Process (or thread) ID
* _process_namespaces.pid_ - Process (or thread) ID
* _process_open_files.pid_ - Process (or thread) ID
* _process_open_pipes.pid_ - Process ID
* _process_open_sockets.pid_ - Process (or thread) ID
* _processes.pid_ - Process (or thread) ID
* _running_apps.pid_ - The pid of the application
* _seccomp_events.pid_ - Process ID
* _services.pid_ - the Process ID of the service
* _shared_memory.pid_ - Process ID to last use the segment
* _socket_events.pid_ - Process (or thread) ID
* _unified_log.pid_ - the pid of the process that made the entry
* _user_events.pid_ - Process (or thread) ID
* _windows_crashes.pid_ - Process ID of the crashed process
* _windows_eventlog.pid_ - Process ID which emitted the event record

*pid_namespace* - keyword, text.text

* _docker_containers.pid_namespace_ - PID namespace
* _process_namespaces.pid_namespace_ - pid namespace inode

*pid_with_namespace* - keyword, number.long

* _apt_sources.pid_with_namespace_ - Pids that contain a namespace
* _authorized_keys.pid_with_namespace_ - Pids that contain a namespace
* _crontab.pid_with_namespace_ - Pids that contain a namespace
* _deb_packages.pid_with_namespace_ - Pids that contain a namespace
* _dns_resolvers.pid_with_namespace_ - Pids that contain a namespace
* _etc_hosts.pid_with_namespace_ - Pids that contain a namespace
* _file.pid_with_namespace_ - Pids that contain a namespace
* _groups.pid_with_namespace_ - Pids that contain a namespace
* _hash.pid_with_namespace_ - Pids that contain a namespace
* _npm_packages.pid_with_namespace_ - Pids that contain a namespace
* _os_version.pid_with_namespace_ - Pids that contain a namespace
* _python_packages.pid_with_namespace_ - Pids that contain a namespace
* _rpm_packages.pid_with_namespace_ - Pids that contain a namespace
* _suid_bin.pid_with_namespace_ - Pids that contain a namespace
* _user_ssh_keys.pid_with_namespace_ - Pids that contain a namespace
* _users.pid_with_namespace_ - Pids that contain a namespace
* _yara.pid_with_namespace_ - Pids that contain a namespace
* _yum_sources.pid_with_namespace_ - Pids that contain a namespace

*pids* - keyword, number.long

* _docker_container_stats.pids_ - Number of processes

*pixels* - keyword, text.text

* _connected_displays.pixels_ - The number of pixels of the display.

*pk_hash* - keyword, text.text

* _keychain_items.pk_hash_ - Hash of associated public key (SHA1 of subjectPublicKey, see RFC 8520 4.2.1.2)

*placement_group_id* - keyword, text.text

* _azure_instance_metadata.placement_group_id_ - Placement group for the VM scale set

*platform* - keyword, text.text

* _os_version.platform_ - OS Platform or ID
* _osquery_packs.platform_ - Platforms this query is supported on

*platform_binary* - keyword, number.long

* _es_process_events.platform_binary_ - Indicates if the binary is Apple signed binary (1) or not (0)

*platform_fault_domain* - keyword, text.text

* _azure_instance_metadata.platform_fault_domain_ - Fault domain the VM is running in

*platform_info* - keyword, number.long

* _msr.platform_info_ - Platform information.

*platform_like* - keyword, text.text

* _os_version.platform_like_ - Closely related platforms

*platform_mask* - keyword, number.long

* _osquery_info.platform_mask_ - The osquery platform bitmask

*platform_update_domain* - keyword, text.text

* _azure_instance_metadata.platform_update_domain_ - Update domain the VM is running in

*plugin* - keyword, text.text

* _authorization_mechanisms.plugin_ - Authorization plugin name

*pnp_device_id* - keyword, text.text

* _disk_info.pnp_device_id_ - The unique identifier of the drive on the system.

*point_to_point* - keyword, text.text

* _interface_addresses.point_to_point_ - PtP address for the interface

*policies* - keyword, text.text

* _curl_certificate.policies_ - Certificate Policies

*policy* - keyword, text.text

* _iptables.policy_ - Policy that applies for this rule.

*policy_constraints* - keyword, text.text

* _curl_certificate.policy_constraints_ - Policy Constraints

*policy_content* - keyword, text.text

* _password_policy.policy_content_ - Policy content

*policy_description* - keyword, text.text

* _password_policy.policy_description_ - Policy description

*policy_identifier* - keyword, text.text

* _password_policy.policy_identifier_ - Policy Identifier

*policy_mappings* - keyword, text.text

* _curl_certificate.policy_mappings_ - Policy Mappings

*port* - keyword, number.long

* _docker_container_ports.port_ - Port inside the container
* _etc_services.port_ - Service port number
* _listening_ports.port_ - Transport layer port

*possibly_hidden* - keyword, number.long

* _wifi_networks.possibly_hidden_ - 1 if network is possibly a hidden network, 0 otherwise

*ppid* - keyword, number.long

* _process_etw_events.ppid_ - Parent Process ID
* _process_file_events.ppid_ - Parent process ID

*pre_cpu_kernelmode_usage* - keyword, number.long

* _docker_container_stats.pre_cpu_kernelmode_usage_ - Last read CPU kernel mode usage

*pre_cpu_total_usage* - keyword, number.long

* _docker_container_stats.pre_cpu_total_usage_ - Last read total CPU usage

*pre_cpu_usermode_usage* - keyword, number.long

* _docker_container_stats.pre_cpu_usermode_usage_ - Last read CPU user mode usage

*pre_online_cpus* - keyword, number.long

* _docker_container_stats.pre_online_cpus_ - Last read online CPUs

*pre_system_cpu_usage* - keyword, number.long

* _docker_container_stats.pre_system_cpu_usage_ - Last read CPU system usage

*predicate* - keyword, text.text

* _unified_log.predicate_ - predicate to search (see `log help predicates`), note that this is merged into the predicate created from the column constraints

*prefix* - keyword, text.text

* _homebrew_packages.prefix_ - Homebrew install prefix

*preread* - keyword, number.long

* _docker_container_stats.preread_ - UNIX time when stats were last read

*prerelease* - keyword, number.long

* _vscode_extensions.prerelease_ - Pre release version

*principal* - keyword, text.text

* _ntfs_acl_permissions.principal_ - User or group to which the ACE applies.

*printer_sharing* - keyword, number.long

* _sharing_preferences.printer_sharing_ - 1 If printer sharing is enabled else 0

*priority* - keyword, text.text

* _deb_packages.priority_ - Package priority

*privileged* - keyword, text.text

* _authorization_mechanisms.privileged_ - If privileged it will run as root, else as an anonymous user
* _docker_containers.privileged_ - Is the container privileged

*probe_error* - keyword, number.long

* _bpf_process_events.probe_error_ - Set to 1 if one or more buffers could not be captured
* _bpf_socket_events.probe_error_ - Set to 1 if one or more buffers could not be captured

*process* - keyword, text.text

* _alf_explicit_auths.process_ - Process name explicitly allowed
* _unified_log.process_ - the name of the process that made the entry

*process_being_tapped* - keyword, number.long

* _event_taps.process_being_tapped_ - The process ID of the target application

*process_sequence_number* - keyword, number.long

* _process_etw_events.process_sequence_number_ - Process Sequence Number - Present only on ProcessStart events

*process_type* - keyword, text.text

* _launchd.process_type_ - Key describes the intended purpose of the job

*process_uptime* - keyword, number.long

* _windows_crashes.process_uptime_ - Uptime of the process in seconds

*processes* - keyword, number.long

* _lxd_instances.processes_ - Number of processes running inside this instance

*processing_time* - keyword, number.long

* _cups_jobs.processing_time_ - How long the job took to process

*processor_number* - keyword, number.long

* _msr.processor_number_ - The processor number as reported in /proc/cpuinfo

*processor_type* - keyword, text.text

* _cpu_info.processor_type_ - The processor type, such as Central, Math, or Video.

*product_id* - keyword, text.text

* _connected_displays.product_id_ - The product ID of the display.

*product_name* - keyword, text.text

* _tpm_info.product_name_ - Product name of the TPM

*product_version* - keyword, text.text

* _file.product_version_ - File product version

*profile* - keyword, text.text

* _apparmor_events.profile_ - Apparmor profile name
* _chrome_extensions.profile_ - The name of the Chrome profile that contains this extension

*profile_domain* - keyword, number.long

* _windows_firewall_rules.profile_domain_ - 1 if the rule profile type is domain

*profile_path* - keyword, text.text

* _chrome_extension_content_scripts.profile_path_ - The profile path
* _chrome_extensions.profile_path_ - The profile path
* _logon_sessions.profile_path_ - The home directory for the logon session.

*profile_private* - keyword, number.long

* _windows_firewall_rules.profile_private_ - 1 if the rule profile type is private

*profile_public* - keyword, number.long

* _windows_firewall_rules.profile_public_ - 1 if the rule profile type is public

*program* - keyword, text.text

* _launchd.program_ - Path to target program

*program_arguments* - keyword, text.text

* _launchd.program_arguments_ - Command line arguments passed to program

*propagation* - keyword, text.text

* _docker_container_mounts.propagation_ - Mount propagation

*properties* - keyword, text.text

* _windows_search.properties_ - Additional property values JSON

*protected* - keyword, number.long

* _app_schemes.protected_ - 1 if this handler is protected (reserved) by macOS, else 0

*protection_disabled* - keyword, number.long

* _carbon_black_info.protection_disabled_ - If the sensor is configured to report tamper events

*protection_status* - keyword, number.long

* _bitlocker_info.protection_status_ - The bitlocker protection status of the drive.

*protection_type* - keyword, text.text

* _processes.protection_type_ - The protection type of the process

*protocol* - keyword

* _bpf_socket_events.protocol_ - The network protocol ID
* _etc_services.protocol_ - Transport protocol (TCP/UDP)
* _iptables.protocol_ - Protocol number identification.
* _listening_ports.protocol_ - Transport protocol (TCP/UDP)
* _process_open_sockets.protocol_ - Transport protocol (TCP/UDP)
* _socket_events.protocol_ - The network protocol ID
* _usb_devices.protocol_ - USB Device protocol
* _windows_firewall_rules.protocol_ - IP protocol of the rule

*provider* - keyword, text.text

* _drivers.provider_ - Driver provider

*provider_guid* - keyword, text.text

* _windows_eventlog.provider_guid_ - Provider guid of the event
* _windows_events.provider_guid_ - Provider guid of the event

*provider_name* - keyword, text.text

* _windows_eventlog.provider_name_ - Provider name of the event
* _windows_events.provider_name_ - Provider name of the event

*pseudo* - keyword, number.long

* _process_memory_map.pseudo_ - 1 If path is a pseudo path, else 0

*public* - keyword, number.long

* _lxd_images.public_ - Whether image is public (1) or not (0)

*publisher* - keyword, text.text

* _azure_instance_metadata.publisher_ - Publisher of the VM image
* _osquery_events.publisher_ - Name of the associated publisher
* _programs.publisher_ - Name of the product supplier.
* _vscode_extensions.publisher_ - Publisher Name

*publisher_id* - keyword, text.text

* _vscode_extensions.publisher_id_ - Publisher ID

*purgeable* - keyword, number.long

* _virtual_memory_info.purgeable_ - Total number of purgeable pages.

*purged* - keyword, number.long

* _virtual_memory_info.purged_ - Total number of purged pages.

*query* - keyword, text.text

* _mdfind.query_ - The query that was run to find the file
* _osquery_schedule.query_ - The exact query to run
* _windows_search.query_ - Windows search query
