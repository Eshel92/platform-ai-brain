<!-- Part 4 of 4 of concepts/csidriver/features/powerflex.md (split because the page is big). -->

## OIDC Authentication Support
### Overview

The PowerFlex CSI driver supports OIDC-based authentication in addition to traditional username/password authentication.
OIDC (OpenID Connect) allows Kubernetes deployments to authenticate to PowerFlex using OAuth2 tokens, providing stronger security and centralized identity management using providers like:

- Keycloak
- Azure AD
- Okta

This means that instead of storing long‑lived PowerFlex credentials inside the Kubernetes Secret, the driver uses short‑lived, automatically refreshed access tokens obtained via the OIDC provider.

### Secret Configuration for OIDC
Below is the required secret structure for OIDC-enabled authentication.
  ```yaml
  - username: "ignored"
    password: "ignored"
    systemID: "2000000000000001"
    endpoint: "https://10.0.0.1"
    skipCertificateValidation: true
    mdm: "10.0.0.2,10.0.0.3"

    # OIDC / CIAM values
    oidcClientId: ""
    oidcClientSecret: ""     # base64 encoded
    # CIAM (optional alternative auth mode)
    ciamClientId: ""
    ciamClientSecret: ""
    issuer: "https://10.0.0.4:1010/realms/CSM"  #for keycloak format
    # https://login.microsoftonline.com/abcd/v2.0" # for azure format
    # https://<okta-domain>.okta.com/oauth2/default # for okta format
    scopes: ""
    # openid","profile","email","custom_scopes"
  ```

Enabling OIDC via CSM-Operator
```yaml
- name: X_CSI_AUTH_TYPE
  value: "OIDC"   # or "" for BasicAuth
```

Enabling OIDC via Helm
```yaml
# "authType" defines the type of authentication that is used.
# Allowed values:
#  "OIDC" - use OIDC authentication
#  "" - by default use Basic authentication
# Default value: "" <empty>
authType: "OIDC"
```

### Pre-requisites for OIDC support

To enable the support for OIDC we need to establish the connection between the ID provider and PowerFlex.

In PowerFlex, Management Virtual Machine (MVM) IP addresses are the IPs assigned to the Management Virtual Machines. MVMs host PowerFlex Manager and other management services. These IP addresses are configured during the PowerFlex deployment process and can be accessed through the PowerFlex Manager user interface by navigating to: System → Components → MVM.

Execute the below steps by logging into the MVM IP:

Env variables needed for the steps:
SSO_IP -  This is the Cluster IP address of the SSO service in Kubernetes Cluster.
PM_TOKEN - This is an access token (JWT) retrieved by logging into PowerFlex via its SSO REST API and can be used for subsequent API calls to PowerFlex services.
IN_IP - This is the External IP address of the rke2-ingress-nginx-controller service, which is typically the load balancer or ingress controller IP used for external traffic.

```bash
export SSO_IP=`kubectl get svc -A | grep "sso " | awk '{print $4}'`
export PM_TOKEN=`curl -k --location --request POST "https://${SSO_IP}:8080/rest/auth/login" --header 'Accept: application/json' --header 'Content-Type: application/json' --data '{"username": "user","password": "password" }' | jq -r .access_token`
export IN_IP=`kubectl get svc -A | grep -m1 rke2-ingress-nginx-controller | sort | awk '{print $5}'`
```

##### **1. Initialize the SSO CIAM config for PowerFlex**

This API initializes the SSO CIAM configuration for PowerFlex.

```bash
curl -k -X POST https://$IN_IP/rest/v1/sso-ciam/init --header 'Accept: application/json' --header 'Content-Type: application/json' --header "Authorization: Bearer ${PM_TOKEN}"
```
>Note: The API returns a unique identifier. Record this value, as it will be required in the following steps under the name CIAM_ID.

##### **2. Configure PowerFlex with Embedded Keycloak as the OIDC Service provider**

This API call registers and configures PowerFlex as an OIDC Service Provider with Embedded Keycloak, enabling secure SSO authentication using OpenID Connect.

