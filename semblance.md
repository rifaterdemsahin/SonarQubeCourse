## Semblance 

### Problems and Solutions in the Project

#### 1. SonarQube Setup Issues
**Problem**: Elasticsearch memory configuration
- Virtual memory areas too low (vm.max_map_count)
- Default value of 65530 insufficient

**Solution**:
```bash
sudo sysctl -w vm.max_map_count=262144
sudo sysctl -w fs.file-max=65536
```

#### 2. Kubernetes Pod Issues
**Problem**: Pod stuck in Pending state
- Missing secret configuration
- Database credentials not found

**Solution**:
```bash
kubectl create namespace sonarqube 2>/dev/null || true
kubectl create secret generic sonar-db-credentials \
  --namespace sonarqube \
  --from-literal=POSTGRES_USER=sonar \
  --from-literal=POSTGRES_PASSWORD=sonar123 \
  --from-literal=POSTGRES_DB=sonar
```

#### 3. GitHub Action Connection Issues
**Problem**: SonarScanner unable to connect to SonarQube server
- Receiving GitHub Codespaces port forwarding page instead of SonarQube response
- Authentication and access issues
- Port visibility problems

#### 4. Minikube stops

**Problem**: Route issues and connection issules

### 5. Test dont exists

Problem : 16:19:01.418 ERROR The folder 'tests' does not exist for 'rifaterdemsahin_SonarQubeCourse_AZcsPUc8EajcHBulmmLO' (base directory = /home/runner/work/SonarQubeCourse/SonarQubeCourse)

6. Cant Code : We couldn't find any results matching selected criteria.


**Solutions**:
1. Server Configuration:
   - Ensure SonarQube server is running
   - Make port visibility public in Codespaces
   - Test URL manually in browser

2. Authentication Setup:
   - Verify `SONAR_TOKEN` in GitHub secrets
   - Check token permissions
   - Ensure proper network access

3. Project Configuration:
   - Review `sonar-project.properties`
   - Verify `sonar.host.url` setting
   - Configure port forwarding correctly
4. minikube start 
 ⚠️ Root Cause
You're likely running this inside GitHub Codespaces, and the SonarScanner is trying to connect to a SonarQube server hosted locally (on localhost or 127.0.0.1) or on an inaccessible port.
Set accesibility to public 

5. create tests folder 

### Debug Commands
```bash
kubectl describe pod -l app=sonarqube -n sonarqube
kubectl port-forward svc/sonarqube 9000:9000 -n sonarqube
kubectl logs -l app=sonarqube -n sonarqube --previous
```
