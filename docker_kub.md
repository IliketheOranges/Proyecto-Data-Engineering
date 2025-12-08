# Goals
1. Short Docker and Kubernetes introduction
2. Overview of the modern container ecosystem
3. Some understanting of the internals of containers, container platforms and container orchestration platforms

# The Problem
- We need reliable, scalable, distributed systems
- __Modern apps benefit from being:__
   - Cloud native
   - Modular
   - Microservice based <small>_(composed of multiple running modules)_</small>
   - Scalability <small>_(vertical & horizontal)_</small>
   - Reliability <small>_(fiable, que funcione)_</small>
   - Resilience  <small>_(si se baja, se sube)_</small>
- __However this brings a lot of complexity__
  - Its difficult for apps to run from lots of small pieces
  - Running multiple instances of the same thing _(microservices)_ even more complicated
- __... We need a solution that takes care of all these things__
  - Enter Container Platforms 
  - Enter Container Orchestration Platforms

# Containers
- __Definition:__ Processes with added isolation & resource management
  - Seems like completely separate system, really just a process using isolation techniques
  - Share the same kernel and HW
- __How does it magically seem like a VM?__
  - Thanks to standards and OS features
    - __Linux namespaces__
      - UTS: Hostname & Domain name 
      - MNT: Mounted filesystems
      - IPC - inter process communication
      - PID - processes
      - NET: Network devices
      - USER: File permissions
    - __Control groups__
      - Limit how much resources a container can use
