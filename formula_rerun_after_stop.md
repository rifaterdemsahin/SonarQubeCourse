# 🎯 SonarQube Port Forwarding

## 📋 Prerequisites - Python Test Libraries

Before proceeding, ensure you have the Python test libraries installed:

```bash
# Install required Python testing packages
pip install pytest pytest-cov
```

These packages are essential for running tests and generating coverage reports that SonarQube will analyze.

## 🚀 Getting Started

To access SonarQube locally, follow these steps:

```bash
# Step 1: Start Minikube with sufficient resources
minikube start --memory=16096 --cpus=6 --addons=storage-provisioner


sudo sysctl -w vm.max_map_count=262144
sudo sysctl -w fs.file-max=65536

# Step 2: Clean up any existing resources
kubectl delete namespace sonarqube --ignore-not-found=true
sleep 10  # Wait for cleanup

# Step 3: Create namespace and secrets
kubectl create namespace sonarqube
kubectl create secret generic sonar-db-credentials \
  --namespace sonarqube \
  --from-literal=POSTGRES_USER=sonar \
  --from-literal=POSTGRES_PASSWORD=sonar123 \
  --from-literal=POSTGRES_DB=sonar

# Step 4: Apply Kubernetes configurations
cd /workspaces/SonarQubeCourse/Symbols

# Create PVC first
kubectl apply -f pvc.yaml -n sonarqube
sleep 5  # Wait for PVC to be created

# Deploy PostgreSQL and wait for it to be ready
kubectl apply -f deployment_postgresql.yaml -n sonarqube
echo "Waiting for PostgreSQL to be ready..."
kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s

# Deploy SonarQube and related services
kubectl apply -f deployment_server.yaml -f service_sonarqube.yaml -n sonarqube
echo "Waiting for SonarQube to be ready..."
kubectl wait --for=condition=ready pod -l app=sonarqube -n sonarqube --timeout=300s

# Apply GitHub integration (optional)
kubectl apply -f github-secrets.yaml -f github-integration.yaml -n sonarqube

# Set up port forwarding
kubectl port-forward svc/sonarqube 9000:9000 -n sonarqube
```

🌐 Access SonarQube in your web browser at:
- http://localhost:9000

Default credentials:
- Username: admin
- Password: admin

After first login, you will be prompted to change the password.

📝 Troubleshooting:
1. If pods are not starting, check logs:
   ```bash
   kubectl logs -l app=sonarqube -n sonarqube
   ```
2. If PostgreSQL is not ready:
   ```bash
   kubectl logs -l app=sonarqube-db -n sonarqube
   ```
3. Check pod status:
   ```bash
   kubectl get pods -n sonarqube
   ```

✨ Happy code analysis! ✨

### Example Output on the terminal 

