<!-- Part 5 of 6 of osquery/exported-fields-reference.md (split because the page is big). -->

* _wmi_event_filters.query_ - Windows Management Instrumentation Query Language (WQL) event query that specifies the set of events for consumer notification, and the specific conditions for notification.

*query_language* - keyword, text.text

* _wmi_event_filters.query_language_ - Query language that the query is written in.

*queue_directories* - keyword, text.text

* _launchd.queue_directories_ - Similar to watch_paths but only with non-empty directories

*raid_disks* - keyword, number.long

* _md_devices.raid_disks_ - Number of configured RAID disks in array

*raid_level* - keyword, number.long

* _md_devices.raid_level_ - Current raid level of the array

*rapl_energy_status* - keyword, number.long

* _msr.rapl_energy_status_ - Run Time Average Power Limiting energy status.

*rapl_power_limit* - keyword, number.long

* _msr.rapl_power_limit_ - Run Time Average Power Limiting power limit.

*rapl_power_units* - keyword, number.long

* _msr.rapl_power_units_ - Run Time Average Power Limiting power units.

*reactivated* - keyword, number.long

* _virtual_memory_info.reactivated_ - Total number of reactivated pages.

*read* - keyword, number.long

* _docker_container_stats.read_ - UNIX time when stats were read

*readonly* - keyword, number.long

* _nfs_shares.readonly_ - 1 if the share is exported readonly else 0

*readonly_rootfs* - keyword, number.long

* _docker_containers.readonly_rootfs_ - Is the root filesystem mounted as read only

*record_timestamp* - keyword, text.text

* _ntfs_journal_events.record_timestamp_ - Journal record timestamp

*record_usn* - keyword, text.text

* _ntfs_journal_events.record_usn_ - The update sequence number that identifies the journal record

*recovery_finish* - keyword, text.text

* _md_devices.recovery_finish_ - Estimated duration of recovery activity

*recovery_progress* - keyword, text.text

* _md_devices.recovery_progress_ - Progress of the recovery activity

*recovery_speed* - keyword, text.text

* _md_devices.recovery_speed_ - Speed of recovery activity

*redirect_accept* - keyword, number.long

* _interface_ipv6.redirect_accept_ - Accept ICMP redirect messages

*ref_pid* - keyword, number.long

* _asl.ref_pid_ - Reference PID for messages proxied by launchd

*ref_proc* - keyword, text.text

* _asl.ref_proc_ - Reference process for messages proxied by launchd

*referenced* - keyword, number.long

* _chrome_extension_content_scripts.referenced_ - 1 if this extension is referenced by the Preferences file of the profile
* _chrome_extensions.referenced_ - 1 if this extension is referenced by the Preferences file of the profile

*referenced_identifier* - keyword, text.text

* _chrome_extensions.referenced_identifier_ - Extension identifier, as specified by the preferences file. Empty if the extension is not in the profile.

*refreshes* - keyword, number.long

* _osquery_events.refreshes_ - Publisher only: number of runloop restarts

*refs* - keyword, number.long

* _kernel_extensions.refs_ - Reference count

*region* - keyword, text.text

* _ec2_instance_metadata.region_ - AWS region in which this instance launched

*registers* - keyword, text.text

* _crashes.registers_ - The value of the system registers
* _kernel_panics.registers_ - A space delimited line of register:value pairs
* _windows_crashes.registers_ - The values of the system registers

*registry* - keyword, text.text

* _osquery_registry.registry_ - Name of the osquery registry

*registry_hive* - keyword, text.text

* _logged_in_users.registry_hive_ - HKEY_USERS registry hive

*registry_path* - keyword, text.text

* _ie_extensions.registry_path_ - Extension identifier

*relative_path* - keyword, text.text

* _wmi_cli_event_consumers.relative_path_ - Relative path to the class or instance.
* _wmi_event_filters.relative_path_ - Relative path to the class or instance.
* _wmi_filter_consumer_binding.relative_path_ - Relative path to the class or instance.
* _wmi_script_event_consumers.relative_path_ - Relative path to the class or instance.

*release* - keyword, text.text

* _apt_sources.release_ - Release name
* _lxd_images.release_ - OS release version on which the image is based
* _rpm_packages.release_ - Package release

*remediation_path* - keyword, text.text

* _windows_security_products.remediation_path_ - Remediation path

*remote_address* - keyword, text.text

* _bpf_socket_events.remote_address_ - Remote address associated with socket
* _process_open_sockets.remote_address_ - Socket remote address
* _socket_events.remote_address_ - Remote address associated with socket

*remote_addresses* - keyword, text.text

* _windows_firewall_rules.remote_addresses_ - Remote addresses for the rule

*remote_apple_events* - keyword, number.long

* _sharing_preferences.remote_apple_events_ - 1 If remote apple events are enabled else 0

*remote_login* - keyword, number.long

* _sharing_preferences.remote_login_ - 1 If remote login is enabled else 0

*remote_management* - keyword, number.long

* _sharing_preferences.remote_management_ - 1 If remote management is enabled else 0

