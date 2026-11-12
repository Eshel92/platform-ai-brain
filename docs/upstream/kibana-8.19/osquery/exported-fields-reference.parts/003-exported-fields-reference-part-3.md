<!-- Part 3 of 6 of osquery/exported-fields-reference.md (split because the page is big). -->

* _windows_update_history.hresult_ - HRESULT value that is returned from the operation on an update

*http_proxy* - keyword, text.text

* _docker_info.http_proxy_ - HTTP proxy

*https_proxy* - keyword, text.text

* _docker_info.https_proxy_ - HTTPS proxy

*hwaddr* - keyword, text.text

* _lxd_networks.hwaddr_ - Hardware address for this network

*iam_arn* - keyword, text.text

* _ec2_instance_metadata.iam_arn_ - If there is an IAM role associated with the instance, contains instance profile ARN

*ibrs_support_enabled* - keyword, number.long

* _kva_speculative_info.ibrs_support_enabled_ - Windows uses IBRS.

*ibytes* - keyword, number.long

* _interface_details.ibytes_ - Input bytes

*icmp_types_codes* - keyword, text.text

* _windows_firewall_rules.icmp_types_codes_ - ICMP types and codes for the rule

*icon_mode* - keyword, number.long

* _quicklook_cache.icon_mode_ - Thumbnail icon mode

*id* - keyword, text.text

* _disk_info.id_ - The unique identifier of the drive on the system.
* _dns_resolvers.id_ - Address type index or order
* _docker_container_envs.id_ - Container ID
* _docker_container_fs_changes.id_ - Container ID
* _docker_container_labels.id_ - Container ID
* _docker_container_mounts.id_ - Container ID
* _docker_container_networks.id_ - Container ID
* _docker_container_ports.id_ - Container ID
* _docker_container_processes.id_ - Container ID
* _docker_container_stats.id_ - Container ID
* _docker_containers.id_ - Container ID
* _docker_image_history.id_ - Image ID
* _docker_image_labels.id_ - Image ID
* _docker_image_layers.id_ - Image ID
* _docker_images.id_ - Image ID
* _docker_info.id_ - Docker system ID
* _docker_network_labels.id_ - Network ID
* _docker_networks.id_ - Network ID
* _iokit_devicetree.id_ - IOKit internal registry ID
* _iokit_registry.id_ - IOKit internal registry ID
* _lxd_images.id_ - Image ID
* _systemd_units.id_ - Unique unit identifier

*identifier* - keyword, text.text

* _browser_plugins.identifier_ - Plugin identifier
* _chrome_extension_content_scripts.identifier_ - Extension identifier
* _chrome_extensions.identifier_ - Extension identifier, computed from its manifest. Empty in case of error.
* _crashes.identifier_ - Identifier of the crashed process
* _firefox_addons.identifier_ - Addon identifier
* _safari_extensions.identifier_ - Extension identifier
* _signature.identifier_ - The signing identifier sealed into the signature
* _system_extensions.identifier_ - Identifier name
* _xprotect_meta.identifier_ - Browser plugin or extension identifier

*identifying_number* - keyword, text.text

* _programs.identifying_number_ - Product identification such as a serial number on software, or a die number on a hardware chip.

*identity* - keyword, text.text

* _xprotect_entries.identity_ - XProtect identity (SHA1) of content

*idle* - keyword, number.long

* _cpu_time.idle_ - Time spent in the idle task

*idrops* - keyword, number.long

* _interface_details.idrops_ - Input drops

*idx* - keyword, number.long

* _kernel_extensions.idx_ - Extension load tag or index

*ierrors* - keyword, number.long

* _interface_details.ierrors_ - Input errors

*image* - keyword, text.text

* _docker_containers.image_ - Docker image (name) used to launch this container
* _drivers.image_ - Path to driver image file

*image_id* - keyword, text.text

* _docker_containers.image_id_ - Docker image ID

*images* - keyword, number.long

* _docker_info.images_ - Number of images

*inactive* - keyword, number.long

* _memory_info.inactive_ - The total amount of buffer or page cache memory, in bytes, that are free and available
* _shadow.inactive_ - Number of days after password expires until account is blocked
* _virtual_memory_info.inactive_ - Total number of inactive pages.

*include_remote* - keyword, number.long

* _users.include_remote_ - 1 to include remote (LDAP/AD) accounts (default 0). Warning: without any uid/username filtering it may list whole LDAP directories

*inetd_compatibility* - keyword, text.text

* _launchd.inetd_compatibility_ - Run this daemon or agent as it was launched from inetd

*inf* - keyword, text.text

* _drivers.inf_ - Associated inf file

*info* - keyword, text.text

* _apparmor_events.info_ - Additional information

*info_access* - keyword, text.text

* _curl_certificate.info_access_ - Authority Information Access

*info_string* - keyword, text.text

* _apps.info_string_ - Info properties CFBundleGetInfoString label

*inherited_from* - keyword, text.text

* _ntfs_acl_permissions.inherited_from_ - The inheritance policy of the ACE.

*iniface* - keyword, text.text

