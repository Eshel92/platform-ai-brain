<!-- Part 4 of 5 of reference/configuration.md (split because the page is big). -->

## User Authentication

**`mms.email.validation`**

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

Corresponds to `Username Validation`.

**`mms.userSvcClass`**

*Type*: string

*Default*: `UserSvcDb`

Select whether to store authentication credentials in the Ops Manager
Application Database or in an LDAP (Lightweight Directory Access Protocol) directory.

Accepted values are:

| Auth Method | Accepted Value |
|---|---|
| Application Database | `UserSvcDb` IMPORTANT: In Ops Manager 6.0, the accepted value is `com.xgen.svc.mms.svc.user.UserSvcDb`. If you use this old accepted value, your Ops Manager instance will not start during preflight checks. |
| LDAP (Lightweight Directory Access Protocol) | `UserSvcLdap` |
| SAML (Security Assertion Markup Language) | `UserSvcSaml` |

Corresponds to `User Authentication Method`.

### Authentication through Ops Manager Application Database

**`mms.password.maxDaysBeforeChangeRequired`**

*Type*: number

Number of days a password is valid before the password expires.

Corresponds to `Days Before Password Change Required`.

**`mms.password.maxDaysInactiveBeforeAccountLock`**

*Type*: number

Maximum number of days with no visits to the Ops Manager website
before Ops Manager locks an account.

Corresponds to `Days Inactive Before Account Lock`.

**`mms.password.maxFailedAttemptsBeforeAccountLock`**

*Type*: number

Number of failed login attempts before an account becomes
locked. Only an an Ops Manager Administrator can unlock a locked account.

Corresponds to `Failed Login Attempts Before Account Lock`.

**`mms.password.minChangesBeforeReuse`**

*Type*: number

Number of previous passwords to remember. You cannot reuse a
remembered password as a new password.

Corresponds to `Password Changes Before Reuse`.

**`mms.login.ratelimit.attemptsAllowed`**

*Type*: number

Number of logins a user from a specific IP address 
can attempt during a timeout period.
You must configure this setting alongside 
`Login Attempts Timeout Period`.

Corresponds to `Login Attempts Allowed Before Timeout`.

**`mms.login.ratelimit.lockedPeriodMinutes`**

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

Corresponds to `Login Attempts Timeout Period`.

**`mms.user.invitationOnly`**

*Type*: boolean

If true, new users can register by invitation only. The invitation
provides a URL (Uniform Resource Locator) that displays the registration link. If false, new
users can register if they have the Ops Manager URL (Uniform Resource Locator).

Corresponds to `Invitation Only Mode`.

**`mms.user.bypassInviteForExistingUsers`**

*Type*: boolean

*Default*: False

This checkbox appears when you set `mms.userSvcClass` to 
`UserSvcDb`.

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

Corresponds to `Bypass Invitation Mode`.

**`mms.user.passwordHashIterations`**

*Type*: number

Number of iterations for the `pbkdf2` hashing algorithm.

Corresponds to `Password Hashing Iterations`.

### Authentication through LDAP

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

**`mms.ldap.bindDn`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) user used to execute searches for other users.

```ini
mms.ldap.bindDn=authUser@acme.example.com
```

Corresponds to `LDAP Bind Dn`.

**`mms.ldap.bindPassword`**

*Type*: string

Password for the search user.

```ini
mms.ldap.bindPassword=<password>
```

Corresponds to `LDAP Bind Password`.

**`mms.ldap.global.role.automationAdmin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global automation
admin role in Ops Manager. Specify projects
using the format used by the LDAP (Lightweight Directory Access Protocol) attribute specified in the
`LDAP User Group` setting. You can specify multiple projects
using the `;;` delimiter. To change the default delimiter, use the
`mms.ldap.project.separator` setting.

```ini
mms.ldap.global.role.automationAdmin=CN\=MMS-AutomationAdmin,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Each Ops Manager global role provides its level of access to all the Ops Manager
projects in the deployment. To
provide access to specific projects, use group-level roles.

