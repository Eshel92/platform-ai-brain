<!-- Converted from tutorial/install-mongodb-community-with-docker.txt (reStructuredText). Includes are inlined. -->

# Install MongoDB Community with Docker

You can run MongoDB community Edition as a Docker container using the 
official MongoDB Community image. Using a Docker image for running your 
MongoDB deployment is useful to:

- Stand up a deployment quickly.
- Help manage configuration files.
- Test different features on multiple versions of MongoDB.

## About This Task

- This page describes the Docker install instructions for MongoDB Community 
  edition. The [MongoDB Enterprise Docker image](https://hub.docker.com/r/mongodb/mongodb-enterprise-server)  
  and [MongoDB Enterprise Kubernetes Operator](https://www.mongodb.com/docs/kubernetes-operator) 
  are recommended for production deployments and should be used together.
  For enterprise instructions, see docker-mongodb-enterprise-install.

- This procedure uses the official [MongoDB community image](https://hub.docker.com/r/mongodb/mongodb-community-server), which 
  is maintained by MongoDB.

- A full description of [Docker](https://docs.docker.com/) is beyond
  the scope of this documentation. This page assumes prior knowledge of
  Docker.

- MongoDB 5.0+ Docker images require [AVX](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) support 
  on your system. If your system does not support AVX, you can
  use a docker image of MongoDB prior to version 5.0. 

  **Warning:**

  Versions of MongoDB prior to 5.0 are EOL'd and 
  no longer supported by MongoDB. These versions should be used for 
  testing purposes only.

- .. include:: /includes/fact-fsync-caveat-docker

  To avoid a filesystem issue while running MongoDB in Docker, use the 
  official MongoDB community image above.

## Before You Begin

- Install [Docker](https://docs.docker.com/install/)

- Install [mongosh](https://www.mongodb.com/docs/mongodb-shell/install/)

## Procedure

**Step 1: Pull the MongoDB Docker Image**

```sh
docker pull mongodb/mongodb-community-server:latest
```

**Step 2: Run the Image as a Container**

```sh
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
```

The `-p 27017:27017` in this command maps the container port to the host port.
This allows you to connect to MongoDB with a `localhost:27017` connection string.

To install a specific version of MongoDB, specify the version
after the `:` in the Docker run command. Docker pulls and 
runs the specified version.

For example, to run MongoDB 5.0:

```sh
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:5.0-ubuntu2004
```

For a full list of available versions, see 
[Tags](https://hub.docker.com/r/mongodb/mongodb-community-server/tags).

**Note:** Add Command Line Options

You can use mongod command-line options 
by appending the command-line options to the docker run command.

For example, consider the `mongod --replSet` docker command-line option:

```bash
docker run -p 27017:27017 -d mongodb/mongodb-community-server:latest --name mongodb --replSet myReplicaSet
```

**Step 3: Check that the Container is Running**

To check the status of your Docker container, run the following 
command:

```sh
docker container ls
```

The output from the `ls` command lists the following fields that 
describe the running container:

- `Container ID`
- `Image`
- `Command`
- `Created`
- `Status`
- `Port`
- `Names` 

```sh
CONTAINER ID   IMAGE                                       COMMAND                  CREATED         STATUS         PORTS       NAMES
c29db5687290   mongodb/mongodb-community-server:5.0-ubi8   "docker-entrypoint.s…"   4 seconds ago   Up 3 seconds   27017/tcp   mongo
```

**Step 4: Connect to the MongoDB Deployment with `mongosh`**

```sh
mongosh --port 27017
```

**Step 5: Validate Your Deployment**

To confirm your MongoDB instance is running, run the `Hello` 
command:

```sh
db.runCommand(
   {
      hello: 1
   }
)
```

The result of this command returns a document describing your 
`mongod` deployment:

```javascript
{
   isWritablePrimary: true,
   topologyVersion: {
      processId: ObjectId("63c00e27195285e827d48908"),
      counter: Long("0")
},
   maxBsonObjectSize: 16777216,
   maxMessageSizeBytes: 48000000,
   maxWriteBatchSize: 100000,
   localTime: ISODate("2023-01-12T16:51:10.132Z"),
   logicalSessionTimeoutMinutes: 30,
   connectionId: 18,
   minWireVersion: 0,
   maxWireVersion: 20,
   readOnly: false,
   ok: 1
}
```

## Next Steps (Optional)

You can use [Cosign](https://github.com/sigstore/cosign) to verify
MongoDB's signature for container images. 

This procedure is optional. You do not need to verify MongoDB's
signature to run MongoDB on Docker or any other containerized platform.

To verify MongoDB's container signature, perform the following steps:

**Step 1: Download and install Cosign**

For installation instructions, see the [Cosign GitHub repository](https://github.com/sigstore/cosign).

**Step 2: Download the MongoDB Server container image's public key**

```sh
curl https://cosign.mongodb.com/server.pem > server.pem
```

**Step 3: Verify the signature**

Run the following command to verify the signature by tag: 

```sh
COSIGN_REPOSITORY=docker.io/mongodb/signatures cosign verify --private-infrastructure --key=./server.pem docker.io/mongodb/mongodb-community-server:latest
```