@rifaterdemsahin ➜ /workspacesud@rifaterdemsahin ➜ /workspaces/S@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ scount=2
udo sysctl -w vm.max_map_count=262144 && sudo sysctl -w fs.file-max=65536
vm.max_map_count = 262144
fs.file-max = 65536
@rifaterdemsahin ➜ /workspaces/S
onarQubeCourse (main) $ kubectl 
delete namespace sonarqube --ignore-not-found=true && sleep 10 && kubectl create namespace sonarqube && kubectl create secret generic sonar-db-credentials --namespace sonarqube --from-literal=POSTGRES_USER=sonar --from-literal=POSTGRES_PASSWORD=sonar123 --from-literal=POSTGRES_DB=sonar
namespace/sonarqube created
secret/sonar-db-credentials created
@rifaterdemsahin ➜ /workspaces/S
onarQubeCourse (main) $ cd /work
spaces/SonarQubeCourse/Symbols && kubectl apply -f pvc.yaml -n sonarqube && sleep 5 && kubectl apply -f deployment_postgresql.yaml -n sonarqube && echo "Waiting for PostgreSQL to be ready..." && kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s
persistentvolumeclaim/sonarqube-data created
deployment.apps/sonarqube-db created
service/sonarqube-db created
Waiting for PostgreSQL to be ready...
E0601 17:40:42.734610   34821 reflector.go:166] "Unhandled Error" err="k8s.io/client-go/tools/watch/informerwatcher.go:146: Failed to watch *unstructured.Unstructured: Get \"https://192.168.49.2:8443/api/v1/namespaces/sonarqube/pods?allowWatchBookmarks=true&fieldSelector=metadata.name%3Dsonarqube-db-775db74f57-7t28v&resourceVersion=434&timeoutSeconds=444&watch=true\": dial tcp 192.168.49.2:8443: connect: no route to host"
W0601 17:40:48.429624   34821 reflector.go:569] k8s.io/client-go/tools/watch/informerwatcher.go:146: failed to list *unstructured.Unstructured: Get "https://192.168.49.2:8443/api/v1/namespaces/sonarqube/pods?fieldSelector=metadata.name%3Dsonarqube-db-775db74f57-7t28v&resourceVersion=434": dial tcp 192.168.49.2:8443: connect: no route to host
E0601 17:40:48.429698   34821 reflector.go:166] "Unhandled Error" err="k8s.io/client-go/tools/watch/informerwatcher.go:146: Failed to watch *unstructured.Unstructured: failed to list *unstructured.Unstructured: Get \"https://192.168.49.2:8443/api/v1/namespaces/sonarqube/pods?fieldSelector=metadata.name%3Dsonarqube-db-775db74f57-7t28v&resourceVersion=434\": dial tcp 192.168.49.2:8443: connect: no route to host"
W0601 17:40:57.581690   34821 reflector.go:569] k8s.io/client-go/tools/watch/informerwatcher.go:146: failed to list *unstructured.Unstructured: Get "https://192.168.49.2:8443/api/v1/namespaces/sonarqube/pods?fieldSelector=metadata.name%3Dsonarqube-db-775db74f57-7t28v&resourceVersion=434": dial tcp 192.168.49.2:8443: connect: no route to host
E0601 17:40:57.581756   34821 reflector.go:166] "Unhandled Error" err="k8s.io/client-go/tools/watch/informerwatcher.go:146: Failed to watch *unstructured.Unstructured: failed to list *unstructured.Unstructured: Get \"https://192.168.49.2:8443/api/v1/namespaces/sonarqube/pods?fieldSelector=metadata.name%3Dsonarqube-db-775db74f57-7t28v&resourceVersion=434\": dial tcp 192.168.49.2:8443: connect: no route to host"
W0601 17:41:07.501685   34821 reflector.go:569] k8s.io/client-go/tools/watch/informerwatcher.go:146: failed to list *unstructured.Unstructured: Get "https://192.168.49.2:8443/api/v1/namespaces/sonarqube/pods?fieldSelector=metadata.name%3Dsonarqube-db-775db74f57-7t28v&resourceVersion=434": dial tcp 192.168.49.2:8443: connect: no route to host
E0601 17:41:07.501742   34821 reflector.go:166] "Unhandled Error" err="k8s.io/client-go/tools/watch/informerwatcher.go:146: Failed to watch *unstructured.Unstructured: failed to list *unstructured.Unstructured: Get \"https://192.168.49.2:8443/api/v1/namespaces/sonarqube/pods?fieldSelector=metadata.name%3Dsonarqube-db-775db74f57-7t28v&resourceVersion=434\": dial tcp 192.168.49.2:8443: connect: no route to host"
W0601 17:41:25.485635   34821 reflector.go:569] k8s.io/client-go/tools/watch/informerwatcher.go:146: failed to list *unstructured.Unstructured: Get "https://192.168.49.2:8443/api/v1/namespaces/sonarqube/pods?fieldSelector=metadata.name%3Dsonarqube-db-775db74f57-7t28v&resourceVersion=434": dial tcp 192.168.49.2:8443: connect: no route to host
E0601 17:41:25.485703   34821 reflector.go:166] "Unhandled Error" err="k8s.io/client-go/tools/watch/informerwatcher.go:146: Failed to watch *unstructured.Unstructured: failed to list *unstructured.Unstructured: Get \"https://192.168.49.2:8443/api/v1/namespaces/sonarqube/pods?fieldSelector=metadata.name%3Dsonarqube-db-775db74f57-7t28v&resourceVersion=434\": dial tcp 192.168.49.2:8443: connect: no route to host"
^C@rifaterdemsahin ➜ /workspaces/S
onarQubeCourse/Symbols (main) $ 
                               kubectl delete namespace sonarqube --ignore-not-fo     und=true && sleep 10 && kubectl create namespace sonarqube && kubectl create secret generic sonar-db-credentials --namespace sonarqube --from-literal=POSTGRES_USER=sonar --from-literal=POSTGRES_PASSWORD=sonar123 --from-literal=POSTGRES_DB=sonar