```bash
curl -vvL -k --request POST \
  --url https://$IN_IP/rest/v1/oidc-sp-config \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer ${PM_TOKEN}" \
  --data "{
  \"sp_id\": \"powerflex-$IN_IP\",
  \"redirect_uri\": \"https://$IN_IP/auth/realms/powerflex/protocol/openid-connect/auth\",
  \"logout_uri\": \"https://$IN_IP/auth/realms/powerflex/protocol/openid-connect/logout\",
  \"required_claims\": [\"email\"],
  \"keycloak_settings\": {
    \"config\": {
      \"clientAuthMethod\": \"client_secret_basic\",
      \"pkceEnabled\": \"true\",
      \"useJwksUrl\": \"true\",
      \"validateSignature\": \"true\"
    },
    \"first_broker_login_flow_alias\": \"first broker login\",
    \"post_broker_login_flow_alias\": null,
    \"link_only\": null,
    \"store_token\": true,
    \"add_read_token_role_on_create\": true,
    \"trust_email\": true
  },
  \"days_to_store_state_code_verifier\": 1
}"
```
##### **3. Add certificates to PowerFlex for CIAM services**

  PowerFlex CIAM must trust the Azure/Keycloak/Okta signing certificate in order to validate RS256‑signed JWT tokens issued by ID provider. This certificate must be added to CIAM as a trusted CA.

  - For Microsoft Azure,

    We have to add the following certificates for CIAM services

    * DigiCert is a trusted Certificate Authority (CA). Azure services use SSL/TLS certificates issued by DigiCert to secure communication.
    * GA2 (GlobalSign or similar root/intermediate) certificates are part of the certificate chain that validates Azure’s identity endpoints.

      They ensure:
      - The OIDC metadata URL `(https://login.microsoftonline.com/...)` and token endpoints are trusted.
      - Secure HTTPS communication between PowerFlex and Azure IdP.


  - For Keycloak,

    We can obtain the Keycloak certificate using either of the following methods.
    - Option 1 — Download the Certificate from Browser
      * Open the Keycloak URL in your browser: `https://<PFMP_IP>/auth/`
      * Click the lock icon in the address bar.
      * View the site certificate.
      * Export or download the certificate.
      * Save it locally
      * Note: Ensure the file includes valid PEM headers:
        ```
        -----BEGIN CERTIFICATE-----
        <certificate-body>
        -----END CERTIFICATE-----
        ```

    - Option 2 — Retrieve the Certificate from the Keycloak UI
      This option retrieves the actual RS256 signing certificate directly from Keycloak’s admin interface.
      * Log in to Keycloak Admin Console - `https://<PFMP_IP>/auth/admin/`
      Log in using the admin credentials obtained via:
        ```bash
          kubectl get secret keycloak-admin-credentials -o json -n powerflex | jq '.data | map_values(@base64d)'
        ```
      * Select the Correct Realm. Open the realm dropdown (top-left corner). Choose the realm used by PowerFlex based on the deployment
      * Navigate to the Keys Tab - Go to: Realm Settings → Keys. This page lists all signing keys for the selected realm.
      * Locate the RS256 Signing Key. Find the row where: Algorithm: RS256,Use: SIG, Status: Active. This is the key used to sign all Keycloak-issued JWT tokens.
      * Export the Certificate. In the RS256 row, click Certificate. A dialog appears showing the Base64‑encoded certificate without PEM headers. Copy the entire certificate and add the proper PEM headers:
        ```
        -----BEGIN CERTIFICATE-----
        <copied-certificate-content>
        -----END CERTIFICATE-----
        ```
  - For Okta,
    - Option 1 — Download the Certificate from Browser
      * Open the Okta URL in  browser: `https://<okta-domain-name>.okta.com`
      * Click the lock icon in the address bar.
      * View the site certificate.
      * Export or download the certificate.
      * Save it locally.

    - Option 2 — Retrieve the Certificate from the Okta UI
      * Log in to the Okta Admin Console  and open Okta tenant `(e.g., https://<okta-domain-name>.okta.com)` by signing in with admin credentials.
      * Navigate to Applications - From the left navigation panel, go to Applications → Applications.
      * Select the  Application - Click on the application for which the certificate is needed.
      * Open the Sign-On Settings - Go to the Sign On tab inside the application.
      * Access the OIDC Signing Certificate.
      * Download the Certificate.

        ``` bash
        CA=`<PEM_FILE_OF_CERTIFICATE>`
        curl -kvvL -X POST https://$IN_IP//Api/V1/CIAM/<CIAM_ID>/x509-certificates --header "Authorization: Bearer ${PM_TOKEN}" --data-raw "
        {
          \"type\": \"CA\",
          \"service\": \"ALL\",
          \"certificate_format\": \"PEM\",
          \"certificate\": \"$CA\"
        }"
        ```

##### **4. Add Microsoft Azure/Keycloak/Okta Identity provider as the service**

  It registers an external identity provider (Azure/Keycloak/Okta) with PowerFlex using OpenID Connect (OIDC). This allows PowerFlex users to authenticate through Azure/Keycloak/Okta instead of local credentials.


