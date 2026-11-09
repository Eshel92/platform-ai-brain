<!-- Converted from reference/config/ui-settings.txt (reStructuredText). Includes are inlined. -->

# Ops Manager Application Settings

Ops Manager stores configuration settings both globally in the
Ops Manager Application Database and locally on each server. Global settings
apply to all your Ops Manager servers. Local settings apply to the server
on which they are configured. Any local settings on a server override
the global settings.

You configure global settings through the Ops Manager interface during
installation. You can edit global settings at any time through the
Admin interface by clicking the General tab and
then clicking Ops Manager Config. If you wish to bypass the
Ops Manager interface's initial configuration and use a configuration
file, see bypass-ui-config.

You may also include global
configuration file settings that do
not have a corresponding setting in the Ops Manager interface. To add
configuration file settings:

1. Click the Admin link in the top right corner of Ops Manager
   to access the settings panels.

2. From the General tab, go to
   Ops Manager Config and select the Custom
   tab.

**Note:**

You configure local settings through a server's
`conf-mms.properties` file. Each server's `conf-mms.properties`
must contain the connection string and authentication settings for
accessing the Ops Manager Application Database. The
`conf-mms.properties` file also contains any overrides of global
settings specific to that server. For more information, see
conf-mms.properties.

## MongoDB Usage

**`Default Ops Manager MongoDB Server Type`**

*Type*: string

*Default*: Production Server

Default MongoDB Enterprise server type for all Enterprise
processes that this Ops Manager instance manages.

The following table shows the accepted Server Type values and the
corresponding number of licenses required for each:

* - Server Intention
  - Environment Purpose
  - License Requirement

* - Production Server
  - Hosts your application to your internal or external end users.

    If an end user might use an environment, it functions as a
    Production environment. This applies whether the environment
    also provides testing, quality assurance, evaluation, or
    development capabilities.

  - One license per server

* - Test/QA Server
  - This type of environment can be used to:

    |  |  |
    |---|---|
    | Test | Exercises your application to verify that it works as designed and expected. The platform configuration might be a less performant version of Production in compute, network, and storage capability. |
    | Assure system quality | Validates your application against a combination of data, hardware, and software configured to simulate Production. The platform configuration should be a smaller scale of Production in compute, network, and storage capability. |
    | Stage | Simulates the Production environment including performance testing and release candidate approval. The platform configuration should mirror Production in compute, network, and storage capability. |

  - One license per server

* - Development Server
  - Hosts in progress design, code, debugging or some combination
    thereof for your application. Used to evaluate if the current
    state of your application can be promoted to another
    environment.
  - None

* - RAM Pool
  - Provides any combination of servers for any environment purpose.
  - One license for any number of servers up to the maximum of
    the total GB of RAM you purchased across these servers.

|  |  |  |
|---|---|---|
| Backing Database | Hosts your Ops Manager backing database. enable-application-database-monitoring to enable this option. | None |

Corresponds to `mms.mongoDbUsage.defaultUsageType`.

**`MongoDB Usage UI`**

*Type*: boolean

Enables the MongoDB Usage UI in the Ops Manager Admin if set to
`true`.

Corresponds to `mms.mongoDbUsage.ui.enabled`.

**`MongoDB Usage Data Collection`**

*Type*: boolean

*Default*: False

Enables the daily collection of MongoDB Usage Data if set to
`true`.

Corresponds to `mms.mongoDbUsage.collectData`.

## Web Server & Email

Configure global settings through the Admin interface.
Ops Manager stores global settings in the Ops Manager Application database.

### Web Server

**`URL to Access Ops Manager`**

*Type*: string

FQDN (fully qualified domain name) and port number of the Ops Manager Application.

To use a port other than `8080`, see
/tutorial/manage-ports.

```ini
http://mms.example.com:8080
```

Corresponds to `mms.centralUrl`.

**Important:**

If you plan on accessing your Ops Manager Application using its IPv6 (Internet Protocol version 6)
address, you must enclose the IPv6 (Internet Protocol version 6) address in square brackets
(`[ ]`) to separate it from its port number.

For example: 

```ini
http://[2600:1f16:777:8700:93c2:b99c:a875:2b10]:8080
```

**`HTTPS PEM Key File`**

*Type*: string

Absolute path to the PEM file that contains the Ops Manager Application's
valid certificate and private key. The PEM file is required if the
Ops Manager Application uses HTTPS (Hypertext Transfer Protocol Secure) to encrypt connections between the
Ops Manager Application, the agents, and the web interface.

The default port for HTTPS (Hypertext Transfer Protocol Secure) access to the Ops Manager Application is
`8443`, as set in `<install_dir>/conf/mms.conf` file. If you
change this default, you must also change the port specified in the
`URL to Access Ops Manager` setting.

Corresponds to `mms.https.PEMKeyFile`.

**`HTTPS PEM Key File Password`**

*Type*: string

Password for the HTTPS (Hypertext Transfer Protocol Secure) PEM key file. You must include this setting
if the PEM (Privacy-Enhanced Mail) key file contains an encrypted private key.

Corresponds to `mms.https.PEMKeyFilePassword`.

**`Client Certificate Mode`**

*Type*: string

*Default*: None

Specifies if Ops Manager requires clients to present valid TLS (Transport Layer Security)/SSL (Secure Sockets Layer)
client certificates when connecting to it. Accepted values are:

- None
- Required for Agents Only
- Required for All Requests

Corresponds to `mms.https.ClientCertificateMode`.

**`CA File`**

*Type*: string

Required if:

- You are using a private certificate authority.
- You set `Client Certificate Mode` to
  Required for Agents Only or Required for All Requests.
- You run Ops Manager in hybrid mode with TLS (Transport Layer Security) enabled.

Specifies the filesystem location of a private certificate authority
file containing the list of acceptable client certificates. The
Ops Manager Application authenticates HTTPS (Hypertext Transfer Protocol Secure) requests from clients bearing a
certificate described in this file.

```ini
/path/to/ca_file.pem
```

Corresponds to `mms.https.CAFile`.

**`Load Balancer Remote IP Header`**

*Type*: string

