@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ minikube delete && minikube start --driver=docker --memory=9096 --cpus=4 --kubernetes-version=v1.27.3 && minikube addons enable storage-provisioner
🔥  Deleting "minikube" in docker ...
🔥  Deleting container "minikube" ...
🔥  Removing /home/codespace/.minikube/machines/minikube ...
💀  Removed all traces of the "minikube" cluster.
😄  minikube v1.35.0 on Ubuntu 20.04 (docker/amd64)
✨  Using the docker driver based on user configuration
📌  Using Docker driver with root privileges
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
🔥  Creating docker container (CPUs=4, Memory=9096MB) ...
🐳  Preparing Kubernetes v1.27.3 on Docker 27.4.1 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass

❗  /usr/local/bin/kubectl is version 1.32.3, which may have incompatibilities with Kubernetes 1.27.3.
    ▪ Want kubectl v1.27.3? Try 'minikube kubectl -- get pods -A'
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
💡  storage-provisioner is an addon maintained by minikube. For any concerns contact minikube on GitHub.
You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  The 'storage-provisioner' addon is enabled
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ sudo sysctl -w vm.max_map_count=262144
 -w fs.file-max=65536vm.max_map_count = 262144
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ sudo sysctl -w fs.file-max=65536
fs.file-max = 65536
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ 
mbols (main) $ sudo sysctl -w fs.file-max=65536@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ @rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ sudo sysctl -w fs.file-max=65536
bash: syntax error near unexpected token `('
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl create namespace sonarqube
namespace/sonarqube created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl create secret generic sonar-db-credentials \
>    --namespace sonarqube \
>    --from-literal=POSTGRES_USER=sonar \
>    --from-literal=POSTGRES_PASSWORD=sonar123 \
>    --from-literal=POSTGRES_DB=sonar
secret/sonar-db-credentials created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ cd /workspaces/SonarQubeCourse/Symbols
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl apply -f pvc.yaml -n sonarqube
ly -f deployment_postgresql.yaml -n sonarqube
kubectl apply -f deployment_server.yaml -f service_sonarqube.yaml -n sonarqube
persistentvolumeclaim/sonarqube-data created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl apply -f deployment_postgresql.yaml -n sonarqube
deployment.apps/sonarqube-db created
service/sonarqube-db created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl apply -f deployment_server.yaml -f service_sonarqube.yaml -n sonarqube
deployment.apps/sonarqube created
service/sonarqube created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s
--for=condition=ready pod -l app=sonarqube -n sonarqube --timeout=300s
pod/sonarqube-db-778f999cd5-k6fn6 condition met
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl wait --for=condition=ready pod -l app=sonarqube -n sonarqube --timeout=300s

pod/sonarqube-55b9ff9c79-nkrxh condition met
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ 
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl port-forward svc/sonarqube 9000:9000 -n sonarqube
Forwarding from 127.0.0.1:9000 -> 9000
Forwarding from [::1]:9000 -> 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000
Handling connection for 9000