- __Open Container Initiative__
  - [OCI](https://opencontainers.org/), [Github](https://github.com/opencontainers)
  - [Linux Foundation](https://www.linuxfoundation.org/) project started by [Docker](https://www.docker.com/), [CoreOS](https://fedoraproject.org/coreos/) and maintainers of [appc](https://github.com/appc/) in 2015 
  - Design open stardards for OS level virtualization (containers)

# Container Ecosystem Overview
- __Container Platforms__
  - What [Docker](https://www.docker.com/) and [DockerHub](https://hub.docker.com/) offer
- __Container Runtimes__
  - __High Level__
    - [Docker Engine](https://docs.docker.com/engine/) 
    - [Podman](https://podman.io/) <small>_open source, daemonless_</small>
  - __Mid Level__
    - [ContainerD](https://containerd.io/) <small>_daemon based, used by Docker and Kubernetes, developed by Docker and now a [CNFC](https://www.cncf.io/) project_</small>
    - [cri-o](https://cri-o.io/) <small>_open source, OCI compliant implementation of the kubernetes CRI (Container Runtime Interface)_</small>
  - __Low Level__
    - [runc](https://github.com/opencontainers/runc) <small>_single binary, more like a container runner/dispatcher, used internally by Docker & Podman_</small>
- __Container Orchestration Platforms__
  - __[Kubernetes / k8s](https://kubernetes.io/es/)__ <small>_the dominant standard, developed by Google, we run implementations that abstract away the details_</small>
    - [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/) <small>_official CLI tool provided by kubernetes_</small>
    - [K3S](https://k3s.io/) <small>_lightweight, single binary distribution_</small>
    - SUSE Rancher, RedHat Openshift ...<small>_open source, enterprise solutions, paid business model_</small>
    - __For single machine, local development__
      - [MiniKube](https://minikube.sigs.k8s.io/docs/) <small>_official kubernetes tool_</small>
      - [Kind](https://minikube.sigs.k8s.io/docs/) <small>Kubernetes in Docker</small> 
    - __Cloud Kubernetes__
      - [GKE - Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine?hl=en)
      - [EKS - Amazon Kubernetes Service](https://aws.amazon.com/eks/)
      - [AKS - Azure Kubernetes Service](https://azure.microsoft.com/en-us/products/kubernetes-service)
      - ... and more
  - __Non Kubernetes__
    - [Docker Swarm](https://docs.docker.com/engine/swarm/) <small>_simple orchestration tool provided by Docker Engine_</small>
    - [HashiCorp Nomad](https://developer.hashicorp.com/nomad) <small>_simple & flexible orchestrator_</small>
    - [Amazon ECS - Elastic Container Service](https://aws.amazon.com/es/ecs/)
- __Other__
  - [Buildah](https://buildah.io/) <small>_(container image builder, used internally by podman)_</small>

# Docker
- __Architecture:__
  - Docker Engine <small>_(Docker CLI + [dockerd](https://docs.docker.com/reference/cli/dockerd/))_</small>
  - Docker registry <small>_([DockerHub](https://hub.docker.com/), from which we pull images)_</small>
  - Running Containers <small>_managed by dockerd_</small>
- __Configuration:__
  - `Dockerfile` <small>_define docker images declaratively using commands</small>
  - `docker-compose.yml` <small>_define management of multiple interconnected containers_</small>
- __Commands:__
   - `docker pull` <small>_download a container image_</small>
   - `docker run` <small>_create and run a container from its image_</small>
   - `docker build` <small>_create an image from a Dockerfile_</small>
   - `docker tag` <small>_alias a local image to prepare it for sharing_</small>
   - `docker push` <small>_upload a tagged local image to a remote registry_</small>
   - `docker compose` <small>_manage a multi container application by reading a docker-compose.yml file_</small>
- __Dockerfile:__
  - __#__ <small>_comment_</small>
  - __FROM__ <small>_Specify the base image_</small>
  - __RUN__ <small>_Run a command inside the container_</small>
  - __COPY__ <small>_Copy files into the container_</small>
  - __ENV__ <small>Environment variable</small>
  - __ENTRYPOINT__ <small>_Configure the initial process for the container_</small>
  - __CMD__ <small>_Set default parameters for the initial process_</small>
- __What happens under the hood when you run a docker command?__
  1. You execute a `docker run` command
  2. Docker CLI sends the command to `dockerd` via REST API
  3. `dockerd` validates command, checks image is available locally and if not pulls it from a repo
  4. `containerd` sets up the container environment and executes `runc` to run the container
  5. `containerd` will then monitor and manage the container throughtout its lifecycle
<center>
    <img width='70%' src='https://miro.medium.com/v2/resize:fit:720/format:webp/0*kDJEckrqtk653KL_'> 
    <img width='70%' src='https://www.docker.com/app/uploads/2024/03/containerd-diagram-v1-1110x782.png'> 
</center>

# Kubernetes [UNFINISHED]
- [CRI](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/) Container Runtime Interface
- __Orchestration Requirements:__ (pag 32)
  - Clustering
  - Discorvery
  - Configuration
  - Access Control
  - Load Balancing 
  - Monitoring
  - Resilience
- __Cross Cutting Concerns__
  - __Dynamic Scheduling__ Allocations of containers to a server can change due to failure or configuration changes 
  - __Distributed State__ Cluster must know what containers are running and where, even during HW or network failures
  - __Multitenancy__ It must be possible to run multiple appllications in a single cluster
  - __HW Isolation__ Clusters must run anywhere and we don't care about the underlying HW (cloud, type of server ...)


# Terminology
- __[Daemon](https://grokipedia.com/page/Daemon_(computing)):__ Background process that is detatched from terminal runs persistently and provides an API or service. They often run as root, are run by `init` or `systemd` and live for the entire life of the OS.
- __[Shim process](https://en.wikipedia.org/wiki/Shim_(computing)):__ A process that acts like a wrapper calling some API or running another process.

# Sources
- [OCI Wikipedia](https://en.wikipedia.org/wiki/Open_Container_Initiative)
- [Docker blog](https://www.docker.com/blog/containerd-vs-docker/#:~:text=Docker%20builds%20on%20containerd%20to,%2C%20testing%2C%20verifying%2C%20and%20sharing)
- [The Book of Kubernetes]()
- [Kubernetes Up and Running](https://eddiejackson.net/azure/Kubernetes_book.pdf)
- [Implementing a container runtime shim](https://iximiuz.com/en/posts/implementing-container-runtime-shim-2/#:~:text=Streaming%20container's%20stdout%20and%20stderr,exit%20code%20of%20the%20container.)
- The rest of URLs in the document

# Examples
## Running a Container
```bash
                                            # Running commands in our system
cat /etc/os-release 
ps -ef
ip -br a                                    # see list of network devices
uname -a                                    # see system info
export hello=world                          # environment variable
echo $hello
                                            # Then in a container
docker run -ti -e hello=docker rockylinux:8 # -ti (interactive terminal) -e (env var)
yum install -y procps iproute               # install basic commands
                                            # then run the same commands in the container for comparison
```
## Filesystem Isolation
```bash
mkdir /tmp/newroot 
cp --parents /bin/bash /bin/ls /tmp/newroot         
cp --parents /lib64/ld-linux-x86-64.so.2 $(ldd /bin/bash /bin/ls | grep '=>' | awk '{print $3}') /tmp/newroot
chroot /tmp/newroot /bin/bash
```
## Containerd & Namespaces
```bash
ctr image pull docker.io/library/alpine:latest
ctr run -t --rm docker.io/library/alpine:latest v2

# in another terminal, while our container is still running
ctr tasks ls
ps -f <container-PID>
lsns | grep <container-PID>
```
- As we can see, there is only loopback address, there is no bridge interface giving us network access like with docker, as this is a low level container runtime
- A process running in a namespace sees a limited view of a particular system resource 
- We can see what namespaces something is using, using the `lsns` command
## Network Isolation
### Listing & Making Network Namespaces
```bash
ip netns list                                       # list network namespaces
ip netns add my_network_ns                          # create network namespace
ip netns exec my_network_ns ip a                    # see it
ip netns exec my_network_ns ip link set dev lo up   # turn the loopback address on
ip netns exec my_network_ns ping -c 1 localhost     # we can now ping it, but only from within itself
                                                    # but it cant talk to anything else on the system
```
### Creating veth pair for Network Namespace
1. We are going to create a virtual ethernet device (aka veth pair)
    1. creating veth device called myveth-peer 
    2. creating a veth device called myveth-host 
    3. placing myveth-peer in network namecape my_network_ns
```bash
ip link set myveth-peer netns my_network_ns
ip link add name myveth-host type veth peer name myveth-peer
```
2. Lets check
```bash
ip a # the last one shows myveth-host, connected device in my_network_ns
ip netns exec my_network_ns ip a # we can see myveth-peer
```
3. We need to bring both sides up
```bash
ip netns exec my_network_ns ip addr add 10.85.0.254/16 dev myveth-peer  # assign ip address to myveth-peer interface inside our namespace
ip netns exec my_network_ns ip link set dev myveth-peer up              # We turn the interface in our namespace up
ip link set dev myveth-host up                                          # turn the other interface myveth-host up
```
4. check it works
```bash
ip a 
ip netns exec my_network_ns ip a
ip netns exec my_network_ns ping -c 1 10.85.0.254                       # ping it from namespace

ping -c 1 10.85.0.254                                                   # expect this to not work
```
As you can see, the ping doesnt work. Because we have successfully created a network interface inside our network namespace, and we have the other end of the veth pair on our host network, but we haven’t connected up a corresponding network device on the host, so there’s no host network interface that can talk to the interface in the network namespace
## Docker
### Container Namespaces
```bash
docker ps
docker inspect -f '{{.State.Pid}}' [CONTAINER-ID]                   # get the PID
docker inspect -f '{{json .NetworkSettings}}' 16cb179425fc | jq .   # get the network part of the json
ps -f --pid PID                                                     # view the process
sudo lsns -p PID                                                    # view the namespaces used by that container
```
### Container Image Contents
```bash
docker run --name nginx -d nginx                # -d sends it to the background
docker exec -ti nginx /bin/bash                 # connect to the already running container
dd if=/dev/urandom of=/tmp/data bs=1M count=10  # write 10MB to /tmp/data
exit                                            # we exited but the container is still running
docker inspect -s nginx | jq '.[0].SizeRw'      # view the size of the image
```
### Image Versions & Layers
```bash
docker pull redis:6.0.13-alpine             
docker pull redis:6.2.3-alpine      # pull a different version
                                    # as we can see, both versions share some layers
docker images | grep redis          # shows the full size of each image
docker system df -v                 # in 'Images space usage:' we can see SIZE & SHARED SIZE

docker run -d --name redis1 redis:6.0.13-alpine
docker run -d --name redis2 redis:6.2.3-alpine

# we can see they each have their own version
docker logs redis1 | grep version
docker logs redis2 | grep version
```
### Building an Image
1. `Dockerfile`
```Dockerfile
FROM nginx
# Add index.html
RUN echo "<html><body><h1>Hello World!</h1></body></html>" > /usr/share/nginx/html/index.html
```
2. `docker build -t IMAGENAME:TAG .` or `docker build -f DOCKERFILE -t IMAGENAME:TAG .` 
    - TAG is optional
    - __careful__ `.` will copy everything in current directory 
## kubernetes [UNFINISHED]