If you use a load balancer with the Ops Manager Application, set this to the
HTTP (Hypertext Transfer Protocol) header field the load balancer uses to identify the
originating client's IP address to the Ops Manager host. When you
specify `Load Balancer Remote IP Header`, do not allow
clients to connect directly to any Ops Manager host. A load
balancer placed in front of the Ops Manager hosts must not
return cached content.

Once `Load Balancer Remote IP Header` is set, Ops Manager
enables the following HTTP (Hypertext Transfer Protocol) headers:

| HTTP (Hypertext Transfer Protocol) Header | Forwards to Ops Manager |
|---|---|
| X-Forwarded-Host | Original host that the client requested in the Host HTTP (Hypertext Transfer Protocol) request header. |
| X-Forwarded-Proto | Protocol used to make the HTTP (Hypertext Transfer Protocol) request. |
| [X-Forwarded-Server](https://www.eclipse.org/jetty/javadoc/current/org/eclipse/jetty/server/ForwardedRequestCustomizer.html) | Hostname of the proxy server. |
| [X-Proxied-Https](https://www.eclipse.org/jetty/javadoc/current/org/eclipse/jetty/server/ForwardedRequestCustomizer.html) | HTTPS (Hypertext Transfer Protocol Secure) status of a request. |

To learn more, see
/tutorial/configure-application-high-availability.

Corresponds to `mms.remoteIp.header`.

### Email

The following email address settings are mandatory. You **must** define
these settings before you can use the Ops Manager Application.

**`From Email Address`**

*Type*: string

Email address used for sending the general emails, such as
Ops Manager alerts. You can include an alias with the email address.

```ini
Ops Manager Alerts <mms-alerts@example.com>
```

Corresponds to `mms.fromEmailAddr`.

**`Reply To Email Address`**

*Type*: string

Email address from which to send replies to general emails.

Corresponds to `mms.replyToEmailAddr`.

**`Admin Email Address`**

*Type*: string

Email address of the Ops Manager admin. This address receives emails
related to problems with Ops Manager.

Corresponds to `mms.adminEmailAddr`.

**`Email Delivery Method Configuration`**

*Type*: string

*Default*: SMTP Email Server

Email interface to use.

This setting is labeled in different ways for the user interface and
the configuration file.

| Delivery Method | UI Setting |
|---|---|
| AWS (Amazon Web Services) SES (Simple Email Service) | AWS Simple Email Service |
| SMTP (Simple Mail Transport Protocol) | SMTP Email Server |

If you set this to SMTP (Simple Mail Transport Protocol) Email Server, you must set:

- `Transport`
- `SMTP Server Hostname`
- `SMTP Server Port`
- `Username`
- `Password`
- `Use SSL`

If you set this to AWS (Amazon Web Services) Simple Email Service, you must set:

- `AWS Endpoint`
- `AWS Access Key`
- `AWS Secret Key`

Corresponds to `mms.emailDaoClass`.

#### SMTP

*Conditional.* The following settings appear if
`Email Delivery Method Configuration` is
`SMTP Email Server`.

**`Transport`**

*Type*: string

*Default*: smtp

Transfer protocol your email provider specifies:

- `smtp` (standard SMTP (Simple Mail Transport Protocol))

Corresponds to `mms.mail.transport`.

**`SMTP Server Hostname`**

*Type*: string

*Default*: localhost

Email hostname your email provider specifies.

```ini
mail.example.com
```

Corresponds to `mms.mail.hostname`.

**`SMTP Server Port`**

*Type*: number

*Default*: 25

Port number for SMTP (Simple Mail Transport Protocol) your email provider specifies.

Corresponds to `mms.mail.port`.

**`Username`**

*Type*: string

User name of the email account. If unset, defaults to disabled
SMTP (Simple Mail Transport Protocol) authentication.

Corresponds to `mms.mail.username`.

**`Password`**

*Type*: string

Password for the email account. If left blank, this setting disables
SMTP (Simple Mail Transport Protocol) authentication.

Corresponds to `mms.mail.password`.

**`Use SSL`**

*Type*: boolean

*Default*: false

Set this to `true` if the transfer protocol uses TLS (Transport Layer Security)/SSL (Secure Sockets Layer).

Corresponds to `mms.mail.tls`.

#### AWS SES

*Conditional.* The following settings appear if
`Email Delivery Method Configuration` is
`AWS Simple Email Service`.

**`AWS Endpoint`**

*Type*: string

*Default*: `https://email.us-east-1.amazonaws.com`

Sets the [sending API endpoint](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/regions.html#region-endpoints)
for the AWS (Amazon Web Services) SES (Simple Email Service).

Corresponds to `aws.ses.endpoint`.

**Note:**

If you use AWS (Amazon Web Services) SES (Simple Email Service) in a region other than US East (N. Virginia),
you must set this value to the appropriate endpoint for your region.

**`AWS Access Key`**

*Type*: string

Access key ID for AWS (Amazon Web Services).

Corresponds to `aws.accesskey`.

**`AWS Secret Key`**

*Type*: string

Secret access key for AWS (Amazon Web Services).

Corresponds to `aws.accesskey`.

## User Authentication

### User Authentication

**`Username Validation`**

*Type*: string

*Default*: false

Determines if Ops Manager requires usernames to be email addresses.

| Value | Description |
|---|---|
| `false` | (**Default**) Username is not required to be an email address. |
| `loose` | Username must contain an `@` symbol followed by a period. |
| `strict` | Username must adhere to a strict email address validation regular expression. |

If set to `strict`, Ops Manager uses the following regular expression
to validate that an email address adheres to the requirements
described in Section 3 of 3696:

```sh
^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$
```

**Example:**

`jane.smith@example.com` is valid. `jane.smith@ex@mple.com`
is not.

To validate usernames, you must add
`mms.email.validation` as a custom property on the
Custom tab of the Ops Manager Config page in the
Admin interface.

Corresponds to `mms.email.validation`.

**`User Authentication Method`**

*Type*: string

*Default*: Application Database

Select whether to store authentication credentials in the Ops Manager
Application Database, a SAML (Security Assertion Markup Language) IdP (Identity Provider), or in an LDAP (Lightweight Directory Access Protocol)
directory.

Accepted values are:

- Application Database
- LDAP
- SAML

Corresponds to `mms.userSvcClass`.

The user interface displays different settings depending on whether
you store credentials in the Ops Manager Application Database or in an
external authentication source.

#### Application Database

**`Password Changes Before Reuse`**

*Type*: number

Number of previous passwords to remember. You cannot reuse a
remembered password as a new password.

Corresponds to `mms.password.minChangesBeforeReuse`.

**`Failed Login Attempts Before Account Lock`**

*Type*: number

Number of failed login attempts before an account becomes
locked. Only an an Ops Manager Administrator can unlock a locked account.

Corresponds to `mms.password.maxFailedAttemptsBeforeAccountLock`.

**`Days Inactive Before Account Lock`**

*Type*: number

Maximum number of days with no visits to the Ops Manager website
before Ops Manager locks an account.

Corresponds to `mms.password.maxDaysInactiveBeforeAccountLock`.

**`Days Before Password Change Required`**

*Type*: number

Number of days a password is valid before the password expires.

Corresponds to `mms.password.maxDaysBeforeChangeRequired`.

**`Login Attempts Allowed Before Timeout`**

*Type*: number

Number of logins a user from a specific IP address 
can attempt during a timeout period.
You must configure this setting alongside 
`Login Attempts Timeout Period`.

Corresponds to `mms.login.ratelimit.attemptsAllowed`.

**`Login Attempts Timeout Period`**

*Type*: number

This setting specifies:

- The time period (in minutes) used to determine 
  if too many login attempts have been made.
- The duration that accounts are locked before you can 
  resume login attempts.

You must configure this setting alongside 
`Login Attempts Allowed Before Timeout`.

**Important:**

The dropdown menu lists the only possible 
values for this setting. Attempting to set a value
in your `conf-mms.properties` file or 
local database 
that is not listed in the dropdown causes an error 
when restarting the Ops Manager instance.

Corresponds to `mms.login.ratelimit.lockedPeriodMinutes`.

**`Invitation Only Mode`**

*Type*: boolean

If true, new users can register by invitation only. The invitation
provides a URL (Uniform Resource Locator) that displays the registration link. If false, new
users can register if they have the Ops Manager URL (Uniform Resource Locator).

Corresponds to `mms.user.invitationOnly`.

**`Bypass Invitation Mode`**

*Type*: boolean

*Default*: False

This checkbox appears when you set `User Authentication Method` to Application Database.

* - Value
  - Results

* - `true`
  -
    - You can add existing users to any organization or project
      without an invitation.
    - Ops Manager deletes and invalidates any pending invitations.
    - *New* users continue to receive and must accept invitations.

* - `false`
  -
    - *All* users continue to receive and must accept invitations.

Corresponds to `mms.user.bypassInviteForExistingUsers`.

**`Password Hashing Iterations`**

*Type*: number

Number of iterations for the `pbkdf2` hashing algorithm.

Corresponds to `mms.user.passwordHashIterations`.

#### LDAP

These settings configure Ops Manager to use an LDAP server for
authentication. If you use LDAP authentication, users must belong to an
LDAP group to log into Ops Manager. You must create LDAP groups for each
Ops Manager user role.

*Settings that begin with* `mms.ldap.global.role` assign Ops Manager
global roles to the members of the specified LDAP
groups. Specify groups using the format used by the LDAP attribute
specified in the `LDAP User Group` setting. You can specify
multiple groups using the `;;` delimiter. To change the default
delimiter, use the `mms.ldap.group.separator` setting. Each
Ops Manager global role provides its level of access to all the Ops Manager
projects in the deployment. To
provide access to specific groups, use 
group-level roles.

**`LDAP URI`**

*Type*: string

URI (Uniform Resource Identifier) for the LDAP (Lightweight Directory Access Protocol) or LDAPS (Secure Lightweight Directory Access Protocol) server.

```ini
ldaps://acme-dc1.acme.example.com:3890
```

Corresponds to `mms.ldap.url`.

**`LDAP SSL CA File`**

*Type*: string

A file containing one or more trusted certificates in PEM format.
Use this setting if you are using LDAPS (Secure Lightweight Directory Access Protocol) and the server is using a
certificate that is not from a well-known Certificate Authority.

```ini
/opt/CA.pem
```

Corresponds to `mms.ldap.ssl.CAFile`.

**`LDAP SSL PEM Key File`**

*Type*: string

A file containing a client certificate and private key. Use this
setting when your TLS (Transport Layer Security)/SSL (Secure Sockets Layer) LDAP (Lightweight Directory Access Protocol) server requires client
certificates.

```ini
/opt/keyFile.pem
```

Corresponds to `mms.ldap.ssl.PEMKeyFile`.

**`LDAP SSL PEM Key File Password`**

*Type*: string

Password for `LDAP SSL PEM Key File`. Use this setting
if the `PEMKeyFile` is encrypted.

Corresponds to `mms.ldap.ssl.PEMKeyFilePassword`.

**`LDAP Bind Dn`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) user used to execute searches for other users.

```ini
authUser@acme.example.com
```

Corresponds to `mms.ldap.bindDn`.

**`LDAP Bind Password`**

*Type*: string

Password for the search user.

Corresponds to `mms.ldap.bindPassword`.

**`LDAP User Base Dn`**

*Type*: string

Base Distinguished Name (DN) that Ops Manager uses to search for
users.

```ini
DC=acme,DC=example,DC=com
```

Corresponds to `mms.ldap.user.baseDn`.

**`LDAP Group Base Dn`**

*Default*: `LDAP User Base Dn` value

Base Distinguished Name (DN) that Ops Manager uses to search for
groups. If left blank, this setting uses the default value.

```ini
OU=groups,DC=acme,DC=com
```

Corresponds to `mms.ldap.group.baseDn`.

**`LDAP User Search Attribute`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) field used for the LDAP (Lightweight Directory Access Protocol) search. This is typically a
username or an email address. The value of this field is also used
as the Ops Manager username.

Corresponds to `mms.ldap.user.searchAttribute`.

**`LDAP Group Member Attribute`**

Field on the group entry containing user Distinguished Names (DN).
The groupOfNames or
groupOfUniqueNames object classes are
commonly used.

```ini
member
```

Corresponds to `mms.ldap.group.member`.

**`LDAP User Group`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) user attribute that contains the list of LDAP (Lightweight Directory Access Protocol) groups
the user belongs to. The LDAP (Lightweight Directory Access Protocol) attribute can use any format to list
the projects, including Common Name (`cn`) or Distinguished Name
(`dn`). All Ops Manager settings in this configuration file that specify
projects must match the chosen format.