*remote_port* - keyword, number.long

* _bpf_socket_events.remote_port_ - Remote network protocol port number
* _process_open_sockets.remote_port_ - Socket remote port
* _socket_events.remote_port_ - Remote network protocol port number

*remote_ports* - keyword, text.text

* _windows_firewall_rules.remote_ports_ - Remote ports for the rule

*removable* - keyword, number.long

* _usb_devices.removable_ - 1 If USB device is removable else 0

*repository* - keyword, text.text

* _portage_packages.repository_ - From which repository the ebuild was used

*request_id* - keyword, text.text

* _carves.request_id_ - Identifying value of the carve request (e.g., scheduled query name, distributed request, etc)

*requested_mask* - keyword, text.text

* _apparmor_events.requested_mask_ - Requested access mask

*requirement* - keyword, text.text

* _gatekeeper_approved_apps.requirement_ - Code signing requirement language

*reservation_id* - keyword, text.text

* _ec2_instance_metadata.reservation_id_ - ID of the reservation

*reshape_finish* - keyword, text.text

* _md_devices.reshape_finish_ - Estimated duration of reshape activity

*reshape_progress* - keyword, text.text

* _md_devices.reshape_progress_ - Progress of the reshape activity

*reshape_speed* - keyword, text.text

* _md_devices.reshape_speed_ - Speed of reshape activity

*resident_size* - keyword, number.long

* _docker_container_processes.resident_size_ - Bytes of private memory used by process
* _processes.resident_size_ - Bytes of private memory used by process

*resolution* - keyword, text.text

* _connected_displays.resolution_ - The resolution of the display.

*resource_group_name* - keyword, text.text

* _azure_instance_metadata.resource_group_name_ - Resource group for the VM

*response_code* - keyword, number.long

* _curl.response_code_ - The HTTP status code for the response

*responsible* - keyword, text.text

* _crashes.responsible_ - Process responsible for the crashed process

*result* - keyword, text.text

* _authenticode.result_ - The signature check result
* _curl.result_ - The HTTP response body

*result_code* - keyword, text.text

* _windows_update_history.result_code_ - Result of an operation on an update

*resync_finish* - keyword, text.text

* _md_devices.resync_finish_ - Estimated duration of resync activity

*resync_progress* - keyword, text.text

* _md_devices.resync_progress_ - Progress of the resync activity

*resync_speed* - keyword, text.text

* _md_devices.resync_speed_ - Speed of resync activity

*retain_count* - keyword, number.long

* _iokit_devicetree.retain_count_ - The device reference count
* _iokit_registry.retain_count_ - The node reference count

*revision* - keyword, text.text

* _deb_packages.revision_ - Package revision
* _hardware_events.revision_ - Device revision (optional)
* _os_version.revision_ - Update Build Revision, refers to the specific revision number of a Windows update
* _platform_info.revision_ - BIOS major and minor revision

*roaming* - keyword, number.long

* _wifi_networks.roaming_ - 1 if roaming is supported, 0 otherwise

*roaming_profile* - keyword, text.text

* _wifi_networks.roaming_profile_ - Describe the roaming profile, usually one of Single, Dual  or Multi

*root* - keyword, text.text

* _processes.root_ - Process virtual root directory

*root_dir* - keyword, text.text

* _docker_info.root_dir_ - Docker root directory

*root_directory* - keyword, text.text

* _launchd.root_directory_ - Key used to specify a directory to chroot to before launch

*root_volume_uuid* - keyword, text.text

* _time_machine_destinations.root_volume_uuid_ - Root UUID of backup volume

*rotation* - keyword, text.text

* _connected_displays.rotation_ - The orientation of the display.

*round_trip_time* - keyword, number.long

* _curl.round_trip_time_ - Time taken to complete the request

*rowid* - keyword, number.long

* _quicklook_cache.rowid_ - Quicklook file rowid key

*rssi* - keyword, number.long

* _wifi_status.rssi_ - The current received signal strength indication (dbm)
* _wifi_survey.rssi_ - The current received signal strength indication (dbm)

*rtadv_accept* - keyword, number.long

* _interface_ipv6.rtadv_accept_ - Accept ICMP Router Advertisement

*rule_details* - keyword, text.text

* _sudoers.rule_details_ - Rule definition

*run_at_load* - keyword, text.text

* _launchd.run_at_load_ - Should the program run on launch load

*run_count* - keyword, number.long

* _prefetch.run_count_ - Number of times the application has been run.

*rw* - keyword, number.long

* _docker_container_mounts.rw_ - 1 if read/write. 0 otherwise

*scheme* - keyword, text.text

* _app_schemes.scheme_ - Name of the scheme/protocol

*scope* - keyword, text.text

* _selinux_settings.scope_ - Where the key is located inside the SELinuxFS mount point.

*screen_sharing* - keyword, number.long

* _sharing_preferences.screen_sharing_ - 1 If screen sharing is enabled else 0

*script* - keyword, text.text

* _chrome_extension_content_scripts.script_ - The content script used by the extension

