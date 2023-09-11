pipeline {
  agent {label 'win32'}
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub')
  }
  stages {
    stage('Build') {
      steps {
        bat 'docker build -t milk49/jenkins-docker-hub:1.0 .'
      }
    }
    stage('Login') {
      steps {
        bat 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u milk49 -p milk12345678'
      }
    }
    stage('Push') {
      steps {
        bat 'docker push milk49/jenkins-docker-hub'
      }
    }
  }
  post {
    always {
      bat'docker logout'
    }
  }
}