**Important:**

Ops Manager deprecated `LDAP User Group`. Use `LDAP Group Member Attribute`.

If you provide values for:

- Both `LDAP User Group` and `LDAP Group Member Attribute`, Ops Manager uses
  `LDAP Group Member Attribute` and ignores `LDAP User Group`.
- `LDAP User Group` only, Ops Manager doesn't recognize
  the user's membership in nested LDAP groups.

```ini
memberOf
```

Corresponds to `mms.ldap.user.group`.

**`LDAP Global Role Owner`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group that has full privileges for the Ops Manager deployment,
including full access to all Ops Manager
projects and all administrative
permissions. Users in the specified LDAP (Lightweight Directory Access Protocol) group receive the
global owner role in Ops Manager. Specify the
project using the format that is used by the LDAP (Lightweight Directory Access Protocol) attribute
specified in the `LDAP User Group` setting.

```ini
CN=MMSGlobalOwner,OU=MMS,OU=acme Groups,DC=acme,DC=example,DC=com
```

Corresponds to `mms.ldap.global.role.owner`.

**`LDAP Referral`**

*Default*: ignore

LDAP (Lightweight Directory Access Protocol) field used to set how to handle referrals. Accepts two values:

- `ignore`: Ignore referrals.
- `follow`: Automatically follow any referrals.