*script_block_count* - keyword, number.long

* _powershell_events.script_block_count_ - The total number of script blocks for this script

*script_block_id* - keyword, text.text

* _powershell_events.script_block_id_ - The unique GUID of the powershell script to which this block belongs

*script_file_name* - keyword, text.text

* _wmi_script_event_consumers.script_file_name_ - Name of the file from which the script text is read, intended as an alternative to specifying the text of the script in the ScriptText property.

*script_name* - keyword, text.text

* _powershell_events.script_name_ - The name of the Powershell script

*script_path* - keyword, text.text

* _powershell_events.script_path_ - The path for the Powershell script

*script_text* - keyword, text.text

* _powershell_events.script_text_ - The text content of the Powershell script
* _wmi_script_event_consumers.script_text_ - Text of the script that is expressed in a language known to the scripting engine. This property must be NULL if the ScriptFileName property is not NULL.

*scripting_engine* - keyword, text.text

* _wmi_script_event_consumers.scripting_engine_ - Name of the scripting engine to use, for example, 'VBScript'. This property cannot be NULL.

*sdb_id* - keyword, text.text

* _appcompat_shims.sdb_id_ - Unique GUID of the SDB.

*sdk* - keyword, text.text

* _browser_plugins.sdk_ - Build SDK used to compile plugin
* _safari_extensions.sdk_ - Bundle SDK used to compile extension

*sdk_version* - keyword, text.text

* _osquery_extensions.sdk_version_ - osquery SDK version used to build the extension

*seconds* - keyword, number.long

* _time.seconds_ - Current seconds in UTC
* _uptime.seconds_ - Seconds of uptime

*section* - keyword, text.text

* _deb_packages.section_ - Package section

*secure_boot* - keyword, number.long

* _secureboot.secure_boot_ - Whether secure boot is enabled

*secure_mode* - keyword, number.long

* _secureboot.secure_mode_ - (Intel) Secure mode: 0 disabled, 1 full security, 2 medium security

*secure_process* - keyword, number.long

* _processes.secure_process_ - Process is secure (IUM) yes=1, no=0

*security_breach* - keyword, text.text

* _chassis_info.security_breach_ - The physical status of the chassis such as Breach Successful, Breach Attempted, etc.

*security_groups* - keyword, text.text

* _ec2_instance_metadata.security_groups_ - Comma separated list of security group names

*security_options* - keyword, text.text

* _docker_containers.security_options_ - List of container security options

*security_type* - keyword, text.text

* _wifi_networks.security_type_ - Type of security on this network
* _wifi_status.security_type_ - Type of security on this network

*self_signed* - keyword, number.long

* _certificates.self_signed_ - 1 if self-signed, else 0

*sender* - keyword, text.text

* _asl.sender_ - Sender's identification string.  Default is process name.
* _unified_log.sender_ - the name of the binary image that made the entry

*sensor_backend_server* - keyword, text.text

* _carbon_black_info.sensor_backend_server_ - Carbon Black server

*sensor_id* - keyword, number.long

* _carbon_black_info.sensor_id_ - Sensor ID of the Carbon Black sensor

*sensor_ip_addr* - keyword, text.text

* _carbon_black_info.sensor_ip_addr_ - IP address of the sensor

*seq_num* - keyword, number.long

* _es_process_events.seq_num_ - Per event sequence number
* _es_process_file_events.seq_num_ - Per event sequence number

*serial* - keyword, text.text

* _certificates.serial_ - Certificate serial number
* _chassis_info.serial_ - The serial number of the chassis.
* _disk_info.serial_ - The serial number of the disk.
* _hardware_events.serial_ - Device serial (optional)
* _usb_devices.serial_ - USB Device serial connection

*serial_number* - keyword, text.text

* _authenticode.serial_number_ - The certificate serial number
* _battery.serial_number_ - The battery's serial number
* _connected_displays.serial_number_ - The serial number of the display. (may not be unique)
* _curl_certificate.serial_number_ - Certificate serial number
* _kernel_keys.serial_number_ - The serial key of the key.
* _memory_devices.serial_number_ - Serial number of memory device

*serial_port_enabled* - keyword, text.text

* _ycloud_instance_metadata.serial_port_enabled_ - Indicates if serial port is enabled for the VM

*series* - keyword, text.text

* _video_info.series_ - The series of the gpu.

*server_name* - keyword, text.text

* _lxd_cluster.server_name_ - Name of the LXD server node
* _lxd_cluster_members.server_name_ - Name of the LXD server node

*server_selection* - keyword, text.text

* _windows_update_history.server_selection_ - Value that indicates which server provided an update

*server_version* - keyword, text.text

* _docker_info.server_version_ - Server version

*service* - keyword, text.text

* _drivers.service_ - Driver service name, if one exists
* _interface_details.service_ - The name of the service the network adapter uses.
* _iokit_devicetree.service_ - 1 if the device conforms to IOService else 0

*service_exit_code* - keyword, number.long

