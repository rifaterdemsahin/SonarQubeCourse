# Install Python test dependencies first
pip install pytest pytest-cov

# Then configure and start minikube
minikube stop && \
minikube config set memory 8192 && \
minikube config set cpus 4 && \
minikube start
minikube config view
kubectl get pods -n sonarqube -w
kubectl logs -f deployment/sonarqube -n sonarqube
