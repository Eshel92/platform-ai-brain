<!-- Converted from tutorial/configure-for-saml-authentication.txt (reStructuredText). Includes are inlined. -->

# Configure Ops Manager Users for SAML (Security Assertion Markup Language) Authentication

You can use an Identity Provider (IdP (Identity Provider)) that runs the Security
Assertion Markup Language (SAML (Security Assertion Markup Language)) service to manage Ops Manager user
authentication and authorization. When you try to navigate to Ops Manager
without an authenticated session, Ops Manager sends you to the IdP (Identity Provider) where
you log in. After you authenticate, you return to the Ops Manager Application.

This tutorial describes how to:

* Configure SAML (Security Assertion Markup Language) authentication for Ops Manager

* Map SAML (Security Assertion Markup Language) groups to Ops Manager organization-roles and
  project-roles.

## Considerations

### Users Remain Authenticated after SAML (Security Assertion Markup Language) Activation

Once you change your Ops Manager instance to use SAML (Security Assertion Markup Language) authentication, all
users remain logged in to the current session. After the authentication
change, users who try to log into Ops Manager are redirected to the SAML (Security Assertion Markup Language)
IdP (Identity Provider).

### Two-Stage Configuration

Some circular logic applies when setting up a SAML (Security Assertion Markup Language) instance. To
create a working integration:

- The IdP (Identity Provider) needs values from the Service Provider and
- The Service Provider needs values from the IdP (Identity Provider).

To start this integration, follow the Prerequisites, then the Procedure
in this tutorial.

## Prerequisites

To configure SAML (Security Assertion Markup Language) integration, you must perform the following actions
for your SAML (Security Assertion Markup Language) IdP (Identity Provider):

1. Install your SAML (Security Assertion Markup Language) IdP (Identity Provider).

#. Verify that your Ops Manager instance can access your IdP (Identity Provider) over the
   network.

#. In the SAML (Security Assertion Markup Language) IdP (Identity Provider), you must:

   a. Create a SAML (Security Assertion Markup Language) user that maps to your Ops Manager Global Owner.

   #. Create a SAML (Security Assertion Markup Language) group that you can map to your Ops Manager
      Global Owner.

   #. Assign the Global Owner SAML (Security Assertion Markup Language) group to your SAML (Security Assertion Markup Language)
      user.

   #. Create a new application for Ops Manager representing Ops Manager.

   #. Configure initial Ops Manager SAML (Security Assertion Markup Language) values for this new
      application:

      i. Set placeholder values for the following fields:

         - SP Entity ID or Issuer
         - Audience URI
         - Assertion Consumer Service (ACS) URL

      #. Set real values for the following fields in your IdP (Identity Provider):

         * - Field
           - Common Value

         * - Signature Algorithm
           - Your IdP (Identity Provider) might have one or more of the following
             values:

             - `rsa-sha1`
             - `dsa-sha1`
             - `rsa-sha256`
             - `rsa-sha384`
             - `rsa-sha512`

         * - Name ID
           - `Email Address`

         * - Name ID Format
           - `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`

      #. Create attributes with Attribute Names for the following
         Attribute Values:

         - Email Address
         - First Name
         - Last Name
         - User Groups

      #. Configure your IdP (Identity Provider) to require signed SAML Responses and 
         Assertions.

      #. Save these values.

## Procedure

To configure SAML (Security Assertion Markup Language) authentication:

**Step 1: Login to your IdP (Identity Provider).**

**Step 2: Copy SAML (Security Assertion Markup Language) IdP (Identity Provider) values.**

From your IdP (Identity Provider), click on the Ops Manager application:

a. Find the Ops Manager metadata values.
#. Copy the following values to a temporary file:

   - SAML Login URL
   - SAML Logout URL
   - X.509 Certificate (for the IdP (Identity Provider))
   - IdP Entity ID or Issuer
   - Signature Algorithm

