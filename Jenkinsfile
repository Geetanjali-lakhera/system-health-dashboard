pipeline {
    agent any

    environment {
        IMAGE_NAME = "system-health-dashboard"
        IMAGE_TAG = "build-${BUILD_NUMBER}"
        CONTAINER_NAME = "jenkins-health-check-${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Tag') {
            steps {
                sh 'docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest'
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    docker run -d \
                      --name ${CONTAINER_NAME} \
                      -p 5001:5000 \
                      -e ENVIRONMENT=production \
                      ${IMAGE_NAME}:${IMAGE_TAG}

                    sleep 5

                    curl --fail http://localhost:5001/health
                '''
            }
        }
    }

    post {
        always {
            sh '''
                docker logs ${CONTAINER_NAME} || true
                docker stop ${CONTAINER_NAME} || true
                docker rm ${CONTAINER_NAME} || true
            '''
        }

        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the stage logs above.'
        }
    }
}
