sonarqube-56f655c4b7-s6jww      0/1     Running   13 (33s ago)   22h
sonarqube-db-55696f4d5c-bfjtc   1/1     Running   6 (34s ago)    22h
@rifaterdemsahin ➜ /workspace
s/SonarQubeCourse (main) $ kubectl port-forward svc/sonarqube 9000:9000 -n sonarqube
Forwarding from 127.0.0.1:9000 -> 9000
Forwarding from [::1]:9000 -> 9000
Handling connection for 9000
E0601 15:29:16.095143  139006 portforward.go:424] "Unhandled Error" err=<
        an error occurred forwarding 9000 -> 9000: error forwarding port 9000 to pod c0df4519f35f16de5287c9fceb8468a0109db4510627d9fa4d10dd308dc137bf, uid : exit status 1: 2025/06/01 15:29:16 socat[4972] E connect(5, AF=2 127.0.0.1:9000, 16): Connection refused
 >
error: lost connection to pod
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl port-forward svc/sonarqube 9000:9000 -
n sonarqube
Forwarding from 127.0.0.1:9000 -> 9000
Forwarding from [::1]:9000 -> 9000
@rifaterdem
sahin ➜ /wo
rkspaces/So
narQubeCour
se (main) $narQubeC
                                            echo "===== Minikube Status =====" && minikube sta     tus
===== Minikube Status =====
minikube
type: Control Plane
host: Stopped
kubelet: Stopped
apiserver: Stopped
kubeconfig: Stopped

@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ minikube start --driver=docker --m
emory=9096 --cpus=4
😄  minikube v1.35.0 on Ubuntu 20.04 (docker/amd64)
✨  Using the docker driver based on existing profile
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
🔄  Restarting existing docker container for "minikube" ...
🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ echo "===== Kubernetes Nodes =====
" && kubectl get nodes -o wide
===== Kubernetes Nodes =====
NAME       STATUS   ROLES           AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME
minikube   Ready    control-plane   22h   v1.32.0   192.168.49.2   <none>        Ubuntu 22.04.5 LTS   6.8.0-1027-azure   docker://27.4.1
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ sleep 10 && echo "===== Kubernetes Components =====" && \
> kubectl get nodes -o wide && \
> echo "\n===== Namespaces =====" && \
> kubectl get namespaces && \
> echo "\n===== SonarQube Resources =====" && \
> kubectl get all -n sonarqube
===== Kubernetes Components =====
NAME       STATUS   ROLES           AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME
minikube   Ready    control-plane   22h   v1.32.0   192.168.49.2   <none>        Ubuntu 22.04.5 LTS   6.8.0-1027-azure   docker://27.4.1
\n===== Namespaces =====
NAME              STATUS   AGE
default           Active   22h
kube-node-lease   Active   22h
kube-public       Active   22h
kube-system       Active   22h
sonarqube         Active   22h
\n===== SonarQube Resources =====
NAME                                READY   STATUS             RESTARTS       AGE
pod/sonarqube-56f655c4b7-s6jww      0/1     CrashLoopBackOff   17 (13s ago)   22h
pod/sonarqube-db-55696f4d5c-bfjtc   0/1     Completed          10 (28s ago)   22h

NAME                   TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/sonarqube      NodePort    10.105.28.18   <none>        9000:30900/TCP   22h
service/sonarqube-db   ClusterIP   10.97.23.181   <none>        5432/TCP         22h

NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/sonarqube      0/1     1            0           22h
deployment.apps/sonarqube-db   0/1     1            0           22h

NAME                                      DESIRED   CURRENT   READY   AGE
replicaset.apps/sonarqube-56f655c4b7      1         1         0       22h
replicaset.apps/sonarqube-db-55696f4d5c   1         1         0       22h
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ minikube status && kubectl config current-context
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

minikube
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ minikube status && kubectl config current-context
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

