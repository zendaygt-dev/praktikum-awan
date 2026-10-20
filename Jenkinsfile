pipeline {
    agent any
    environment {
        IMAGE_NAME = 'zendaydev/praktikum-awan'
        REGISTRY_CREDENTIALS = 'credential-laprak1'
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { sh 'echo "Mulai build aplikasi"' }
        }
        stage('Build Docker Image') {
            steps { sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .' }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: REGISTRY_CREDENTIALS,
                        usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push $IMAGE_NAME:$BUILD_NUMBER'
                    sh 'docker tag $IMAGE_NAME:$BUILD_NUMBER $IMAGE_NAME:latest'
                    sh 'docker push $IMAGE_NAME:latest'
                }
            }
        }
        stage('Deploy App + Database') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up -d'
            }
        }
        stage('Test') {
            steps {
                sh 'sleep 15 && curl -f http://localhost:5000/db'
            }
        }
    }
    post { always { echo 'Selesai build' } }
}