> **Note:**
> - `CLIENT_ID` – Client ID of Microsoft Azure / Keycloak / Okta
> - `CLIENT_SECRET` – Client secret of Microsoft Azure / Keycloak / Okta
> - `IDP` – AzureEntraID / Keycloak / Okta
> - For **Azure**,
>   `IDP_METADATA_URL` – `https://login.microsoftonline.com/<Tenant_id>/v2.0`
>   where `<Tenant_id>` is the Azure Active Directory tenant the identity provider belongs to.
> - For **Keycloak**,
>   `IDP_METADATA_URL` – `https://<keycloak_ip>/realms/CSM`
>   where the realm name is the name of the realm where the application is created.
> - For **Okta**,
>   `IDP_METADATA_URL` – `https://<okta-domain-name>.okta.com/oauth2/default`
>   where `<okta-domain-name>` is the name of the Okta domain where the application is created.


  ```bash
    curl -kvvL --request POST \
      --url https://$IN_IP/rest/v1/oidc-services \
      --header 'Content-Type: application/json' \
      --header "Authorization: Bearer ${PM_TOKEN}" \
      --data "{
      \"name\": \"azure\",
      \"is_enabled\": true,
      \"idp_metadata_url\": \"$IDP_METADATA_URL\",
      \"claims_mapper\": [
        {
          \"name\": \"email\",
          \"value\": \"email\"
        },
        {
          \"name\": \"given_name\",
          \"value\": \"firstName\"
        },
        {
          \"name\": \"preferred_username\",
          \"value\": \"username\"
        },
        {
          \"name\": \"family_name\",
          \"value\": \"lastName\"
        }
      ],
      \"client_id\": \"$CLIENT_ID\",
      \"client_secret\": \"$CLIENT_SECRET\",
      \"scopes\": [
        \"openid\",
        \"profile\",
        \"email\",
        \"offline_access\"
      ],
      \"pkce_enabled\": true,
      \"code_challenge_method\": \"S256\",
      \"idp_type\": \"$IDP\"
    }"
  ```

  >Note: An ID will be generated for the service, which will be referred to as SERVICE_ID_IDP


#### (Optional) Configure the Service ID in the Identity Provider

Since PowerFlex relies on embedded Keycloak for OIDC, a valid redirect URI must be configured for browser-based SSO.

**Redirect URI format:** - `https://<PFMP_IP>/auth/realms/powerflex/broker/<SERVICE_ID_IDP>/endpoint`

#### In Microsoft Azure
- Navigate to the **Authentication** tab.
- Update the **Redirect URIs** section.
- Ensure the redirect URI includes the **PowerFlex Management IP (PFMP_IP)** or a resolvable hostname.

##### In Keycloak
- Log in to **Keycloak**.
- Select **Realm**.
- Go to **Clients** → open the client.
- Under **Settings**, add the URI under **Valid Redirect URIs**.
- Click **Save**.

##### In Okta
- Navigate to the **OIDC application**.
- Go to **General** → **Sign-in redirect URIs**.
- Add the PowerFlex Keycloak broker endpoint using the **PFMP IP** or a resolvable hostname.

###### **5. Configure API permissions**

- In Azure
  + Open the application page and select API permissions.
  + Under Microsoft Graph, add:
    + offline_access
    + User.Read
  + Click Update permissions to apply the changes

- In Keycloak,
  - Add the below to Client Scopes → Default Client Scopes:
    ```
      openid
      profile
      email
      roles
      offline_access
    ```
  - Clients → keycloak_user_client -> Mappers, add mappers:
    ```
      email → email
      preferred_username → username
      given_name → firstName
      family_name → lastName
    ```

- In Okta,

  - Navigate to: Security → API → Authorization Servers
  - Select the relevant Authorization Server.
  - Add a Custom Scope.
  - Update access policies as needed to allow the scope for the client.

  Also, Ensure the scope is allowed in Access Policies and the relevant Rule for the client application
>Note: Okta performs strict scope validation and does not allow requesting scopes that are not explicitly defined in the Authorization Server. Hence, a custom scope must be created before it can be requested by the client.

##### **6. Create OAuth2 client in CIAM**

This will create a new OAuth2 client in CIAM

