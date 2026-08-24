pipeline {
    agent any

    stages {

        stage('Source Code') {
            steps {
                echo 'Checking out Smart Traffic Monitoring source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker images...'
                bat 'docker compose build'
            }
        }

        stage('Test') {
            steps {
                echo 'Running application tests...'
                bat 'docker compose run --rm backend pytest'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Checking Python source code...'

                bat 'python -m py_compile backend\\app.py'
                bat 'python -m py_compile backend\\database.py'
                bat 'python -m py_compile backend\\traffic_analysis.py'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging application using Docker...'
                bat 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting Smart Traffic Monitoring containers...'
                bat 'docker compose up -d'
            }
        }

        stage('Deployment Verification') {
            steps {
                echo 'Checking running Docker containers...'
                bat 'docker compose ps'
            }
        }
    }

    post {

        success {
            echo '=========================================='
            echo 'CI/CD Pipeline completed successfully!'
            echo 'Smart Traffic Monitoring deployed!'
            echo '=========================================='
        }

        failure {
            echo '=========================================='
            echo 'CI/CD Pipeline failed!'
            echo 'Please check the failed stage and logs.'
            echo '=========================================='
        }

        always {
            echo 'CI/CD Pipeline execution completed.'
        }
    }
}
