pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'profile'
    }

    stages {
        stage('Checkout') {
            steps {
                // Check out your code from the repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build a Docker image from your Flask code
                    docker.build(env.DOCKER_IMAGE_NAME)
                }
            }
        }

        stage('Run pytest') {
            steps {
                script {
                    // Run pytest inside the Docker container
                    docker.image(env.DOCKER_IMAGE_NAME).inside {
                        // Install pytest and any other dependencies
                        sh 'pip install pytest'
                        
                        // Run pytest
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            when {
                // Define conditions for when to push the Docker image (optional)
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    // Push the Docker image to a container registry (e.g., Docker Hub)
                    docker.withRegistry('https://registry.example.com', 'your-registry-credentials') {
                        docker.image(env.DOCKER_IMAGE_NAME).push()
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up (optional)
            cleanWs()
            docker.image(env.DOCKER_IMAGE_NAME).remove()
        }
    }
}