* _iptables.iniface_ - Input interface for the rule.

*iniface_mask* - keyword, text.text

* _iptables.iniface_mask_ - Input interface mask for the rule.

*inode* - keyword, number.long

* _device_file.inode_ - Filesystem inode number
* _device_hash.inode_ - Filesystem inode number
* _file.inode_ - Filesystem inode number
* _file_events.inode_ - Filesystem inode number
* _process_memory_map.inode_ - Mapped path inode, 0 means uninitialized (BSS)
* _process_open_pipes.inode_ - Pipe inode number
* _quicklook_cache.inode_ - Parsed file ID (inode) from fs_id

*inodes* - keyword, number.long

* _device_partitions.inodes_ - Number of meta nodes
* _mounts.inodes_ - Mounted device used inodes

*inodes_free* - keyword, number.long

* _mounts.inodes_free_ - Mounted device free inodes

*inodes_total* - keyword, number.long

* _lxd_storage_pools.inodes_total_ - Total number of inodes available in this storage pool

*inodes_used* - keyword, number.long

* _lxd_storage_pools.inodes_used_ - Number of inodes used

*input_eax* - keyword, text.text

* _cpuid.input_eax_ - Value of EAX used

*install_date* - keyword

* _os_version.install_date_ - The install date of the OS.
* _patches.install_date_ - Indicates when the patch was installed. Lack of a value does not indicate that the patch was not installed.
* _programs.install_date_ - Date that this product was installed on the system. 
* _shared_resources.install_date_ - Indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

*install_location* - keyword, text.text

* _programs.install_location_ - The installation location directory of the product.

*install_source* - keyword, text.text

* _programs.install_source_ - The installation source of the product.

*install_time* - keyword

* _appcompat_shims.install_time_ - Install time of the SDB
* _chrome_extensions.install_time_ - Extension install time, in its original Webkit format
* _package_receipts.install_time_ - Timestamp of install time
* _rpm_packages.install_time_ - When the package was installed

*install_timestamp* - keyword, number.long

* _chrome_extensions.install_timestamp_ - Extension install time, converted to unix time

*installed_at* - keyword, number.long

* _vscode_extensions.installed_at_ - Installed Timestamp

*installed_by* - keyword, text.text

* _patches.installed_by_ - The system context in which the patch as installed.

*installed_on* - keyword, text.text

* _patches.installed_on_ - The date when the patch was installed.

*installer_name* - keyword, text.text

* _package_receipts.installer_name_ - Name of installer process

*instance_id* - keyword, text.text

* _ec2_instance_metadata.instance_id_ - EC2 instance ID
* _ec2_instance_tags.instance_id_ - EC2 instance ID
* _osquery_info.instance_id_ - Unique, long-lived ID per instance of osquery
* _ycloud_instance_metadata.instance_id_ - Unique identifier for the VM

*instance_identifier* - keyword, text.text

* _hvci_status.instance_identifier_ - The instance ID of Device Guard.

*instance_type* - keyword, text.text

* _ec2_instance_metadata.instance_type_ - EC2 instance type

*instances* - keyword, number.long

* _pipes.instances_ - Number of instances of the named pipe

*interface* - keyword, text.text

* _arp_cache.interface_ - Interface of the network for the MAC
* _interface_addresses.interface_ - Interface name
* _interface_details.interface_ - Interface name
* _interface_ipv6.interface_ - Interface name
* _routes.interface_ - Route local interface
* _wifi_status.interface_ - Name of the interface
* _wifi_survey.interface_ - Name of the interface

*interleave_data_depth* - keyword, number.long

* _memory_device_mapped_addresses.interleave_data_depth_ - The max number of consecutive rows from memory device that are accessed in a single interleave transfer; 0 indicates device is non-interleave

*interleave_position* - keyword, number.long

* _memory_device_mapped_addresses.interleave_position_ - The position of the device in a interleave, i.e. 0 indicates non-interleave, 1 indicates 1st interleave, 2 indicates 2nd interleave, etc.

*internal* - keyword, number.long

* _osquery_registry.internal_ - 1 If the plugin is internal else 0

*internet_settings* - keyword, text.text

* _windows_security_center.internet_settings_ - The health of the Internet Settings

*internet_sharing* - keyword, number.long

* _sharing_preferences.internet_sharing_ - 1 If internet sharing is enabled else 0

*interval* - keyword, number.long

* _docker_container_stats.interval_ - Difference between read and preread in nano-seconds
* _osquery_schedule.interval_ - The interval in seconds to run this query, not an exact interval

*iowait* - keyword, number.long

* _cpu_time.iowait_ - Time spent waiting for I/O to complete

*ip* - keyword, text.text

* _seccomp_events.ip_ - Instruction pointer value

*ip_address* - keyword, text.text

* _docker_container_networks.ip_address_ - IP address

*ip_prefix_len* - keyword, number.long

* _docker_container_networks.ip_prefix_len_ - IP subnet prefix length

*ipackets* - keyword, number.long

* _interface_details.ipackets_ - Input packets

*ipc_namespace* - keyword, text.text

