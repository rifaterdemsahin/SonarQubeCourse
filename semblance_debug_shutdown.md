@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ # Global variables (tech debt: should avoid globals)
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ 
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ echo "===== Minikube Status ====="
===== Minikube Status =====


echo "===== Kubernetes Nodes ====="
kubectl get nodes -o wide

echo "===== SonarQube Namespace Status ====="
kubectl get ns sonarqube || echo "Names@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ minikube status
pace 'sonarqube' does not exist"

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
done🎉  minikube 1.36.0 is available! Download it: https://github.com/kubernetes/minikube/releases/tag/v1.36.0
💡  To disable this notice, run: 'minikube config set WantUpdateNotification false'

minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ 
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ echo "===== Kubernetes Nodes ====="
===== Kubernetes Nodes =====
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get nodes -o wide
NAME       STATUS   ROLES           AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME
minikube   Ready    control-plane   65m   v1.27.3   192.168.49.2   <none>        Ubuntu 22.04.5 LTS   6.8.0-1027-azure   docker://27.4.1
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ 
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ echo "===== SonarQube Namespace Status ====="
===== SonarQube Namespace Status =====
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get ns sonarqube || echo "Namespace 'sonarqube' does not exist"
NAME        STATUS   AGE
sonarqube   Active   62m
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ 
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ echo "===== SonarQube Pods ====="
===== SonarQube Pods =====
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get pods -n sonarqube || echo "Failed to get pods in namespace 'sonarqube'"
NAME                            READY   STATUS    RESTARTS        AGE
sonarqube-55b9ff9c79-nkrxh      1/1     Running   4 (5m47s ago)   62m
sonarqube-db-778f999cd5-k6fn6   1/1     Running   2 (6m5s ago)    62m
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ 
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ echo "===== SonarQube Pod Details ====="
===== SonarQube Pod Details =====
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl describe pods -n sonarqube || echo "Cannot describe pods - are they created?"
Name:             sonarqube-55b9ff9c79-nkrxh
Namespace:        sonarqube
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 01 Jun 2025 15:58:30 +0000
Labels:           app=sonarqube
                  pod-template-hash=55b9ff9c79
Annotations:      <none>
Status:           Running
IP:               10.244.0.7
IPs:
  IP:           10.244.0.7