Corresponds to `mms.ldap.referral`.

**`LDAP User First Name`**

*Type*: string

*Default*: `givenName` per RFC2256

LDAP (Lightweight Directory Access Protocol) user attribute that contains the user's first name. After
successful LDAP (Lightweight Directory Access Protocol) authentication, Ops Manager synchronizes the specified
LDAP (Lightweight Directory Access Protocol) attribute with the first name from the Ops Manager user record.

```ini
givenName
```

Corresponds to `mms.ldap.user.firstName`.

**`LDAP User Last Name`**

*Type*: string

*Default*: `surname` per RFC2256

LDAP (Lightweight Directory Access Protocol) user attribute that contains the user's last name. After
successful LDAP (Lightweight Directory Access Protocol) authentication, Ops Manager synchronizes the specified
LDAP (Lightweight Directory Access Protocol) attribute with the last name from the Ops Manager user record.

```ini
sn
```

Corresponds to `mms.ldap.user.lastName`.

**`LDAP User Email`**

*Type*: string

*Default*: `mail` per RFC2256

LDAP (Lightweight Directory Access Protocol) user attribute that contains the user's email address.
After successful LDAP (Lightweight Directory Access Protocol) authentication, Ops Manager synchronizes the
specified LDAP (Lightweight Directory Access Protocol) attribute with the email address from the Ops Manager
user record.

```ini
mail
```

Corresponds to `mms.ldap.user.email`.

**`LDAP Global Role Automation Admin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global automation
admin role in Ops Manager. Specify projects
using the format used by the LDAP (Lightweight Directory Access Protocol) attribute specified in the
`LDAP User Group` setting. You can specify multiple projects
using the `;;` delimiter. To change the default delimiter, use the
`mms.ldap.project.separator` setting.

```ini
CN=MMS-AutomationAdmin,OU=MMS,OU=acme Groups,DC=acme,DC=example,DC=com
```

Each Ops Manager global role provides its level of access to all the Ops Manager
projects in the deployment. To
provide access to specific projects, use group-level roles.

Corresponds to `mms.ldap.global.role.automationAdmin`.

**`LDAP Global Role Backup Admin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global backup admin
role in Ops Manager.

```ini
CN=MMS-BackupAdmin,OU=MMS,OU=acme Groups,DC=acme,DC=example,DC=com
```

Corresponds to `mms.ldap.global.role.backupAdmin`.

**`LDAP Global Role Monitoring Admin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global monitoring
admin role in Ops Manager.

```ini
CN=MMS-MonitoringAdmin,OU=MMS,OU=acme Groups,DC=acme,DC=example,DC=com
```

Corresponds to `mms.ldap.global.role.monitoringAdmin`.

**`LDAP Global Role User Admin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global user admin role in Ops Manager.

```ini
CN=MMS-UserAdmin,OU=MMS,OU=acme Groups,DC=acme,DC=example,DC=com
```

Corresponds to `mms.ldap.global.role.userAdmin`.

**`LDAP Global Role Read Only`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the
global read-only role in Ops Manager.

```ini
CN=MMS-ReadOnly,OU=MMS,OU=acme Groups,DC=acme,DC=example,DC=com
```

Corresponds to `mms.ldap.global.role.readOnly`.

#### SAML

**`Identity Provider URI`**

*Type*: string

URI (Uniform Resource Identifier) of the Identity Provider (IdP (Identity Provider)) that you use to coordinate
your Single Sign-On. This might be referred to as the *EntityId* or
the *Identity Provider Issuer*.

**`SSO Endpoint URL`**

*Type*: string

URL (Uniform Resource Locator) of the Single Sign-On endpoint that Ops Manager calls when a user
attempts to sign in.

**`SLO Endpoint URL`**

*Type*: string

URL (Uniform Resource Locator) of the Single Logout endpoint that Ops Manager calls when a user
attempts to log out. If set, when a user attempts to log out of
Ops Manager, they log out of your IdP (Identity Provider). If left blank, logging out of
Ops Manager doesn't log the user out of their IdP (Identity Provider) session.

**`Identity Provider X509 certificate`**

*Type*: string

Certificate provided by your IdP (Identity Provider) that Ops Manager uses to verify its
validity to the IdP (Identity Provider).

**`Path to SP Certificate PEM Key File`**

*Type*: string

Absolute path to the PEM file for the certificate that the SP (Service Provider)
uses to sign requests, containing both the private and public key. If
this is left blank, Ops Manager doesn't sign SAML (Security Assertion Markup Language) auth requests to the
IdP (Identity Provider) and you can't encrypt SAML (Security Assertion Markup Language) assertions.

**`Password for SP Certificate PEM Key File`**

