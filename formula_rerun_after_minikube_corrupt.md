Here’s a rewritten, cleanly structured version tailored as a **step-by-step guide for an AI agent** (or a teammate) to reboot SonarQube after a corrupted Minikube instance:

---

# 🛠️ SonarQube Reboot Guide After Minikube Corruption

This guide walks through the full recovery process for running SonarQube locally when Minikube becomes corrupt or non-functional.

---

## 🔁 1. Reboot Minikube

Start by attempting to start Minikube with appropriate resources:

```bash
minikube start --memory=9096 --cpus=4
minikube status
```

### ❗ If You See This Error:

```
❌  K8S_INSTALL_FAILED_CONTAINER_RUNTIME_NOT_RUNNING
```

It means Minikube is in a broken state. Run the following to reset completely:

```bash
minikube delete --all
minikube start --driver=docker --memory=9096 --cpus=4
```

Then, recheck status:

```bash
minikube status
```

---

## 🔧 2. System Prerequisites (Linux only)

Ensure required system settings are applied:

```bash
sudo sysctl -w vm.max_map_count=262144
sudo sysctl -w fs.file-max=65536
```

---

## 🧹 3. Cleanup Old Resources

Delete any old SonarQube resources to avoid conflicts:

```bash
kubectl delete namespace sonarqube --ignore-not-found=true
sleep 10
```

---

## 🚀 4. Setup Namespace and Secrets

Create the `sonarqube` namespace and DB secrets:

```bash
kubectl create namespace sonarqube

kubectl create secret generic sonar-db-credentials \
  --namespace sonarqube \
  --from-literal=POSTGRES_USER=sonar \
  --from-literal=POSTGRES_PASSWORD=sonar123 \
  --from-literal=POSTGRES_DB=sonar
```

---

## 📦 5. Apply Kubernetes Configurations

Navigate to your deployment folder:

```bash
cd /workspaces/SonarQubeCourse/Symbols
```

### Step-by-step Deployment:

1. **Persistent Volume Claim**

   ```bash
   kubectl apply -f pvc.yaml -n sonarqube
   sleep 5
   ```

2. **PostgreSQL Deployment**

   ```bash
   kubectl apply -f deployment_postgresql.yaml -n sonarqube
   kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s
   ```

3. **SonarQube Server + Service**

   ```bash
   kubectl apply -f deployment_server.yaml -f service_sonarqube.yaml -n sonarqube
   kubectl wait --for=condition=ready pod -l app=sonarqube -n sonarqube --timeout=300s
   ```

4. **(Optional) GitHub Integration**

   ```bash
   kubectl apply -f github-secrets.yaml -f github-integration.yaml -n sonarqube
   ```

---

## 🌐 6. Access SonarQube Locally

Set up port forwarding:

```bash
kubectl port-forward svc/sonarqube 9000:9000 -n sonarqube
```

Then visit [http://localhost:9000](http://localhost:9000)

**Default Credentials**:

* Username: `admin`
* Password: `admin` (you’ll be prompted to change it on first login)

---

## 🧪 7. Troubleshooting

Check logs or pod states using:

```bash
kubectl logs -l app=sonarqube -n sonarqube
kubectl logs -l app=sonarqube-db -n sonarqube
kubectl get pods -n sonarqube
```

---

✨ **You're now ready to scan code with SonarQube again!** ✨

Let me know if you want to convert this into a runnable script or automate it via GitHub Actions or Logic Apps.