* _services.service_exit_code_ - The service-specific error code that the service returns when an error occurs while the service is starting or stopping

*service_id* - keyword, text.text

* _windows_update_history.service_id_ - Service identifier of an update service that is not a Windows update

*service_key* - keyword, text.text

* _drivers.service_key_ - Driver service registry key

*service_name* - keyword, text.text

* _windows_firewall_rules.service_name_ - Service name property of the application

*service_type* - keyword, text.text

* _services.service_type_ - Service Type: OWN_PROCESS, SHARE_PROCESS and maybe Interactive (can interact with the desktop)

*ses* - keyword, number.long

* _seccomp_events.ses_ - Session ID of the session from which the analyzed process was invoked

*session_id* - keyword, number.long

* _logon_sessions.session_id_ - The Terminal Services session identifier.
* _process_etw_events.session_id_ - Session ID
* _winbaseobj.session_id_ - Terminal Services Session Id

*session_owner* - keyword, text.text

* _authorizations.session_owner_ - Label top-level key

*set* - keyword, number.long

* _memory_devices.set_ - Identifies if memory device is one of a set of devices.  A value of 0 indicates no set affiliation.

*setup_mode* - keyword, number.long

* _secureboot.setup_mode_ - Whether setup mode is enabled

*severity* - keyword, number.long

* _syslog_events.severity_ - Syslog severity

*sgid* - keyword

* _docker_container_processes.sgid_ - Saved group ID
* _process_events.sgid_ - Saved group ID at process start
* _process_file_events.sgid_ - Saved group ID of the process using the file
* _processes.sgid_ - Unsigned saved group ID

*sha1* - keyword, text.text

* _apparmor_profiles.sha1_ - A unique hash that identifies this policy.
* _certificates.sha1_ - SHA1 hash of the raw certificate contents
* _device_hash.sha1_ - SHA1 hash of provided inode data
* _file_events.sha1_ - The SHA1 of the file after change
* _hash.sha1_ - SHA1 hash of provided filesystem data
* _rpm_packages.sha1_ - SHA1 hash of the package contents

*sha1_fingerprint* - keyword, text.text

* _curl_certificate.sha1_fingerprint_ - SHA1 fingerprint

*sha256* - keyword, text.text

* _apparmor_profiles.sha256_ - A unique hash that identifies this policy.
* _carves.sha256_ - A SHA256 sum of the carved archive
* _device_hash.sha256_ - SHA256 hash of provided inode data
* _file_events.sha256_ - The SHA256 of the file after change
* _hash.sha256_ - SHA256 hash of provided filesystem data
* _rpm_package_files.sha256_ - SHA256 file digest from RPM info DB

*sha256_fingerprint* - keyword, text.text

* _curl_certificate.sha256_fingerprint_ - SHA-256 fingerprint

*shard* - keyword, number.long

* _osquery_packs.shard_ - Shard restriction limit, 1-100, 0 meaning no restriction

*share* - keyword, text.text

* _nfs_shares.share_ - Filesystem path to the share

*shared* - keyword, text.text

* _authorizations.shared_ - Label top-level key

*shell* - keyword, text.text

* _users.shell_ - User's configured default shell

*shell_only* - keyword, number.long

* _osquery_flags.shell_only_ - Is the flag shell only?

*shmid* - keyword, number.long

* _shared_memory.shmid_ - Shared memory segment ID

*shortcut_comment* - keyword, text.text

* _file.shortcut_comment_ - Comment on the shortcut

*shortcut_run* - keyword, text.text

* _file.shortcut_run_ - Window mode the target of the shortcut should be run in

*shortcut_start_in* - keyword, text.text

* _file.shortcut_start_in_ - Full path to the working directory to use when executing the shortcut target

*shortcut_target_location* - keyword, text.text

* _file.shortcut_target_location_ - Folder name where the shortcut target resides

*shortcut_target_path* - keyword, text.text

* _file.shortcut_target_path_ - Full path to the file the shortcut points to

*shortcut_target_type* - keyword, text.text

* _file.shortcut_target_type_ - Display name for the target type

*sid* - keyword, text.text

* _background_activities_moderator.sid_ - User SID.
* _certificates.sid_ - SID
* _logged_in_users.sid_ - The user's unique security identifier
* _office_mru.sid_ - User SID
* _shellbags.sid_ - User SID
* _userassist.sid_ - User SID.

*sig* - keyword, number.long

* _seccomp_events.sig_ - Signal value sent to process by seccomp

*sig_group* - keyword, text.text

* _yara.sig_group_ - Signature group used

*sigfile* - keyword, text.text

* _yara.sigfile_ - Signature file used

*signature* - keyword, text.text

* _curl_certificate.signature_ - Signature

*signature_algorithm* - keyword, text.text

* _curl_certificate.signature_algorithm_ - Signature Algorithm

*signatures_up_to_date* - keyword, number.long

* _windows_security_products.signatures_up_to_date_ - 1 if product signatures are up to date, else 0

*signed* - keyword, number.long