```bash
curl -kL --request POST \
  --url https://$IN_IP/rest/v1/oauth2-clients \
  --header 'Content-Type: application/json' \
  --header "Authorization: Bearer ${PM_TOKEN}" \
  --data "{
  \"client_name\": \"idp_oidc_client\",
  \"redirect_uris\": [\"\"],
  \"authorization_code_flow\": false,
  \"client_credentials_flow\": false,
  \"token_exchange_enabled\": true,
  \"offline_access_enabled\": true,
  \"client_offline_session_idle\": 1,
  \"client_offline_session_max\": 1,
  \"client_security_level\": \"TRUSTED\"
}"
```
>Note: The ID and secret generated in this step will be referred to as CIAM_CLIENT_ID and CIAM_CLIENT_SECRET in the subsequent steps.

##### **7. Add the application to CIAM**

This command will add the application to CIAM

- ROLE refers to the role assigned to all tokens exchanged for a specific Identity Provider (IdP) and Application ID, enabling access to the PowerFlex APIs.
- CIAM_CLIENT_ID is the client ID issued by the CIAM system.
- IDP_CLIENT_ID represents the client ID configured in the identity provider (Azure, Keycloak, or Okta).
- METADATA denotes the metadata URL of the corresponding Azure, Keycloak, or Okta application.
- SERVICE_ID_IDP identifies the service ID associated with the configured identity provider.

  ```bash
  curl -kLvv --request POST \
    --url https://$IN_IP/rest/v1/oauth2-token-exchanges \
    --header 'Content-Type: application/json' \
    --header 'clientId: ' \
    --header "Authorization: Bearer ${PM_TOKEN}" \
    --data "{
    \"ciam_oauth2_client_id\": \"$CIAM_CLIENT_ID\",
    \"customer_client_id\": \"$IDP_CLIENT_ID\",
    \"customer_metadata_url\": \"$METADATA\",
    \"idp_service_id\": \"$SERVICE_ID_IDP\",
    \"static_roles\": [
      \"$ROLE\"
    ]}"
  ```
> Note: Record this application ID; it will be referred to as APP_ID.

##### **8. Activate the CIAM Login Client**

This step activates and synchronizes the CIAM OAuth2 client created so that it becomes a login-capable client in PowerFlex CIAM.
CIAM creates a user in Keycloak realm of embedded keycloak and assigns it the given role.

```bash
curl -k -X PATCH https://$IN_IP/rest/v1/login-clients/$CIAM_CLIENT_ID --header 'Accept: application/json' --header 'Content-Type: application/json' --header "Authorization: Bearer ${PM_TOKEN}" --data '{}'
```

##### **9. Legacy Workaround: Configure Keycloak User Attributes for PowerFlex Block API (Pre‑PFMP 5.1)**

This step configures role mapping between Azure/Keycloak/Okta and PowerFlex roles within the PowerFlex Realm inside Keycloak (the internal identity provider embedded in PowerFlex).
This mapping ensures that when a token exchange occurs, CIAM and Keycloak assign the correct PowerFlex roles (e.g., SuperUser, Monitor, Administrator) to the authenticated user.

Although CIAM handles identity federation and token exchange, PowerFlex REST APIs rely on Keycloak role mappings for authorization.

This step ensures:

- The exchanged CIAM token contains the correct PowerFlex role required for API access.
- The static role assigned during CIAM token exchange is recognized by Keycloak and mapped to the corresponding PowerFlex authorization roles.

CIAM token exchange assigns a static role (e.g., "SuperUser") that must be recognized by Keycloak

```bash
export KC_PASS=`kubectl get secret keycloak-admin-credentials -o json -n powerflex | jq '.data | map_values(@base64d)' | jq -r '.["password"]'`
export ACCESS_TOKEN=`curl -k --location --request POST 'https://keycloak-http.powerflex/auth/realms/master/protocol/openid-connect/token' -d "client_id=admin-cli" -d "username=keycloak" -d "password=$KC_PASS" -d "grant_type=password" | jq -r .access_token`
curl -X GET "https://keycloak-http.powerflex/auth/admin/realms/powerflex/users" -H "Content-Type: application/json" -H "Authorization: bearer ${ACCESS_TOKEN}" | jq
```
>Note: Capture the ID from the above command that corresponds to the username from Step 7 (i.e., APP_ID). This ID will be referred to as APP_USER.

```bash
curl -k -X POST https://$IN_IP/rest/v1/users/$APP_USER/repair --header 'Accept: application/json' --header 'Content-Type: application/json' \
 --header "Authorization: Bearer ${PM_TOKEN}"
 ```
Once all the steps are completed, a handshake is successfully established between the identity provider and PowerFlex.