* _docker_containers.ipc_namespace_ - IPC namespace
* _process_namespaces.ipc_namespace_ - ipc namespace inode

*ipv4_address* - keyword, text.text

* _lxd_networks.ipv4_address_ - IPv4 address

*ipv4_forwarding* - keyword, number.long

* _docker_info.ipv4_forwarding_ - 1 if IPv4 forwarding is enabled. 0 otherwise

*ipv4_internet* - keyword, number.long

* _connectivity.ipv4_internet_ - True if any interface is connected to the Internet via IPv4

*ipv4_local_network* - keyword, number.long

* _connectivity.ipv4_local_network_ - True if any interface is connected to a routed network via IPv4

*ipv4_no_traffic* - keyword, number.long

* _connectivity.ipv4_no_traffic_ - True if any interface is connected via IPv4, but has seen no traffic

*ipv4_subnet* - keyword, number.long

* _connectivity.ipv4_subnet_ - True if any interface is connected to the local subnet via IPv4

*ipv6_address* - keyword, text.text

* _docker_container_networks.ipv6_address_ - IPv6 address
* _lxd_networks.ipv6_address_ - IPv6 address

*ipv6_gateway* - keyword, text.text

* _docker_container_networks.ipv6_gateway_ - IPv6 gateway

*ipv6_internet* - keyword, number.long

* _connectivity.ipv6_internet_ - True if any interface is connected to the Internet via IPv6

*ipv6_local_network* - keyword, number.long

* _connectivity.ipv6_local_network_ - True if any interface is connected to a routed network via IPv6

*ipv6_no_traffic* - keyword, number.long

* _connectivity.ipv6_no_traffic_ - True if any interface is connected via IPv6, but has seen no traffic

*ipv6_prefix_len* - keyword, number.long

* _docker_container_networks.ipv6_prefix_len_ - IPv6 subnet prefix length

*ipv6_subnet* - keyword, number.long

* _connectivity.ipv6_subnet_ - True if any interface is connected to the local subnet via IPv6

*irq* - keyword, number.long

* _cpu_time.irq_ - Time spent servicing interrupts

*is_active* - keyword, number.long

* _running_apps.is_active_ - (DEPRECATED)

*is_hidden* - keyword, number.long

* _groups.is_hidden_ - IsHidden attribute set in OpenDirectory
* _users.is_hidden_ - IsHidden attribute set in OpenDirectory

*iso_8601* - keyword, text.text

* _time.iso_8601_ - Current time (ISO format) in UTC

*issuer* - keyword, text.text

* _certificates.issuer_ - Certificate issuer distinguished name (deprecated, use issuer2)

*issuer2* - keyword, text.text

* _certificates.issuer2_ - Certificate issuer distinguished name

*issuer_alternative_names* - keyword, text.text

* _curl_certificate.issuer_alternative_names_ - Issuer Alternative Name

*issuer_common_name* - keyword, text.text

* _curl_certificate.issuer_common_name_ - Issuer common name

*issuer_name* - keyword, text.text

* _authenticode.issuer_name_ - The certificate issuer name

*issuer_organization* - keyword, text.text

* _curl_certificate.issuer_organization_ - Issuer organization

*issuer_organization_unit* - keyword, text.text

* _curl_certificate.issuer_organization_unit_ - Issuer organization unit

*job_id* - keyword, number.long

* _systemd_units.job_id_ - Next queued job id

*job_path* - keyword, text.text

* _systemd_units.job_path_ - The object path for the job

*job_type* - keyword, text.text

* _systemd_units.job_type_ - Job type

*json_cmdline* - keyword, text.text

* _bpf_process_events.json_cmdline_ - Command line arguments, in JSON format

*keep_alive* - keyword, text.text

* _launchd.keep_alive_ - Should the process be restarted if killed

*kernel_extensions* - keyword, number.long

* _secureboot.kernel_extensions_ - (Apple Silicon) Allow user management of kernel extensions from identified developers (1 if allowed)

*kernel_memory* - keyword, number.long

* _docker_info.kernel_memory_ - 1 if kernel memory limit support is enabled. 0 otherwise

*kernel_version* - keyword, text.text

* _docker_info.kernel_version_ - Kernel version
* _docker_version.kernel_version_ - Kernel version
* _kernel_panics.kernel_version_ - Version of the system kernel

*key* - keyword, text.text

* _authorized_keys.key_ - Key encoded as base64
* _azure_instance_tags.key_ - The tag key
* _chrome_extensions.key_ - The extension key, from the manifest file
* _docker_container_envs.key_ - Environment variable name
* _docker_container_labels.key_ - Label key
* _docker_image_labels.key_ - Label key
* _docker_network_labels.key_ - Label key
* _docker_volume_labels.key_ - Label key
* _ec2_instance_tags.key_ - Tag key
* _extended_attributes.key_ - Name of the value generated from the extended attribute
* _known_hosts.key_ - parsed authorized keys line
* _launchd_overrides.key_ - Name of the override key
* _lxd_instance_config.key_ - Configuration parameter name
* _lxd_instance_devices.key_ - Device info param name
* _mdls.key_ - Name of the metadata key
* _plist.key_ - Preference top-level key
* _power_sensors.key_ - The SMC key on macOS
* _preferences.key_ - Preference top-level key
* _process_envs.key_ - Environment variable name
* _registry.key_ - Name of the key to search for
* _selinux_settings.key_ - Key or class name.
* _smc_keys.key_ - 4-character key
* _temperature_sensors.key_ - The SMC key on macOS

