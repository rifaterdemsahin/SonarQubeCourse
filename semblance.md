## Semblance 

### Errors found in the project and the solutions

Error : Sonar Qube Setup Configuration

The error occurs because the SonarScanner CLI is receiving an HTML response from a GitHub Codespaces port forwarding page instead of the expected SonarQube server response. This suggests that the SonarQube server URL configured in your setup is pointing to a GitHub Codespaces URL (likely due to a misconfiguration in sonar-project.properties or the GitHub Actions workflow), causing the scanner to fail when trying to communicate with the SonarQube server.
Here’s how to fix the issue:
1. Verify SonarQube Server URL
The SonarScanner is trying to connect to a SonarQube server but is hitting a GitHub Codespaces port forwarding page. Check the sonar.host.url in your sonar-project.properties file or the configuration passed to the sonar-scanner command.
Action: Open the sonar-project.properties file in your repository (located at /home/runner/work/SonarQubeCourse/SonarQubeCourse/sonar-project.properties as per the log).
Check: Ensure sonar.host.url is set to the correct SonarQube server URL. For example:
properties
sonar.host.url=https://your-sonarqube-server.com
Common Mistake: If you’re running SonarQube locally or in a Codespace, the URL might be incorrectly set to a GitHub Codespaces forwarding URL (e.g., https://<codespace-name>.github.dev). Instead, it should point to the actual SonarQube server instance (e.g., http://localhost:9000 for a local server or the public URL of your SonarQube instance).
2. Check SonarQube Server Availability
Ensure the SonarQube server is running and accessible from the GitHub Actions runner.
If running locally: If SonarQube is running in your GitHub Codespace or locally, you need to expose it to the GitHub Actions runner. GitHub Codespaces port forwarding doesn’t work directly in GitHub Actions because the runner is a separate environment.
Solution: Deploy SonarQube to a publicly accessible server (e.g., a cloud-hosted instance) or use a tunneling service like ngrok to expose your local SonarQube server.
Install ngrok in your Codespace or local environment.
Run ngrok http 9000 to expose the SonarQube server (default port is 9000).
Update sonar.host.url in sonar-project.properties with the ngrok URL (e.g., https://<ngrok-id>.ngrok.io).
If running on a hosted server: Ensure the SonarQube server is reachable by pinging the URL from the GitHub Actions runner or testing it with curl:
bash
curl -v https://your-sonarqube-server.com
If it returns an HTML page like the one in the logs, the URL is incorrect.
3. Update GitHub Actions Workflow
If the sonar.host.url is passed via the GitHub Actions workflow (e.g., in the SonarSource/sonarqube-scan-action step), ensure it’s correctly configured.
Check the Workflow File: Look at the .yml file in .github/workflows/ for the SonarQube scan step. It might look like:
yaml
- name: Run SonarQube Scan
  uses: SonarSource/sonarqube-scan-action@v5
  with:
    projectKey: your-project-key
    organization: your-organization
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: https://your-sonarqube-server.com
Fix: Ensure SONAR_HOST_URL points to the correct SonarQube server. If it’s missing or incorrect, update it to the proper URL.
4. Authentication Issues
The HTML response includes an authentication URL (https://github.com/codespaces/auth/...), indicating a possible authentication or access issue.
Check SonarQube Token:
Ensure the SONAR_TOKEN environment variable is correctly set in your GitHub Actions workflow and matches a valid token generated from your SonarQube server.
Generate a new token in SonarQube:
Log in to your SonarQube instance.
Go to My Account > Security.
Generate a new token and update it in your GitHub repository’s secrets (SONAR_TOKEN).
Update the workflow to include:
yaml
env:
  SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
Bypass Codespaces Authentication (if applicable): If you’re intentionally using a Codespace-hosted SonarQube instance, you may need to handle port forwarding authentication. However, this is not recommended for GitHub Actions, as runners cannot easily handle Codespaces’ authentication pages. Instead, use a publicly accessible SonarQube instance.
5. Cache Configuration (Optional Optimization)
The logs show the SonarScanner CLI is downloaded every time because the cache key sonar-scanner-cli-7.1.0.4889-Linux-X64 is not found. While this doesn’t cause the error, it slows down the workflow.
Fix: Ensure the actions/cache@v4 step is correctly configured to cache the SonarScanner CLI. Example:
yaml
- name: Cache SonarScanner
  uses: actions/cache@v4
  with:
    path: ${{ runner.temp }}/sonar-scanner-cli-7.1.0.4889-Linux-X64
    key: sonar-scanner-cli-7.1.0.4889-Linux-X64
Placement: Place this step before the sonarqube-scan-action to avoid redownloading the CLI.
6. Debug the Scanner
To get more details, enable debug logging as suggested in the error message.
Action: Modify the sonarqube-scan-action step to include the -X flag:
yaml
- name: Run SonarQube Scan
  uses: SonarSource/sonarqube-scan-action@v5
  with:
    args: -X
  env:
    SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
    SONAR_HOST_URL: https://your-sonarqube-server.com
Outcome: This will provide detailed logs, which may reveal additional clues about the connection issue.
7. Example Fixed Workflow
Here’s an example of a corrected GitHub Actions workflow:
yaml
name: SonarQube Scan
on:
  push:
    branches: [main]
jobs:
  sonarqube:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Cache SonarScanner
        uses: actions/cache@v4
        with:
          path: ${{ runner.temp }}/sonar-scanner-cli-7.1.0.4889-Linux-X64
          key: sonar-scanner-cli-7.1.0.4889-Linux-X64
      - name: Run SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@v5
        with:
          args: -X
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: https://your-sonarqube-server.com
8. Verify SonarQube Server Setup
If you’re running SonarQube in a Codespace or locally:
Ensure the server is started before the GitHub Actions workflow runs. For example, start it with:
bash
docker run -d -p 9000:9000 sonarqube:latest
Access the SonarQube UI (e.g., http://localhost:9000) to confirm it’s running and accessible.
If using a cloud-hosted SonarQube instance, verify the server is not behind a firewall or proxy blocking the GitHub Actions runner.
9. Test the Fix
Push your changes to the repository and trigger the GitHub Actions workflow.
Check the logs to ensure the SonarScanner connects to the correct SonarQube server and completes the scan without errors.
Summary
The primary issue is that the SonarQube server URL is incorrectly set, leading to a GitHub Codespaces port forwarding page response. Fix this by:
Correcting sonar.host.url in sonar-project.properties or the workflow.
Ensuring the SonarQube server is accessible (use ngrok or a hosted instance if needed).
Verifying the SONAR_TOKEN and workflow configuration.
Optionally, fixing the cache step to reduce execution time.
If the issue persists, share the updated sonar-project.properties and workflow file for further debugging.

---

Debug :kubectl describe pod -l app=sonarqube -n sonarqube

---

@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl port-forward svc/sonarqube 9000:9000 -n sonarqube
error: unable to forward port because pod is not running. Current status=Pending


error: unable to forward port because pod is not running. Current status=Pending
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl describe pod -l app=sonarqube -n sonarqube
Name:             sonarqube-56f655c4b7-h84vw
Namespace:        sonarqube
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sat, 31 May 2025 16:59:35 +0000
Labels:           app=sonarqube
                  pod-template-hash=56f655c4b7
Annotations:      <none>
Status:           Pending
IP:               10.244.0.3
IPs:
  IP:           10.244.0.3
Controlled By:  ReplicaSet/sonarqube-56f655c4b7
Containers:
  sonarqube:
    Container ID:   
    Image:          sonarqube:9.9-community
    Image ID:       
    Port:           9000/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       CreateContainerConfigError
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     2
      memory:  4Gi
    Requests:
      cpu:      1
      memory:   2Gi
    Liveness:   http-get http://:9000/ delay=120s timeout=1s period=30s #success=1 #failure=3
    Readiness:  http-get http://:9000/ delay=60s timeout=1s period=30s #success=1 #failure=3
    Environment:
      SONAR_JDBC_URL:       jdbc:postgresql://sonarqube-db:5432/sonar
      SONAR_JDBC_USERNAME:  <set to the key 'POSTGRES_USER' in secret 'sonar-db-credentials'>      Optional: false
      SONAR_JDBC_PASSWORD:  <set to the key 'POSTGRES_PASSWORD' in secret 'sonar-db-credentials'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-4l6r6 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-4l6r6:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age               From               Message
  ----     ------     ----              ----               -------
  Normal   Scheduled  113s              default-scheduler  Successfully assigned sonarqube/sonarqube-56f655c4b7-h84vw to minikube
  Normal   Pulling    112s              kubelet            Pulling image "sonarqube:9.9-community"
  Normal   Pulled     95s               kubelet            Successfully pulled image "sonarqube:9.9-community" in 17.312s (17.312s including waiting). Image size: 604265948 bytes.
  Warning  Failed     5s (x9 over 95s)  kubelet            Error: secret "sonar-db-credentials" not found
  Normal   Pulled     5s (x8 over 94s)  kubelet            Container image "sonarqube:9.9-community" already present on machine
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ 

kubectl create namespace sonarqube 2>/dev/null || true && kubectl create secret generic sonar-db-credentials \
  --namespace sonarqube \
  --from-literal=POSTGRES_USER=sonar \
  --from-literal=POSTGRES_PASSWORD=sonar123 \
  --from-literal=POSTGRES_DB=sonar


---

@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ kubectl logs -l app=sonarqube -n sonarqube --previous
ERROR: [1] bootstrap checks failed. You must address the points described in the following [1] lines before starting Elasticsearch.
bootstrap check failure [1] of [1]: max virtual memory areas vm.max_map_count [65530] is too low, increase to at least [262144]
ERROR: Elasticsearch did not exit normally - check the logs at /opt/sonarqube/logs/sonarqube.log
2025.05.31 17:11:54 INFO  es[][o.e.n.Node] stopping ...
2025.05.31 17:11:54 INFO  es[][o.e.n.Node] stopped
2025.05.31 17:11:54 INFO  es[][o.e.n.Node] closing ...
2025.05.31 17:11:54 INFO  es[][o.e.n.Node] closed
2025.05.31 17:11:54 WARN  app[][o.s.a.p.AbstractManagedProcess] Process exited with exit value [ElasticSearch]: 78
2025.05.31 17:11:54 INFO  app[][o.s.a.SchedulerImpl] Process[ElasticSearch] is stopped
2025.05.31 17:11:54 INFO  app[][o.s.a.SchedulerImpl] SonarQube is stopped
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse/Symbols (main) $ 


sudo sysctl -w vm.max_map_count=262144
sudo sysctl -w fs.file-max=65536