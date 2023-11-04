pipeline {
    agent any
    stages{
        stage('Build docker image'){
            steps{
                script{
                    sh 'docker stop counter-app || true && docker rm counter-app || true' // Stop and remove container if running
                    sh 'docker image prune' // Remove the previously built image
                    sh 'docker build -t counter-app .' // Build the new version
                }
            }
        }
        stage('Deploy container'){
            steps{
                script{
                    sh 'docker run --name counter-app --restart unless-stopped -dp 80:80 counter-app'
                }
            }
        }
        stage('Test URL Availability') {
            steps {
                script {
                    def url = 'http://ec2-52-57-150-144.eu-central-1.compute.amazonaws.com/'
                    def response = sh(script: "curl --write-out '%{http_code}' --silent --output /dev/null ${url}", returnStdout: true)

                    if (response != "200") {
                        currentBuild.result = 'FAILURE'
                        error("URL ${url} is unavailable (HTTP status code: ${response})")
                    }
                }
            }
        }
    }
}