---
applies_to:
  stack:
navigation_title: "GPU vector indexing"
---

# GPU accelerated vector indexing
```{applies_to}
stack: preview 9.3, ga 9.4
```

Elasticsearch can use GPU acceleration to significantly speed up the indexing of
dense vectors. GPU indexing is based on the
[Nvidia cuVS library](https://developer.nvidia.com/cuvs) and leverages the
parallel processing capabilities of graphics processing units to accelerate
the construction of HNSW vector search indexes. GPU accelerated vector
indexing is particularly beneficial for large-scale vector datasets and
high-throughput indexing scenarios, freeing up CPU resources for other tasks.

## Requirements

GPU vector indexing requires the following:

* An [Enterprise subscription](https://www.elastic.co/subscriptions)
* A supported NVIDIA GPU (Ampere architecture or better, compute capability
  >= 8.0) with a minimum 8GB of GPU memory
* GPU driver, CUDA and
  [cuVS runtime libraries](https://docs.rapids.ai/api/cuvs/stable/build/)
  installed on the node. Refer to the
  [Elastic support matrix](https://www.elastic.co/support/matrix) for
  supported CUDA and cuVS versions.
* `LD_LIBRARY_PATH` environment variable configured to include the cuVS
  libraries path and its dependencies (CUDA, rmm, etc.)
* Supported platform: Linux x86_64 only, Java 22 or higher
* Supported dense vector configurations: `hnsw` and `int8_hnsw`; `float`
  element type only


## Configuration

GPU vector indexing is controlled by the
[`vectors.indexing.use_gpu`](/reference/elasticsearch/configuration-reference/node-settings.md#gpu-vector-indexing-settings)
node-level setting.

## Elasticsearch Docker image with GPU support

An example Dockerfile is provided that extends the official Elasticsearch Docker image
to add the dependencies required for GPU support.

::::{warning}
This Dockerfile serves as an example implementation, and is not fully supported
like our official Docker images.
::::

::::{dropdown} Example Dockerfile
```plaintext
FROM docker.elastic.co/elasticsearch/elasticsearch:9.3.0

USER root

# See https://gitlab.com/nvidia/container-images/cuda/-/blob/master/dist/12.9.1/ubi9/base/Dockerfile?ref_type=heads
# and https://gitlab.com/nvidia/container-images/cuda/-/blob/master/dist/12.9.1/ubi9/devel/Dockerfile?ref_type=heads
# We are installing nvidia/cuda drivers/libraries the same way that nvidia does in their images

ENV CUVS_VERSION=25.12.0

ENV NVARCH=x86_64
ENV NVIDIA_REQUIRE_CUDA="cuda>=12.9 brand=unknown,driver>=535,driver<536 brand=grid,driver>=535,driver<536 brand=tesla,driver>=535,driver<536 brand=nvidia,driver>=535,driver<536 brand=quadro,driver>=535,driver<536 brand=quadrortx,driver>=535,driver<536 brand=nvidiartx,driver>=535,driver<536 brand=vapps,driver>=535,driver<536 brand=vpc,driver>=535,driver<536 brand=vcs,driver>=535,driver<536 brand=vws,driver>=535,driver<536 brand=cloudgaming,driver>=535,driver<536 brand=unknown,driver>=550,driver<551 brand=grid,driver>=550,driver<551 brand=tesla,driver>=550,driver<551 brand=nvidia,driver>=550,driver<551 brand=quadro,driver>=550,driver<551 brand=quadrortx,driver>=550,driver<551 brand=nvidiartx,driver>=550,driver<551 brand=vapps,driver>=550,driver<551 brand=vpc,driver>=550,driver<551 brand=vcs,driver>=550,driver<551 brand=vws,driver>=550,driver<551 brand=cloudgaming,driver>=550,driver<551 brand=unknown,driver>=560,driver<561 brand=grid,driver>=560,driver<561 brand=tesla,driver>=560,driver<561 brand=nvidia,driver>=560,driver<561 brand=quadro,driver>=560,driver<561 brand=quadrortx,driver>=560,driver<561 brand=nvidiartx,driver>=560,driver<561 brand=vapps,driver>=560,driver<561 brand=vpc,driver>=560,driver<561 brand=vcs,driver>=560,driver<561 brand=vws,driver>=560,driver<561 brand=cloudgaming,driver>=560,driver<561 brand=unknown,driver>=565,driver<566 brand=grid,driver>=565,driver<566 brand=tesla,driver>=565,driver<566 brand=nvidia,driver>=565,driver<566 brand=quadro,driver>=565,driver<566 brand=quadrortx,driver>=565,driver<566 brand=nvidiartx,driver>=565,driver<566 brand=vapps,driver>=565,driver<566 brand=vpc,driver>=565,driver<566 brand=vcs,driver>=565,driver<566 brand=vws,driver>=565,driver<566 brand=cloudgaming,driver>=565,driver<566 brand=unknown,driver>=570,driver<571 brand=grid,driver>=570,driver<571 brand=tesla,driver>=570,driver<571 brand=nvidia,driver>=570,driver<571 brand=quadro,driver>=570,driver<571 brand=quadrortx,driver>=570,driver<571 brand=nvidiartx,driver>=570,driver<571 brand=vapps,driver>=570,driver<571 brand=vpc,driver>=570,driver<571 brand=vcs,driver>=570,driver<571 brand=vws,driver>=570,driver<571 brand=cloudgaming,driver>=570,driver<571"
ENV NV_CUDA_CUDART_VERSION=12.9.79-1
ENV CUDA_VERSION=12.9.1

ENV NV_CUDA_LIB_VERSION=12.9.1-1
ENV NV_NVPROF_VERSION=12.9.79-1
ENV NV_NVPROF_DEV_PACKAGE=cuda-nvprof-12-9-${NV_NVPROF_VERSION}
ENV NV_CUDA_CUDART_DEV_VERSION=12.9.79-1
ENV NV_NVML_DEV_VERSION=12.9.79-1
ENV NV_LIBCUBLAS_DEV_VERSION=12.9.1.4-1
ENV NV_LIBNPP_DEV_VERSION=12.4.1.87-1
ENV NV_LIBNPP_DEV_PACKAGE=libnpp-devel-12-9-${NV_LIBNPP_DEV_VERSION}
ENV NV_LIBNCCL_DEV_PACKAGE_NAME=libnccl-devel
ENV NV_LIBNCCL_DEV_PACKAGE_VERSION=2.27.3-1
ENV NCCL_VERSION=2.27.3
ENV NV_LIBNCCL_DEV_PACKAGE=${NV_LIBNCCL_DEV_PACKAGE_NAME}-${NV_LIBNCCL_DEV_PACKAGE_VERSION}+cuda12.9
ENV NV_CUDA_NSIGHT_COMPUTE_VERSION=12.9.1-1
ENV NV_CUDA_NSIGHT_COMPUTE_DEV_PACKAGE=cuda-nsight-compute-12-9-${NV_CUDA_NSIGHT_COMPUTE_VERSION}

ENV NV_NVTX_VERSION=12.9.79-1
ENV NV_LIBNPP_VERSION=12.4.1.87-1
ENV NV_LIBNPP_PACKAGE=libnpp-12-9-${NV_LIBNPP_VERSION}
ENV NV_LIBCUBLAS_VERSION=12.9.1.4-1
ENV NV_LIBNCCL_PACKAGE_NAME=libnccl
ENV NV_LIBNCCL_PACKAGE_VERSION=2.27.3-1
ENV NV_LIBNCCL_VERSION=2.27.3
ENV NCCL_VERSION=2.27.3
ENV NV_LIBNCCL_PACKAGE=${NV_LIBNCCL_PACKAGE_NAME}-${NV_LIBNCCL_PACKAGE_VERSION}+cuda12.9

ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility
ENV RAFT_DEBUG_LOG_FILE=/dev/null

# Install nvidia drivers
RUN microdnf install -y dnf
RUN dnf install -y 'dnf-command(config-manager)'
RUN dnf config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel9/x86_64/cuda-rhel9.repo

RUN dnf upgrade -y && dnf install -y \
    cuda-cudart-12-9-${NV_CUDA_CUDART_VERSION} \
    cuda-compat-12-9 \
    && dnf clean all \
    && rm -rf /var/cache/yum/*

# Set up env vars for various libraries (cuda, libcuvs)
RUN echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf.d/nvidia.conf
ENV PATH=/usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}
ENV LIBCUVS_DIR="/opt/cuvs"
ENV LD_LIBRARY_PATH=${LIBCUVS_DIR}:/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/cuda/lib64

# Install other required nvidia and cuda libraries, as well as tar and gzip
RUN dnf install -y \
    cuda-libraries-12-9-${NV_CUDA_LIB_VERSION} \
    cuda-nvtx-12-9-${NV_NVTX_VERSION} \
    ${NV_LIBNPP_PACKAGE} \
    libcublas-12-9-${NV_LIBCUBLAS_VERSION} \
    ${NV_LIBNCCL_PACKAGE} \
    tar gzip \
    && dnf clean all \
    && rm -rf /var/cache/yum/*

# Grab the libcuvs library from Elastic's gcs archive
# These are tarballs that contain only the libraries necessary from nvidia's libcuvs builds in conda
# Note: this is temporary until nvidia begins publishing minimal libcuvs tarballs along with their releases
RUN mkdir -p "$LIBCUVS_DIR" && \
    chmod 775 "$LIBCUVS_DIR" && \
    cd "$LIBCUVS_DIR" && \
    CUVS_ARCHIVE="libcuvs-$CUVS_VERSION.tar.gz" && \
    curl -fO "https://storage.googleapis.com/elasticsearch-cuvs-snapshots/libcuvs/$CUVS_ARCHIVE" && \
    tar -xzf "$CUVS_ARCHIVE" && \
    rm -f "$CUVS_ARCHIVE" && \
    if [[ -d "$CUVS_VERSION" ]]; then mv "$CUVS_VERSION/*" ./; fi

# Reset the user back to elasticsearch
USER 1000:0
```

::::

### Requirements

The host machine running the Docker container needs
[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
installed and configured.

### Build it

```sh
docker build -t es-gpu .
```

### Run it

```sh
docker run \
  -p 9200:9200 \
  -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  -e "vectors.indexing.use_gpu=true" \
  --user elasticsearch \
  --gpus all \
  --rm -it es-gpu
```

## Monitoring
```{applies_to}
stack: ga 9.3.2
```

Use the `GET _xpack/usage` API to monitor GPU vector indexing status and usage
across all nodes in the cluster:

```console
GET _xpack/usage?filter_path=gpu_vector_indexing
```
% TEST[skip:Requires GPU hardware]

```console-result
{
  "gpu_vector_indexing": {
    "available": true, <1>
    "enabled": true, <2>
    "index_build_count": 30, <3>
    "nodes_with_gpu": 3, <4>
    "nodes": [ <5>
      { "type": "NVIDIA L4", "memory_in_bytes": 24000000000,
        "enabled": true, "index_build_count": 10 },
      { "type": "NVIDIA L4", "memory_in_bytes": 24000000000,
        "enabled": true, "index_build_count": 10 },
      { "type": "NVIDIA A100", "memory_in_bytes": 80000000000,
        "enabled": true, "index_build_count": 10 }
    ]
  }
}
```
1. Whether the current license permits GPU indexing.
2. Whether at least one node has GPU hardware configured and has not disabled it via `vectors.indexing.use_gpu=false`.
3. Total number of GPU index builds across the cluster.
4. Number of data nodes with GPU support.
5. Per-node GPU details including type, memory, enabled status, and build count.

## Troubleshooting
By default, Elasticsearch uses GPU indexing for supported vector types if a
compatible GPU and required libraries are detected.
Check server logs for messages indicating whether Elasticsearch has detected a GPU.

If you see a message like the following, a GPU was successfully detected and
GPU indexing will be used:
```
[o.e.x.g.GPUSupport ] [elasticsearch-0] Found compatible GPU [NVIDIA L4] (id: [0])
```
If you don't see this message, look for warning messages explaining why GPU
indexing is not being used, such as an unsupported environment, missing
libraries, or an incompatible GPU.


### Node fails to start with `vectors.indexing.use_gpu: true`

To enforce GPU indexing, set `vectors.indexing.use_gpu: true` in
`elasticsearch.yml`.
The node will fail to start if GPU indexing is not available, e.g. if a GPU
is not detected by Elasticsearch, or if the runtime is not supported, or if the
necessary dependencies are not correctly configured, etc.

If the node fails to start, check:
* A supported NVIDIA GPU is present
* CUDA runtime libraries and drivers are installed (check with `nvidia-smi`)
* `LD_LIBRARY_PATH` includes paths to the cuVS libraries and to their
  dependencies (e.g. CUDA)
* Supported platform: Linux x86_64 with Java 22 or higher


### Performance not improved with GPU indexing

If you are sure that GPU indexing is enabled but don't see performance
improvement, check the following:

* Ensure supported vector index types and element type are used
* Ensure the dataset is large enough to benefit from GPU acceleration
* Check if there are different bottlenecks affecting the indexing process:
  using GPU indexing accelerates the HNSW graph building, but speedups can be
  limited by other factors.
   * Indexing throughput depends on how fast you can get data into Elasticsearch.
     Check network speed and client performance. Use multiple clients if
     needed.
   * JSON parsing could dominate the computation: use base64 encoded vectors
     as opposed to json arrays
   * Storage speed is also important: as the GPU is able to process lots of
     data, you need a storage solution that is able to keep up. Avoid using
     network attached storage, and prefer fast NVMe to extract the most
     performance
* Consider monitoring CPU usage to demonstrate offloading to GPU
* Consider monitoring GPU usage (e.g. with `nvidia-smi`)