*key_algorithm* - keyword, text.text

* _certificates.key_algorithm_ - Key algorithm used

*key_file* - keyword, text.text

* _authorized_keys.key_file_ - Path to the authorized_keys file
* _known_hosts.key_file_ - Path to known_hosts file

*key_group_name* - keyword, text.text

* _user_ssh_keys.key_group_name_ - The group of the private key. Supported for a subset of key_types implemented by OpenSSL

*key_length* - keyword, number.long

* _user_ssh_keys.key_length_ - The cryptographic length of the cryptosystem to which the private key belongs, in bits. Definition of cryptographic length is specific to cryptosystem. -1 if unavailable

*key_security_bits* - keyword, number.long

* _user_ssh_keys.key_security_bits_ - The number of security bits of the private key, bits of security as defined in NIST SP800-57. -1 if unavailable

*key_strength* - keyword, text.text

* _certificates.key_strength_ - Key size used for RSA/DSA, or curve name

*key_type* - keyword, text.text

* _user_ssh_keys.key_type_ - The type of the private key. One of [rsa, dsa, dh, ec, hmac, cmac], or the empty string.

*key_usage* - keyword, text.text

* _certificates.key_usage_ - Certificate key usage and extended key usage
* _curl_certificate.key_usage_ - Usage of key in certificate

*keychain_path* - keyword, text.text

* _keychain_acls.keychain_path_ - The path of the keychain

*keyword* - keyword, text.text

* _portage_keywords.keyword_ - The keyword applied to the package

*keywords* - keyword, text.text

* _windows_eventlog.keywords_ - A bitmask of the keywords defined in the event
* _windows_events.keywords_ - A bitmask of the keywords defined in the event

*kva_shadow_enabled* - keyword, number.long

* _kva_speculative_info.kva_shadow_enabled_ - Kernel Virtual Address shadowing is enabled.

*kva_shadow_inv_pcid* - keyword, number.long

* _kva_speculative_info.kva_shadow_inv_pcid_ - Kernel VA INVPCID is enabled.

*kva_shadow_pcid* - keyword, number.long

* _kva_speculative_info.kva_shadow_pcid_ - Kernel VA PCID flushing optimization is enabled.

*kva_shadow_user_global* - keyword, number.long

* _kva_speculative_info.kva_shadow_user_global_ - User pages are marked as global.

*label* - keyword, text.text

* _apparmor_events.label_ - AppArmor label
* _augeas.label_ - The label of the configuration item
* _authorization_mechanisms.label_ - Label of the authorization right
* _authorizations.label_ - Item name, usually in reverse domain format
* _block_devices.label_ - Block device label string
* _device_partitions.label_ - The partition name as stored in the partition table
* _keychain_acls.label_ - An optional label tag that may be included with the keychain entry
* _keychain_items.label_ - Generic item name
* _launchd.label_ - Daemon or agent service name
* _launchd_overrides.label_ - Daemon or agent service name
* _quicklook_cache.label_ - Parsed version 'gen' field
* _sandboxes.label_ - UTI-format bundle or label ID

*language* - keyword, text.text

* _programs.language_ - The language of the product.

*last_change* - keyword, number.long

* _interface_details.last_change_ - Time of last device modification (optional)
* _shadow.last_change_ - Date of last password change (starting from UNIX epoch date)

*last_connected* - keyword, number.long

* _wifi_networks.last_connected_ - Last time this network was connected to as a unix_time

*last_executed* - keyword, number.long

* _osquery_schedule.last_executed_ - UNIX time stamp in seconds of the last completed execution

*last_execution_time* - keyword, number.long

* _background_activities_moderator.last_execution_time_ - Most recent time application was executed.
* _userassist.last_execution_time_ - Most recent time application was executed.

*last_hit_date* - keyword, number.long

* _quicklook_cache.last_hit_date_ - Apple date format for last thumbnail cache hit

*last_loaded* - keyword, text.text

* _kernel_panics.last_loaded_ - Last loaded module before panic

*last_memory* - keyword, number.long

* _osquery_schedule.last_memory_ - Resident memory in bytes left allocated after collecting results of the latest execution

*last_opened_time* - keyword

* _apps.last_opened_time_ - The time that the app was last used
* _office_mru.last_opened_time_ - Most recent opened time file was opened

*last_run_code* - keyword, text.text

* _scheduled_tasks.last_run_code_ - Exit status code of the last task run

*last_run_message* - keyword, text.text

* _scheduled_tasks.last_run_message_ - Exit status message of the last task run

*last_run_time* - keyword, number.long

