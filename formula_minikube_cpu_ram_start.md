minikube stop && \
minikube config set memory 8192 && \
minikube config set cpus 4 && \
minikube start
minikube config view
kubectl get pods -n sonarqube -w
kubectl logs -f deployment/sonarqube -n sonarqube