**Step 3: Navigate to the User Authentication tab of the Ops Manager Config page.**

Open the Ops Manager Application and navigate to: Admin
arrow-right General arrow-right
Ops Manager Config arrow-right
User Authentication.

**Step 4: Set the User Authentication option to SAML.**

**Step 5: Set the required SAML (Security Assertion Markup Language) IdP (Identity Provider) setting values in Ops Manager.**

Type the values from the IdP (Identity Provider) for the following SAML (Security Assertion Markup Language) fields:

* - Field
  - Necessity
  - Action
  - Default

* - Identity Provider URI
  - Required
  - Type the URI (Uniform Resource Identifier) for your IdP (Identity Provider) you use to coordinate your
    Single Sign-On.

    This URI (Uniform Resource Identifier) is the IdP Entity ID or Issuer from the
    SAML (Security Assertion Markup Language) IdP (Identity Provider).

    This URI (Uniform Resource Identifier) must be the same as the `Issuer URI` in the SAML 
    response.

  - None

* - SSO Endpoint URL
  - Required
  - Type the Single-Sign On URL (Uniform Resource Locator) for your IdP (Identity Provider).

    This URL (Uniform Resource Locator) is the SAML Login URL from your IdP (Identity Provider).

  - None

* - SLO Endpoint URL
  - Optional
  - Type the SAML (Security Assertion Markup Language) IdP (Identity Provider) URL (Uniform Resource Locator) to be called if you want the
    Ops Manager user to log out of their IdP (Identity Provider) when the Ops Manager user logs
    out of Ops Manager.

    This is the SAML Logout URL from your IdP (Identity Provider).

  - None

* - Identity Provider X509 Certificate
  - Required
  - Paste your IdP (Identity Provider)'s X.509 Certificate in this field. The IdP (Identity Provider)
    provides the certificate in PEM (Privacy-Enhanced Mail) format. Make sure you
    include the entire certificate content including and starting
    with `-----BEGIN CERTIFICATE-----` and including and ending
    with `-----END CERTIFICATE-----`. Ops Manager uses this certificate
    to verify itself with the IdP (Identity Provider).

    This is the X.509 Certificate from your
    IdP (Identity Provider).

    This must be the same X.509 Certificate that you
    use to sign SAML Responses and Assertions.

  - None

* - Identity Provider Signature Algorithm
  - Required
  - Select the algorithm used to encrypt the signature sent to and
    from the IdP (Identity Provider). The accepted values are:

    - `rsa-sha1`
    - `dsa-sha1`
    - `rsa-sha256`
    - `rsa-sha384`
    - `rsa-sha512`

    This is the Signature Algorithm from your
    IdP (Identity Provider).
  - None

* - Require Encrypted Assertions
  - Optional
  - Select whether or not your IdP (Identity Provider) encrypts the assertions it
    sends to Ops Manager.
  - `false`

* - Global Role Owner Group
  - Required
  - Type the name of the group in the SAML (Security Assertion Markup Language) Group Member
    Attribute that has full privileges over this deployment,
    including full access to all groups and all administrative
    permissions. This group has the `Global Owner` role
    for this Ops Manager instance.

    You added this group to your IdP (Identity Provider) settings as part of your
    prerequisites.

    This value must match the group member attribute value sent in the 
    SAML (Security Assertion Markup Language) response. If you use Azure (Microsoft Azure) AD (Active Directory) as your IdP (Identity Provider), enter the
    group's Object ID in this field instead of the group's name. 
  - None

* - SAML (Security Assertion Markup Language) Attribute For User First Name
  - Required
  - Type the name of the SAML (Security Assertion Markup Language) Attribute that contains User's
    First Name
  - None

* - SAML (Security Assertion Markup Language) Attribute For User Last Name
  - Required
  - Type the name of the SAML (Security Assertion Markup Language) Attribute that contains User's
    Last Name
  - None

