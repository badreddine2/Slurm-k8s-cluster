# Slurm kubernetes Cluster

Before starting the installation of the k8s-slurm cluster you must install the following :

* Install minikube : https://minikube.sigs.k8s.io/docs/start/
* Install the kubectl tool : https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
* Install munge&slurm locally : https://slurm.schedmd.com/quickstart_admin.html#quick_start


## Containers and Pods

Inside k8s-pods repo you will find different yaml file, each yaml file is a pod configuration.

*  slurm-mysql :
    * This pod contains two containers (Slurmdbd and Mysql)
*  slurmctld-pod :
    * this pod contains only slurmctld container and service NodePort to communicate with slurmd which is outside of the pod
* slurmdbd-pod :
    * Contains only slurmdbd container


## Building the Docker Image

Attention : if you build a new image, make sure to replace your new image in the pod configuration ", for example image: badreddine970/slurmdbd:latest ---> image: your_new_image

Build the image locally:

```console
docker build -t <image_name>:21.08.6 .
```

Build a different version of Slurm using Docker build args and the Slurm Git
tag:

```console
docker build --build-arg SLURM_TAG="slurm-19-05-2-1" -t <image_name>:19.05.2 .
```
Or just change the version in Dockerfile, here "ARG SLURM_TAG=slurm-21-08-6-1"

## Starting the Cluster
Run minikube start to have a fully operational local Kubernetes cluster running on your machine and be ready for development and testing purposes
```console
minikube start
```

Once the minikube start is finished you can execute the pods using kubectl tool:

1- Execute slurm-mysql first:
```console
kubectl apply -f slurm-mysql.yaml
```
2-  Execute slurmctld-pod ans the NodePort service

```console
kubetcl apply -f slurmctld-pod.yaml
```
* then execute the bash script to put NordPort IP in your slurm.conf 
```console
sh script.sh
```

## K8s information

* To have an overview on your k8s slurm cluster, execute 
```console
kubectl get all 
```
* to get pod/container logs
```console
kubectl logs <pod_name>
kubectl logs <pod_name> -c <container_name>
kubectl describe pod <pod_name>
```
## Accessing the Cluster

* To acces to a pod or containers which are running inside the pod :
```console
# to access to a pod
kubectl exec -it <pod_name> -- /bin/bash 
``` 
```console
# to access to a container inside the pod     
kubectl exec -it <pod_name> -c <container_name> -- /bin/bash
```


## Deleting the Cluster

## Updating the Cluster


kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/namespace.yaml

kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.12.1/manifests/metallb.yaml