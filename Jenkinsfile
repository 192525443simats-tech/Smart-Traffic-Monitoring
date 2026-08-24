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
                sh 'docker compose build'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests...'
                sh 'docker compose run --rm backend pytest'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Checking Python source code...'
                sh 'python3 -m py_compile backend/app.py'
                sh 'python3 -m py_compile backend/database.py'
                sh 'python3 -m py_compile backend/traffic_analysis.py'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging application using Docker...'
                sh 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Starting Smart Traffic Monitoring containers...'
                sh 'docker compose up -d'
            }
        }

        stage('Deployment Verification') {
            steps {
                echo 'Checking running Docker containers...'
                sh 'docker compose ps'
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
