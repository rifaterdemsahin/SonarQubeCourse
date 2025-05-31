# 🎯 SonarQube Port Forwarding

To access SonarQube locally, follow these steps 🚀:

```bash
# Step 1: Start Minikube with sufficient resources
minikube start --memory=9096 --cpus=4

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