* _drivers.signed_ - Whether the driver is signed or not
* _signature.signed_ - 1 If the file is signed else 0

*signing_algorithm* - keyword, text.text

* _certificates.signing_algorithm_ - Signing algorithm used

*signing_id* - keyword, text.text

* _es_process_events.signing_id_ - Signature identifier of the process

*sigrule* - keyword, text.text

* _yara.sigrule_ - Signature strings used

*sigurl* - keyword, text.text

* _yara.sigurl_ - Signature url

*size* - keyword

* _acpi_tables.size_ - Size of compiled table data
* _block_devices.size_ - Block device size in blocks
* _carves.size_ - Size of the carved archive
* _cups_jobs.size_ - The size of the print job
* _deb_packages.size_ - Package size in bytes
* _device_file.size_ - Size of file in bytes
* _disk_events.size_ - Size of partition in bytes
* _docker_image_history.size_ - Size of instruction in bytes
* _file.size_ - Size of file in bytes
* _file_events.size_ - Size of file in bytes
* _kernel_extensions.size_ - Bytes of wired memory used by extension
* _kernel_modules.size_ - Size of module content
* _logical_drives.size_ - The total amount of space, in bytes, of the drive (-1 on failure).
* _lxd_images.size_ - Size of image in bytes
* _lxd_storage_pools.size_ - Size of the storage pool
* _md_devices.size_ - size of the array in blocks
* _memory_devices.size_ - Size of memory device in Megabyte
* _package_bom.size_ - Expected file size
* _platform_info.size_ - Size in bytes of firmware
* _portage_packages.size_ - The size of the package
* _prefetch.size_ - Application file size.
* _quicklook_cache.size_ - Parsed version size field
* _rpm_package_files.size_ - Expected file size in bytes from RPM info DB
* _rpm_packages.size_ - Package size in bytes
* _shared_memory.size_ - Size in bytes
* _smbios_tables.size_ - Table entry size in bytes
* _smc_keys.size_ - Reported size of data in bytes
* _windows_search.size_ - The item size in bytes.

*size_bytes* - keyword, number.long

* _docker_images.size_bytes_ - Size of image in bytes

*sku* - keyword, text.text

* _azure_instance_metadata.sku_ - SKU for the VM image
* _chassis_info.sku_ - The Stock Keeping Unit number if available.

*slot* - keyword

* _md_drives.slot_ - Slot position of disk
* _portage_packages.slot_ - The slot used by package

*smbios_tag* - keyword, text.text

* _chassis_info.smbios_tag_ - The assigned asset tag number of the chassis.

*socket* - keyword

* _listening_ports.socket_ - Socket handle or inode number
* _process_open_sockets.socket_ - Socket handle or inode number
* _socket_events.socket_ - The local path (UNIX domain socket only)

*socket_designation* - keyword, text.text

* _cpu_info.socket_designation_ - The assigned socket on the board for the given CPU.

*soft_limit* - keyword, text.text

* _ulimit_info.soft_limit_ - Current limit value

*softirq* - keyword, number.long

* _cpu_time.softirq_ - Time spent servicing softirqs

*sort* - keyword, text.text

* _windows_search.sort_ - Sort for windows api

*source* - keyword, text.text

* _apt_sources.source_ - Source file
* _autoexec.source_ - Source table of the autoexec item
* _deb_packages.source_ - Package source
* _docker_container_mounts.source_ - Source path on host
* _lxd_storage_pools.source_ - Storage pool source
* _package_install_history.source_ - Install source: usually the installer process name
* _routes.source_ - Route source
* _rpm_packages.source_ - Source RPM package name (optional)
* _shellbags.source_ - Shellbags source Registry file
* _startup_items.source_ - Directory or plist containing startup item
* _sudoers.source_ - Source file containing the given rule
* _windows_events.source_ - Source or channel of the event
* _yum_sources.source_ - Source file

*source_path* - keyword, text.text

* _systemd_units.source_path_ - Path to the (possibly generated) unit configuration file

*source_url* - keyword, text.text

* _firefox_addons.source_url_ - URL that installed the addon

*space_total* - keyword, number.long

* _lxd_storage_pools.space_total_ - Total available storage space in bytes for this storage pool

*space_used* - keyword, number.long

* _lxd_storage_pools.space_used_ - Storage space used in bytes

*spare_disks* - keyword, number.long

* _md_devices.spare_disks_ - Number of idle disks in array

*spec_version* - keyword, text.text

* _tpm_info.spec_version_ - Trusted Computing Group specification that the TPM supports

*speculative* - keyword, number.long

* _virtual_memory_info.speculative_ - Total number of speculative pages.

*speed* - keyword, number.long

* _interface_details.speed_ - Estimate of the current bandwidth in bits per second.

*src_ip* - keyword, text.text

* _iptables.src_ip_ - Source IP address.

*src_mask* - keyword, text.text

* _iptables.src_mask_ - Source IP address mask.

*src_port* - keyword, text.text

* _iptables.src_port_ - Protocol source port(s).

*ssh_config_file* - keyword, text.text