* - SAML (Security Assertion Markup Language) Attribute For User Email
  - Required
  - Type the name of the SAML (Security Assertion Markup Language) Attribute that contains User's
    Email Address.
  - None

* - SAML (Security Assertion Markup Language) Group Member Attribute
  - Required
  - Type the name of the SAML (Security Assertion Markup Language) Attribute that contains the list
    of groups Ops Manager uses to map roles to Projects and
    Organizations.
  - `groups`

**Step 6: Add any needed optional SAML (Security Assertion Markup Language) IdP (Identity Provider) settings to Ops Manager.**

Type the values from the IdP (Identity Provider) for the following SAML (Security Assertion Markup Language) fields:

* - Field
  - Necessity
  - Action
  - Default

* - Path to SP Certificate PEM Key File
  - Optional
  - Type the absolute file path to the PEM (Privacy-Enhanced Mail)-formatted certificate
    that the Service Provider uses to sign requests. This
    certificate includes the private and public key.

    If this field is left blank:

    - Ops Manager doesn't sign SAML (Security Assertion Markup Language) authentication requests to
      the IdP (Identity Provider).
    - You can't encrypt SAML (Security Assertion Markup Language) assertions.
  - None

* - Password For SP Certificate PEM Key File
  - Conditional
  - If you encrypted the private key in your SP PEM (Privacy-Enhanced Mail) file, type
    its password in this field.
  - None

* - Global Automation Admin Role
  - Optional
  - Type the name of the group whose members have the
    `Global Automation Admin` role.

    This value must match the group member attribute value sent in the 
    SAML (Security Assertion Markup Language) response. If you use Azure (Microsoft Azure) AD (Active Directory) as your IdP (Identity Provider), enter the
    group's Object ID in this field instead of the group's name. 
  - None

* - Global Backup Admin Role
  - Optional
  - Type the name of the group whose members have the
    `Global Backup Admin` role.

    This value must match the group member attribute value sent in the 
    SAML (Security Assertion Markup Language) response. If you use Azure (Microsoft Azure) AD (Active Directory) as your IdP (Identity Provider), enter the
    group's Object ID in this field instead of the group's name. 
  - None

* - Global Monitoring Admin Role
  - Optional
  - Type the name of the group whose members have the
    `Global Monitoring Admin` role.

    This value must match the group member attribute value sent in the 
    SAML (Security Assertion Markup Language) response. If you use Azure (Microsoft Azure) AD (Active Directory) as your IdP (Identity Provider), enter the
    group's Object ID in this field instead of the group's name. 
  - None

* - Global User Admin Role
  - Optional
  - Type the name of the group whose members have the
    `Global User Admin` role.

    This value must match the group member attribute value sent in the 
    SAML (Security Assertion Markup Language) response. If you use Azure (Microsoft Azure) AD (Active Directory) as your IdP (Identity Provider), enter the
    group's Object ID in this field instead of the group's name. 
  - None

* - Global Read Only Role
  - Optional
  - Type the name of the group whose members have the
    `Global Read Only` role.

    This value must match the group member attribute value sent in the 
    SAML (Security Assertion Markup Language) response. If you use Azure (Microsoft Azure) AD (Active Directory) as your IdP (Identity Provider), enter the
    group's Object ID in this field instead of the group's name. 
  - None

**Step 7: Click Save.**

**Step 8: Log in as a global owner.**

Log in to Ops Manager as a user that is part of the SAML group
specified in the Ops Manager SAML Global Role Owner field.

Upon successful login, Ops Manager displays your projects page.

**Step 9: Associate SAML groups with project roles.**

**Note:**

You must have any global role
to create a new project.

a. Click Admin > General > Projects.

#. Click Create a New Project.

#. In Project Name, type a name for the new Ops Manager project.

#. Enter the SAML groups that correspond to
   each project role.

   **Important:**

   You must use the fully qualified distinguished name for each
   group. If multiple LDAP or SAML groups correspond to the same role,
   separate them with two semicolons (`;;`). Remove a group
   from a role's field to revoke the group's access for that
   role.