Controlled By:  ReplicaSet/sonarqube-55b9ff9c79
Containers:
  sonarqube:
    Container ID:   docker://213f42ac580330053fad969746d8c33b15dedfec7e51334b9ab065b27bb465f4
    Image:          sonarqube:9.9-community
    Image ID:       docker-pullable://sonarqube@sha256:93f94e0ea6148cd02d52378049dad85d0f2d6c90c485578317f76addf2af9f3d
    Port:           9000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 01 Jun 2025 16:56:08 +0000
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Sun, 01 Jun 2025 16:53:06 +0000
      Finished:     Sun, 01 Jun 2025 16:55:16 +0000
    Ready:          True
    Restart Count:  4
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
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-hr7b2 (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-hr7b2:
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
  Type     Reason          Age                   From               Message
  ----     ------          ----                  ----               -------
  Normal   Scheduled       62m                   default-scheduler  Successfully assigned sonarqube/sonarqube-55b9ff9c79-nkrxh to minikube
  Normal   Pulling         62m                   kubelet            Pulling image "sonarqube:9.9-community"
  Normal   Pulled          61m                   kubelet            Successfully pulled image "sonarqube:9.9-community" in 20.50922694s (37.187780665s including waiting)
  Normal   Created         61m                   kubelet            Created container sonarqube
  Normal   Started         61m                   kubelet            Started container sonarqube
  Normal   SandboxChanged  9m6s                  kubelet            Pod sandbox changed, it will be killed and re-created.
  Warning  Unhealthy       6m                    kubelet            Readiness probe failed: Get "http://10.244.0.7:9000/": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
  Warning  Unhealthy       5m51s                 kubelet            Liveness probe failed: Get "http://10.244.0.7:9000/": read tcp 10.244.0.1:53402->10.244.0.7:9000: read: connection reset by peer
  Warning  BackOff         5m8s (x9 over 8m50s)  kubelet            Back-off restarting failed container sonarqube in pod sonarqube-55b9ff9c79-nkrxh_sonarqube(4e6571e7-30fd-47e7-bd21-eb882f499139)
  Normal   Pulled          4m55s (x4 over 9m5s)  kubelet            Container image "sonarqube:9.9-community" already present on machine
  Normal   Created         4m55s (x4 over 9m5s)  kubelet            Created container sonarqube
  Normal   Started         4m55s (x4 over 9m5s)  kubelet            Started container sonarqube


Name:             sonarqube-db-778f999cd5-k6fn6
Namespace:        sonarqube
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 01 Jun 2025 15:58:29 +0000
Labels:           app=sonarqube-db
                  pod-template-hash=778f999cd5
Annotations:      <none>
Status:           Running
IP:               10.244.0.5
IPs:
  IP:           10.244.0.5
Controlled By:  ReplicaSet/sonarqube-db-778f999cd5
Containers:
  postgres:
    Container ID:   docker://c1a438d6bb3cbe71ec556d6ad086589348d9880b09745ef1ce8032d86ad6124d
    Image:          postgres:13
    Image ID:       docker-pullable://postgres@sha256:9b6a9504a4b804c8f0cf52f4d16477289f8e1dfa269a689d778feaca6fbe1f4f
    Port:           5432/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 01 Jun 2025 16:55:22 +0000
    Last State:     Terminated
      Reason:       Error
      Exit Code:    137
      Started:      Sun, 01 Jun 2025 16:51:58 +0000
      Finished:     Sun, 01 Jun 2025 16:54:58 +0000
    Ready:          True
    Restart Count:  2
    Limits:
      cpu:     1
      memory:  2Gi
    Requests:
      cpu:     500m
      memory:  1Gi
    Environment:
      POSTGRES_USER:      <set to the key 'POSTGRES_USER' in secret 'sonar-db-credentials'>      Optional: false
      POSTGRES_PASSWORD:  <set to the key 'POSTGRES_PASSWORD' in secret 'sonar-db-credentials'>  Optional: false
      POSTGRES_DB:        <set to the key 'POSTGRES_DB' in secret 'sonar-db-credentials'>        Optional: false
    Mounts:
      /var/lib/postgresql/data from postgres-data (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6h49r (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  postgres-data:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  sonarqube-data
    ReadOnly:   false
  kube-api-access-6h49r:
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
  Type     Reason          Age                   From               Message
  ----     ------          ----                  ----               -------
  Normal   Scheduled       62m                   default-scheduler  Successfully assigned sonarqube/sonarqube-db-778f999cd5-k6fn6 to minikube
  Normal   Pulling         62m                   kubelet            Pulling image "postgres:13"
  Normal   Pulled          62m                   kubelet            Successfully pulled image "postgres:13" in 16.678523743s (16.678679343s including waiting)
  Normal   Created         62m                   kubelet            Created container postgres
  Normal   Started         62m                   kubelet            Started container postgres
  Normal   SandboxChanged  9m6s                  kubelet            Pod sandbox changed, it will be killed and re-created.
  Warning  BackOff         5m55s                 kubelet            Back-off restarting failed container postgres in pod sonarqube-db-778f999cd5-k6fn6_sonarqube(e893e20c-f91b-4329-8695-e8f839dc45b8)
  Normal   Pulled          5m42s (x2 over 9m5s)  kubelet            Container image "postgres:13" already present on machine
  Normal   Created         5m41s (x2 over 9m5s)  kubelet            Created container postgres
  Normal   Started         5m41s (x2 over 9m5s)  kubelet            Started container postgres
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ 
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ echo "===== Events in SonarQube Namespace ====="
===== Events in SonarQube Namespace =====
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ kubectl get events -n sonarqube --sort-by='.metadata.creationTimestamp'
LAST SEEN   TYPE      REASON                  OBJECT                                 MESSAGE
62m         Normal    ScalingReplicaSet       deployment/sonarqube-db                Scaled up replica set sonarqube-db-778f999cd5 to 1
62m         Normal    Scheduled               pod/sonarqube-db-778f999cd5-k6fn6      Successfully assigned sonarqube/sonarqube-db-778f999cd5-k6fn6 to minikube
62m         Normal    ProvisioningSucceeded   persistentvolumeclaim/sonarqube-data   Successfully provisioned volume pvc-583f69ed-ddea-4f41-80bd-83ab17f94b84
62m         Normal    ExternalProvisioning    persistentvolumeclaim/sonarqube-data   waiting for a volume to be created, either by external provisioner "k8s.io/minikube-hostpath" or manually created by system administrator
62m         Normal    Provisioning            persistentvolumeclaim/sonarqube-data   External provisioner is provisioning volume for claim "sonarqube/sonarqube-data"
62m         Normal    SuccessfulCreate        replicaset/sonarqube-db-778f999cd5     Created pod: sonarqube-db-778f999cd5-k6fn6
62m         Normal    SuccessfulCreate        replicaset/sonarqube-55b9ff9c79        Created pod: sonarqube-55b9ff9c79-nkrxh
62m         Normal    Scheduled               pod/sonarqube-55b9ff9c79-nkrxh         Successfully assigned sonarqube/sonarqube-55b9ff9c79-nkrxh to minikube
62m         Normal    ScalingReplicaSet       deployment/sonarqube                   Scaled up replica set sonarqube-55b9ff9c79 to 1
62m         Normal    Pulling                 pod/sonarqube-db-778f999cd5-k6fn6      Pulling image "postgres:13"
62m         Normal    Pulling                 pod/sonarqube-55b9ff9c79-nkrxh         Pulling image "sonarqube:9.9-community"
62m         Normal    Started                 pod/sonarqube-db-778f999cd5-k6fn6      Started container postgres
62m         Normal    Created                 pod/sonarqube-db-778f999cd5-k6fn6      Created container postgres
62m         Normal    Pulled                  pod/sonarqube-db-778f999cd5-k6fn6      Successfully pulled image "postgres:13" in 16.678523743s (16.678679343s including waiting)
61m         Normal    Started                 pod/sonarqube-55b9ff9c79-nkrxh         Started container sonarqube
61m         Normal    Created                 pod/sonarqube-55b9ff9c79-nkrxh         Created container sonarqube
61m         Normal    Pulled                  pod/sonarqube-55b9ff9c79-nkrxh         Successfully pulled image "sonarqube:9.9-community" in 20.50922694s (37.187780665s including waiting)
4m55s       Normal    Created                 pod/sonarqube-55b9ff9c79-nkrxh         Created container sonarqube
9m6s        Normal    SandboxChanged          pod/sonarqube-db-778f999cd5-k6fn6      Pod sandbox changed, it will be killed and re-created.
5m42s       Normal    Pulled                  pod/sonarqube-db-778f999cd5-k6fn6      Container image "postgres:13" already present on machine
5m41s       Normal    Created                 pod/sonarqube-db-778f999cd5-k6fn6      Created container postgres
5m41s       Normal    Started                 pod/sonarqube-db-778f999cd5-k6fn6      Started container postgres
4m55s       Normal    Started                 pod/sonarqube-55b9ff9c79-nkrxh         Started container sonarqube
4m55s       Normal    Pulled                  pod/sonarqube-55b9ff9c79-nkrxh         Container image "sonarqube:9.9-community" already present on machine
9m6s        Normal    SandboxChanged          pod/sonarqube-55b9ff9c79-nkrxh         Pod sandbox changed, it will be killed and re-created.
5m8s        Warning   BackOff                 pod/sonarqube-55b9ff9c79-nkrxh         Back-off restarting failed container sonarqube in pod sonarqube-55b9ff9c79-nkrxh_sonarqube(4e6571e7-30fd-47e7-bd21-eb882f499139)
6m          Warning   Unhealthy               pod/sonarqube-55b9ff9c79-nkrxh         Readiness probe failed: Get "http://10.244.0.7:9000/": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
5m55s       Warning   BackOff                 pod/sonarqube-db-778f999cd5-k6fn6      Back-off restarting failed container postgres in pod sonarqube-db-778f999cd5-k6fn6_sonarqube(e893e20c-f91b-4329-8695-e8f839dc45b8)
5m51s       Warning   Unhealthy               pod/sonarqube-55b9ff9c79-nkrxh         Liveness probe failed: Get "http://10.244.0.7:9000/": read tcp 10.244.0.1:53402->10.244.0.7:9000: read: connection reset by peer
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ 
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ echo "===== Logs from SonarQube Pods ====="
===== Logs from SonarQube Pods =====
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ for pod in $(kubectl get pods -n sonarqube -o jsonpath="{.items[*].metadata.name}"); do
>   echo "---- Logs from pod: $pod ----"
>   kubectl logs -n sonarqube $pod --all-containers=true
> done
---- Logs from pod: sonarqube-55b9ff9c79-nkrxh ----
2025.06.01 16:56:09 INFO  app[][o.s.a.AppFileSystem] Cleaning or creating temp directory /opt/sonarqube/temp
2025.06.01 16:56:09 INFO  app[][o.s.a.es.EsSettings] Elasticsearch listening on [HTTP: 127.0.0.1:9001, TCP: 127.0.0.1:43259]
2025.06.01 16:56:10 INFO  app[][o.s.a.ProcessLauncherImpl] Launch process[ELASTICSEARCH] from [/opt/sonarqube/elasticsearch]: /opt/sonarqube/elasticsearch/bin/elasticsearch
2025.06.01 16:56:10 INFO  app[][o.s.a.SchedulerImpl] Waiting for Elasticsearch to be up and running
2025.06.01 16:56:12 INFO  es[][o.e.n.Node] version[7.17.15], pid[26], build[default/tar/0b8ecfb4378335f4689c4223d1f1115f16bef3ba/2023-11-10T22:03:46.987399016Z], OS[Linux/6.8.0-1027-azure/amd64], JVM[Eclipse Adoptium/OpenJDK 64-Bit Server VM/17.0.15/17.0.15+6]
2025.06.01 16:56:12 INFO  es[][o.e.n.Node] JVM home [/opt/java/openjdk]
2025.06.01 16:56:12 INFO  es[][o.e.n.Node] JVM arguments [-XX:+UseG1GC, -Djava.io.tmpdir=/opt/sonarqube/temp, -XX:ErrorFile=/opt/sonarqube/logs/es_hs_err_pid%p.log, -Des.networkaddress.cache.ttl=60, -Des.networkaddress.cache.negative.ttl=10, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -Djna.tmpdir=/opt/sonarqube/temp, -XX:-OmitStackTraceInFastThrow, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, -Dio.netty.allocator.numDirectArenas=0, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Dlog4j2.formatMsgNoLookups=true, -Djava.locale.providers=COMPAT, -Dcom.redhat.fips=false, -Des.enforce.bootstrap.checks=true, -Xmx512m, -Xms512m, -XX:MaxDirectMemorySize=256m, -XX:+HeapDumpOnOutOfMemoryError, -Des.path.home=/opt/sonarqube/elasticsearch, -Des.path.conf=/opt/sonarqube/temp/conf/es, -Des.distribution.flavor=default, -Des.distribution.type=tar, -Des.bundled_jdk=false]
2025.06.01 16:56:12 INFO  es[][o.e.p.PluginsService] loaded module [analysis-common]
2025.06.01 16:56:12 INFO  es[][o.e.p.PluginsService] loaded module [lang-painless]
2025.06.01 16:56:12 INFO  es[][o.e.p.PluginsService] loaded module [parent-join]
2025.06.01 16:56:12 INFO  es[][o.e.p.PluginsService] loaded module [reindex]
2025.06.01 16:56:12 INFO  es[][o.e.p.PluginsService] loaded module [transport-netty4]
2025.06.01 16:56:12 INFO  es[][o.e.p.PluginsService] no plugins loaded
2025.06.01 16:56:12 INFO  es[][o.e.e.NodeEnvironment] using [1] data paths, mounts [[/ (overlay)]], net usable_space [7.9gb], net total_space [31.3gb], types [overlay]
2025.06.01 16:56:12 INFO  es[][o.e.e.NodeEnvironment] heap size [512mb], compressed ordinary object pointers [true]
2025.06.01 16:56:12 INFO  es[][o.e.n.Node] node name [sonarqube], node ID [fRF3MrqqTv-uwtdWK-Fuhg], cluster name [sonarqube], roles [data_frozen, master, remote_cluster_client, data, data_content, data_hot, data_warm, data_cold, ingest]
2025.06.01 16:56:15 INFO  es[][o.e.t.NettyAllocator] creating NettyAllocator with the following configs: [name=unpooled, suggested_max_allocation_size=256kb, factors={es.unsafe.use_unpooled_allocator=null, g1gc_enabled=true, g1gc_region_size=1mb, heap_size=512mb}]
2025.06.01 16:56:15 INFO  es[][o.e.i.r.RecoverySettings] using rate limit [40mb] with [default=40mb, read=0b, write=0b, max=0b]
2025.06.01 16:56:15 INFO  es[][o.e.d.DiscoveryModule] using discovery type [zen] and seed hosts providers [settings]
2025.06.01 16:56:15 INFO  es[][o.e.g.DanglingIndicesState] gateway.auto_import_dangling_indices is disabled, dangling indices will not be automatically detected or imported and must be managed manually
2025.06.01 16:56:16 INFO  es[][o.e.n.Node] initialized
2025.06.01 16:56:16 INFO  es[][o.e.n.Node] starting ...
2025.06.01 16:56:16 INFO  es[][o.e.t.TransportService] publish_address {127.0.0.1:43259}, bound_addresses {127.0.0.1:43259}
2025.06.01 16:56:16 INFO  es[][o.e.b.BootstrapChecks] explicitly enforcing bootstrap checks
2025.06.01 16:56:16 INFO  es[][o.e.c.c.Coordinator] setting initial configuration to VotingConfiguration{fRF3MrqqTv-uwtdWK-Fuhg}
2025.06.01 16:56:16 INFO  es[][o.e.c.s.MasterService] elected-as-master ([1] nodes joined)[{sonarqube}{fRF3MrqqTv-uwtdWK-Fuhg}{QZdtrDnoT6-vlI4g8mGduA}{127.0.0.1}{127.0.0.1:43259}{cdfhimrsw} elect leader, _BECOME_MASTER_TASK_, _FINISH_ELECTION_], term: 1, version: 1, delta: master node changed {previous [], current [{sonarqube}{fRF3MrqqTv-uwtdWK-Fuhg}{QZdtrDnoT6-vlI4g8mGduA}{127.0.0.1}{127.0.0.1:43259}{cdfhimrsw}]}
2025.06.01 16:56:16 INFO  es[][o.e.c.c.CoordinationState] cluster UUID set to [2SEp2lCEQhKGijBD6F-JUQ]
2025.06.01 16:56:16 INFO  es[][o.e.c.s.ClusterApplierService] master node changed {previous [], current [{sonarqube}{fRF3MrqqTv-uwtdWK-Fuhg}{QZdtrDnoT6-vlI4g8mGduA}{127.0.0.1}{127.0.0.1:43259}{cdfhimrsw}]}, term: 1, version: 1, reason: Publication{term=1, version=1}
2025.06.01 16:56:16 INFO  es[][o.e.h.AbstractHttpServerTransport] publish_address {127.0.0.1:9001}, bound_addresses {127.0.0.1:9001}
2025.06.01 16:56:16 INFO  es[][o.e.n.Node] started
2025.06.01 16:56:16 INFO  es[][o.e.g.GatewayService] recovered [0] indices into cluster_state
2025.06.01 16:56:16 INFO  app[][o.s.a.SchedulerImpl] Process[es] is up
2025.06.01 16:56:16 INFO  app[][o.s.a.ProcessLauncherImpl] Launch process[WEB_SERVER] from [/opt/sonarqube]: /opt/java/openjdk/bin/java -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/opt/sonarqube/temp -XX:-OmitStackTraceInFastThrow --add-opens=java.base/java.util=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED --add-opens=java.rmi/sun.rmi.transport=ALL-UNNAMED --add-exports=java.base/jdk.internal.ref=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.management/sun.management=ALL-UNNAMED --add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED -Dcom.redhat.fips=false -Xmx512m -Xms128m -XX:+HeapDumpOnOutOfMemoryError -Dhttp.nonProxyHosts=localhost|127.*|[::1] -cp ./lib/sonar-application-9.9.8.100196.jar:/opt/sonarqube/lib/jdbc/postgresql/postgresql-42.5.1.jar org.sonar.server.app.WebServer /opt/sonarqube/temp/sq-process5784959159167374126properties
WARNING: A terminally deprecated method in java.lang.System has been called
WARNING: System::setSecurityManager has been called by org.sonar.process.PluginSecurityManager (file:/opt/sonarqube/lib/sonar-application-9.9.8.100196.jar)
WARNING: Please consider reporting this to the maintainers of org.sonar.process.PluginSecurityManager
WARNING: System::setSecurityManager will be removed in a future release
2025.06.01 16:56:17 INFO  web[][o.s.p.ProcessEntryPoint] Starting Web Server
2025.06.01 16:56:18 INFO  web[][o.s.s.p.LogServerVersion] SonarQube Server / 9.9.8.100196 / a6b73d92af974da59414bc4a00dde2882016ea70
2025.06.01 16:56:18 INFO  web[][o.sonar.db.Database] Create JDBC data source for jdbc:postgresql://sonarqube-db:5432/sonar
2025.06.01 16:56:18 INFO  web[][c.z.h.HikariDataSource] HikariPool-1 - Starting...
2025.06.01 16:56:18 INFO  web[][c.z.h.p.HikariPool] HikariPool-1 - Added connection org.postgresql.jdbc.PgConnection@59942b48
2025.06.01 16:56:18 INFO  web[][c.z.h.HikariDataSource] HikariPool-1 - Start completed.
2025.06.01 16:56:19 INFO  web[][o.s.s.p.ServerFileSystemImpl] SonarQube home: /opt/sonarqube
2025.06.01 16:56:19 INFO  web[][o.s.s.u.SystemPasscodeImpl] System authentication by passcode is disabled
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy C# Code Quality and Security / 8.51.0.59060 / e14c642f118958f22fd08841dc42f9aae480366a
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy Configuration detection fot Code Quality and Security / 1.2.0.267 / 4f37ba9ffb37a96d5883e52ad392ed32c5c6eaab
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy Flex Code Quality and Security / 2.8.0.3166 / 01f66bdddc678966c81a9064ed139156a6a89c97
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy Go Code Quality and Security / 1.11.0.3905 / e1f28bc000e04ca01881e84218d01d464a17a36f
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy HTML Code Quality and Security / 3.7.1.3306 / d720acc6860c6d8b69ec4d17570a398a1e216da1
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy IaC Code Quality and Security / 1.11.0.2847 / 6892bd3a7320b3c110717acfdb18c4c7451069fd
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy JaCoCo / 1.3.0.1538 / 74a7798c7cea687c72ed9df40c93eb7ea2a58c49
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy Java Code Quality and Security / 7.16.0.30901 / 4b1436558dfd5fc00c8d9aae8bb0364ba122c73e
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy JavaScript/TypeScript/CSS Code Quality and Security / 9.13.0.20537 / 68ff7657415044b86033814795ed95fc1f1558f1
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy Kotlin Code Quality and Security / 2.12.0.1956 / a6df1ae252bd62d63f8673c28f87ad14258a7904
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy PHP Code Quality and Security / 3.27.1.9352 / 3ddc5a03e1a7e3729d41e7c1a30a37d5715958c7
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy Python Code Quality and Security / 3.24.1.11916 / cc8f4fa745eb33d31c3869bdfdfd45514e67c1fe
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy Ruby Code Quality and Security / 1.11.0.3905 / e1f28bc000e04ca01881e84218d01d464a17a36f
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy Scala Code Quality and Security / 1.11.0.3905 / e1f28bc000e04ca01881e84218d01d464a17a36f
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy Text Code Quality and Security / 2.0.2.1090 / 7eb026363b98f5f98b43c603772b5177869c2c6a
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy VB.NET Code Quality and Security / 8.51.0.59060 / e14c642f118958f22fd08841dc42f9aae480366a
2025.06.01 16:56:20 INFO  web[][o.s.s.p.ServerPluginManager] Deploy XML Code Quality and Security / 2.7.0.3820 / 656bccc1910d50c8984536bd2dfd917066b858e6
2025.06.01 16:56:21 INFO  web[][o.s.s.p.d.m.c.PostgresCharsetHandler] Verify that database charset supports UTF8
2025.06.01 16:56:21 INFO  web[][o.s.s.e.EsClientProvider] Connected to local Elasticsearch: [http://localhost:9001]
2025.06.01 16:56:21 WARN  web[][o.s.a.s.w.WebService$Action] Description is not set on action api/monitoring/metrics
2025.06.01 16:56:21 WARN  web[][o.s.a.s.w.WebService$Action] Since is not set on action api/monitoring/metrics
2025.06.01 16:56:21 WARN  web[][o.s.a.s.w.WebService$Action] The response example is not set on action api/monitoring/metrics
2025.06.01 16:56:21 WARN  web[][o.s.a.s.w.WebService$Action] The response example is not set on action api/system/liveness
2025.06.01 16:56:21 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.platform.web.WebServiceFilter@5600a5da [pattern=UrlPattern{inclusions=[/api/system/migrate_db.*, ...], exclusions=[/api/components/update_key, ...]}]
2025.06.01 16:56:21 INFO  web[][o.s.s.a.EmbeddedTomcat] HTTP connector enabled on port 9000
2025.06.01 16:56:22 INFO  web[][o.s.s.p.DetectPluginChange] Detect plugin changes
2025.06.01 16:56:22 INFO  web[][o.s.s.p.DetectPluginChange] No plugin change detected
2025.06.01 16:56:23 INFO  web[][o.s.s.e.IndexCreator] Create index [metadatas]
2025.06.01 16:56:24 INFO  es[][o.e.c.m.MetadataCreateIndexService] [metadatas] creating index, cause [api], templates [], shards [1]/[0]
2025.06.01 16:56:24 INFO  es[][o.e.c.r.a.AllocationService] Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[metadatas][0]]]).
2025.06.01 16:56:24 INFO  web[][o.s.s.e.IndexCreator] Create type metadatas/metadata
2025.06.01 16:56:24 INFO  es[][o.e.c.m.MetadataMappingService] [metadatas/Vyw1T6iuSYaRMI65uzuPaA] create_mapping [metadata]
2025.06.01 16:56:24 INFO  web[][o.s.s.e.IndexCreator] Create index [components]
2025.06.01 16:56:25 INFO  es[][o.e.c.m.MetadataCreateIndexService] [components] creating index, cause [api], templates [], shards [5]/[0]
2025.06.01 16:56:25 INFO  es[][o.e.c.r.a.AllocationService] Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[components][4]]]).
2025.06.01 16:56:25 INFO  web[][o.s.s.e.IndexCreator] Create type components/auth
2025.06.01 16:56:25 INFO  es[][o.e.c.m.MetadataMappingService] [components/nXp7A15DTSO-SZhIMqmDkw] create_mapping [auth]
2025.06.01 16:56:25 INFO  web[][o.s.s.e.IndexCreator] Create index [projectmeasures]
2025.06.01 16:56:25 INFO  es[][o.e.c.m.MetadataCreateIndexService] [projectmeasures] creating index, cause [api], templates [], shards [5]/[0]
2025.06.01 16:56:25 INFO  es[][o.e.c.r.a.AllocationService] Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[projectmeasures][4]]]).
2025.06.01 16:56:25 INFO  web[][o.s.s.e.IndexCreator] Create type projectmeasures/auth
2025.06.01 16:56:25 INFO  es[][o.e.c.m.MetadataMappingService] [projectmeasures/FarWTn8eTlS-9kyIGACcsg] create_mapping [auth]
2025.06.01 16:56:25 INFO  web[][o.s.s.e.IndexCreator] Create index [rules]
2025.06.01 16:56:25 INFO  es[][o.e.c.m.MetadataCreateIndexService] [rules] creating index, cause [api], templates [], shards [2]/[0]
2025.06.01 16:56:25 INFO  es[][o.e.c.r.a.AllocationService] Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[rules][0], [rules][1]]]).
2025.06.01 16:56:26 INFO  web[][o.s.s.e.IndexCreator] Create type rules/rule
2025.06.01 16:56:26 INFO  es[][o.e.c.m.MetadataMappingService] [rules/21cguKekQke0bYi1o0M6hw] create_mapping [rule]
2025.06.01 16:56:26 INFO  web[][o.s.s.e.IndexCreator] Create index [issues]
2025.06.01 16:56:26 INFO  es[][o.e.c.m.MetadataCreateIndexService] [issues] creating index, cause [api], templates [], shards [5]/[0]
2025.06.01 16:56:26 INFO  es[][o.e.c.r.a.AllocationService] Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[issues][4]]]).
2025.06.01 16:56:26 INFO  web[][o.s.s.e.IndexCreator] Create type issues/auth
2025.06.01 16:56:26 INFO  es[][o.e.c.m.MetadataMappingService] [issues/lSQUM2noTGaVHwS3gu6vgA] create_mapping [auth]
2025.06.01 16:56:26 INFO  web[][o.s.s.e.IndexCreator] Create index [users]
2025.06.01 16:56:26 INFO  es[][o.e.c.m.MetadataCreateIndexService] [users] creating index, cause [api], templates [], shards [1]/[0]
2025.06.01 16:56:26 INFO  es[][o.e.c.r.a.AllocationService] Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[users][0]]]).
2025.06.01 16:56:26 INFO  web[][o.s.s.e.IndexCreator] Create type users/user
2025.06.01 16:56:26 INFO  es[][o.e.c.m.MetadataMappingService] [users/BAidncMwS3KqaD8CYbphpg] create_mapping [user]
2025.06.01 16:56:26 INFO  web[][o.s.s.e.IndexCreator] Create index [views]
2025.06.01 16:56:26 INFO  es[][o.e.c.m.MetadataCreateIndexService] [views] creating index, cause [api], templates [], shards [5]/[0]
2025.06.01 16:56:26 INFO  es[][o.e.c.r.a.AllocationService] Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[views][4]]]).
2025.06.01 16:56:26 INFO  web[][o.s.s.e.IndexCreator] Create type views/view
2025.06.01 16:56:26 INFO  es[][o.e.c.m.MetadataMappingService] [views/NMREQ5XPRhSFLD03zOlNqA] create_mapping [view]
2025.06.01 16:56:27 INFO  web[][o.s.s.s.LogServerId] Server ID: 9B767396-AZcsOBRKEajcHBulmcR7
2025.06.01 16:56:27 WARN  web[][o.s.s.a.LogOAuthWarning] For security reasons, OAuth authentication should use HTTPS. You should set the property 'Administration > Configuration > Server base URL' to a HTTPS URL.
2025.06.01 16:56:27 INFO  web[][o.s.s.p.UpdateCenterClient] Update center: https://update.sonarsource.org/update-center.properties
2025.06.01 16:56:29 WARN  web[][o.s.a.s.w.WebService$Action] The response example is not set on action saml/validation_init
2025.06.01 16:56:29 WARN  web[][o.s.a.s.w.WebService$Action] The response example is not set on action api/system/liveness
2025.06.01 16:56:29 WARN  web[][o.s.a.s.w.WebService$Action] The response example is not set on action api/plugins/download
2025.06.01 16:56:29 WARN  web[][o.s.a.s.w.WebService$Action] The response example is not set on action api/analysis_cache/get
2025.06.01 16:56:29 WARN  web[][o.s.a.s.w.WebService$Action] The response example is not set on action api/alm_integrations/check_pat
2025.06.01 16:56:29 WARN  web[][o.s.a.s.w.WebService$Action] The response example is not set on action api/push/sonarlint_events
2025.06.01 16:56:29 INFO  web[][o.s.s.n.NotificationDaemon] Notification service started (delay 60 sec.)
2025.06.01 16:56:29 INFO  web[][o.s.s.a.p.ExpiredSessionsCleaner] Purge of expired session tokens has removed 0 elements
2025.06.01 16:56:29 INFO  web[][o.s.s.a.p.ExpiredSessionsCleaner] Purge of expired SAML message ids has removed 0 elements
2025.06.01 16:56:29 INFO  web[][o.s.s.t.TelemetryDaemon] Sharing of SonarQube statistics is enabled.
2025.06.01 16:56:30 INFO  web[][o.s.s.s.GeneratePluginIndex] Generate scanner plugin index
2025.06.01 16:56:30 INFO  web[][o.s.s.s.RegisterPermissionTemplates] Register permission templates
2025.06.01 16:56:30 INFO  web[][o.s.s.s.RenameDeprecatedPropertyKeys] Rename deprecated property keys
2025.06.01 16:56:30 INFO  web[][o.s.s.s.RegisterPlugins] Register plugins
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.platform.web.SonarLintConnectionFilter@4c88cd6c [pattern=UrlPattern{inclusions=[/api/*], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.platform.web.WebServiceFilter@77b01e7b [pattern=UrlPattern{inclusions=[/api/issues/delete_comment.*, ...], exclusions=[/api/authentication/login.*, ...]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.platform.web.WebServiceReroutingFilter@37b9ffc1 [pattern=UrlPattern{inclusions=[/api/components/bulk_update_key, ...], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.authentication.DefaultAdminCredentialsVerifierFilter@477b1da9 [pattern=UrlPattern{inclusions=[/*], exclusions=[*.css, ...]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.authentication.InitFilter@4d125b87 [pattern=UrlPattern{inclusions=[/sessions/init/*], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.authentication.SamlValidationRedirectionFilter@3aa6c798 [pattern=UrlPattern{inclusions=[/oauth2/callback/saml], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.authentication.OAuth2CallbackFilter@421970fa [pattern=UrlPattern{inclusions=[/oauth2/callback/*], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.authentication.ResetPasswordFilter@5d10ab45 [pattern=UrlPattern{inclusions=[/*], exclusions=[*.css, ...]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.authentication.ws.LoginAction@70bfd4ab [pattern=UrlPattern{inclusions=[/api/authentication/login], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.authentication.ws.LogoutAction@486b6cbb [pattern=UrlPattern{inclusions=[/api/authentication/logout], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.authentication.ws.ValidateAction@459b0df3 [pattern=UrlPattern{inclusions=[/api/authentication/validate], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.saml.ws.ValidationInitAction@72af9b7 [pattern=UrlPattern{inclusions=[/saml/validation_init], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.saml.ws.ValidationAction@26a0a85d [pattern=UrlPattern{inclusions=[/saml/validation], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.user.ws.ChangePasswordAction@2810d03 [pattern=UrlPattern{inclusions=[/api/users/change_password], exclusions=[]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.p.w.MasterServletFilter] Initializing servlet filter org.sonar.server.plugins.PluginsRiskConsentFilter@e1790cc [pattern=UrlPattern{inclusions=[/*], exclusions=[*.css, ...]}]
2025.06.01 16:56:30 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [rules/rule/activeRule]...
2025.06.01 16:56:32 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [rules/rule/activeRule] done | time=2177ms
2025.06.01 16:56:32 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [rules/rule]...
2025.06.01 16:56:42 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [rules/rule] done | time=10115ms
2025.06.01 16:56:42 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [users/user]...
2025.06.01 16:56:42 INFO  es[][o.e.c.s.IndexScopedSettings] updating [index.refresh_interval] from [30s] to [-1]
2025.06.01 16:56:42 INFO  es[][o.e.c.s.IndexScopedSettings] updating [index.refresh_interval] from [30s] to [-1]
2025.06.01 16:56:42 INFO  es[][o.e.c.s.IndexScopedSettings] updating [index.refresh_interval] from [-1] to [30s]
2025.06.01 16:56:42 INFO  es[][o.e.c.s.IndexScopedSettings] updating [index.refresh_interval] from [-1] to [30s]
2025.06.01 16:56:42 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [users/user] done | time=345ms
2025.06.01 16:56:42 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [projectmeasures/auth/projectmeasure]...
2025.06.01 16:56:43 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [projectmeasures/auth/projectmeasure] done | time=284ms
2025.06.01 16:56:43 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [components/auth/component]...
2025.06.01 16:56:43 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [components/auth/component] done | time=152ms
2025.06.01 16:56:43 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [views/view]...
2025.06.01 16:56:43 INFO  es[][o.e.c.s.IndexScopedSettings] updating [index.refresh_interval] from [30s] to [-1]
2025.06.01 16:56:43 INFO  es[][o.e.c.s.IndexScopedSettings] updating [index.refresh_interval] from [30s] to [-1]
2025.06.01 16:56:43 INFO  es[][o.e.c.s.IndexScopedSettings] updating [index.refresh_interval] from [-1] to [30s]
2025.06.01 16:56:43 INFO  es[][o.e.c.s.IndexScopedSettings] updating [index.refresh_interval] from [-1] to [30s]
2025.06.01 16:56:43 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of type [views/view] done | time=185ms
2025.06.01 16:56:43 INFO  web[][o.s.s.e.IndexerStartupTask] Trigger asynchronous indexing of type [issues/auth/issue]...
2025.06.01 16:56:43 INFO  web[][o.s.s.i.i.AsyncIssueIndexingImpl] 0 pending indexation task found to be deleted...
2025.06.01 16:56:43 INFO  web[][o.s.s.i.i.AsyncIssueIndexingImpl] 0 completed indexation task found to be deleted...
2025.06.01 16:56:43 INFO  web[][o.s.s.i.i.AsyncIssueIndexingImpl] Indexation task deletion complete.
2025.06.01 16:56:43 INFO  web[][o.s.s.i.i.AsyncIssueIndexingImpl] Deleting tasks characteristics...
2025.06.01 16:56:43 INFO  web[][o.s.s.i.i.AsyncIssueIndexingImpl] Tasks characteristics deletion complete.
2025.06.01 16:56:43 INFO  web[][o.s.s.i.i.AsyncIssueIndexingImpl] 1 branch found in need of issue sync.
2025.06.01 16:56:43 INFO  web[][o.s.s.i.i.AsyncIssueIndexingImpl] 1 projects found in need of issue sync.
2025.06.01 16:56:43 INFO  web[][o.s.s.e.IndexerStartupTask] Trigger asynchronous indexing of type [issues/auth/issue] done | time=107ms
2025.06.01 16:56:43 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of types [components/auth],[projectmeasures/auth],[issues/auth]...
2025.06.01 16:56:44 INFO  web[][o.s.s.e.IndexerStartupTask] Indexing of types [components/auth],[projectmeasures/auth],[issues/auth] done | time=394ms
2025.06.01 16:56:44 INFO  web[][o.s.s.q.ProjectsInWarningDaemon] Counting number of projects in warning is not started as there are no projects in this situation.
2025.06.01 16:56:44 INFO  web[][o.s.s.p.p.PlatformLevelStartup] Running Community Edition
2025.06.01 16:56:44 INFO  app[][o.s.a.SchedulerImpl] Process[web] is up
2025.06.01 16:56:44 INFO  app[][o.s.a.ProcessLauncherImpl] Launch process[COMPUTE_ENGINE] from [/opt/sonarqube]: /opt/java/openjdk/bin/java -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djava.io.tmpdir=/opt/sonarqube/temp -XX:-OmitStackTraceInFastThrow --add-opens=java.base/java.util=ALL-UNNAMED --add-exports=java.base/jdk.internal.ref=ALL-UNNAMED --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.nio=ALL-UNNAMED --add-opens=java.base/sun.nio.ch=ALL-UNNAMED --add-opens=java.management/sun.management=ALL-UNNAMED --add-opens=jdk.management/com.sun.management.internal=ALL-UNNAMED -Dcom.redhat.fips=false -Xmx512m -Xms128m -XX:+HeapDumpOnOutOfMemoryError -Dhttp.nonProxyHosts=localhost|127.*|[::1] -cp ./lib/sonar-application-9.9.8.100196.jar:/opt/sonarqube/lib/jdbc/postgresql/postgresql-42.5.1.jar org.sonar.ce.app.CeServer /opt/sonarqube/temp/sq-process3145273551063693591properties
2025.06.01 16:56:44 INFO  web[][o.s.s.p.Platform] Web Server is operational
WARNING: A terminally deprecated method in java.lang.System has been called
WARNING: System::setSecurityManager has been called by org.sonar.process.PluginSecurityManager (file:/opt/sonarqube/lib/sonar-application-9.9.8.100196.jar)
WARNING: Please consider reporting this to the maintainers of org.sonar.process.PluginSecurityManager
WARNING: System::setSecurityManager will be removed in a future release
2025.06.01 16:56:45 INFO  ce[][o.s.p.ProcessEntryPoint] Starting Compute Engine
2025.06.01 16:56:45 INFO  ce[][o.s.ce.app.CeServer] Compute Engine starting up...
2025.06.01 16:56:45 INFO  ce[][o.sonar.db.Database] Create JDBC data source for jdbc:postgresql://sonarqube-db:5432/sonar
2025.06.01 16:56:45 INFO  ce[][c.z.h.HikariDataSource] HikariPool-1 - Starting...
2025.06.01 16:56:45 INFO  ce[][c.z.h.p.HikariPool] HikariPool-1 - Added connection org.postgresql.jdbc.PgConnection@5c9a8187
2025.06.01 16:56:45 INFO  ce[][c.z.h.HikariDataSource] HikariPool-1 - Start completed.
2025.06.01 16:56:46 INFO  ce[][o.s.s.p.ServerFileSystemImpl] SonarQube home: /opt/sonarqube
2025.06.01 16:56:47 INFO  ce[][o.s.c.c.CePluginRepository] Load plugins
2025.06.01 16:56:48 INFO  ce[][o.s.c.c.ComputeEngineContainerImpl] Running Community edition
2025.06.01 16:56:48 INFO  ce[][o.s.ce.app.CeServer] Compute Engine is started
2025.06.01 16:56:48 INFO  app[][o.s.a.SchedulerImpl] Process[ce] is up
2025.06.01 16:56:48 INFO  app[][o.s.a.SchedulerImpl] SonarQube is operational
2025.06.01 16:56:50 INFO  ce[][o.s.c.t.CeWorkerImpl] Execute task | project=rifaterdemsahin_SonarQubeCourse_AZcsPUc8EajcHBulmmLO | type=ISSUE_SYNC | branch=main | branchType=BRANCH | id=AZcsbJdwi3W1qxuL7iAJ
2025.06.01 16:56:50 INFO  ce[AZcsbJdwi3W1qxuL7iAJ][o.s.c.t.s.ComputationStepExecutor] Ignore orphan component | status=SUCCESS | time=2ms
2025.06.01 16:56:50 INFO  ce[AZcsbJdwi3W1qxuL7iAJ][o.s.s.e.EsClientProvider] Connected to local Elasticsearch: [http://localhost:9001]
2025.06.01 16:56:51 INFO  ce[AZcsbJdwi3W1qxuL7iAJ][o.s.c.t.p.t.IndexIssuesStep] indexing issues of branch AZcsPUc_EajcHBulmmLP
2025.06.01 16:56:52 INFO  ce[AZcsbJdwi3W1qxuL7iAJ][o.s.c.t.s.ComputationStepExecutor] index issues | status=SUCCESS | time=1322ms
2025.06.01 16:56:52 INFO  ce[AZcsbJdwi3W1qxuL7iAJ][o.s.c.t.CeWorkerImpl] Executed task | project=rifaterdemsahin_SonarQubeCourse_AZcsPUc8EajcHBulmmLO | type=ISSUE_SYNC | branch=main | branchType=BRANCH | id=AZcsbJdwi3W1qxuL7iAJ | status=SUCCESS | time=1881ms
---- Logs from pod: sonarqube-db-778f999cd5-k6fn6 ----

PostgreSQL Database directory appears to contain a database; Skipping initialization

2025-06-01 16:55:22.857 UTC [1] LOG:  starting PostgreSQL 13.21 (Debian 13.21-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
2025-06-01 16:55:22.858 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2025-06-01 16:55:22.858 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2025-06-01 16:55:22.860 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2025-06-01 16:55:22.873 UTC [27] LOG:  database system was interrupted; last known up at 2025-06-01 16:51:59 UTC
2025-06-01 16:55:23.036 UTC [27] LOG:  database system was not properly shut down; automatic recovery in progress
2025-06-01 16:55:23.039 UTC [27] LOG:  redo starts at 0/295F2E8
2025-06-01 16:55:23.050 UTC [27] LOG:  invalid record length at 0/2965988: wanted 24, got 0
2025-06-01 16:55:23.050 UTC [27] LOG:  redo done at 0/2965950
2025-06-01 16:55:23.089 UTC [1] LOG:  database system is ready to accept connections
@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ 

---

The output shows a Kubernetes setup with Minikube running a SonarQube deployment, but there are issues causing instability, particularly with the SonarQube pod (sonarqube-55b9ff9c79-nkrxh). Here's a breakdown of the problem and potential solutions:
Issue Summary
Pod Restarts and Failures:
The SonarQube pod (sonarqube-55b9ff9c79-nkrxh) has restarted 4 times, and the database pod (sonarqube-db-778f999cd5-k6fn6) has restarted twice.
Events indicate liveness and readiness probe failures for the SonarQube pod:
Readiness probe failed: Get "http://10.244.0.7:9000/": context deadline exceeded (Client.Timeout exceeded while awaiting headers).
Liveness probe failed: Get "http://10.244.0.7:9000/": read tcp 10.244.0.1:53402->10.244.0.7:9000: read: connection reset by peer.
These failures suggest that the SonarQube web server is not responding on port 9000 as expected, causing Kubernetes to restart the pod.
Pod Sandbox Issues:
Both pods experienced a SandboxChanged event, indicating that the pod sandbox was killed and re-created, which could be related to networking or container runtime issues in Minikube.
Database Pod Issues:
The database pod (sonarqube-db-778f999cd5-k6fn6) terminated with exit code 137 (out-of-memory error) in its last state, indicating possible resource constraints.
The logs show the PostgreSQL database recovering from an improper shutdown, which may indicate instability or resource issues.
Resource Constraints:
The SonarQube pod has CPU/memory limits of 2 CPU/4Gi and requests of 1 CPU/2Gi. The database pod has limits of 1 CPU/2Gi and requests of 0.5 CPU/1Gi.
The Minikube node has limited resources (7.9GB usable disk space), and exit code 137 suggests the database pod may have been killed due to memory pressure.
SonarQube Logs:
The SonarQube pod logs show the application starting, connecting to Elasticsearch and PostgreSQL, and initializing indices. However, the liveness/readiness probe failures indicate the web server is not fully operational or is slow to respond.
Warnings about deprecated System::setSecurityManager calls and OAuth authentication needing HTTPS are present but likely not critical to the issue.
Root Causes
Liveness/Readiness Probe Failures: The SonarQube web server (port 9000) is not responding within the configured probe timeouts (1s timeout, 30s period). This could be due to:
Slow startup of the SonarQube application, especially with resource constraints.
Network issues within Minikube (e.g., CNI plugin problems causing SandboxChanged).
Incorrect probe configuration (e.g., insufficient delay or timeout).
Resource Issues: The database pod's exit code 137 suggests it ran out of memory, likely due to insufficient resources allocated to Minikube or the pod's memory limit being too restrictive.
Minikube Environment: Running in a resource-constrained environment (e.g., Codespaces or a low-memory VM) could exacerbate these issues, especially with SandboxChanged events indicating potential container runtime or networking instability.
Recommended Fixes
Adjust Liveness/Readiness Probes:
SonarQube can take time to start, especially with limited resources. Increase the probe timeouts and initial delays:
yaml
livenessProbe:
  httpGet:
    path: /
    port: 9000
  initialDelaySeconds: 180  # Increase from 120s
  timeoutSeconds: 5        # Increase from 1s
  periodSeconds: 30
  failureThreshold: 5      # Increase from 3
readinessProbe:
  httpGet:
    path: /
    port: 9000
  initialDelaySeconds: 120  # Increase from 60s
  timeoutSeconds: 5        # Increase from 1s
  periodSeconds: 30
  failureThreshold: 5      # Increase from 3
Apply the updated configuration using kubectl apply -f <your-deployment-file>.yaml.
Increase Resource Limits:
The database pod's exit code 137 indicates memory issues. Increase its memory limit/request:
yaml
resources:
  limits:
    cpu: "1"
    memory: "3Gi"  # Increase from 2Gi
  requests:
    cpu: "500m"
    memory: "2Gi"  # Increase from 1Gi
Similarly, consider increasing the SonarQube pod's memory limit if it continues to struggle:
yaml
resources:
  limits:
    cpu: "2"
    memory: "6Gi"  # Increase from 4Gi
  requests:
    cpu: "1"
    memory: "3Gi"  # Increase from 2Gi
Check Minikube Resources:
Ensure Minikube has sufficient resources. Check the VM's allocated CPU/memory:
bash
minikube config view
If running in a constrained environment (e.g., Codespaces), increase Minikube's resources:
bash
minikube stop
minikube config set memory 8192  # 8GB
minikube config set cpus 4       # 4 CPUs
minikube start
Verify disk space:
bash
df -h
Ensure the Minikube VM has enough disk space (current usable space is 7.9GB, which is low).
Investigate Networking Issues:
The SandboxChanged events suggest issues with the container runtime or CNI plugin. Ensure Minikube's networking is stable:
bash
minikube ssh
docker ps  # Check container runtime
If using a specific CNI plugin (e.g., Flannel, Calico), verify its status:
bash
kubectl get pods -n kube-system
Consider resetting the network stack:
bash
minikube stop
minikube delete
minikube start
Verify Database Connectivity:
Ensure the SonarQube pod can reach the database (sonarqube-db:5432). Check the service configuration:
bash
kubectl get svc -n sonarqube
Test connectivity from the SonarQube pod:
bash
kubectl exec -n sonarqube sonarqube-55b9ff9c79-nkrxh -- ping sonarqube-db
kubectl exec -n sonarqube sonarqube-55b9ff9c79-nkrxh -- nc -zv sonarqube-db 5432
If connectivity fails, check DNS or service routing in Minikube.
Check SonarQube Logs for Errors:
The provided logs look normal, but monitor for additional errors after applying fixes:
bash
kubectl logs -n sonarqube sonarqube-55b9ff9c79-nkrxh --tail 100
Look for database connection errors or Elasticsearch issues.
Update Minikube:
The output shows Minikube 1.36.0 is available. Update to the latest version to rule out bugs:
bash
minikube stop
minikube delete
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
minikube start
Disable Update Notification (Optional):
To suppress the Minikube update notification:
bash
minikube config set WantUpdateNotification false
Next Steps
Apply the probe and resource changes to the SonarQube and database deployments.
Restart the pods:
bash
kubectl delete pod -n sonarqube sonarqube-55b9ff9c79-nkrxh sonarqube-db-778f999cd5-k6fn6
Monitor pod status and logs:
bash
kubectl get pods -n sonarqube -w
kubectl logs -n sonarqube sonarqube-55b9ff9c79-nkrxh --follow
If issues persist, check Minikube logs for deeper insight:
bash
minikube logs
Additional Notes
The global variables comment (# Global variables (tech debt: should avoid globals)) suggests a script or configuration issue unrelated to the Kubernetes setup. If this is part of a larger script, ensure variables are properly scoped to avoid side effects.
The HTTPS warning for OAuth can be ignored unless you plan to enable OAuth authentication, in which case configure a secure server base URL in SonarQube.
If you need help with specific steps (e.g., editing YAML files, debugging logs), please provide more details or the relevant configuration files.