* _ssh_configs.ssh_config_file_ - Path to the ssh_config file

*ssh_public_key* - keyword, text.text

* _ec2_instance_metadata.ssh_public_key_ - SSH public key. Only available if supplied at instance launch time
* _ycloud_instance_metadata.ssh_public_key_ - SSH public key. Only available if supplied at instance launch time

*ssid* - keyword, text.text

* _wifi_networks.ssid_ - SSID octets of the network
* _wifi_status.ssid_ - SSID octets of the network
* _wifi_survey.ssid_ - SSID octets of the network

*stack_trace* - keyword, text.text

* _crashes.stack_trace_ - Most recent frame from the stack trace
* _windows_crashes.stack_trace_ - Multiple stack frames from the stack trace

*start* - keyword, text.text

* _memory_map.start_ - Start address of memory region
* _process_memory_map.start_ - Virtual start address (hex)

*start_interval* - keyword, text.text

* _launchd.start_interval_ - Frequency to run in seconds

*start_on_mount* - keyword, text.text

* _launchd.start_on_mount_ - Run daemon or agent every time a filesystem is mounted

*start_time* - keyword, number.long

* _docker_container_processes.start_time_ - Process start in seconds since boot (non-sleeping)
* _osquery_info.start_time_ - UNIX time in seconds when the process started
* _processes.start_time_ - Process start time in seconds since Epoch, in case of error -1

*start_type* - keyword, text.text

* _services.start_type_ - Service start type: BOOT_START, SYSTEM_START, AUTO_START, DEMAND_START, DISABLED

*started_at* - keyword, text.text

* _docker_containers.started_at_ - Container start time as string

*starting_address* - keyword, text.text

* _memory_array_mapped_addresses.starting_address_ - Physical stating address, in kilobytes, of a range of memory mapped to physical memory array
* _memory_device_mapped_addresses.starting_address_ - Physical stating address, in kilobytes, of a range of memory mapped to physical memory array

*state* - keyword

* _alf_exceptions.state_ - Firewall exception state
* _battery.state_ - One of the following: "AC Power" indicates the battery is connected to an external power source, "Battery Power" indicates that the battery is drawing internal power, "Off Line" indicates the battery is off-line or no longer connected
* _chrome_extensions.state_ - 1 if this extension is enabled
* _docker_container_processes.state_ - Process state
* _docker_containers.state_ - Container state (created, restarting, running, removing, paused, exited, dead)
* _lxd_networks.state_ - Network status
* _md_drives.state_ - State of the drive
* _process_open_sockets.state_ - TCP socket state
* _processes.state_ - Process state
* _scheduled_tasks.state_ - State of the scheduled task
* _system_extensions.state_ - System extension state
* _windows_optional_features.state_ - Installation state value. 1 == Enabled, 2 == Disabled, 3 == Absent
* _windows_security_products.state_ - State of protection

*state_timestamp* - keyword, text.text

* _windows_security_products.state_timestamp_ - Timestamp for the product state

*stateful* - keyword, number.long

* _lxd_instances.stateful_ - Whether the instance is stateful(1) or not(0)

*statename* - keyword, text.text

* _windows_optional_features.statename_ - Installation state name. 'Enabled','Disabled','Absent'

*status* - keyword, text.text

* _carves.status_ - Status of the carve, can be STARTING, PENDING, SUCCESS, or FAILED
* _chassis_info.status_ - If available, gives various operational or nonoperational statuses such as OK, Degraded, and Pred Fail.
* _deb_packages.status_ - Package status
* _docker_containers.status_ - Container status information
* _kernel_modules.status_ - Kernel module status
* _lxd_cluster_members.status_ - Status of the node (Online/Offline)
* _lxd_instances.status_ - Instance state (running, stopped, etc.)
* _md_devices.status_ - Current state of the array
* _ntdomains.status_ - The current status of the domain object.
* _process_events.status_ - OpenBSM Attribute: Status of the process
* _services.status_ - Service Current status: STOPPED, START_PENDING, STOP_PENDING, RUNNING, CONTINUE_PENDING, PAUSE_PENDING, PAUSED
* _shared_memory.status_ - Destination/attach status
* _shared_resources.status_ - String that indicates the current status of the object.
* _socket_events.status_ - Either 'succeeded', 'failed', 'in_progress' (connect() on non-blocking socket) or 'no_client' (null accept() on non-blocking socket)
* _startup_items.status_ - Startup status; either enabled or disabled

*stderr_path* - keyword, text.text

* _launchd.stderr_path_ - Pipe stderr to a target path

*stdout_path* - keyword, text.text

* _launchd.stdout_path_ - Pipe stdout to a target path

*steal* - keyword, number.long

* _cpu_time.steal_ - Time spent in other operating systems when running in a virtualized environment

*stealth_enabled* - keyword, number.long

* _alf.stealth_enabled_ - 1 If stealth mode is enabled else 0

*stibp_support_enabled* - keyword, number.long

* _kva_speculative_info.stibp_support_enabled_ - Windows uses STIBP.

