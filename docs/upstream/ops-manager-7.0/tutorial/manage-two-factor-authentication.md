<!-- Converted from tutorial/manage-two-factor-authentication.txt (reStructuredText). Includes are inlined. -->

# Manage Two-Factor Authentication for Ops Manager

## Overview

Administrators can enable two-factor authentication. When enabled,
two-factor authentication requires a user to enter a verification code
to log in and to perform certain protected operations. Operations that
require two-factor authentication include:

- restoring and deleting snapshots,

- stopping and terminating Backup for a sharded cluster or
  replica set,

- inviting and adding users,

- generating new two-factor authentication backup codes, and

- saving phone numbers for two-factor authentication.

Optionally, administrators can set up two-factor authentication with Twilio. This
allows users to receive their authentication codes via SMS.

Users configure two-factor authentication on their accounts through their
Ops Manager user profiles, where they select whether to
receive their verification codes through voice calls, text messages (SMS),
or the Google Authenticator application. If your organization does not use
[Twilio](http://www.twilio.com/docs/quickstart), then users can receive
codes only through Google Authenticator.

Administrators can reset accounts for individual users as needed. Reseting
a user's account clears out the user's existing settings for two-factor
authentication. When the user next performs an action that requires
verification, Ops Manager forces the user to re-enter settings for two-factor
authentication.

## Procedures

### Enable Two-factor Authentication

**Step 1: Go to User Authentication in the Ops Manager Config panel.**

a. Click on Admin on the upper-right hand corner. 

#. From the Ops Manager Admin screen, click on General > 
   Ops Manager Config > User Authentication.

**Step 2: Configure `Multi-Factor Authentication (MFA)`.**

a. Select Multi-Factor Auth Level.

   | Level | Description |
   |---|---|
   | `OPTIONAL` | Users can choose to set up two-factor authentication for their Ops Manager account. |
   | `REQUIRED` | All users **must** set up two-factor authentication. |
   | `REQUIRED_FOR_GLOBAL_ROLES` | Users who possess a global role must set up two-factor authentication, while two-factor authentication is optional for all other users. |

#. Optional. Select whether users can reset their two-factor 
   authentication setting via email.

#. Optional. Specify the  Authenticator app issuer.
   If blank, the issuer is the domain name of the Ops Manager
   installation.

### *Optional*. Enable Twilio Integration

To allow users to receive their authentication codes via SMS,
administrators can optionally enable integration with Twilio.

**Step 1: Go to `Miscellaneous` in the Ops Manager Config panel.**

a. Click on Admin on the upper-right hand corner. 

#. From the Ops Manager Admin screen, click on General > 
   Ops Manager Config > Miscellaneous.

**Step 2: Configure `Twilio Integration`.**

Enter the following to allow delivery of alerts and SMS multi-factor
authentication codes through Twilio:

**Note:**

If you Twilio integration, ensure that
Ops Manager servers can access the `twilio.com` domain.

| Field | Description |
|---|---|
| Account SID | [Twilio](http://www.twilio.com/docs/quickstart) account ID. |
| Twilio Auth Token | Twilio API access token |
| Twilio From Number | Twilio phone number from which to send the alerts and authentication codes to users. |

### Reset a User's Two-factor Authentication Account

Resetting the user's account clears out any existing two-factor
authentication information. The user will be forced to set it up again at
the next login.

You must have the `global user admin` or `global owner` role to perform this procedure.

**Step 1: Open Ops Manager Administration.**

To open Administration, click the Admin link in the
Ops Manager banner.

**Step 2: Select the Users page.**

**Step 3: Locate the user and click the pencil icon on the user's line.**

**Step 4: Select the Clear Two Factor Auth checkbox.**
