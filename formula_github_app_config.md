# 🔗 SonarQube GitHub App Configuration Guide

## 📋 Configuration Steps

1. **🔐 First, ensure the GitHub integration secret is applied:**
```bash
kubectl apply -f Symbols/github-integration.yaml -n sonarqube
```

2. **🔄 Restart SonarQube pod to pick up new configuration:**
```bash
kubectl rollout restart deployment sonarqube -n sonarqube
```

3. **📝 Configuration Values for SonarQube UI**

Use these values in the SonarQube GitHub configuration page:

- **Configuration name**: `GitHub-Integration`
- **GitHub API URL**: `https://api.github.com`
- **GitHub App ID**: `1325434`
- **Client ID**: `Iv23li0pkUtl3Hv8R9k6`
- **Client Secret**: `35a203b7269dd85dce1b5c5be56354043bc41c0a`
- **Private Key**: 
```
# Copy content from the file:
cat /workspaces/SonarQubeCourse/Symbols/sonarqubecourseapp.2025-05-26.private-key.pem
```

4. **✅ Verification Steps**
   - Ensure all fields are filled correctly
   - Click "Save" to apply the configuration
   - Test the connection using the "Check Connection" button if available

## 🔍 Troubleshooting

If the configuration doesn't work:

1. **🔐 Check Secrets:**
```bash
kubectl get secrets -n sonarqube
kubectl describe secret github-integration -n sonarqube
```

2. **📋 Check SonarQube Logs:**
```bash
kubectl logs -f deployment/sonarqube -n sonarqube
```

3. **🔄 If needed, delete and recreate the secret:**
```bash
kubectl delete secret github-integration -n sonarqube
kubectl apply -f Symbols/github-integration.yaml -n sonarqube
```

## 📌 Important Notes

- Make sure the GitHub App is properly installed on your GitHub organization/repository
- The private key should be in PEM format
- All fields are case-sensitive
- The GitHub API URL must end without a trailing slash