* _prefetch.last_run_time_ - Most recent time application was run.
* _scheduled_tasks.last_run_time_ - Timestamp the task last ran

*last_system_time* - keyword, number.long

* _osquery_schedule.last_system_time_ - System time in milliseconds of the latest execution

*last_unloaded* - keyword, text.text

* _kernel_panics.last_unloaded_ - Last unloaded module before panic

*last_used_at* - keyword, text.text

* _lxd_images.last_used_at_ - ISO time for the most recent use of this image in terms of container spawn

*last_user_time* - keyword, number.long

* _osquery_schedule.last_user_time_ - User time in milliseconds of the latest execution

*last_wall_time_ms* - keyword, number.long

* _osquery_schedule.last_wall_time_ms_ - Wall time in milliseconds of the latest execution

*launch_type* - keyword, text.text

* _xprotect_entries.launch_type_ - Launch services content type

*layer_id* - keyword, text.text

* _docker_image_layers.layer_id_ - Layer ID

*layer_order* - keyword, number.long

* _docker_image_layers.layer_order_ - Layer Order (1 = base layer)

*level* - keyword

* _asl.level_ - Log level number.  See levels in asl.h.
* _unified_log.level_ - the severity level of the entry
* _windows_eventlog.level_ - Severity level associated with the event
* _windows_events.level_ - The severity level associated with the event

*license* - keyword, text.text

* _chocolatey_packages.license_ - License under which package is launched
* _npm_packages.license_ - License under which package is launched
* _python_packages.license_ - License under which package is launched

*link_speed* - keyword, number.long

* _interface_details.link_speed_ - Interface speed in Mb/s

*linked_against* - keyword, text.text

* _kernel_extensions.linked_against_ - Indexes of extensions this extension is linked against

*load_percentage* - keyword, number.long

* _cpu_info.load_percentage_ - The current percentage of utilization of the CPU.

*load_state* - keyword, text.text

* _systemd_units.load_state_ - Reflects whether the unit definition was properly loaded

*local_address* - keyword, text.text

* _bpf_socket_events.local_address_ - Local address associated with socket
* _process_open_sockets.local_address_ - Socket local address
* _socket_events.local_address_ - Local address associated with socket

*local_addresses* - keyword, text.text

* _windows_firewall_rules.local_addresses_ - Local addresses for the rule

*local_hostname* - keyword, text.text

* _ec2_instance_metadata.local_hostname_ - Private IPv4 DNS hostname of the first interface of this instance
* _system_info.local_hostname_ - Local hostname (optional)

*local_ipv4* - keyword, text.text

* _ec2_instance_metadata.local_ipv4_ - Private IPv4 address of the first interface of this instance

*local_port* - keyword, number.long

* _bpf_socket_events.local_port_ - Local network protocol port number
* _process_open_sockets.local_port_ - Socket local port
* _socket_events.local_port_ - Local network protocol port number

*local_ports* - keyword, text.text

* _windows_firewall_rules.local_ports_ - Local ports for the rule

*local_timezone* - keyword, text.text

* _time.local_timezone_ - Current local timezone in of the system

*location* - keyword, text.text

* _azure_instance_metadata.location_ - Azure Region the VM is running in
* _firefox_addons.location_ - Global, profile location
* _memory_arrays.location_ - Physical location of the memory array
* _package_receipts.location_ - Optional relative install path on volume

*lock* - keyword, text.text

* _chassis_info.lock_ - If TRUE, the frame is equipped with a lock.

*lock_status* - keyword, number.long

* _bitlocker_info.lock_status_ - The accessibility status of the drive from Windows.

*locked* - keyword, number.long

* _shared_memory.locked_ - 1 if segment is locked else 0

*lockout_bad_count* - keyword, number.long

* _security_profile_info.lockout_bad_count_ - Number of failed logon attempts after which a user account MUST be locked out

*log_file_disk_quota_mb* - keyword, number.long

* _carbon_black_info.log_file_disk_quota_mb_ - Event file disk quota in MB

*log_file_disk_quota_percentage* - keyword, number.long

* _carbon_black_info.log_file_disk_quota_percentage_ - Event file disk quota in a percentage

*logging_driver* - keyword, text.text

* _docker_info.logging_driver_ - Logging driver

*logging_enabled* - keyword, number.long

* _alf.logging_enabled_ - 1 If logging mode is enabled else 0

*logging_option* - keyword, number.long

* _alf.logging_option_ - Firewall logging option

*logical_processors* - keyword, number.long

* _cpu_info.logical_processors_ - The number of logical processors of the CPU.

*logon_domain* - keyword, text.text

* _logon_sessions.logon_domain_ - The name of the domain used to authenticate the owner of the logon session.

*logon_id* - keyword, number.long

* _logon_sessions.logon_id_ - A locally unique identifier (LUID) that identifies a logon session.

*logon_script* - keyword, text.text

* _logon_sessions.logon_script_ - The script used for logging on.

*logon_server* - keyword, text.text

* _logon_sessions.logon_server_ - The name of the server used to authenticate the owner of the logon session.