Corresponds to `LDAP Global Role Automation Admin`.

**`mms.ldap.global.role.backupAdmin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global backup admin
role in Ops Manager.

```ini
mms.ldap.global.role.backupAdmin=CN\=MMS-BackupAdmin,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role Backup Admin`.

**`mms.ldap.global.role.monitoringAdmin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global monitoring
admin role in Ops Manager.

```ini
mms.ldap.global.role.monitoringAdmin=CN\=MMS-MonitoringAdmin,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role Monitoring Admin`.

**`mms.ldap.global.role.owner`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group that has full privileges for the Ops Manager deployment,
including full access to all Ops Manager
projects and all administrative
permissions. Users in the specified LDAP (Lightweight Directory Access Protocol) group receive the
global owner role in Ops Manager. Specify the
project using the format that is used by the LDAP (Lightweight Directory Access Protocol) attribute
specified in the `LDAP User Group` setting.

```ini
mms.ldap.global.role.owner=CN\=MMSGlobalOwner,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role Owner`.

**`mms.ldap.global.role.readOnly`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the
global read-only role in Ops Manager.

```ini
mms.ldap.global.role.readOnly=CN\=MMS-ReadOnly,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role Read Only`.

**`mms.ldap.global.role.userAdmin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global user admin role in Ops Manager.

```ini
mms.ldap.global.role.userAdmin=CN\=MMS-UserAdmin,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role User Admin`.

**`mms.ldap.group.baseDn`**

*Type*: string

*Default*: `LDAP User Base Dn` value

Base Distinguished Name (DN) that Ops Manager uses to search for
groups. If left blank, this setting uses the default value.

```ini
mms.ldap.group.baseDn=OU\=groups,DC\=acme,DC\=com
```

Corresponds to `LDAP Group Base Dn`.

**`mms.ldap.group.member`**

*Type*: string

Field on the group entry containing user Distinguished Names (DN).
The groupOfNames or
groupOfUniqueNames object classes are
commonly used.

```ini
mms.ldap.group.member=member
```

Corresponds to `LDAP Group Member Attribute`.

**`mms.ldap.group.separator`**

*Type*: string

*Default*: `;;`

To set the LDAP (Lightweight Directory Access Protocol) separator, follow the Modify a Custom Setting procedure using the following values:

|  |  |
|---|---|
| Key | `mms.ldap.group.separator` |
| Value | `<desired-separator>` |

Each of the global role values takes a delimited list of projects:

```ini
"dbas,sysadmins"
```

If a group value contains the delimiter, the delimiter must be set
to another value.

**Example:**

If you have the group value `"CN\=foo,DN\=bar"` and the
delimiter is `,` then Ops Manager parses `"CN\=foo,DN\=bar"` as two
elements rather than as the description for a single group.

**`mms.ldap.referral`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) field used to set how to handle referrals. Accepts two values:

- `ignore`: Ignore referrals.
- `follow`: Automatically follow any referrals.

Corresponds to `LDAP Referral`.

**`mms.ldap.ssl.CAFile`**

*Type*: string

A file containing one or more trusted certificates in PEM format.
Use this setting if you are using LDAPS (Secure Lightweight Directory Access Protocol) and the server is using a
certificate that is not from a well-known Certificate Authority.

```ini
mms.ldap.ssl.CAFile=/opt/CA.pem
```

Corresponds to `LDAP SSL CA File`.

**`mms.ldap.ssl.PEMKeyFile`**

*Type*: string

A file containing a client certificate and private key. Use this
setting when your TLS (Transport Layer Security)/SSL (Secure Sockets Layer) LDAP (Lightweight Directory Access Protocol) server requires client
certificates.

```ini
mms.ldap.ssl.PEMKeyFile=/opt/keyFile.pem
```

Corresponds to `LDAP SSL PEM Key File`.

**`mms.ldap.ssl.PEMKeyFilePassword`**

*Type*: string

Password for `LDAP SSL PEM Key File`. Use this setting
if the `PEMKeyFile` is encrypted.

```ini
mms.ldap.ssl.PEMKeyFilePassword=<password>
```

Corresponds to `LDAP SSL PEM Key File Password`.

**`mms.ldap.url`**

*Type*: string

URI (Uniform Resource Identifier) for the LDAP (Lightweight Directory Access Protocol) or LDAPS (Secure Lightweight Directory Access Protocol) server.

```ini
mms.ldap.url=ldaps://acme-dc1.acme.example.com:3890
```

Corresponds to `LDAP URI`.

**`mms.ldap.user.baseDn`**

*Type*: string

Base Distinguished Name (DN) that Ops Manager uses to search for
users.

Escape the `=` sign with `\`.

```ini
mms.ldap.user.baseDn=DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP User Base Dn`.

**`mms.ldap.user.email`**

*Type*: string

*Default*: `mail` per RFC2256

LDAP (Lightweight Directory Access Protocol) user attribute that contains the user's email address.
After successful LDAP (Lightweight Directory Access Protocol) authentication, Ops Manager synchronizes the
specified LDAP (Lightweight Directory Access Protocol) attribute with the email address from the Ops Manager
user record.

```ini
mms.ldap.user.email=mail
```

Corresponds to `LDAP User Email`.

**`mms.ldap.user.firstName`**

*Type*: string

*Default*: `givenName` per RFC2256

LDAP (Lightweight Directory Access Protocol) user attribute that contains the user's first name. After
successful LDAP (Lightweight Directory Access Protocol) authentication, Ops Manager synchronizes the specified
LDAP (Lightweight Directory Access Protocol) attribute with the first name from the Ops Manager user record.

```ini
mms.ldap.user.firstName=givenName
```

Corresponds to `LDAP User First Name`.

**`mms.ldap.user.group`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) user attribute that contains the list of LDAP (Lightweight Directory Access Protocol) groups
the user belongs to. The LDAP (Lightweight Directory Access Protocol) attribute can use any format to list
the projects, including Common Name (`cn`) or Distinguished Name
(`dn`). All Ops Manager settings in this configuration file that specify
projects must match the chosen format.

**Important:**

Ops Manager deprecated `mms.ldap.user.group`. Use `mms.ldap.group.member`.

If you provide values for:

- Both `mms.ldap.user.group` and `mms.ldap.group.member`, Ops Manager uses
  `mms.ldap.group.member` and ignores `mms.ldap.user.group`.
- `mms.ldap.user.group` only, Ops Manager doesn't recognize
  the user's membership in nested LDAP groups.

```ini
mms.ldap.user.group=memberOf
```

Corresponds to `LDAP User Group`.

**`mms.ldap.user.lastName`**

*Type*: string

*Default*: `surname` per RFC2256

LDAP (Lightweight Directory Access Protocol) user attribute that contains the user's last name. After
successful LDAP (Lightweight Directory Access Protocol) authentication, Ops Manager synchronizes the specified
LDAP (Lightweight Directory Access Protocol) attribute with the last name from the Ops Manager user record.

```ini
mms.ldap.user.lastName=sn
```

Corresponds to `LDAP User Last Name`.

**`mms.ldap.user.searchAttribute`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) field used for the LDAP (Lightweight Directory Access Protocol) search. This is typically a
username or an email address. The value of this field is also used
as the Ops Manager username.

```ini
mms.ldap.user.searchAttribute=<myAccountName>
```

Corresponds to `LDAP User Search Attribute`.

**`mms.login.newDeviceNotification.enabled`**

*Type*: boolean

Indicator as to the user should be notified that they have logged
in from a new device.

Corresponds to `New Device Login Notification`.

### Authentication through SAML

**`mms.saml.idp.uri`**

*Type*: string

URI (Uniform Resource Identifier) of the Identity Provider (IdP (Identity Provider)) that you use to coordinate
your Single Sign-On. This might be referred to as the *EntityId* or
the *Identity Provider Issuer*.

**`mms.saml.sso.url`**

*Type*: string

URL (Uniform Resource Locator) of the Single Sign-On endpoint that Ops Manager calls when a user
attempts to sign in.

**`mms.saml.slo.url`**

*Type*: string

URL (Uniform Resource Locator) of the Single Logout endpoint that Ops Manager calls when a user
attempts to log out. If set, when a user attempts to log out of
Ops Manager, they log out of your IdP (Identity Provider). If left blank, logging out of
Ops Manager doesn't log the user out of their IdP (Identity Provider) session.

**`mms.saml.x509.cert`**

*Type*: string

Certificate provided by your IdP (Identity Provider) that Ops Manager uses to verify its
validity to the IdP (Identity Provider).

**`mms.saml.ssl.PEMKeyFile`**

*Type*: string

Absolute path to the PEM file for the certificate that the SP (Service Provider)
uses to sign requests, containing both the private and public key. If
this is left blank, Ops Manager doesn't sign SAML (Security Assertion Markup Language) auth requests to the
IdP (Identity Provider) and you can't encrypt SAML (Security Assertion Markup Language) assertions.

**`mms.saml.ssl.PEMKeyFilePassword`**

*Type*: string

Required if the PEM (Privacy-Enhanced Mail) file contains an encrypted private key. Specify
the password for PEM (Privacy-Enhanced Mail) file.

**`mms.saml.encrypted.assertions`**

*Type*: boolean

Flag that indicates whether or not the IdP (Identity Provider) encrypts the assertions
it sends to Ops Manager.

**`mms.saml.signedAssertions`**

*Type*: boolean

*Default*: `true`

Flag that indicates whether or not the IdP (Identity Provider) signs the assertions
it sends to Ops Manager.

**Important:**

Ensure that either the assertions or the response are signed. 
The configuration will fail the verification and Ops Manager returns 
an error if either the assertions or the response aren't signed.

Corresponds to `SAML Signed Assertions`.

**`mms.saml.signedMessages`**

*Type*: boolean

*Default*: `true`

Flag that indicates whether or not the IdP (Identity Provider) signs the responses
it sends to Ops Manager.

**Important:**

Ensure that either the assertions or the response are signed. 
The configuration will fail the verification and Ops Manager returns 
an error if either the assertions or the response aren't signed.

Corresponds to `SAML Signed Messages`.

**`mms.saml.signature.algorithm`**

*Type*: string

Algorithm to encrypt the signature sent to and from the IdP (Identity Provider).

You must use one of the following full W3.org signature algorithm values:

- `http://www.w3.org/2001/04/xmldsig-more#rsa-sha1`
- `http://www.w3.org/2000/09/xmldsig#dsa-sha1`
- `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`
- `http://www.w3.org/2001/04/xmldsig-more#rsa-sha384`
- `http://www.w3.org/2001/04/xmldsig-more#rsa-sha512`

