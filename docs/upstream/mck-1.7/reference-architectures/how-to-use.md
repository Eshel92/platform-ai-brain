<!-- Converted from reference-architectures/how-to-use.txt (reStructuredText). Includes are inlined. -->

# How to Use Reference Architectures

You can use reference architectures to quickly and efficiently build out your 
MongoDB Kubernetes Operator infrastructure. These resources are 
opinionated, and as such, they are not in any way exhaustive of the wide range 
of potential deployment implementations. Instead, they are meant to serve as a 
practical reference and starting point as you work through the process 
of deploying or upgrading your MongoDB resources running in Kubernetes. 

This documentation organizes reference architectures in distinct modules that 
you can combine and use as needed. Moreover, the reference architecture section 
includes all the information you need to stand up a tested, working deployment 
of each of the following implementations:

- Multi-Cluster Architecture

## How to Execute

Each section of the reference architecture contains complete and working code 
snippets. If you would like to clone the source code to your local machine 
rather than copying and pasting from the guides directly, you can find 
it in the [MongoDB Controllers for Kubernetes Operator repository](https://github.com/mongodb/mongodb-kubernetes). 

```bash
git clone https://github.com/mongodb/mongodb-kubernetes.git
cd mongodb-kubernetes
git checkout 1.7.0
cd public/architectures
```

Each module contains a `env_variables.sh` file listing the required environment 
variables. Before you can run any of the steps described within a given module, 
you must first set the required variables. To do so, navigate to the module, 
adjust env_variables.sh and run the following:

```bash
source env_variables.sh
```

To complete the procedures in most of the modules, you don't need check out the 
source code directly; you can simply copy and paste the provided code examples. 
However, in some cases (e.g. installing Istio Service Mesh), you need to navigate
into the source code directory, because the steps execute some more complicated 
scripts that are not available to copy and paste.

## Limitations

MongoDB Support doesn't provide assistance with third-party software. While each 
of the sections in the reference architecture is tested in each release of 
Kubernetes Operator, MongoDB support cannot extend to include assistance with tools 
that are not developed and released by MongoDB.
