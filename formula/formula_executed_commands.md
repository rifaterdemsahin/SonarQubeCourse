@rifaterdemsahin ➜ /workspaces/SonarQubeCourse (main) $ history
    1  sudo sysctl -w vm.max_map_count=262144
    2  sudo sysctl -w fs.file-max=65536
    3  sudo sysctl -w vm.max_map_count=262144
    4  sudo sysctl -w fs.file-max=65536
    5  # Clean up existing resources
    6  kubectl delete namespace sonarqube --ignore-not-found=true
    7  sleep 10
    8  # Clean up existing resources
    9  kubectl delete namespace sonarqube --ignore-not-found=true
   10  sleep 10
   11  # Create new namespace and secrets
   12  kubectl create namespace sonarqube
   13  kubectl create secret generic sonar-db-credentials   --namespace sonarqube   --from-literal=POSTGRES_USER=sonar   --from-literal=POSTGRES_PASSWORD=sonar123   --from-literal=POSTGRES_DB=sonar
   14  # Navigate to Symbols directory
   15  cd /workspaces/SonarQubeCourse/Symbols
   16  # Apply configurations
   17  kubectl apply -f pvc.yaml -n sonarqube
   18  sleep 5
   19  # Deploy PostgreSQL
   20  kubectl apply -f deployment_postgresql.yaml -n sonarqube
   21  kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s
   22  # Deploy SonarQube
   23  kubectl apply -f deployment_server.yaml -f service_sonarqube.yaml -n sonarqube
   24  kubectl wait --for=condition=ready pod -l app=sonarqube -n sonarqube --timeout=300s
   25  # Set up port forwarding
   26  sudo sysctl -w vm.max_map_count=262144 && sudo sysctl -w fs.file-max=65536
   27  kubectl delete namespace sonarqube --ignore-not-found=true && sleep 10 && kubectl create namespace sonarqube && kubectl create secret generic sonar-db-credentials --namespace sonarqube --from-literal=POSTGRES_USER=sonar --from-literal=POSTGRES_PASSWORD=sonar123 --from-literal=POSTGRES_DB=sonar
   28  cd /workspaces/SonarQubeCourse/Symbols && kubectl apply -f pvc.yaml -n sonarqube && sleep 5 && kubectl apply -f deployment_postgresql.yaml -n sonarqube && echo "Waiting for PostgreSQL to be ready..." && kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s
   29  kubectl delete namespace sonarqube --ignore-not-found=true && sleep 10 && kubectl create namespace sonarqube && kubectl create secret generic sonar-db-credentials --namespace sonarqube --from-literal=POSTGRES_USER=sonar --from-literal=POSTGRES_PASSWORD=sonar123 --from-literal=POSTGRES_DB=sonar
   30  minikube status
   31  minikube start --memory=16096 --cpus=6
   32  minikube start --memory=16096 --cpus=6 --addons=storage-provisioner
   33  sudo sysctl -w vm.max_map_count=262144 && sudo sysctl -w fs.file-max=65536
   34  kubectl delete namespace sonarqube --ignore-not-found=true && sleep 10 && kubectl create namespace sonarqube
   35  kubectl create secret generic sonar-db-credentials   --namespace sonarqube   --from-literal=POSTGRES_USER=sonar   --from-literal=POSTGRES_PASSWORD=sonar123   --from-literal=POSTGRES_DB=sonar
   36  cd /workspaces/SonarQubeCourse/Symbols && kubectl apply -f pvc.yaml -n sonarqube && sleep 5
   37  kubectl apply -f deployment_postgresql.yaml -n sonarqube && echo "Waiting for PostgreSQL to be ready..." && kubectl wait --for=condition=ready pod -l app=sonarqube-db -n sonarqube --timeout=120s
   38  kubectl apply -f deployment_server.yaml -f service_sonarqube.yaml -n sonarqube && echo "Waiting for SonarQube to be ready..." && kubectl wait --for=condition=ready pod -l app=sonarqube -n sonarqube --timeout=300s
   39  kubectl apply -f github-secrets.yaml -f github-integration.yaml -n sonarqube
   40  htop
   41  ls -l /workspaces/SonarQubeCourse/Symbols/scanfiles.py
   42  ls -la /workspaces/SonarQubeCourse/Symbols/
   43  cd /workspaces/SonarQubeCourse/Symbols && python -m pytest --cov=. --cov-report=xml tests/
   44  pip install pytest pytest-cov
   45  cd /workspaces/SonarQubeCourse/Symbols && python -m pytest --cov=. --cov-report=xml tests/
   46  pip install -r requirements.txt
   47  python -m pytest /workspaces/SonarQubeCourse/Symbols/tests/scanfiles_test.py -v
   48  python -m pytest --cov=/workspaces/SonarQubeCourse/Symbols/scanfiles.py --cov-report=xml /workspaces/SonarQubeCourse/Symbols/tests/scanfiles_test.py -v
   49  cd /workspaces/SonarQubeCourse/Symbols && PYTHONPATH=/workspaces/SonarQubeCourse/Symbols python -m pytest tests/scanfiles_test.py --cov=. --cov-report=xml -v
   50  cd /workspaces/SonarQubeCourse && python -m pytest Symbols/tests/scanfiles_test.py --cov=Symbols --cov-report=xml
   51  pwd && ls -la coverage.xml Symbols/coverage.xml
   52  cd /workspaces/SonarQubeCourse && python -m pytest Symbols/tests/scanfiles_test.py --cov=Symbols --cov-report=xml
   53  cd /workspaces/SonarQubeCourse/Symbols && python -m pytest tests/scanfiles_test.py --cov=. --cov-config=.coveragerc --cov-report=xml
   54  cd /workspaces/SonarQubeCourse/Symbols && python -m pytest tests/scanfiles_test.py -v
   55  cd /workspaces/SonarQubeCourse && tree -a -I ".git"
   56  sudo apt-get update && sudo apt-get install -y tree
   57  history