pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        PYTHONPATH = "${WORKSPACE}"
        VENV_PATH = "${WORKSPACE}/venv"
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    python -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest pytest-cov flake8 black isort
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo "Running Flake8..."
                    flake8 app tests
                    echo "Running Black..."
                    black --check app tests
                    echo "Running isort..."
                    isort --check-only app tests
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . ${VENV_PATH}/bin/activate
                    pytest tests/ --cov=app --cov-report=xml --cov-report=term-missing
                '''
            }
            post {
                always {
                    junit 'test-results/*.xml'
                    cobertura coberturaReportFile: 'coverage.xml'
                }
            }
        }

        stage('Build') {
            steps {
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo "Building application..."
                    # Add any build steps here if needed
                '''
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    . ${VENV_PATH}/bin/activate
                    echo "Deploying application..."
                    # Add deployment steps here
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
} 