minikube
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl rollout restart deployment sonarqube -n sonarqube
deployment.apps/sonarqube restarted
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get deployment sonarqube -n sonarqube
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
sonarqube   0/1     1            0           22h
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get deployment sonarqube -n sonarqube
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
sonarqube   0/1     1            0           22h
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get deployment sonarqube -n sonarqube
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
sonarqube   0/1     1            0           22h
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get deployment sonarqube -n sonarqube
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
sonarqube   0/1     1            0           22h
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get deployment sonarqube -n sonarqube
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
sonarqube   0/1     1            0           22h
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get deployment sonarqube -n sonarqube
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
sonarqube   0/1     1            0           22h
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl rollout restart deployment sonarqube -n sonarqube
deployment.apps/sonarqube restarted
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get deployment sonarqube -n sonarqube
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
sonarqube   0/1     1            0           22h
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl rollout status deployment sonarqube -n sonarqube
Waiting for deployment "sonarqube" rollout to finish: 1 old replicas are pending termination...
^C@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get pvc -n sonarqube
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
sonarqube-data   Bound    pvc-d8725237-0261-4bce-8b25-57b888e8c281   2Gi        RWO            standard       <unset>                 22h
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ echo "===== Pod Status =====" && \
> kubectl get pods -n sonarqube && \
> echo "\n===== Pod Events =====" && \
> kubectl get events -n sonarqube --sort-by='.metadata.creationTimestamp' | tail -n 10
===== Pod Status =====
NAME                            READY   STATUS             RESTARTS         AGE
sonarqube-54766cc499-2nmcs      0/1     Completed          5 (97s ago)      3m24s
sonarqube-848ff98d48-cmj56      0/1     CrashLoopBackOff   4 (85s ago)      2m55s
sonarqube-db-55696f4d5c-bfjtc   0/1     CrashLoopBackOff   14 (2m34s ago)   22h
\n===== Pod Events =====
2m56s       Normal    SuccessfulCreate        replicaset/sonarqube-848ff98d48        Created pod: sonarqube-848ff98d48-cmj56
2m56s       Normal    SuccessfulDelete        replicaset/sonarqube-56f655c4b7        Deleted pod: sonarqube-56f655c4b7-s6jww
2m56s       Normal    ScalingReplicaSet       deployment/sonarqube                   Scaled down replica set sonarqube-56f655c4b7 from 1 to 0
2m56s       Normal    ScalingReplicaSet       deployment/sonarqube                   Scaled up replica set sonarqube-848ff98d48 from 0 to 1
2m55s       Warning   FailedScheduling        pod/sonarqube-848ff98d48-cmj56         0/1 nodes are available: 1 Insufficient cpu. preemption: 0/1 nodes are available: 1 No preemption victims found for incoming pod.
2m53s       Normal    Scheduled               pod/sonarqube-848ff98d48-cmj56         Successfully assigned sonarqube/sonarqube-848ff98d48-cmj56 to minikube
87s         Normal    Pulled                  pod/sonarqube-848ff98d48-cmj56         Container image "sonarqube:9.9-community" already present on machine
87s         Normal    Created                 pod/sonarqube-848ff98d48-cmj56         Created container: sonarqube
87s         Normal    Started                 pod/sonarqube-848ff98d48-cmj56         Started container sonarqube
14s         Warning   BackOff                 pod/sonarqube-848ff98d48-cmj56         Back-off restarting failed container sonarqube in pod sonarqube-848ff98d48-cmj56_sonarqube(707f313d-1236-4bbb-b534-2c7b61246927)
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ minikube stop && minikube start --driver=docker --memory=9096 --cpus=4
✋  Stopping node "minikube"  ...
🛑  Powering off "minikube" via SSH ...
🛑  1 node stopped.
😄  minikube v1.35.0 on Ubuntu 20.04 (docker/amd64)
✨  Using the docker driver based on existing profile
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
🔄  Restarting existing docker container for "minikube" ...
🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: default-storageclass, storage-provisioner
^C
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl delete namespace sonarqube --ignore-not-found=true
namespace "sonarqube" deleted
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ sleep 5 && \
> kubectl create namespace sonarqube && \
> kubectl create secret generic sonar-db-credentials \
>   --namespace sonarqube \
>   --from-literal=POSTGRES_USER=sonar \
>   --from-literal=POSTGRES_PASSWORD=sonar123 \
>   --from-literal=POSTGRES_DB=sonar
namespace/sonarqube created
secret/sonar-db-credentials created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ cd /workspaces/SonarQubeCourse/Symbols && \
> kubectl apply -f pvc.yaml -n sonarqube
persistentvolumeclaim/sonarqube-data created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl cluster-info
Kubernetes control plane is running at https://192.168.49.2:8443
CoreDNS is running at https://192.168.49.2:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl apply -f deployment_postgresql.yaml -n sonarqube && \
> echo "Waiting for PostgreSQL to be ready..." && \
> kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s
deployment.apps/sonarqube-db created
service/sonarqube-db created
Waiting for PostgreSQL to be ready...
pod/sonarqube-db-55696f4d5c-ntb5m condition met
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl apply -f deployment_server.yaml -f service_sonarqube.yaml -n sonarqube && \
> echo "Waiting for SonarQube to be ready..." && \
> kubectl wait --for=condition=ready pod -l app=sonarqube -n sonarqube --timeout=300s
deployment.apps/sonarqube created
service/sonarqube created
Waiting for SonarQube to be ready...
^Cecho "===== Pods Status =====" && \
kubectl get pods -n sonarqube && \
echo "\n===== Services Status =====" && \
kubectl get svc -n sonarqube && \
ech@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ echo "===== Pods Status =====" && \
> kubectl get pods -n sonarqube && \
> echo "\n===== Services Status =====" && \
> kubectl get svc -n sonarqube && \
> echo "\n===== PVC Status =====" && \
> kubectl get pvc -n sonarqube
===== Pods Status =====
NAME                            READY   STATUS    RESTARTS     AGE
sonarqube-56f655c4b7-jmt2f      0/1     Running   1 (3s ago)   12s
sonarqube-db-55696f4d5c-ntb5m   1/1     Running   1 (3s ago)   52s
\n===== Services Status =====
NAME           TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
sonarqube      NodePort    10.99.13.250     <none>        9000:30900/TCP   12s
sonarqube-db   ClusterIP   10.102.143.239   <none>        5432/TCP         52s
\n===== PVC Status =====
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
sonarqube-data   Bound    pvc-f21240cf-0b27-4d80-aa38-0e127328daf1   2Gi        RWO            standard       <unset>                 71s
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ minikube delete && \
> minikube start --driver=docker --memory=9096 --cpus=4 --kubernetes-version=v1.27.3 && \
> minikube addons enable storage-provisioner
🔥  Deleting "minikube" in docker ...
🔥  Deleting container "minikube" ...
🔥  Removing /home/codespace/.minikube/machines/minikube ...
💀  Removed all traces of the "minikube" cluster.
😄  minikube v1.35.0 on Ubuntu 20.04 (docker/amd64)
✨  Using the docker driver based on user configuration
📌  Using Docker driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
💾  Downloading Kubernetes v1.27.3 preload ...