# SonarQube Port Forwarding

To access SonarQube locally, you'll need to set up port forwarding:

```bash
# Forward SonarQube's default port (9000)
kubectl port-forward svc/sonarqube-service 9000:9000 -n sonarqube
```

Access SonarQube through your web browser at:
- http://localhost:9000

Default credentials:
- Username: admin
- Password: admin