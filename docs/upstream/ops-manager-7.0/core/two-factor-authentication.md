<!-- Converted from core/two-factor-authentication.txt (reStructuredText). Includes are inlined. -->

# Manage Your Two-Factor Authentication Options

Two-factor authentication provides a second layer of security for your
Ops Manager account.

When enabled, Ops Manager requires 2FA (two-factor authentication) to help users control access to
their Ops Manager accounts.

To log into Ops Manager, a user must provide their password ("something
you know"), as well as a second time-sensitive verification code,
delivered during authentication ("something you have"). By requiring
both factors, Ops Manager can grant authentication requests with a higher
degree of confidence.

**Note:**

If an `Organization Owner` enables multi-factor authentication for an
organization, all
organization members must enable multi-factor authentication individually to access the
organization. Organization members who have not enabled MFA (Multi-Factor Authentication) are
able to access Ops Manager, but not the organization for which MFA (Multi-Factor Authentication) is
required.

After you enter your username and password, you are prompted for a
six-digit time-sensitive verification code. This code is sent to a
separate device, such as a mobile phone or security token, that you
can read and enter into Ops Manager and complete your login.

**Note:**

To enable or disable two-factor authentication for the entire Ops Manager
environment, see /tutorial/manage-two-factor-authentication.

Ops Manager provides the following sources for 2FA (two-factor authentication) verification codes:

tabs:

  - id: phone
    name: Text/Voice
    content: |

      Text Messages (SMS (short message service))
        When Ops Manager prompts you for a verification code,
        Ops Manager sends the 6-digit verification code using text
        (SMS (short message service)) to the provided phone number.

        The cellular carrier's SMS (short message service) rates apply.

      Automated Voice Calls (US / Canada only)
        When Ops Manager prompts you for a verification code,
        Ops Manager calls the provided phone number. An automated
        system repeats the 6-digit verification code a total of
        three times before hanging up.

        The cellular carrier's Voice Call rates apply.

        **Note:**

        Ops Manager users who operate within a geographic region
        with limited cellular service coverage or reliability may
        encounter delays in receiving the 2FA (two-factor authentication) code via SMS (short message service) or
        Voice. Consider using a 2FA (two-factor authentication) app or device instead.

  - id: app
    name: 2FA App
    content: |

      When Ops Manager prompts you for a verification code, you can
      provide one that is generated in a 2FA (two-factor authentication) app. You must pair
      the 2FA (two-factor authentication) app with Ops Manager first.

      This tutorial uses the Google Authenticator mobile app.

      There are other mobile device apps and web browser plug-ins
      that provide 2FA (two-factor authentication) capabilities. You can use any that support
      the TOTP (Time-based One-Time Password).

      You can pair only one app with Ops Manager at any one time.

  - id: token
    name: 2FA device
    content: |

      When Ops Manager prompts you for a verification code, you can
      provide one that is generated in a 2FA (two-factor authentication) PIV (personal identity verification) device. You
      must pair the PIV (personal identity verification) device app with Ops Manager first using an
      2FA (two-factor authentication) app. These devices must support TOTP (Time-based One-Time Password).

      This procedure uses a YubiKey security key, specifically
      those that work with
      [Authenticator Codes](https://support.yubico.com/support/solutions/articles/15000006419-using-your-yubikey-with-authenticator-codes).
      Other 2FA (two-factor authentication) PIV (personal identity verification) hardware devices that use TOTP (Time-based One-Time Password) should
      work in a similar fashion.

      **Note:** Informational Reference only

      MongoDB does not endorse the aforementioned service, and
      its reference is intended only as informational. Defer to
      your organization's procedures in selecting the
      appropriate vendor or service for supporting 2FA (two-factor authentication) via
      smart card or similar device.

## Configure Two-Factor Authentication

hidden: true

tabs:
  - id: phone
    name: Text/Voice
    content: |

      **Step 1: Go to your Ops Manager Account Settings.**

      In Ops Manager, click your username in the top-right corner
      and select Account.

      **Step 2: Enable Two-Factor Authentication.**

      Click Enable 2FA or click pencil-alt.

      When prompted for verification:

      - If you are setting up 2FA (two-factor authentication), enter your password.
      - If you are editing your 2FA (two-factor authentication) settings, enter a 2FA (two-factor authentication) code.
      - Click Verify.

      **Step 3: Configure Voice/SMS Authentication.**

      a. Click Primary Method

      #. Click Voice/SMS Number.

      #. In the Enter your phone number box, enter your
         preferred mobile phone number.

      #. Select your preferred method of receiving codes:

         - Text Message (SMS) *or*

         - Voice Call (US / Canada Only)

      #. Click Verify.

      #. Once you receive the verification code, enter that code into the 
         into the Verify your code boxes. Each digit is
         entered in its own box.

      Ops Manager automatically verifies the code and saves your settings.

  - id: app
    name: 2FA App
    content: |

      **Step 1: Go to your Ops Manager Account Settings.**

      In Ops Manager, click your username in the top-right corner
      and select Account.

      **Step 2: Enable Two-Factor Authentication.**

      Click Enable 2FA or click pencil-alt.

      When prompted for verification:

      - If you are setting up 2FA (two-factor authentication), enter your password.
      - If you are editing your 2FA (two-factor authentication) settings, enter a 2FA (two-factor authentication) code.
      - Click Verify.

      **Step 3: Configure your Ops Manager 2FA (two-factor authentication) settings.**

      a. Click Primary Method.

      #. Click Google Authenticator.

      **Step 4: On your mobile device or web browser, install Google Authenticator.**

      Although only Google Authenticator is displayed in the
      UI, any TOTP (Time-based One-Time Password) mobile app or web browser plug-in may be used.

      **Note:**

      Wherever you see the phrase **Google Authenticator** in this
      procedure, you can substitute the name of your preferred 2FA (two-factor authentication)
      app.

      | App | iOS | Android | Windows Phone | Blackberry |
      |---|---|---|---|---|
      | Google Authenticator | [Link](https://itunes.apple.com/us/app/google-authenticator/id388497605) | [Link](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) |  |  |
      | Duo Mobile | [Link](https://itunes.apple.com/us/app/duo-mobile/id422663827) | [Link](https://play.google.com/store/apps/details?id=com.duosecurity.duomobile) | [Link](https://www.microsoft.com/en-us/p/duo-mobile/9nblggh08m1g#activetab=pivot:overviewtab) |  |
      | Authy | [Link](https://itunes.apple.com/us/app/google-authenticator/id388497605) | [Link](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2) |  |  |
      | Microsoft Authenticator | [Link](https://itunes.apple.com/us/app/microsoft-authenticator/id983156458?mt=8) | [Link](https://play.google.com/store/apps/details?id=com.azure.authenticator&hl=en_US) | [Link](https://www.microsoft.com/en-us/p/microsoft-authenticator/9nblgggzmcj6?cid=msft_web_chart) |  |
      | Gauth |  |  |  | [Link](https://appworld.blackberry.com/webstore/content/19908006/?countrycode=US&lang=en) |

      **Step 5: Add Ops Manager to Google Authenticator.**

      #. Start Google Authenticator.

      #. Click **+**.

      #. Choose how to pair the Google Authenticator app with Ops Manager.

         - If your mobile device or web browser supports scanning barcodes,
           click Scan a barcode.

           Enable the device's camera, if prompted, and point the device
           at the Ops Manager page to capture the barcode.

         - If your mobile device or web browser does not support scanning
           barcodes, or if you prefer to enter a key, click
           Enter provided key.

           1. Ops Manager displays the Ops Manager Account with a
              Key.

           #. In Google Authenticator, click
              Enter provided key 
              then enter the account and key.

              (Duo Mobile, Authy and other apps have similar prompts.)

           After the barcode is scanned or account and key are entered, 
           the Google Authenticator app produces a 6-digit code 
           to verify the pairing.

      #. Once you receive the verification code, enter that code into the 
         into the Verify your code boxes. Each digit is
         entered in its own box.

      Ops Manager automatically verifies the code and saves your settings.

      **See also:**

      - Pairing third-party applications with [Duo Mobile](https://guide.duo.com/third-party-accounts)

      - Pairing third-party applications with [Authy](https://support.authy.com/hc/en-us/articles/360006303934-Add-a-New-Two-Factor-Authentication-2FA-Account-Token-in-the-Authy-App)

      - Pairing third-party applications with [Microsoft Authenticator](https://support.microsoft.com/en-us/help/4026727/microsoft-account-how-to-use-the-microsoft-authenticator-app)

  - id: token
    name: 2FA device
    content: |

      **Step 1: Download and install the Yubico Authenticator.**

      a. From a web browser, download the
         [Yubico Authenticator](https://www.yubico.com/products/services-software/download/yubico-authenticator/)
         application. 

      #. Double-click on the installer and follow the prompts.

      **Step 2: Insert your Yubikey into a USB port.**

      **Step 3: Go to your Ops Manager Account Settings.**

      In Ops Manager, click your username in the top-right corner
      and select Account.

      **Step 4: Enable Two-Factor Authentication.**

      Click Enable 2FA or click pencil-alt.

      When prompted for verification:

      - If you are setting up 2FA (two-factor authentication), enter your password.
      - If you are editing your 2FA (two-factor authentication) settings, enter a 2FA (two-factor authentication) code.
      - Click Verify.

      **Step 5: Configure your Ops Manager 2FA (two-factor authentication) settings.**

      a. Click Primary Method.

      #. Click Google Authenticator.

      **Step 6: Add Ops Manager to the Yubikey.**

      a. Start the Yubico Authenticator.

      #. Make sure that your web browser is open to your Ops Manager
         Two-Factor Authentication modal with the
         Google Authenticator button selected.

      #. From the File menu in Yubico Authenticator, select
         Scan QR code....

      #. In the New credential dialog box, confirm the
         following settings:

         | Option | Accepted Value | Keep Default? |
         |---|---|---|
         | Issuer | The name you want to display in the Yubico Authenticator application for Ops Manager. | Your choice |
         | Account name | Your Ops Manager username. | Yes |
         | Secret key | Token generated from the QR code. | Yes |
         | Type | Method that determines when to generate a new code. | Yes |
         | Algorithm | Encryption algorithm the token uses. | Yes |
         | Period | Duration that each verification code is valid. | Yes |
         | Digits | Number of digits in the verification code. | Yes |
         | Requires touch | Indicates user must be touching the contacts on the Yubikey when verification code is accepted. | User choice |

      #. Click Save credential.

         The verification code displays in the Yubico Authenticator under
         the heading you gave Ops Manager as the Issuer.

      #. Once you receive the verification code, enter that code into the 
         into the Verify your code boxes. Each digit is
         entered in its own box.

         **Note:**

         You can copy the code from the Yubico Authenticator
         application. Click the name you gave as Issuer
         then select Copy to Clipboard from the
         Edit menu.

      Ops Manager automatically verifies the code and saves your settings.

### Two-Factor Authentication on a Shared Account

A global team that shares the same Ops Manager account can use Google
Authenticator and use the same seed code for all team members. To
generate a common seed code that all team members can use, select the
Can't scan the barcode? link when
Configuring Two-Factor Authentication with Google Authenticator.

## Generate New Recovery Codes

As a backup, you can generate recovery codes to use in place of a sent
code when you do not have access to a phone, 2FA (two-factor authentication) app or 2FA (two-factor authentication) device. Each recovery code is single-use, and you
should save these codes in a secure place. When you generate new
recovery codes, you invalidate previously generated ones.

**Step 1: Go to your Ops Manager Account Settings.**

In Ops Manager, click your username in the top-right corner
and select Account.

**Step 2: Edit your Two-Factor Authentication settings.**

Click pencil-alt to the right of
Two Factor Authentication.

When prompted for verification, enter a 2FA (two-factor authentication) code then click
Verify.

**Step 3: Click Show Recovery Codes.**

Each time you expand this box, Ops Manager generates a new set of codes.

Keep the codes in a safe place. Each code can be used in conjunction
with your username and password to not only access Ops Manager but to
reset your security settings on Ops Manager.

 

## Reset Legacy Two Factor Authentication

If you have legacy 2FA (two-factor authentication) enabled and you lose access to your 2FA (two-factor authentication) device,
you can reset 2FA (two-factor authentication) for your account. 

#. Log in to Ops Manager with your username and password.

#. When the 2FA (two-factor authentication) prompt displays:

   a. Click the Reset your two-factor authentication link.

   b. Click Ops Manager user? Click here at the
      bottom of the Reset Two Factor Authentication
      modal.

#. Type your Ops Manager username.

#. Click Reset Two Factor Authentication.

   Ops Manager emails a link to the e-mail account associated with the Ops Manager
   username.

#. Check your email.

#. Click the link that Ops Manager sent to start the 2FA (two-factor authentication) reset procedure.

#. Follow the directions on the 2FA (two-factor authentication) reset page. After completing the
   reset procedure, Ops Manager allows you to log in to the Ops Manager account
   without requiring a 2FA (two-factor authentication) code.
