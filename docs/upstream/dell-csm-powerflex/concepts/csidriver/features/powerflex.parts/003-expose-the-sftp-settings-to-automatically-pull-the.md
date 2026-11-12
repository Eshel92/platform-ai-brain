<!-- Part 3 of 4 of concepts/csidriver/features/powerflex.md (split because the page is big). -->

## Expose the SFTP settings to automatically pull the scini.ko kernel module
PowerFlex CSI driver version 2.14.0 and above supports exposing the SFTP settings to automatically pull the scini.ko kernel module.

This feature allows the configuration of SFTP settings to automatically pull the scini.ko kernel module from a specified SFTP repository or SFTP repository of Dell. This ensures that the necessary kernel module is available and up-to-date on the cluster.

The driver will try to find the kernel modules in the following order:

- Pre-compiled Modules:

Driver will fetch pre-compiled kernel modules for various Linux kernels that are typically included in PowerFlex SDC installation packages. These modules are stored in a driver cache.

- Automatic Fetching from SFTP repository:

Driver will fetch the necessary kernel modules from a remote SFTP repository. This is configured through environment variables and secrets in the deployment templates.

- Automatic SDC Compilation:

If a matching pre-compiled module or the kernel module from SFTP repository is not available, driver will compile the SDC driver automatically. This involves compiling the scini.ko kernel module to match the running kernel.


> <span style="font-size: 18px;"><strong>ℹ️ NOTE:</strong></span>
Before setting up or upgrading the cluster, the user must verify that the updated scini.ko tar file is available on the MFT (SFTP) server. It is essential to ensure that the tar file matches the kernel version of the cluster. Proceed with the deployment only if a matching kernel module is found.

### Configuration Steps

#### Enable SFTP Repository Settings:

Enable the SFTP repository settings by enabling the SDC SFTP Repo and configuring the SFTP repository address, username, and secret.

 *NOTE:*
- Exposing SFTP settings to automatically pull scini.ko modules is only available for SDC 3.6.5, 4.5.4 and 5.x.
- Ensure that sdcrepo-private-secret and sdcrepo-public-secret are created from the secrets file.
  ```bash
  kubectl create secret generic sdcsftprepo-private-secret -n vxflexos --from-file=user_private_rsa_key=sftp-secret-private.crt
  kubectl create secret generic sdcsftprepo-public-secret -n vxflexos --from-file=repo_public_rsa_key=sftp-secret-public.crt
  ```
- Private key of SFTP server should be obtained and public key should be pulled from known hosts after logging in to server via private key.
- The secrets should have permissions set to 600 to ensure security and proper access control. Setting permissions to 600 ensures that only the owner has read and write access, preventing unauthorized users from accessing or modifying the secrets.
- After creating the private SFTP server,
  scini.tar should be located in the folder structure with the format of RHEL version as the username followed by sdc kernel version. For example the format should be `RHEL9/4.5.4000.111/5.14.0-503.40.1.el9_5.x86_64/scini.tar`.
  SSH Configuration on the Server should be enabled for public key authentication and public key should be added to authorized keys. For example, in /etc/ssh/sshd_config the following config should exist
    ```ssh
        PubkeyAuthentication yes
        AuthorizedKeysFile .ssh/authorized_keys
        Match Group sftpusers
            ChrootDirectory /home
            ForceCommand internal-sftp
            AllowTcpForwarding no
            X11Forwarding no
    ```

## NVMe/TCP Support

Starting with v2.16.0, the CSI PowerFlex driver supports NVMe/TCP connectivity with PowerFlex 4.x and 5.0. This feature allows the driver to communicate with PowerFlex arrays using the standard NVMe/TCP protocol, eliminating the dependency on the proprietary Storage Data Client (SDC) for worker nodes.

### Configuration Requirements

To enable NVMe/TCP, the following configurations must be applied:

1.  **Block Protocol**: Explicitly set the `blockProtocol` parameter to `NVMeTCP` in [secret.yaml](https://github.com/dell/csi-powerflex/blob/main/samples/secret.yaml).
    ```yaml
    blockProtocol: "NVMeTCP"
    ```
     **Note:**
     * If `blockProtocol` is not specified or set to `auto` in the vxflexos-config secret, the driver automatically detects the available initiators on the host and selects the appropriate protocol. The selection priority is SDC first, followed by NVMe/TCP.
     * When configuring the driver with multiple PowerFlex arrays, the blockProtocol value must be the same for all arrays.

2.  **Disable SDC**: SDC deployment must be disabled to ensure the driver relies on NVMe/TCP.
    *   **Helm**: Set `sdc.enabled` to `false` in [values.yaml](https://github.com/dell/helm-charts/blob/csi-vxflexos-{{< version-docs key="driver_latestVersion" >}}/charts/csi-vxflexos/values.yaml).
    *   **Operator**: Set `X_CSI_SDC_ENABLED` to `false` in the Custom Resource (CR) [here](https://github.com/dell/csm-operator/blob/release/{{< version-docs key="csm-operator_latest_version">}}/samples/{{< version-docs key="csm-operator_latest_samples_dir" >}}/storage_csm_powerflex_{{< version-docs key="Det_sample_operator_pflex" >}}.yaml).

      > **IMPORTANT**: The driver prioritizes SDC over NVMe/TCP. If SDC is enabled (default) or detected on the node, the driver will default to SDC communication, if `blockProtocol` is set to `auto`.

### Migration to NVMe/TCP

To transition existing nodes from SDC to NVMe/TCP, perform the following steps:

1.  **Uninstall SDC**: Remove the SDC kernel module and package from all worker nodes.
2.  **Remove Node Label**: Manually remove the SDC identification label from each node using `kubectl`:
    ```bash
    kubectl label node <node-name> csi-vxflexos.dellemc.com/<system-id>-
    ```
3.  **Verification**: Upon migration and restart, the driver will detect NVMe/TCP capability and automatically apply the new label: `csi-vxflexos.dellemc.com/<system-id>-nvmetcp=true`.

    > **Important:** Automatic migration of existing SDC volumes to NVMe/TCP is not supported. After removing SDC, the driver will detect NVMe/TCP and schedule new workloads using NVMe/TCP on those nodes.

**Limitations**

- Container Storage Modules Replication is not supported with NVMeTCP protocol on PowerFlex 4.x
- Automatic migration of SDC volume to NVMeTCP is not supported