#. Click Add Project.

a. Click Admin > General > Projects.

#. In the Actions column for a project, click
   `ellipsis`, then click
   Edit SAML Settings.

#. Enter the SAML groups that correspond to each project
   role. 

   **Important:**

   You must use the fully qualified distinguished name for each
   group. If multiple LDAP or SAML groups correspond to the same role,
   separate them with two semicolons (`;;`). Remove a group
   from a role's field to revoke the group's access for that
   role.

#. Click Save Changes.

**Step 10: Associate SAML groups with organization roles.**

**Note:**

You must have any global role
to create a new organization.

a. Click Admin > General > Organizations.

#. Click Create a New Organization.

#. In Organization Name, type a name for the new Ops Manager organization.

#. Enter the SAML groups that correspond to
   each organization role.

   **Important:**

   You must use the fully qualified distinguished name for each
   group. If multiple LDAP or SAML groups correspond to the same role,
   separate them with two semicolons (`;;`). Remove a group
   from a role's field to revoke the group's access for that
   role.

#. Click Add Organization.

a. Click Admin > General > Organizations.

b. Click the Edit Org button.

c. Enter the SAML groups that correspond to
   each organization role.

   **Important:**

   You must use the fully qualified distinguished name for each
   group. If multiple LDAP or SAML groups correspond to the same role,
   separate them with two semicolons (`;;`). Remove a group
   from a role's field to revoke the group's access for that
   role.

#. Click Save Changes.

**Step 11: Add your MongoDB deployments.**

Specify the SAML authentication settings when adding a MongoDB
deployment.

**Step 12: Export your Ops Manager Metadata.**

After you save the SAML (Security Assertion Markup Language) configuration, a link to
Download the Metadata XML File appears.

Click this link to download the SAML (Security Assertion Markup Language) SP metadata XML file.

This metadata file should look similar to this example:

```XML
<?xml version="1.0"?>
<md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" validUntil="2019-09-13T20:36:00Z" cacheDuration="PT604800S" entityID="http://ec2-3-88-178-252.compute-1.amazonaws.com:8080" ID="ONELOGIN_f95ad815-e8da-4ab3-a799-3c581484cd6a">
  <md:SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
    <md:SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="http://ec2-3-88-178-252.compute-1.amazonaws.com:8080/saml/logout"/>
    <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat>
    <md:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="http://ec2-3-88-178-252.compute-1.amazonaws.com:8080/saml/assert" index="1"/>
  </md:SPSSODescriptor>
</md:EntityDescriptor>
```

**Step 13: Import the SAML (Security Assertion Markup Language) SP Metadata into your IdP (Identity Provider).**

If your IdP (Identity Provider) offers the option, import your metadata into the IdP (Identity Provider).
Ops Manager serves as the Service Provider (SP) for your IdP (Identity Provider).

Provide the following values in the metadata XML (eXtensible Markup Language) file to IdP (Identity Provider):

| Field | Common Value |
|---|---|
| SP Entity ID or Issuer | `<OpsManagerHost>:<Port>` |
| Audience URI | `<OpsManagerHost>:<Port>` |
| Assertion Consumer Service (ACS) URL | `<OpsManagerHost>:<Port>/saml/assert` |
| Single Logout URL | `<OpsManagerHost>:<Port>/saml/logout` |

If one or more of these values are missing, use the guidelines listed
in the previous table to set those values.

Save these values in your IdP (Identity Provider).

**Step 14: Test the SAML (Security Assertion Markup Language) integration between Ops Manager and your IdP (Identity Provider).**

a. In a private browser window, go to your Ops Manager instance.

   You are redirected to your IdP (Identity Provider).

b. Authenicate with your IdP (Identity Provider).

   You are then redirected to your Ops Manager instance.
