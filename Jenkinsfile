pipeline {
    agent any
    stages{
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker build -t counter-app .'
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