## install Jenkins instance on Kubernetes
(based on this page: [Install Jenkins using helm](https://argo-cd.readthedocs.io/en/stable/getting_started/](https://sweetcode.io/how-to-setup-jenkins-ci-cd-pipeline-on-kubernetes-cluster-with-helm/))

### Requirements
- Installed kubectl command-line tool.
- Connected to a Kubernetes cluster - Have a kubeconfig file (default location is ~/.kube/config).
- Install helm.
 
### Install Argo CD
```
sudo apt install helm
```
Add jenkins to your helm repo:
```
helm repo add jenkins https://charts.jenkins.io
```

Update your repo:
```
helm repo update
```

Install the official jenkins package:
```
helm install myjenkins jenkins/jenkins
```

Get the password:
```
kubectl get secret --namespace default myjenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode```

Get the loadbalancer ip:
```
kubectl get svc --namespace=...('default' is the default namespace for the installation) 
```

Go to the website where the IP is the external-service-IP of the 'Jenkins' service with port 8080

Login to jenkins using the username: 'admin' and and the above password
