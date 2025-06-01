To debug issues with:

* `kubectl get pods -n sonarqube`
* `minikube status`

You can use the following shell script or commands step-by-step to help understand what’s going wrong. Here's a full script and explanation:

---

### ✅ **Debug Script for SonarQube on Minikube**

```bash
#!/bin/bash

echo "===== Minikube Status ====="
minikube status

echo "===== Kubernetes Nodes ====="
kubectl get nodes -o wide

echo "===== SonarQube Namespace Status ====="
kubectl get ns sonarqube || echo "Namespace 'sonarqube' does not exist"

echo "===== SonarQube Pods ====="
kubectl get pods -n sonarqube || echo "Failed to get pods in namespace 'sonarqube'"

echo "===== SonarQube Pod Details ====="
kubectl describe pods -n sonarqube || echo "Cannot describe pods - are they created?"

echo "===== Events in SonarQube Namespace ====="
kubectl get events -n sonarqube --sort-by='.metadata.creationTimestamp'

echo "===== Logs from SonarQube Pods ====="
for pod in $(kubectl get pods -n sonarqube -o jsonpath="{.items[*].metadata.name}"); do
  echo "---- Logs from pod: $pod ----"
  kubectl logs -n sonarqube $pod --all-containers=true
done
```

---

### 🔍 Additional Manual Commands

If you're doing this manually, run the following:

1. **Check if Minikube is running:**

   ```bash
   minikube status
   ```

2. **Verify your Kubernetes context:**

   ```bash
   kubectl config current-context
   ```

3. **List all namespaces to ensure `sonarqube` exists:**

   ```bash
   kubectl get namespaces
   ```

4. **Check pods in the SonarQube namespace:**

   ```bash
   kubectl get pods -n sonarqube
   ```

5. **Get detailed info on failing pods (if any):**

   ```bash
   kubectl describe pod <pod-name> -n sonarqube
   ```

6. **Get logs from a pod:**

   ```bash
   kubectl logs <pod-name> -n sonarqube
   ```

7. **Check for deployment status:**

   ```bash
   kubectl get deployments -n sonarqube
   kubectl describe deployment <deployment-name> -n sonarqube
   ```

---

If you're stuck at a particular step, feel free to share the output, and I can help interpret or guide you further.