*Type*: string

Required if the PEM (Privacy-Enhanced Mail) file contains an encrypted private key. Specify
the password for PEM (Privacy-Enhanced Mail) file.

**`Require Encrypted Assertions`**

*Type*: boolean

Flag that indicates whether or not the IdP (Identity Provider) encrypts the assertions
it sends to Ops Manager.

**`SAML Signed Assertions`**

*Type*: boolean

*Default*: `true`

Flag that indicates whether or not the IdP (Identity Provider) signs the assertions
it sends to Ops Manager.

**Important:**

Ensure that either the assertions or the response are signed. 
The configuration will fail the verification and Ops Manager returns 
an error if either the assertions or the response aren't signed.

Corresponds to `mms.saml.signedAssertions`.

**`SAML Signed Messages`**

*Type*: boolean

*Default*: `true`

Flag that indicates whether or not the IdP (Identity Provider) signs the responses
it sends to Ops Manager.

**Important:**

Ensure that either the assertions or the response are signed. 
The configuration will fail the verification and Ops Manager returns 
an error if either the assertions or the response aren't signed.

Corresponds to `mms.saml.signedMessages`.

**`Identity Provider Signature Algorithm`**

*Type*: string

Algorithm to encrypt the signature sent to and from the IdP (Identity Provider).

In the Select an Algorithm menu, there are five choices:

- `rsa-sha1`
- `dsa-sha1`
- `rsa-sha256`
- `rsa-sha384`
- `rsa-sha512`

**`Global Role Owner Group`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have full
privileges over this deployment, including full access to all groups
and all administrative permissions.

**`Global Automation Admin Role`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Automation Admin` role.

**`Global Backup Admin Role`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Backup Admin` role.

**`Global Monitoring Admin Role`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Monitoring Admin` role.

**`Global User Admin Role`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global User Admin` role.

