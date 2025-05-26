## 🛠️ Paying Technical Debt by Refactoring

- 📝 Added formula_refactoring_log
- 🔄 Update: install.md >>> environment.md 
- 📄 Update: readme.md _readme.md
- 🗑️ Delete: sonarqube-k8s.yaml
- 🗑️ Add: sonarqube name space added for grouping > best practice 
- ⚙️ Update environment:
    ```bash
kubectl apply -f Symbols/deployment_postgresql.yaml && kubectl apply -f Symbols/deployment_server.yaml && kubectl apply -f Symbols/pvc.yaml && kubectl apply -f Symbols/service_sonarqube.yaml
    ```
    ```bash
kubectl apply -f Symbols/github-secrets.yaml
kubectl apply -f Symbols/github-integration.yaml    
```

- Github Secrets yamls
- Gitignore not to be exposed
    # Ignore GitHub secrets
    Symbols/github-secrets.yaml

    # General ignores
    *.env
    *.secret

- 🎨 Semblance file update
- 🚀 Run
- 💾 Commit

Explanation:
- 🛠️ - Represents technical work/refactoring
- 📝 - New file creation
- 🔄 - File updates/changes
- 📄 - Document modification
- 🗑️ - Deletion
- ⚙️ - Configuration/environment setup
- 🎨 - Style/appearance changes
- 🚀 - Execution/running
- 💾 - Saving changes/committing