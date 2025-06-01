# 🎯 SonarQube Re-Run Guide

## 🔄 Resuming SonarQube in Minikube (Codespaces Paused State)
## 📚 Prerequisites - Python Test Libraries

Before proceeding, ensure you have the necessary Python test libraries installed:

```bash
# Install required Python testing packages
pip install pytest pytest-cov
```

These packages are essential for running tests and generating coverage reports that SonarQube will analyze.


### 🚀 Step 1: Initialize Minikube
```bash
# Start Minikube with enhanced resources
minikube start --memory=9096 --cpus=4
```

### ⚙️ Step 2: Configure System Settings
```bash
# Adjust virtual memory settings
sudo sysctl -w vm.max_map_count=262144

# Set file descriptor limits
sudo sysctl -w fs.file-max=65536
```

kubectl rollout restart deployment sonarqube-db deployment/sonarqube -n sonarqube && \
kubectl rollout status deployment/sonarqube-db -n sonarqube && \
kubectl rollout status deployment/sonarqube -n sonarqube

### 🔗 Step 3: Enable Port Forwarding
```bash
# Forward SonarQube service port
kubectl port-forward svc/sonarqube 9000:9000 -n sonarqube
```

### 🌐 Access SonarQube
1. Click the port forwarding link in your environment
2. Navigate to the SonarQube web interface

### 🔑 Login Credentials ( first time login )
- Username: `admin`
- Password: `admin`