**Important:**

You must specify the complete W3.org signature algorithm URL, not 
a simple string value. Using simple string values, such as `rsa-sha256`, 
causes Ops Manager to return an `unauthorized` error because the 
IdP (Identity Provider) cannot validate the signatures properly.

**Example:**

```text
mms.saml.signature.algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256
```

**`mms.saml.global.role.owner`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have full
privileges over this deployment, including full access to all groups
and all administrative permissions.

**`mms.saml.global.role.automationAdmin`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Automation Admin` role.

**`mms.saml.global.role.backupAdmin`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Backup Admin` role.

**`mms.saml.global.role.monitoringAdmin`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Monitoring Admin` role.

**`mms.saml.global.role.userAdmin`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global User Admin` role.

**`mms.saml.global.role.readOnly`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Read Only` role.

**`mms.saml.user.firstName`**

*Type*: string

SAML (Security Assertion Markup Language) User Attribute that contains the user's first name.

**`mms.saml.user.lastName`**

*Type*: string

SAML (Security Assertion Markup Language) User Attribute that contains the user's last name.

**`mms.saml.user.email`**

*Type*: string

SAML (Security Assertion Markup Language) User Attribute that contains the user's email address.

**`mms.saml.group.member`**

*Type*: string

*Default*: `groups`

SAML (Security Assertion Markup Language) Attribute that contains the list of groups Ops Manager uses to
map roles to Projects and Organizations.

Corresponds to `SAML Group Member Attribute`.

### Multi-Factor Authentication (MFA)

**`mms.multiFactorAuth.level`**

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

Corresponds to `Multi-factor Auth Level`.

**`mms.multiFactorAuth.allowReset`**

*Type*: boolean

*Default*: False

When `true`, Ops Manager allows users to reset their two-factor
authentication settings via email in an analogous fashion to
resetting their passwords.

To reset two-factor authentication, a user must:

- be able to receive email at the address associated with the user
  account.
- know the user account's password.
- know the `agent API key` for each Ops Manager project the user
  belongs to.

Corresponds to `Multi-factor Auth Allow Reset`.

**`mms.multiFactorAuth.issuer`**

*Type*: string

If Google Authenticator provides two-factor authentication, this
string is the `issuer` in the Google Authenticator app. If left
blank, the `issuer` is the domain name of the Ops Manager installation.

Corresponds to `Multi-factor Auth Issuer`.

**`mms.multiFactorAuth.require`**

*Type*: boolean

*Default*: False

When `true`, Ops Manager will require two-factor authentication for
users to log in or to perform certain destructive operations within
the application.

If you configure
Twilio integration,
users may obtain their second factor tokens via Google
Authenticator, SMS, or voice calls. Otherwise, the only mechanism
to provide two-factor authentication is Google Authenticator.

### reCaptcha and Session Length

**`reCaptcha.enabled.registration`**

*Type*: boolean

*Default*: false

Indicator as to you want a new user to validate themselves
using reCaptcha validation when they register to use Ops Manager.

Set to `true` to require
[reCaptcha](https://www.google.com/recaptcha)
validation when a new user registers.

This setting requires a
[reCaptcha account](https://www.google.com/recaptcha/admin).

Corresponds to `ReCaptcha Enabled On Registration`.

**`reCaptcha.enabled`**

*Type*: boolean

*Default*: false

Indicator as to you want a user to validate themselves using
reCaptcha validation when they log into Ops Manager.

Set to `true` to require
[reCaptcha](https://www.google.com/recaptcha)
validation when a user logs in.

This setting requires a
[reCaptcha account](https://www.google.com/recaptcha/admin).

Corresponds to `ReCaptcha Enabled`.

**`reCaptcha.private.key`**

*Type*: string

ReCaptcha private key associated with your account.

Corresponds to `ReCaptcha Private Key`.

**`reCaptcha.public.key`**

*Type*: string

ReCaptcha public key associated with your account.

Corresponds to `ReCaptcha Public Key`.

**`mms.session.maxHours`**

*Type*: number

Number of hours before a session on the Ops Manager website expires.

**Note:**

Session Max Hours reflects the total Ops Manager session time, not
just idle time. Both active and idle sessions expire when 
Session Max Hours elapses.

Set this value to `0` to use browser session cookies only.

Corresponds to `Session Max Hours`.

**`mms.session.mode`**

*Type*: String

Either `None` or `Idle`.

`None` disables idle session timeout.
`Idle` logs users out after a period of inactivity.

**`mms.session.idleTimeoutMinutes`**

*Type*: number

The maximum amount of time in minutes that a session can be active with no user activity.
