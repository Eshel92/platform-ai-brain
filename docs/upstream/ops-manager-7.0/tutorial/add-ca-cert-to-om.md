<!-- Converted from tutorial/add-ca-cert-to-om.txt (reStructuredText). Includes are inlined. -->

# Add CA Certificate to Ops Manager Java Trust Store

In order to connect a webhook to Ops Manager with HTTPS, you'll need to import your 
CA certificate into the Ops Manager Java Trust Store. 

## Prerequisites

- Have an accessible Ops Manager deployment

## Add CA Cert to Ops Manager Java Truststore

**Step 1: Add the CA certificate of the webhook into the Ops Manager HTTP server.**

After adding the absolute path to your webhook trust store to the following command, 
run it to add your CA certificate to the Ops Manager Java trust store. 

```sh
sudo /opt/mongodb/mms/jdk/bin/keytool -noprompt -storepass changeit -import -trustcacerts -alias Webhook_CA -file <AbsolutePathofWebhookTrustStore> -keystore /opt/mongodb/mms/jdk/lib/security/cacerts
```

**Step 2: Confirm that the webhook CA certificate has been added.**

Run the following command to confirm that the CA certificate has been added successfully.

```sh
sudo /opt/mongodb/mms/jdk/bin/keytool -noprompt -storepass changeit -list -v -keystore /opt/mongodb/mms/jdk/lib/security/cacerts | grep -i Webhook_CA
```

**Step 3: Restart Ops Manager.**

Restart the Ops Manager server in order for the certificates to reload and the
change to take effect. 

```sh
sudo systemctl restart mongodb-mms
```

**Step 4: Test an HTTPS request to Ops Manager to confirm connectivity.**

a. Convert your Java keystore file into PEM format.

   Java keystores are stored in either JKS (Java KeyStore) or PKCS12 format. These formats
   are incompatible with the curl `--cacert` option.

   Use a tool of your choosing, such as `openssl`, to convert your Java keystore file.

#. Replace the placeholder text in the following command with the path to your PEM certificate
   and your webhook URL: 

   ```sh
   sudo curl -vvvv --cacert </path/to/cacerts.pem> <WebhookURL>
   ```

#. Run the command to test your webhook's HTTPS connectivity with Ops Manager.
