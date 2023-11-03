pipeline {
    agent any
    stages{
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker stop counter-app || true && docker rm counter-app || true' // Stop and remove container if running
                    sh 'docker image rm counter-app' // Remove the previously built image
                    sh 'docker build -t counter-app .' // Build the new version
                }
            }
        }
        stage('Deploy container'){
            steps{
                script{
                    sh 'docker run -p 80:80 counter-app'
                }
            }
        }
    }
}