Unable to connect to the server: dial tcp 192.168.49.2:8443: connect: no route to host
@rifaterdemsahin ➜ /workspaces/S
onarQubeCourse/Symbols (main) $ 
                               s
minikube
type: Control Plane
host: Stopped
kubelet: Stopped
apiserver: Stopped
kubeconfig: Stopped

@rifaterdemsahin ➜ /workspaces/S
onarQubeCourse/Symbols (main) $ 
                               minikube start --memory=16096 --cpus=6
😄  minikube v1.35.0 on Ubuntu 20.04 (docker/amd64)
✨  Using the docker driver based on existing profile
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
🔄  Restarting existing docker container for "minikube" ...
🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: default-storageclass, storage-provisioner
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
@rifaterdemsahin ➜ /workspaces/S
onarQubeCourse/Symbols (main) $ 
                               minikube start --memory=16096 --cpus=6 --addons=st     orage-provisioner
😄  minikube v1.35.0 on Ubuntu 20.04 (docker/amd64)
✨  Using the docker driver based on existing profile
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
🏃  Updating the running docker "minikube" container ...
🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ sudo sysctl -w vm.max_map_count=262144 && sudo sysctl -w fs.file-max=65536
vm.max_map_count = 262144
fs.file-max = 65536
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl delete namespace sonarqube --ignore-not-found=true && sleep 10 && kubectl create namespace sonarqube
namespace "sonarqube" deleted
namespace/sonarqube created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl create secret generic sonar-db-credentials \
>   --namespace sonarqube \
>   --from-literal=POSTGRES_USER=sonar \
>   --from-literal=POSTGRES_PASSWORD=sonar123 \
>   --from-literal=POSTGRES_DB=sonar
secret/sonar-db-credentials created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ cd /workspaces/SonarQubeCourse/Symbols && kubectl apply -f pvc.yaml -n sonarqube && sleep 5
persistentvolumeclaim/sonarqube-data created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl apply -f deployment_postgresql.yaml -n sonarqube && echo "Waiting for PostgreSQL to be ready..." && kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s
deployment.apps/sonarqube-db created
service/sonarqube-db created
Waiting for PostgreSQL to be ready...
pod/sonarqube-db-775db74f57-gndnc condition met
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl apply -f deployment_server.yaml -f service_sonarqube.yaml -n sonarqube && echo "Waiting for SonarQube to be ready..." && kubectl wait --for=condition=ready pod -l app=sonarqube -n sonarqube --timeout=300s
deployment.apps/sonarqube created
service/sonarqube created
Waiting for SonarQube to be ready...
pod/sonarqube-78f96c6bf9-6bdxd condition met
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl apply -f github-secrets.yaml -f github-integration.yaml -n sonarqube
secret/github-secrets created
secret/github-integration created
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ 