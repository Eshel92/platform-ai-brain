<!-- Converted from core/csfle/reference/libmongocrypt.txt (reStructuredText). Includes are inlined. -->

# Install libmongocrypt

## Overview

Learn how to install `libmongocrypt`, a core component
of Client-Side Field Level Encryption.

**Warning:**

Do not build `libmongocrypt` from source. Use one of the installation
methods listed on this page.

## macOS Installation

```sh
brew install mongodb/brew/libmongocrypt
```

## Windows Installation

Click [here](https://github.com/mongodb/libmongocrypt/releases/latest) 
to see the latest `libmongocrypt` release. 

Use `gpg` to verify the signature. The public key for `libmongocrypt` 
is available [here](https://pgp.mongodb.com/).

## Linux Installation

### Debian

**Step 1: **

Import the public key used to sign the package repositories:

```sh
sudo sh -c 'curl -s --location https://pgp.mongodb.com/libmongocrypt.asc | gpg --dearmor >/etc/apt/trusted.gpg.d/libmongocrypt.gpg'
```

**Step 2: **

Add the MongoDB repository to your package sources:

**Important:**

Change `<release>` in the following shell command to your platform release (e.g. "xenial" or "buster").

```sh
echo "deb https://libmongocrypt.s3.amazonaws.com/apt/debian <release>/libmongocrypt/1.16 main" | sudo tee /etc/apt/sources.list.d/libmongocrypt.list
```

**Step 3: **

Update the package cache:

```sh
sudo apt-get update
```

**Step 4: **

Install `libmongocrypt`:

```sh
sudo apt-get install -y libmongocrypt-dev
```

### Ubuntu

**Step 1: **

Import the public key used to sign the package repositories:

```sh
sudo sh -c 'curl -s --location https://pgp.mongodb.com/libmongocrypt.asc | gpg --dearmor >/etc/apt/trusted.gpg.d/libmongocrypt.gpg'
```

**Step 2: **

Add the MongoDB repository to your package sources:

**Important:**

Change `<release>` in the following shell command to your platform release (e.g. "xenial" or "buster").

```sh
echo "deb https://libmongocrypt.s3.amazonaws.com/apt/ubuntu <release>/libmongocrypt/1.16 universe" | sudo tee /etc/apt/sources.list.d/libmongocrypt.list
```

**Step 3: **

Update the package cache:

```sh
sudo apt-get update
```

**Step 4: **

Install `libmongocrypt`:

```sh
sudo apt-get install -y libmongocrypt-dev
```

### RedHat

**Step 1: **

Create a repository file for the `libmongocrypt` package:

```sh
[libmongocrypt]
name=libmongocrypt repository
baseurl=https://libmongocrypt.s3.amazonaws.com/yum/redhat/$releasever/libmongocrypt/1.16/x86_64
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/libmongocrypt.asc
```

**Step 2: **

Install the `libmongocrypt` package:

```sh
sudo yum install -y libmongocrypt
```

### Amazon Linux 2

**Step 1: **

Create a repository file for the `libmongocrypt` package:

```sh
[libmongocrypt]
name=libmongocrypt repository
baseurl=https://libmongocrypt.s3.amazonaws.com/yum/amazon/2/libmongocrypt/1.16/x86_64
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/libmongocrypt.asc
```

**Step 2: **

Install the `libmongocrypt` package:

```sh
sudo yum install -y libmongocrypt
```

### Amazon Linux 2023

**Step 1: **

Create a `/etc/yum.repos.d/libmongocrypt.repo`
repository file:

```toml
[libmongocrypt]
name=libmongocrypt repository
baseurl=https://libmongocrypt.s3.amazonaws.com/yum/amazon/2023/libmongocrypt/1.16/x86_64
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/libmongocrypt.asc
```

**Step 2: **

Install the `libmongocrypt` package:

```sh
sudo yum install -y libmongocrypt
```

### Amazon Linux

**Step 1: **

Create a `/etc/yum.repos.d/libmongocrypt.repo`
repository file:

```toml
[libmongocrypt]
name=libmongocrypt repository
baseurl=https://libmongocrypt.s3.amazonaws.com/yum/amazon/2013.03/libmongocrypt/1.16/x86_64
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/libmongocrypt.asc
```

**Step 2: **

Install the `libmongocrypt` package:

```sh
sudo yum install -y libmongocrypt
```

### Suse

**Step 1: **

Import the public key used to sign the package repositories:

```sh
sudo rpm --import https://pgp.mongodb.com/libmongocrypt.asc
```

**Step 2: **

Add the repository to your package sources:

**Important:**

Change `<release>` in the following shell command to your platform release (e.g. "12" or "15").

```sh
sudo zypper addrepo --gpgcheck "https://libmongocrypt.s3.amazonaws.com/zypper/suse/<release>/libmongocrypt/1.16/x86_64" libmongocrypt
```

**Step 3: **

Install the `libmongocrypt` package:

```sh
sudo zypper -n install libmongocrypt
```
