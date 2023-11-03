pipeline {
    agent any
    stages{
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker stop counter-app' // Stop the running container
                    sh 'docker rm counter-app' // Remove the stopped container
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