*storage* - keyword, number.long

* _unified_log.storage_ - the storage category for the entry

*storage_driver* - keyword, text.text

* _docker_info.storage_driver_ - Storage driver

*store* - keyword, text.text

* _certificates.store_ - Certificate system store

*store_id* - keyword, text.text

* _certificates.store_id_ - Exists for service/user stores. Contains raw store id provided by WinAPI.

*store_location* - keyword, text.text

* _certificates.store_location_ - Certificate system store location

*strings* - keyword, text.text

* _yara.strings_ - Matching strings
* _yara_events.strings_ - Matching strings

*sub_state* - keyword, text.text

* _systemd_units.sub_state_ - The low-level unit activation state, values depend on unit type

*subclass* - keyword, text.text

* _usb_devices.subclass_ - USB Device subclass

*subject* - keyword, text.text

* _certificates.subject_ - Certificate distinguished name (deprecated, use subject2)

*subject2* - keyword, text.text

* _certificates.subject2_ - Certificate distinguished name

*subject_alternative_names* - keyword, text.text

* _curl_certificate.subject_alternative_names_ - Subject Alternative Name

*subject_info_access* - keyword, text.text

* _curl_certificate.subject_info_access_ - Subject Information Access

*subject_key_id* - keyword, text.text

* _certificates.subject_key_id_ - SKID an optionally included SHA1

*subject_key_identifier* - keyword, text.text

* _curl_certificate.subject_key_identifier_ - Subject Key Identifier

*subject_name* - keyword, text.text

* _authenticode.subject_name_ - The certificate subject name

*subkey* - keyword, text.text

* _plist.subkey_ - Intermediate key path, includes lists/dicts
* _preferences.subkey_ - Intemediate key path, includes lists/dicts

*subnet* - keyword, text.text

* _docker_networks.subnet_ - Network subnet

*subscription_id* - keyword, text.text

* _azure_instance_metadata.subscription_id_ - Azure subscription for the VM

*subscriptions* - keyword, number.long

* _osquery_events.subscriptions_ - Number of subscriptions the publisher received or subscriber used

*subsystem* - keyword, text.text

* _system_controls.subsystem_ - Subsystem ID, control type
* _unified_log.subsystem_ - the subsystem of the os_log_t used

*subsystem_model* - keyword, text.text

* _pci_devices.subsystem_model_ - Device description of PCI device subsystem

*subsystem_model_id* - keyword, text.text

* _pci_devices.subsystem_model_id_ - Model ID of PCI device subsystem

*subsystem_vendor* - keyword, text.text

* _pci_devices.subsystem_vendor_ - Vendor of PCI device subsystem

*subsystem_vendor_id* - keyword, text.text

* _pci_devices.subsystem_vendor_id_ - Vendor ID of PCI device subsystem

*success* - keyword, number.long

* _socket_events.success_ - Deprecated. Use the 'status' column instead

*suid* - keyword

* _docker_container_processes.suid_ - Saved user ID
* _process_events.suid_ - Saved user ID at process start
* _process_file_events.suid_ - Saved user ID of the process using the file
* _processes.suid_ - Unsigned saved user ID

*summary* - keyword, text.text

* _chocolatey_packages.summary_ - Package-supplied summary
* _python_packages.summary_ - Package-supplied summary

*superblock_state* - keyword, text.text

* _md_devices.superblock_state_ - State of the superblock

*superblock_update_time* - keyword, number.long

* _md_devices.superblock_update_time_ - Unix timestamp of last update

*superblock_version* - keyword, text.text

* _md_devices.superblock_version_ - Version of the superblock

*support_url* - keyword, text.text

* _windows_update_history.support_url_ - Hyperlink to the language-specific support information for an update

*swap_cached* - keyword, number.long

* _memory_info.swap_cached_ - The amount of swap, in bytes, used as cache memory

*swap_free* - keyword, number.long

* _memory_info.swap_free_ - The total amount of swap free, in bytes

*swap_ins* - keyword, number.long

* _virtual_memory_info.swap_ins_ - The total number of compressed pages that have been swapped out to disk.

*swap_limit* - keyword, number.long

* _docker_info.swap_limit_ - 1 if swap limit support is enabled. 0 otherwise

*swap_outs* - keyword, number.long

* _virtual_memory_info.swap_outs_ - The total number of compressed pages that have been swapped back in from disk.

*swap_total* - keyword, number.long

* _memory_info.swap_total_ - The total amount of swap available, in bytes

*symlink* - keyword, number.long

* _file.symlink_ - 1 if the path is a symlink, otherwise 0

*syscall* - keyword, text.text

* _bpf_process_events.syscall_ - System call name
* _bpf_socket_events.syscall_ - System call name
* _process_events.syscall_ - Syscall name: fork, vfork, clone, execve, execveat
* _seccomp_events.syscall_ - Type of the system call

*system* - keyword, number.long

* _cpu_time.system_ - Time spent in system mode

*system_cpu_usage* - keyword, number.long

