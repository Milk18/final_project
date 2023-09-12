pipeline {
  agent {label 'win32'}
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    $env:DOCKERHUB_CREDENTIALS = credentials('dockerhub')
  }
  stages {
    stage ('Run app') {
      steps {
        bat 'start /B python C:/jenkins/workspace/test/flaskapp/main.py'
      }
    }
    stage ('test app') {
      steps {
        bat 'pytest C:/jenkins/workspace/test/flaskapp/test.py'
      }
    }
    stage('Build') {
      steps {
        bat 'docker build -t milk49/jenkins-docker-hub:1.0 .'
      }
    }
    stage('Login') {
      steps {
        bat 'docker login -u \"%DOCKERHUB_CREDENTIALS_USR%\" -p \"%DOCKERHUB_CREDENTIALS_PSW%\"'
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
