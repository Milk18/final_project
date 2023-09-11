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
        bat 'def username = DOCKERHUB_CREDENTIALS_USR'
        bat 'def password = DOCKERHUB_CREDENTIALS_PSW'
        bat "echo ${password} | docker login -u ${username} --password-stdin"
      }
    }
    stage('Push') {
      steps {
        bat 'docker push milk49/jenkins-docker-hub:1.0'
      }
    }
  }
  post {
    always {
      bat'docker logout'
    }
  }
}
