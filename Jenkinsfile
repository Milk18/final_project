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
        bat 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'
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
