# 🔄 SonarQube Setup and Configuration Log

## 🛠️ Technical Debt and Refactoring Changes

### 📝 File Management
- ✨ Created formula_refactoring_log.md
- 🔄 Renamed install.md to environment.md
- 📄 Updated readme.md to _readme.md
- 🗑️ Removed sonarqube-k8s.yaml
- 📁 Added sonarqube namespace for better organization

### ⚙️ Environment Configuration
```bash
kubectl apply -f Symbols/deployment_postgresql.yaml && kubectl apply -f Symbols/deployment_server.yaml && kubectl apply -f Symbols/pvc.yaml && kubectl apply -f Symbols/service_sonarqube.yaml
```

### 🔐 Security Configuration
```bash
kubectl apply -f Symbols/github-secrets.yaml
kubectl apply -f Symbols/github-integration.yaml    
```

### 🔒 Security Management
- Added GitHub Secrets YAML files
- Updated .gitignore for security:
  ```
  # 🔐 GitHub secrets
  Symbols/github-secrets.yaml

  # 📌 General security ignores
  *.env
  *.secret
  ```

### 🎯 Security
- Implementation for the security steps included 
- gitignore security files 
    - secrets
    - integration
    - private keys 

### 🎯 Final Steps
- 🎨 Updated semblance file
- Update the environments file
- 🚀 Executed configuration
- 💾 Committed changes
- Formula to rerun with oneliner script

### 🎯 SonarQube inside settings from the ui
- Add the necesary cat private key
- Select organization
- Select the repo again
- Use global settings
- analysis method githubs actions 
- new token generate
- update token > https://github.com/rifaterdemsahin/SonarQubeCourse/settings/secrets/actions/SONAR_TOKEN
- update project key > sonar.projectKey=rifaterdemsahin_SonarQubeCourse_067c4f08-21de-4da3-b6b8-a8ab7ea167ef
- Now we have a pvc


### 🎯 Commit
- Set Port visibility to public on codespaces ports
- Check Sonarqube

## 📚 Legend
- 🛠️ Technical work/refactoring
- 📝 New file creation
- 🔄 File updates/changes
- 📄 Document modification
- 🗑️ Deletion
- ⚙️ Configuration setup
- 🎨 Style changes
- 🚀 Execution
- 💾 Save/commit
- 🔐 Security-related
- 📁 Directory/namespace changes