## install Jenkins instance on Kubernetes
(based on this page: [Install Jenkins using helm](https://argo-cd.readthedocs.io/en/stable/getting_started/](https://sweetcode.io/how-to-setup-jenkins-ci-cd-pipeline-on-kubernetes-cluster-with-helm/))

### Requirements
- Installed kubectl command-line tool.
- Connected to a Kubernetes cluster - Have a kubeconfig file (default location is ~/.kube/config).
- Install helm.
 
### Install Jenkins
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
kubectl get secret --namespace default myjenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode
```
Get the LoadBalancer ip:
```
kubectl get svc --namespace=...('default' is the default namespace for the installation) 
```

Go to the website where the IP is the external-service-IP of the 'Jenkins' service with port 8080

Login to jenkins using the username: 'admin' and the above password.

Install the suggested plugins and follow the given instructions.

### Install plugins

![plot](../images/jenkinsplugin.png)

Click on "Manage Jenkins" on the left side. \
Click on the "Plugins" section. \
Go to "Available plugins". \
Search for: 'Blue Ocean', 'Docker plugin', 'Docker', 'Kubernetes plugin', 'Pipeline' \
note that the multibranch workflow plugin is not supported anymore, and we now need to use the 
'Multibranch Pipeline' job type.

### Create pipeline job
In the Dashboard, click "+ New Item" \
Select 'Multibranch Pipeline', give a name, and click 'ok'. \
Give it a display name and description as you like. \
Under 'Branch Sources' select git. \
Enter this project url repo, and put the credentials we configured earlier.


