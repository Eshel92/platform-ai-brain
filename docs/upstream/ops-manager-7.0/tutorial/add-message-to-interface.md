<!-- Converted from tutorial/add-message-to-interface.txt (reStructuredText). Includes are inlined. -->

# Add a Message to the Interface

## Overview

You can display a message on any page of the Ops Manager interface to notify
users of information or events, such as impending maintenance windows.

## Procedures

### Add a Message

#. Click the Admin link in the upper right corner of the
   Ops Manager interface.

#. Click the General tab and then click Messages.

#. Click the Add Message button.

#. Enter the message and the page or page prefix. The page prefix allows
   you to specify a path of a single page or the URL prefix of a group of
   pages. The prefix must begin with a `/` character.

   For example, entering the page prefix `/settings/profile` will
   display a message on the default Settings page and
   Account page but not on any other page in the
   application.

#. Click the Active checkbox to make the message live.
   Optionally, you can leave the box unchecked to disable the message.

#. Click Add.

Once added, active messages take 60 seconds before they display.

### Disable a Message

#. Click the Admin link in the upper right corner of the
   Ops Manager interface.

#. Click the General tab and then click Messages.

#. Click the orange square button to the right of the alert.

To re-enable a disabled message, click the grey button.

### Delete a Message

#. Click the Admin link in the upper right corner of the
   Ops Manager interface.

#. Click the General tab and then click Messages.

#. Click the garbage can icon to the right of the alert.
