# 🎯 SonarQube Port Forwarding

To access SonarQube locally, follow these steps 🚀:

```bash
# Start Minikube and forward SonarQube port in one go! 🔥
minikube start --memory=9096 --cpus=4 && kubectl create namespace sonarqube  &&
 kubectl create secret generic sonar-db-credentials \
  --namespace sonarqube \
  --from-literal=POSTGRES_USER=sonar \
  --from-literal=POSTGRES_PASSWORD=sonar123 \
  --from-literal=POSTGRES_DB=sonar &&
   cd /workspaces/SonarQubeCourse/Symbols && kubectl apply -f deployment_postgresql.yaml -f deployment_server.yaml -f pvc.yaml -f service_sonarqube.yaml -f github-secrets.yaml -f github-integration.yaml -n sonarqube && sleep 10 && kubectl port-forward svc/sonarqube 9000:9000 -n sonarqube
```

🌐 Access SonarQube in your web browser at:
- http://localhost:9000

✨ Happy code analysis! ✨
