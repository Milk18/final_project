pipeline {
    agent {
        kubernetes {
            label 'dind-agent'
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: dind
    image: milk49/dind:latest
    env:
    - name: DOCKER_HOST
      value: unix:///var/run/docker-dind.sock
    securityContext:
      privileged: true
    volumeMounts:
    - mountPath: /var/run
      name: docker-sock
  volumes:
  - name: docker-sock
    emptyDir: {}
"""
        }
    }
    stages {
         stage ('Run app') {
      steps {
        sh 'python3 flaskapp/main.py &'
      }
    }
    stage ('test app') {
      steps {
        sh 'pytest flaskapp/test.py'
      }
    }
        stage('Build and Push Docker Image') {
             when {
                changeset 'main.py'
            }
            steps {
                container('dind') {
                    script {
                        sh 'dockerd &'
                        sh 'sleep 5'
                        sh 'docker build -t milk49/profile-app:latest .'
                        withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                            sh '''
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            docker push milk49/profile-app:latest
                            '''
                        }
                    }
                }
            }
        }
    }
}