*logon_sid* - keyword, text.text

* _logon_sessions.logon_sid_ - The user's security identifier (SID).

*logon_time* - keyword, number.long

* _logon_sessions.logon_time_ - The time the session owner logged on.

*logon_to_change_password* - keyword, number.long

* _security_profile_info.logon_to_change_password_ - Determines if logon session is required to change the password

*logon_type* - keyword, text.text

* _logon_sessions.logon_type_ - The logon method.

*lsa_anonymous_name_lookup* - keyword, number.long

* _security_profile_info.lsa_anonymous_name_lookup_ - Determines if an anonymous user is allowed to query the local LSA policy

*mac* - keyword, text.text

* _arp_cache.mac_ - MAC address of broadcasted address
* _ec2_instance_metadata.mac_ - MAC address for the first network interface of this EC2 instance
* _interface_details.mac_ - MAC of interface (optional)

*mac_address* - keyword, text.text

* _docker_container_networks.mac_address_ - MAC address

*machine_name* - keyword, text.text

* _windows_crashes.machine_name_ - Name of the machine where the crash happened

*magic_db_files* - keyword, text.text

* _magic.magic_db_files_ - Colon(:) separated list of files where the magic db file can be found. By default one of the following is used: /usr/share/file/magic/magic, /usr/share/misc/magic or /usr/share/misc/magic.mgc

*main* - keyword, number.long

* _connected_displays.main_ - If the display is the main display.

*maintainer* - keyword, text.text

* _apt_sources.maintainer_ - Repository maintainer
* _deb_packages.maintainer_ - Package maintainer

*major* - keyword, number.long

* _os_version.major_ - Major release version

*major_version* - keyword, number.long

* _windows_crashes.major_version_ - Windows major version of the machine

*managed* - keyword, number.long

* _lxd_networks.managed_ - 1 if network created by LXD, 0 otherwise

*mandatory_label* - keyword, text.text

* _process_etw_events.mandatory_label_ - Primary token mandatory label sid - Present only on ProcessStart events

*manifest_hash* - keyword, text.text

* _chrome_extensions.manifest_hash_ - The SHA256 hash of the manifest.json file

*manifest_json* - keyword, text.text

* _chrome_extensions.manifest_json_ - The manifest file of the extension

*manual* - keyword, number.long

* _managed_policies.manual_ - 1 if policy was loaded manually, otherwise 0

*manufacture_date* - keyword, number.long

* _battery.manufacture_date_ - The date the battery was manufactured UNIX Epoch

*manufactured_week* - keyword, number.long

* _connected_displays.manufactured_week_ - The manufacture week of the display. This field is 0 if not supported

*manufactured_year* - keyword, number.long

* _connected_displays.manufactured_year_ - The manufacture year of the display. This field is 0 if not supported

*manufacturer* - keyword, text.text

* _battery.manufacturer_ - The battery manufacturer's name
* _chassis_info.manufacturer_ - The manufacturer of the chassis.
* _cpu_info.manufacturer_ - The manufacturer of the CPU.
* _disk_info.manufacturer_ - The manufacturer of the disk.
* _drivers.manufacturer_ - Device manufacturer
* _interface_details.manufacturer_ - Name of the network adapter's manufacturer.
* _memory_devices.manufacturer_ - Manufacturer ID string
* _video_info.manufacturer_ - The manufacturer of the gpu.

*manufacturer_id* - keyword, number.long

* _tpm_info.manufacturer_id_ - TPM manufacturers ID

*manufacturer_name* - keyword, text.text

* _tpm_info.manufacturer_name_ - TPM manufacturers name

*manufacturer_version* - keyword, text.text

* _tpm_info.manufacturer_version_ - TPM version

*mask* - keyword, text.text

* _interface_addresses.mask_ - Interface netmask
* _portage_keywords.mask_ - If the package is masked

*match* - keyword, text.text

* _chrome_extension_content_scripts.match_ - The pattern that the script is matched against
* _iptables.match_ - Matching rule that applies.

*matches* - keyword, text.text

* _yara.matches_ - List of YARA matches
* _yara_events.matches_ - List of YARA matches

*max* - keyword, number.long

* _fan_speed_sensors.max_ - Maximum speed
* _shadow.max_ - Maximum number of days between password changes

*max_capacity* - keyword, number.long

* _battery.max_capacity_ - The battery's actual capacity when it is fully charged in mAh
* _memory_arrays.max_capacity_ - Maximum capacity of array in gigabytes

*max_clock_speed* - keyword, number.long

* _cpu_info.max_clock_speed_ - The maximum possible frequency of the CPU.

*max_instances* - keyword, number.long

* _pipes.max_instances_ - The maximum number of instances creatable for this pipe

*max_results* - keyword, number.long

* _windows_search.max_results_ - Maximum number of results returned by windows api, set to -1 for unlimited

*max_rows* - keyword, number.long

* _unified_log.max_rows_ - the max number of rows returned (defaults to 100)

*max_speed* - keyword, number.long

* _memory_devices.max_speed_ - Max speed of memory device in megatransfers per second (MT/s)

