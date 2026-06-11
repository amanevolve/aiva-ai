pipeline {
    agent any

    // These environment variables will be pulled from Jenkins settings
    environment {
        DOCKER_IMAGE_FRONTEND = "${env.DOCKER_USERNAME}/aiva-frontend:latest"
        DOCKER_IMAGE_BACKEND = "${env.DOCKER_USERNAME}/aiva-backend:latest"
        APP_DIR = "/home/ubuntu/aiva-ai"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "📥 Pulling latest code from repository..."
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                echo "📦 Building Aiva Frontend and Backend images..."
                script {
                    docker.build("${DOCKER_IMAGE_FRONTEND}", "./frontend")
                    docker.build("${DOCKER_IMAGE_BACKEND}", "./backend")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo "☁️ Pushing images to Docker Hub..."
                // Requires a credential in Jenkins named 'dockerhub-credentials'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                    sh "docker push ${DOCKER_IMAGE_FRONTEND}"
                    sh "docker push ${DOCKER_IMAGE_BACKEND}"
                }
            }
        }

        stage('Deploy to App Server') {
            steps {
                echo "🚀 Deploying to AWS EC2 Instance..."
                // Requires an SSH credential in Jenkins named 'app-server-ssh-key'
                sshagent(['app-server-ssh-key']) {
                    // SSH into the server, pull the fresh images, and restart containers
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@${env.APP_SERVER_IP} '
                        cd ${APP_DIR} &&
                        docker compose pull &&
                        docker compose up -d
                    '
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully! Aiva is live."
        }
        failure {
            echo "❌ Pipeline failed. Check the Jenkins logs for details."
        }
    }
}