**`Global Read Only Role`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Read Only` role.

**`SAML Attribute for User First Name`**

*Type*: string

SAML (Security Assertion Markup Language) User Attribute that contains the user's first name.

**`SAML Attribute for User Last Name`**

*Type*: string

SAML (Security Assertion Markup Language) User Attribute that contains the user's last name.

**`SAML Attribute for User Email`**

*Type*: string

SAML (Security Assertion Markup Language) User Attribute that contains the user's email address.

**`SAML Group Member Attribute`**

*Type*: string

*Default*: `groups`

SAML (Security Assertion Markup Language) Attribute that contains the list of groups Ops Manager uses to
map roles to Projects and Organizations.

Corresponds to `mms.saml.group.member`.

### Multi-Factor Authentication (MFA)

**`Multi-factor Auth Level`**

*Type*: string

*Default*: OFF

Configures the two-factor authentication "level":

| Setting | Description |
|---|---|
| `OFF` | Disables two-factor authentication. Ops Manager does not use two-factor authentication. |
| `OPTIONAL` | Users can choose to set up two-factor authentication for their Ops Manager account. |
| `REQUIRED_FOR_GLOBAL_ROLES` | Users who possess a global role *must* set up two-factor authentication. Two factor authentication is optional for all other users. |
| `REQUIRED` | *All* users must set up two-factor authentication for their Ops Manager account. |

Two-factor authentication is recommended for the security of your
Ops Manager deployment.

**Warning:**

If enabling `mms.multiFactorAuth.level` through the
configuration file, you must create a
user account first before updating the
configuration file. Otherwise, you cannot login to Ops Manager.

**Note:**

If you enable Twilio integration
(optional), ensure that Ops Manager servers can access the
`twilio.com` domain.

Corresponds to `mms.multiFactorAuth.level`.

**`Multi-factor Auth Allow Reset`**

*Type*: boolean

*Default*: false

When `true`, Ops Manager allows users to reset their two-factor
authentication settings via email in an analogous fashion to
resetting their passwords.

To reset two-factor authentication, a user must:

- be able to receive email at the address associated with the user
  account.
- know the user account's password.
- know the `agent API key` for each Ops Manager project the user
  belongs to.

Corresponds to `mms.multiFactorAuth.allowReset`.

**`Multi-factor Auth Issuer`**

*Type*: string

If Google Authenticator provides two-factor authentication, this
string is the `issuer` in the Google Authenticator app. If left
blank, the `issuer` is the domain name of the Ops Manager installation.

Corresponds to `mms.multiFactorAuth.issuer`.

### Other Authentication Options

**`ReCaptcha Enabled On Registration`**

*Default*: false

Indicator as to you want a new user to validate themselves
using reCaptcha validation when they register to use Ops Manager.

Set to `true` to require
[reCaptcha](https://www.google.com/recaptcha)
validation when a new user registers.

This setting requires a
[reCaptcha account](https://www.google.com/recaptcha/admin).

Corresponds to `reCaptcha.enabled.registration`.

**`ReCaptcha Enabled On Login`**

*Type*: boolean

*Default*: false

Requirement for users to validate themselves with
reCaptcha validation when they log into Ops Manager.

Set to `true` to require
[reCaptcha](https://www.google.com/recaptcha)
validation when a user logs in.

This setting requires a
[reCaptcha account](https://www.google.com/recaptcha/admin).

Corresponds to `reCaptcha.enabled`.

**`Session Max Hours`**

*Type*: number

Number of hours before a session on the Ops Manager website expires.

**Note:**

Session Max Hours reflects the total Ops Manager session time, not
just idle time. Both active and idle sessions expire when 
Session Max Hours elapses.

Set this value to `0` to use browser session cookies only.

Corresponds to `mms.session.maxHours`.

**`New Device Login Notification`**

Indicator as to the user should be notified that they have logged
in from a new device.

Corresponds to `mms.login.newDeviceNotification.enabled`.

**`ReCaptcha Public Key`**

*Type*: string

ReCaptcha public key associated with your account.

Corresponds to `reCaptcha.public.key`.

**`ReCaptcha Private Key`**

*Type*: string

ReCaptcha private key associated with your account.

Corresponds to `reCaptcha.private.key`.

**`Idle Session Timeout Max Minutes`**

*Type*: int

*Default*: None

The maximum time, in minutes, a session remains open with no user
activity. After this time elapses without user activity, Ops Manager logs
the user out.

You must set `Idle Session Timeout Mode` in order to use
this setting.

Corresponds to `mms.session.idleTimeoutMinutes`.

**`Idle Session Timeout Mode`**

*Type*: string

*Default*: None

Mode of the idle session timeout feature.

Set to `"idle"` to allow Ops Manager to log out users after a period of
inactivity.

The duration of this period of inactivity is determined by the
`Idle Session Timeout Max Minutes`.

Corresponds to `mms.session.mode`.

## Backup

The following settings determine:

- How much Ops Manager compresses file system store snapshots.
- How frequently Ops Manager takes snapshots.
- How long Ops Manager stores snapshots.

To set these values, click the Admin link, then
the General tab, then the Ops Manager Config
page, and then the Backup section.

**See also:**

See snapshot-frequency-and-retention to learn more about
how often snapshots are taken and how long they can be retained.

### Backup Snapshots

**`File System Store Gzip Compression Level`**

*Type*: integer

*Default*: 6

Determines how much Ops Manager compresses file system-based snapshots.
The level ranges from `0` to `9`:

- `0` provides no compression.

- `1` to `9` increases the degree of compression at a cost of
  how fast the snapshot is compressed. Level `1` compresses
  snapshots the least but at the fastest speed. Level `9`
  compresses snapshots the most but at the slowest speed.

**Note:**

Changing File System Store Gzip Compression Level
affects new snapshots only. It does not affect the compression
level of existing snapshots.

Corresponds to `backup.fileSystemSnapshotStore.gzip.compressionLevel`.

### Backup Snapshots Schedule

**`Snapshot Interval (Hours)`**

*Type*: integer

*Default*: 24

Specifies the time, in hours, between two consecutive snapshots.

Accepted values are:

**6**, **8**, **12**, or **24**

Corresponds to `brs.snapshotSchedule.interval`.

**`Base Retention of Snapshots (in Days)`**

*Type*: integer

*Default*: 2

Specifies how many days an interval snapshot is stored. The accepted
values vary depending upon the value of `Snapshot Interval (Hours)`:

|  |  |
|---|---|
| `Snapshot Interval (Hours)` | Accepted Values |
| < `24` | **2**, **3**, **4**, or **5**. |
| = `24` | **2**, **3**, **4**, **5**, **6**, **7**, **8**, **9**, **10**, **11**, **12**, **13**, **14**, **15**, **16**, **17**, **18**, **19**, **20**, **21**, **22**, **23**, **24**, **25**, **26**, **27**, **28**, **29**, **30**. |

Corresponds to `brs.snapshotSchedule.retention.base`.

**`Daily Retention of Snapshots (in Days)`**

*Type*: integer

*Default*: 0

Specifies how many days a daily snapshot is stored.

Accepted values are:

- **No daily retention**
- One of the following integers: **3**, **4**, **5**, **6**, **7**,
  **15**, **30**, **60**, **90**, **120**, **180**, or **360**

Corresponds to `brs.snapshotSchedule.retention.daily`.

**`Weekly Retention of Snapshots (in Weeks)`**

*Type*: integer

*Default*: 2

Specifies how many weeks a weekly snapshot is stored.

Accepted values are:

- **No weekly retention**
- One of the following integers: **1**, **2**, **3**, **4**, **5**,
  **6**, **7**, **8**, **12**, **16**, **20**, **24**, and **52**

Corresponds to `brs.snapshotSchedule.retention.weekly`.

**`Monthly Retention of Snapshots (in Months)`**

*Type*: integer

*Default*: 1

Specifies how many months a monthly snapshot is stored.

Accepted values are:

- **No monthly retention**
- One of the following integers: **1**, **2**, **3**, **4**, **5**,
  **6**, **7**, **8**, **9**, **10**, **11**, **12**, **13**,
  **18**, **24**, **36**, **48**, **60**, **72**,  or **84**

Corresponds to `brs.snapshotSchedule.retention.monthly`.

**`Restore Digest Method`**

*Type*: string

*Default*: SHA1

Specifies whether or not to generate a SHA1 checksum
for restore archive files.

Accepted values are `SHA1` or `NONE`.

Corresponds to `brs.restore.digest.method`.

### PIT Restore

**`PIT Window (In Hours)`**

*Type*: integer

*Default*: 24

Duration time in hours when you can 
restore from a specific point-in-time (PIT).

Corresponds to `brs.pitWindowInHours`.

### KMIP Server Configuration

**`KMIP Server Host`**

*Type*: string

*Default*: None

Specifies the hostname of a KMIP (Key Management Interoperability) server. 

Starting in MongoDB 4.2.1 (and 4.0.14),
you can specify more than one KMIP (Key Management Interoperability) server 
in a comma-seperated list. 

**Important:**

In MongoDB versions earlier than 4.0.14 or 4.2.1,
Ops Manager uses only the first KMIP (Key Management Interoperability) hostname in a list of KMIP (Key Management Interoperability)
server hostnames. 

Corresponds to `backup.kmip.server.host`.

**`KMIP Server Port`**

*Type*: integer

*Default*: 5696

Specifies the port of the KMIP (Key Management Interoperability) server.

Corresponds to `backup.kmip.server.port`.

**`KMIP Server CA File`**

*Type*: string

*Default*: `/opt/mongodb-mms/classes/kmip_server_test.pem`

Specifies a `.PEM`-format file that contains one or more
certificate authorities.

Corresponds to `backup.kmip.server.ca.file`.

### Queryable Snapshot Configuration

**`Proxy Server Port`**

*Type*: integer

*Default*: 25999

Port for the queryable backup host.

**Note:**

After updating `Proxy Server Port`, restart the Web
Server for the change to take effect.

Corresponds to `brs.queryable.proxyPort`.

**`Proxy Server PEM File`**

*Type*: string

*Default*: `/etc/mongodb-mms/queryable-backup.pem`

Required if using Queryable Snapshot. PEM (Privacy-Enhanced Mail) file that contains the
full certificate chain for one or more trusted certificates and the
associated private keys.

`Proxy Server PEM File` has the following restrictions:

- This PEM file must be different than the one used for HTTPS (Hypertext Transfer Protocol Secure)
  connections to Ops Manager (`HTTPS PEM Key File`).
- This PEM file should use a key length greater than 512-bit. Using a
  2048-bit RSA key is recommended.
- This PEM file should use a message digest stronger than `sha1`,
  such as `sha256`.

**Note:**

After updating `Proxy Server PEM File`, restart the Web
Server for the change to take effect.

Corresponds to `brs.queryable.pem`.

**`Proxy Server PEM File Password`**

*Type*: string

Required if `Proxy Server PEM File` is encrypted.

**Note:**

After updating `Proxy Server PEM File Password`, restart
the Web Server for the change to take effect.

Corresponds to `brs.queryable.pem.pwd`.

**`Expiration (Hours)`**

*Type*: integer

*Default*: 24

Duration time in hours for a Queryable Snapshop once initiated.

Corresponds to `brs.queryable.expiration`.

**`Read Cache Size (MB)`**

*Default*: 512

Size (in megabytes) that you allocate from the JVM (Java Virtual Machine) heap for the
global snapshot cache. The global snapshot cache optimizes
repeated queries for the same snapshot data to the Queryable
Snapshots.

**Important:**

MongoDB does not advise changing this value unless MongoDB support
directs you to change it.

Corresponds to `brs.queryable.lruCacheCapacityMB`.

**`Queryable Startup Timeout (Seconds)`**

*Default*: 60

Number of seconds to wait for the Queryable Snapshot to prepare
before timing out.

Corresponds to `brs.queryable.mounttimeout`.

**`Mongo Connection Timeout (Seconds)`**

*Default*: 30

Number of seconds to wait for a connection to the Queryable Snapshot
mongod instance before timing out.

Corresponds to `brs.queryable.connecttimeout`.

## Permissions

### Usage Information Collection

Toggle to On to allow MongoDB, Inc. to collect generic
usage information.

## Backing DBs

This setting allows you to monitor your Ops Manager backing databases
through your Ops Manager Application.

**`Application Database Monitoring`**

*Type*: string

*Default*: false

Flag that indicates that Ops Manager can monitor its application
database.

To monitor the application databases, you need to:

1. Click Enable on this page.
2. Install the MongoDB Agent on the application database hosts.
3. Add the application database.

**See also:**

To follow the full procedure, see
/tutorial/enable-appdb-monitoring.

## Miscellaneous

### HTTP/HTTPS Proxy

**`Proxy Host`**

*Type*: string

Specify the hostname of the HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure) proxy to which you
wish to connect.

```ini
proxy.example.com
```

Corresponds to `http.proxy.host`.

**`Proxy Port`**

*Type*: integer

Specify the port on which you wish to connect to the host. You must
specify both the `Proxy Port` and `Proxy Host` to
use a proxy.

Corresponds to `http.proxy.port`.

**`Non Proxy Hosts`**

*Type*: string

Specify a pipe-separated (`|`) list of internal hosts
to bypass the outgoing proxy that you configured.

```ini
*.foo.com|localhost
```

Corresponds to `http.proxy.nonProxyHosts`.

**`Proxy Username`**

*Type*: string

If the proxy requires authentication, use this setting to specify
the username with which to connect to the proxy.

Corresponds to `http.proxy.username`.

**`Proxy Password`**

*Type*: string

If the proxy requires authentication, use this setting to specify
the password with which to connect to the proxy.

Corresponds to `http.proxy.password`.

### Twilio Integration

To receive alert notifications via SMS (short message service) or 2FA (two-factor authentication) code,
you must have a [Twilio](http://www.twilio.com/docs/quickstart)
account.

**`Account SID`**

*Type*: string

[Twilio](http://www.twilio.com/docs/quickstart) account ID.

Corresponds to `twilio.account.sid`.

**`Twilio Auth Token`**

*Type*: string

Twilio API (Application Programming Interface) token.

Corresponds to `twilio.auth.token`.

**`Twilio From Number`**

*Type*: string

Twilio phone number.

Corresponds to `twilio.from.num`.

### MongoDB Version Management

The following settings determine how Ops Manager knows what MongoDB
releases exist and how the MongoDB binaries are supplied to the
Ops Manager server. The Automations and Backup Daemons use these
binaries when deploying MongoDB.

**`Installer Download Source`**

*Type*: string

*Default*: remote

You need to select the Source for agents to download 
MongoDB binaries:

|  |  |
|---|---|
| remote | All Agents and Ops Manager hosts download MongoDB binaries from a remote source in the background. An internet connection is required on all hosts. You can specify the remote source for downloading MongoDB binaries with the `Base URL` field. If you don't, Base URL defaults to **mongodb.com** and **fastdl.mongodb.org**. |
| hybrid | Agents get MongoDB binaries from Ops Manager, which fetches binaries from a remote source. You can specify the remote source for downloading MongoDB binaries with the `Base URL` field. If you don't, Base URL defaults to **mongodb.com** and **fastdl.mongodb.org**. |
| local | Agents get MongoDB binaries from Ops Manager, which has them on disk. An Ops Manager administrator must provide installers from the MongoDB Download Center and upload them into the `Versions Directory`. Ops Manager serves the installers to Agent hosts. The Version Manifest must be updated manually. No hosts in the deployment require an internet connection. |

Corresponds to `automation.versions.source`.

**`Base URL`**

*Type*: string

*Default*: mongodb.com, fastdl.mongodb.org

HTTP(S) endpoint to fetch MongoDB binaries from. If the endpoint is 
an HTTPS endpoint, the Certificate Authority file specified by 
`httpsCAFile` will be used to validate the certificate. If 
Base URL is unset, the remote URLs for mongodb binaries 
are **mongodb.com** and **fastdl.mongodb.org**.

Corresponds to `automation.versions.download.baseUrl`.

**`Versions Directory`**

*Type*: string

*Default*:  `/opt/mongodb/mms/mongodb-releases/`

Specify the directory on the Ops Manager Application server where Ops Manager
stores the MongoDB binaries. The Automation accesses the
binaries when installing or changing versions of MongoDB on your
deployments. If you set `Version Manifest Source` to run in
`Local` mode, the Backup Daemons also access the MongoDB binaries
from this directory. See /tutorial/configure-local-mode for
more information.

Corresponds to `automation.versions.directory`.

**`Backup Versions Auto Download`**

*Type*: boolean

*Default*: True

Flag indicating whether the Backup Daemons automatically install the
versions of MongoDB that the Backup Daemons need.

|  |  |
|---|---|
| `true` | The daemons retrieve the binaries from MongoDB Inc. over the internet. |
| `false` | Backup Daemons do not have internet access and require that an Ops Manager administrator manually download and extract every archived version of a MongoDB release that the backup daemons need. The administrator must place the extracted binaries into the `Versions Directory` on the Ops Manager hosts. |

**Warning:**

Set to `false` when Ops Manager is running in
Local Mode.

Corresponds to `mongodb.release.autoDownload`.

**`Backup Versions Auto Download Enterprise Builds`**

*Type*: boolean

Flag indicating whether the Backup Daemons automatically install the
Enterprise editions of the versions of MongoDB that the Backup
Daemons need. Requires `Backup Versions Auto Download` be set to `true`.

**Warning:**

If you plan on running
`MongoDB Enterprise` on
Linux hosts, then you must manually install a set of dependencies
to each host *before installing MongoDB*. The MongoDB manual
provides the appropriate command to install the dependencies.

See /tutorial/configure-local-mode.

Corresponds to `mongodb.release.autoDownload.enterprise`.

**`Required Module For Backup`**

*Type*: string

*Default*: Enterprise Preferred

Specifies whether to use MongoDB Community or Enterprise binaries
for backup.

Accepted values are:

- Enterprise Preferred
- Enterprise Required
- Community Required

When Enterprise Required or Community Required is selected, Ops Manager only uses those
binaries for backup. When Enterprise Preferred is selected, Ops Manager uses
Enterprise binaries if available and Community binaries if they are
not.

**Note:**

When Enterprise Required is selected, you must either set `Backup Versions Auto Download Enterprise Builds` to
`true` or manually place Enterprise binaries in the `Versions Directory`
in Local Mode.

**Warning:**

Backup fails when either Enterprise Required or Community Required is selected,
but the `Versions Directory` does not contain the required binary.

Corresponds to `mongodb.release.modulePreference`.

### Default Monitoring Data Retention

Ops Manager gathers metric data at a 10-second granularity. The
Default Monitoring Data Retention table determines how long
Ops Manager stores metric data. For each increasing granularity level,
Ops Manager computes the data based on the averages from the previous
granularity level.

**Note:**

Ops Manager gathers Replication Lag and Replication Headroom
metrics at an 85-second granularity regardless of your project's
default granularity level.

The table determines the default settings for new groups. If you change
the settings, Ops Manager prompts you whether to also apply the settings
to existing groups. To change the settings for a specific group without
changing the Ops Manager default settings, see
groups-page-admin-ui.

Increasing the retention period for a granularity requires more storage
on the Ops Manager Application Database.

**Note:**

If you decrease the retention period for existing projects, Ops Manager
doesn't recover available disk capacity on the file system at that
moment. If you change the retention period, Ops Manager can use additional
disk capacity in the short term when transitioning to the shorter
retention period.

**`Default Monitoring Data Retention 1 Minute`**

*Type*: string

*Default*: 2 days

Length of time that Ops Manager stores metric data at the minute
granularity level. Ops Manager computes the data based on the averages
from the hourly granularity level.

The default setting applies to new projects. If you change this
settings, Ops Manager prompts you whether to also apply that change to
existing projects. To change the settings for a specific project
without changing the Ops Manager default settings, see
groups-page-admin-ui.

Accepted values are:

- 2 days
- 14 days

Increasing the retention period for a granularity requires more
storage on the Ops Manager Application Database.

**`Default Monitoring Data Retention 1 Hour`**

*Type*: string

*Default*: 2 months

Length of time that Ops Manager stores metric data at the hourly
granularity level. Ops Manager computes the data based on the averages
from the daily granularity level.

The default setting applies to new projects. If you change this
settings, Ops Manager prompts you whether to also apply that change to
existing projects. To change the settings for a specific project
without changing the Ops Manager default settings, see
groups-page-admin-ui.

Accepted values are:

- 2 months
- 12 months

Increasing the retention period for a granularity requires more
storage on the Ops Manager Application Database.

**`Default Monitoring Data Retention 1 Day`**

*Type*: string

*Default*: Forever

Length of time that Ops Manager stores metric data at the daily
granularity level.

The default setting applies to new projects. If you change this
settings, Ops Manager prompts you whether to also apply that change to
existing projects. To change the settings for a specific project
without changing the Ops Manager default settings, see
groups-page-admin-ui.

Increasing the retention period for a granularity requires more
storage on the Ops Manager Application Database.

### Alerts

**`Webhook URL`**

Corresponds to `mms.alerts.webhook.adminEndpoint`.

**`Webhook Secret`**

Corresponds to `mms.alerts.webhook.adminSecret`.

### Kubernetes Setup

**`Kubernetes Secret Setup`**

*Type*: string

Path to the YAML file that contains your Programmatic API Key as a Kubernetes secret to create or update 
Kubernetes [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/) 
in your Ops Manager project.

This file must be in YAML format and must be stored under 
`/mongodb-ops-manager/` directory. 

Corresponds to `kubernetes.templates.credentialsFilePath`.

**`Kubernetes ConfigMap Setup`**

*Type*: string

Path to the YAML file that contains the ConfigMap to use to link to 
your Ops Manager project.

This file must be in YAML format and must be stored under 
`/mongodb-ops-manager/` directory. 

Corresponds to `kubernetes.templates.projectFilePath`.

## Custom

To configure certain settings, you need to add the setting and value to
the Custom page.

These settings include:

- `mms.admin.diagnostics.archiveDocAgeLimit`
- `mms.admin.diagnostics.archiveDocCountLimit`
- `mms.admin.diagnostics.archiveDocSizeLimit`
- `mms.automation.agentFeatures.migrationHosts.canManageDeployments`
- `mms.disableCiphers`
- `mms.ldap.group.separator`
- `mms.minimumTLSVersion`
- `mongodb.disable.numa`
- `opsgenie.api.url`

### Modifying a Custom Setting

To add a custom setting:

1. Type the setting into the Key box.
2. Type the desired setting value into the Value box.
3. Click Save.