*max_voltage* - keyword, number.long

* _memory_devices.max_voltage_ - Maximum operating voltage of device in millivolts

*maximum_allowed* - keyword, number.long

* _shared_resources.maximum_allowed_ - Limit on the maximum number of users allowed to use this resource concurrently. The value is only valid if the AllowMaximum property is set to FALSE.

*maximum_password_age* - keyword, number.long

* _security_profile_info.maximum_password_age_ - Determines the maximum number of days that a password can be used before the client requires the user to change it

*md5* - keyword, text.text

* _acpi_tables.md5_ - MD5 hash of table content
* _device_hash.md5_ - MD5 hash of provided inode data
* _file_events.md5_ - The MD5 of the file after change
* _hash.md5_ - MD5 hash of provided filesystem data
* _smbios_tables.md5_ - MD5 hash of table entry

*md_device_name* - keyword, text.text

* _md_drives.md_device_name_ - md device name

*mdm_managed* - keyword, number.long

* _system_extensions.mdm_managed_ - 1 if managed by MDM system extension payload configuration, 0 otherwise

*mdm_operations* - keyword, number.long

* _secureboot.mdm_operations_ - (Apple Silicon) Allow remote (MDM) management of kernel extensions and automatic software updates (1 if allowed)

*mechanism* - keyword, text.text

* _authorization_mechanisms.mechanism_ - Name of the mechanism that will be called

*media_name* - keyword, text.text

* _disk_events.media_name_ - Disk event media name string

*mem* - keyword, number.double

* _docker_container_processes.mem_ - Memory utilization as percentage

*member_config_description* - keyword, text.text

* _lxd_cluster.member_config_description_ - Config description

*member_config_entity* - keyword, text.text

* _lxd_cluster.member_config_entity_ - Type of configuration parameter for this node

*member_config_key* - keyword, text.text

* _lxd_cluster.member_config_key_ - Config key

*member_config_name* - keyword, text.text

* _lxd_cluster.member_config_name_ - Name of configuration parameter

*member_config_value* - keyword, text.text

* _lxd_cluster.member_config_value_ - Config value

*memory* - keyword, number.long

* _docker_info.memory_ - Total memory

*memory_array_error_address* - keyword, text.text

* _memory_error_info.memory_array_error_address_ - 32 bit physical address of the error based on the addressing of the bus to which the memory array is connected

*memory_array_handle* - keyword, text.text

* _memory_array_mapped_addresses.memory_array_handle_ - Handle of the memory array associated with this structure

*memory_array_mapped_address_handle* - keyword, text.text

* _memory_device_mapped_addresses.memory_array_mapped_address_handle_ - Handle of the memory array mapped address to which this device range is mapped to

*memory_available* - keyword, number.long

* _memory_info.memory_available_ - The amount of physical RAM, in bytes, available for starting new applications, without swapping

*memory_cached* - keyword, number.long

* _docker_container_stats.memory_cached_ - Memory cached

*memory_device_handle* - keyword, text.text

* _memory_device_mapped_addresses.memory_device_handle_ - Handle of the memory device structure associated with this structure

*memory_error_correction* - keyword, text.text

* _memory_arrays.memory_error_correction_ - Primary hardware error correction or detection method supported

*memory_error_info_handle* - keyword, text.text

* _memory_arrays.memory_error_info_handle_ - Handle, or instance number, associated with any error that was detected for the array

*memory_free* - keyword, number.long

* _memory_info.memory_free_ - The amount of physical RAM, in bytes, left unused by the system

*memory_limit* - keyword, number.long

* _docker_container_stats.memory_limit_ - Memory limit
* _docker_info.memory_limit_ - 1 if memory limit support is enabled. 0 otherwise

*memory_max_usage* - keyword, number.long

* _docker_container_stats.memory_max_usage_ - Memory maximum usage

*memory_total* - keyword, number.long

* _memory_info.memory_total_ - Total amount of physical RAM, in bytes

*memory_type* - keyword, text.text

* _memory_devices.memory_type_ - Type of memory used

*memory_type_details* - keyword, text.text

* _memory_devices.memory_type_details_ - Additional details for memory device

*memory_usage* - keyword, number.long

* _docker_container_stats.memory_usage_ - Memory usage

*message* - keyword, text.text

* _apparmor_events.message_ - Raw audit message
* _asl.message_ - Message text.
* _lxd_cluster_members.message_ - Message from the node (Online/Offline)
* _selinux_events.message_ - Message
* _syslog_events.message_ - The syslog message
* _unified_log.message_ - composed message
* _user_events.message_ - Message from the event

*metadata_endpoint* - keyword, text.text

* _ycloud_instance_metadata.metadata_endpoint_ - Endpoint used to fetch VM metadata

*metalink* - keyword, text.text

* _yum_sources.metalink_ - Metalink URL

*method* - keyword, text.text

* _curl.method_ - The HTTP method for the request

*metric* - keyword, number.long

* _interface_details.metric_ - Metric based on the speed of the interface
* _routes.metric_ - Cost of route. Lowest is preferred

