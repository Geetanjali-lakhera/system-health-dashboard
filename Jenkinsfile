pipeline {
    agent any

    environment {
        IMAGE_NAME = "system-health-dashboard"
        IMAGE_TAG = "build-${BUILD_NUMBER}"
        CONTAINER_NAME = "jenkins-health-check-${BUILD_NUMBER}"
        NETWORK_NAME = "jenkins-net"
    }

    stages {

        stage('Install') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    ./venv/bin/python -m pytest -v
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Tag') {
            steps {
                sh '''
                    docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    docker network inspect ${NETWORK_NAME} >/dev/null 2>&1 || \
                    docker network create ${NETWORK_NAME}

                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        --network ${NETWORK_NAME} \
                        -e ENVIRONMENT=production \
                        ${IMAGE_NAME}:${IMAGE_TAG}

                    sleep 5

                    curl --fail \
                        http://${CONTAINER_NAME}:5000/health
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