# 🛠️ SonarQube Recovery Guide: Post-Minikube Corruption

This guide provides steps to restore SonarQube after Minikube corruption.

## 📋 Prerequisites

- Docker installed and running
- Minikube
- kubectl
- 9GB RAM available
- 4 CPU cores

## 🔄 Recovery Steps

### 1. Reset Minikube

```bash
minikube delete --all
minikube start --driver=docker --memory=9096 --cpus=4 --kubernetes-version=v1.27.3
minikube addons enable storage-provisioner
```

### 2. System Configuration (Linux)

```bash
sudo sysctl -w vm.max_map_count=262144
sudo sysctl -w fs.file-max=65536
```

### 3. Setup Environment

```bash
# Create namespace
kubectl create namespace sonarqube

# Create database secrets
kubectl create secret generic sonar-db-credentials \
   --namespace sonarqube \
   --from-literal=POSTGRES_USER=sonar \
   --from-literal=POSTGRES_PASSWORD=sonar123 \
   --from-literal=POSTGRES_DB=sonar
```

### 4. Deploy Components

```bash
cd /workspaces/SonarQubeCourse/Symbols

# Apply configurations
kubectl apply -f pvc.yaml -n sonarqube
kubectl apply -f deployment_postgresql.yaml -n sonarqube
kubectl apply -f deployment_server.yaml -f service_sonarqube.yaml -n sonarqube

# Wait for deployments
kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s
kubectl wait --for=condition=ready pod -l app=sonarqube -n sonarqube --timeout=300s
```

### 5. Access SonarQube

```bash
kubectl port-forward svc/sonarqube 9000:9000 -n sonarqube
```

Visit: http://localhost:9000
- Username: `admin`
- Password: `admin`

### 6. Troubleshooting

```bash
kubectl get pods -n sonarqube
kubectl logs -l app=sonarqube -n sonarqube
kubectl logs -l app=sonarqube-db -n sonarqube
```

## 🔍 Health Check

```bash
kubectl get deployment sonarqube -n sonarqube
kubectl rollout status deployment sonarqube -n sonarqube
```

✨ SonarQube should now be operational! ✨
> add the configuration : obsidian://open?vault=secondbrain&file=secondbrain%2F4%20_Archieve%2Fresetup%20appid%20and%20config%20for%20sonarqube%20project%201%206%202025