*metric_name* - keyword, text.text

* _prometheus_metrics.metric_name_ - Name of collected Prometheus metric

*metric_value* - keyword, number.double

* _prometheus_metrics.metric_value_ - Value of collected Prometheus metric

*mft_entry* - keyword, number.long

* _shellbags.mft_entry_ - Directory master file table entry.

*mft_sequence* - keyword, number.long

* _shellbags.mft_sequence_ - Directory master file table sequence.

*mime_encoding* - keyword, text.text

* _magic.mime_encoding_ - MIME encoding data from libmagic

*mime_type* - keyword, text.text

* _magic.mime_type_ - MIME type data from libmagic

*min* - keyword, number.long

* _fan_speed_sensors.min_ - Minimum speed
* _shadow.min_ - Minimal number of days between password changes

*min_api_version* - keyword, text.text

* _docker_version.min_api_version_ - Minimum API version supported

*min_version* - keyword, text.text

* _xprotect_meta.min_version_ - The minimum allowed plugin version.

*min_voltage* - keyword, number.long

* _memory_devices.min_voltage_ - Minimum operating voltage of device in millivolts

*minimum_password_age* - keyword, number.long

* _security_profile_info.minimum_password_age_ - Determines the minimum number of days that a password must be used before the user can change it

*minimum_password_length* - keyword, number.long

* _security_profile_info.minimum_password_length_ - Determines the least number of characters that can make up a password for a user account

*minimum_system_version* - keyword, text.text

* _apps.minimum_system_version_ - Minimum version of macOS required for the app to run

*minor* - keyword, number.long

* _os_version.minor_ - Minor release version

*minor_version* - keyword, number.long

* _windows_crashes.minor_version_ - Windows minor version of the machine

*minute* - keyword, text.text

* _crontab.minute_ - The exact minute for the job

*minutes* - keyword, number.long

* _time.minutes_ - Current minutes in UTC
* _uptime.minutes_ - Minutes of uptime

*minutes_to_full_charge* - keyword, number.long

* _battery.minutes_to_full_charge_ - The number of minutes until the battery is fully charged. This value is -1 if this time is still being calculated. On Windows this is calculated from the charge rate and capacity and may not agree with the number reported in "Power & Battery"

*minutes_until_empty* - keyword, number.long

* _battery.minutes_until_empty_ - The number of minutes until the battery is fully depleted. This value is -1 if this time is still being calculated

*mirror* - keyword, number.long

* _connected_displays.mirror_ - If the display is mirrored or not. This field is 1 if mirrored and 0 if not mirrored.

*mirrorlist* - keyword, text.text

* _yum_sources.mirrorlist_ - Mirrorlist URL

*mnt_namespace* - keyword, text.text

* _docker_containers.mnt_namespace_ - Mount namespace
* _process_namespaces.mnt_namespace_ - mnt namespace inode

*mode* - keyword, text.text

* _apparmor_profiles.mode_ - How the policy is applied.
* _device_file.mode_ - Permission bits
* _docker_container_mounts.mode_ - Mount options (rw, ro)
* _file.mode_ - Permission bits
* _file_events.mode_ - Permission bits
* _package_bom.mode_ - Expected permissions
* _process_events.mode_ - File mode permissions
* _process_open_pipes.mode_ - Pipe open mode (r/w)
* _rpm_package_files.mode_ - File permissions mode from info DB
* _wifi_status.mode_ - The current operating mode for the Wi-Fi interface

*model* - keyword, text.text

* _battery.model_ - The battery's model number
* _block_devices.model_ - Block device model string identifier
* _chassis_info.model_ - The model of the chassis.
* _cpu_info.model_ - The model of the CPU.
* _hardware_events.model_ - Hardware device model
* _pci_devices.model_ - PCI Device model
* _usb_devices.model_ - USB Device model string
* _video_info.model_ - The model of the gpu.

*model_id* - keyword, text.text

* _hardware_events.model_id_ - Hex encoded Hardware model identifier
* _pci_devices.model_id_ - Hex encoded PCI Device model identifier
* _usb_devices.model_id_ - Hex encoded USB Device model identifier

*modified* - keyword, text.text

* _authorizations.modified_ - Label top-level key
* _keychain_items.modified_ - Date of last modification

*modified_time* - keyword, number.long

* _package_bom.modified_time_ - Timestamp the file was installed
* _shellbags.modified_time_ - Directory Modified time.
* _shimcache.modified_time_ - File Modified time.

*module* - keyword, text.text

* _windows_crashes.module_ - Path of the crashed module within the process

*module_backtrace* - keyword, text.text

* _kernel_panics.module_backtrace_ - Modules appearing in the crashed module's backtrace

*module_path* - keyword, text.text

* _services.module_path_ - Path to ServiceDll

*month* - keyword, text.text

* _crontab.month_ - The month of the year for the job
* _time.month_ - Current month in UTC

*mount_namespace_id* - keyword, text.text

* _deb_packages.mount_namespace_id_ - Mount namespace id
* _file.mount_namespace_id_ - Mount namespace id