* _docker_container_stats.system_cpu_usage_ - CPU system usage

*system_model* - keyword, text.text

* _kernel_panics.system_model_ - Physical system model, for example 'MacBookPro12,1 (Mac-E43C1C25D4880AD6)'

*system_time* - keyword, number.long

* _osquery_schedule.system_time_ - Total system time in milliseconds spent executing
* _processes.system_time_ - CPU time in milliseconds spent in kernel space

*tag* - keyword, text.text

* _syslog_events.tag_ - The syslog tag

*tags* - keyword, text.text

* _docker_image_history.tags_ - Comma-separated list of tags
* _docker_images.tags_ - Comma-separated list of repository tags
* _yara.tags_ - Matching tags
* _yara_events.tags_ - Matching tags

*tapping_process* - keyword, number.long

* _event_taps.tapping_process_ - The process ID of the application that created the event tap.

*target* - keyword

* _fan_speed_sensors.target_ - Target speed
* _iptables.target_ - Target that applies for this rule.

*target_name* - keyword, text.text

* _prometheus_metrics.target_name_ - Address of prometheus target

*target_path* - keyword, text.text

* _file_events.target_path_ - The path associated with the event
* _yara_events.target_path_ - The path scanned

*task* - keyword, number.long

* _windows_eventlog.task_ - Task value associated with the event
* _windows_events.task_ - Task value associated with the event

*team* - keyword, text.text

* _system_extensions.team_ - Signing team ID

*team_id* - keyword, text.text

* _es_process_events.team_id_ - Team identifier of the process

*team_identifier* - keyword, text.text

* _signature.team_identifier_ - The team signing identifier sealed into the signature

*temporarily_disabled* - keyword, number.long

* _wifi_networks.temporarily_disabled_ - 1 if this network is temporarily disabled, 0 otherwise

*terminal* - keyword, text.text

* _user_events.terminal_ - The network protocol ID

*threads* - keyword, number.long

* _docker_container_processes.threads_ - Number of threads used by process
* _processes.threads_ - Number of threads used by process

*throttled* - keyword, number.long

* _virtual_memory_info.throttled_ - Total number of throttled pages.

*tid* - keyword, number.long

* _bpf_process_events.tid_ - Thread ID
* _bpf_socket_events.tid_ - Thread ID
* _unified_log.tid_ - the tid of the thread that made the entry
* _windows_crashes.tid_ - Thread ID of the crashed thread
* _windows_eventlog.tid_ - Thread ID which emitted the event record

*time* - keyword

* _apparmor_events.time_ - Time of execution in UNIX time
* _asl.time_ - Unix timestamp.  Set automatically
* _bpf_process_events.time_ - Time of execution in UNIX time
* _bpf_socket_events.time_ - Time of execution in UNIX time
* _carves.time_ - Time at which the carve was kicked off
* _disk_events.time_ - Time of appearance/disappearance in UNIX time
* _docker_container_processes.time_ - Cumulative CPU time. [DD-]HH:MM:SS format
* _es_process_events.time_ - Time of execution in UNIX time
* _es_process_file_events.time_ - Time of execution in UNIX time
* _file_events.time_ - Time of file event
* _hardware_events.time_ - Time of hardware event
* _kernel_panics.time_ - Formatted time of the event
* _last.time_ - Entry timestamp
* _logged_in_users.time_ - Time entry was made
* _ntfs_journal_events.time_ - Time of file event
* _package_install_history.time_ - Label date as UNIX timestamp
* _powershell_events.time_ - Timestamp the event was received by the osquery event publisher
* _process_etw_events.time_ - Event timestamp in Unix format
* _process_events.time_ - Time of execution in UNIX time
* _process_file_events.time_ - Time of execution in UNIX time
* _seccomp_events.time_ - Time of execution in UNIX time
* _selinux_events.time_ - Time of execution in UNIX time
* _shell_history.time_ - Entry timestamp. It could be absent, default value is 0.
* _socket_events.time_ - Time of execution in UNIX time
* _syslog_events.time_ - Current unix epoch time
* _user_events.time_ - Time of execution in UNIX time
* _user_interaction_events.time_ - Time
* _windows_events.time_ - Timestamp the event was received
* _xprotect_reports.time_ - Quarantine alert time
* _yara_events.time_ - Time of the scan

*time_nano_sec* - keyword, number.long

* _asl.time_nano_sec_ - Nanosecond time.

*time_range* - keyword, text.text

* _windows_eventlog.time_range_ - System time to selectively filter the events

*time_windows* - keyword, number.long

* _process_etw_events.time_windows_ - Event timestamp in Windows format

*timeout* - keyword, text.text

* _authorizations.timeout_ - Label top-level key
* _curl_certificate.timeout_ - Set this value to the timeout in seconds to complete the TLS handshake (default 4s, use 0 for no timeout)
* _kernel_keys.timeout_ - The amount of time until the key will expire, expressed in human-readable form. The string perm here means that the key is permanent (no timeout).  The string expd means that the key has already expired.

*timestamp* - keyword, text.text
