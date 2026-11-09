<!-- Converted from reference/troubleshooting/authentication.txt (reStructuredText). Includes are inlined. -->

# Authentication

## Two-Factor Authentication

### Missed SMS (short message service) Authentication Tokens

**Warning:** Use Authenticator Apps When Possible

Authenticator applications are the preferred method to SMS (short message service) for
two-factor authentication. SMS (short message service) is an older protocol with many
known security vulnerabilities. The U.S.
NIST (National Institute for Standards and Technology)
advised abandoning SMS (short message service) for 2FA (two-factor authentication) in section 5.1.3.2 of its
Digital Identity Guidelines.

If are using SMS (short message service), but do not receive the authentication tokens via
SMS (short message service):

1. Refer to the /core/two-factor-authentication
   page for more details about using two-factor authentication. This
   page includes any limitations which may affect SMS (short message service) delivery times.

2. Enter the SMS (short message service) phone number with country code first followed by the
   area code and the phone number.

   If you are outside of the United States or Canada, include `011`
   and the [country code](https://countrycode.org/)  because Ops Manager
   uses the U.S.-based [Twilio](https://www.twilio.com) to send text
   messages. As an alternative to your non-U.S. telephone number, use
   a [Google Voice](https://voice.google.com) telephone number.

   **Example:**

   For New Zealand enter `01164` before the phone number. 

   If you do not receive the authentication token in a reasonable
   amount of time, contact your Ops Manager system administrator.

   **See also:**

   To learn more about limits of SMS (short message service) for 2FA (two-factor authentication), see 
   SMS delivery considerations.

### Delete or Reset Two-Factor Authentication

Contact your system administrator to remove or reset two-factor
authentication on your account.

For administrative information on two-factor authentication, see
/tutorial/manage-two-factor-authentication.

## LDAP

### Forgot to Change `MONGODB-CR` Error

If your MongoDB deployment uses LDAP for authentication, and you
find the following error message:

**Warning:**

You forgot to change `MONGODB-CR` to `LDAP (PLAIN)` since
they both take username/password.
