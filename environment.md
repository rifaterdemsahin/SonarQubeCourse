# 🎯 SonarQube Installation Guide

This guide provides step-by-step instructions for installing and configuring SonarQube using Kubernetes (Minikube). 🚀

## 📋 Prerequisites

Before starting the installation, ensure you have the following tools installed:

- 🔄 Minikube
- ⚓ kubectl
- 🐧 A Linux/Unix-based system
- 💾 At least 4GB of RAM available
- 🐳 Docker (optional, but recommended)

## 💻 System Requirements

### 🔧 Memory Settings

SonarQube requires specific memory settings to function properly. Run these commands before starting:

```bash
sudo sysctl -w vm.max_map_count=262144
sudo sysctl -w fs.file-max=65536
```

📝 To make these changes permanent, add them to `/etc/sysctl.conf`.

## 🛠️ Installation Steps

1. **🚀 Start Minikube**
   ```bash
   minikube start --memory=9096 --cpus=4
   ```

2. **📦 Apply SonarQube Kubernetes Configuration**
   ```bash
kubectl create namespace sonarqube
kubectl apply -f Symbols/deployment_postgresql.yaml && kubectl apply -f Symbols/deployment_server.yaml && kubectl apply -f Symbols/pvc.yaml && kubectl apply -f Symbols/service_sonarqube.yaml
   ```

🔐 Create database credentials:
```bash
kubectl create secret generic sonar-db-credentials -n sonarqube \
  --from-literal=POSTGRES_USER=sonar \
  --from-literal=POSTGRES_PASSWORD=sonarpass
```

3. **✅ Verify Installation**
   ```bash
   kubectl get pods
   kubectl get services
   ```

## 🌐 Accessing SonarQube

1. 🔗 Get the SonarQube URL:
   ```bash
   kubectl port-forward svc/sonarqube-service 9000:9000
   ```

2. 🌍 Open the URL in your browser

3. 🔑 Default credentials:
   - Username: admin
   - Password: admin

## ⚙️ Post-Installation Steps

1. 🔒 Change the default admin password
2. 📊 Configure your first project
3. 🎯 Set up quality gates
4. 🔌 Install relevant plugins

## 🔍 Troubleshooting

Common issues and their solutions:

1. **🚫 Pod fails to start**
   - 🔍 Check memory settings
   - 📊 Verify resource limits in yaml file
   - 📝 Check logs: `kubectl logs [pod-name]`

2. **💾 Memory Issues**
   - ✔️ Ensure vm.max_map_count is set correctly
   - 📊 Verify sufficient RAM allocation to Minikube

## 🛠️ Maintenance

Regular maintenance tasks:

1. 💾 Backup your SonarQube data
2. 🔄 Update SonarQube version when new releases are available
3. 📊 Monitor system resources
4. 📝 Review and update quality profiles


## Secrets in Repo
- Set url and token
   - https://github.com/rifaterdemsahin/SonarQubeCourse/settings/secrets/actions

## 📚 Additional Resources

- 📖 [Official SonarQube Documentation](https://docs.sonarqube.org/)
- 🔧 [Kubernetes Documentation](https://kubernetes.io/docs/)
- 🚀 [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)

