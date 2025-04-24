pipeline {
  agent any

  environment {
    SELENIUM_REMOTE_URL = "http://localhost:4444/wd/hub"
  }

  stages {
    stage('Clone Repository') {
      steps {
        checkout scm
      }
    }

    stage('Start Selenium Grid + Report Server') {
      steps {
        sh 'docker-compose up -d --remove-orphans'
        sh 'sleep 5' // 稍等容器啟動穩定
      }
    }

    stage('Run Tests') {
      steps {
        sh './run-tests.sh'
      }
    }

    stage('Publish HTML Report') {
      steps {
        publishHTML([
          allowMissing: false,
          alwaysLinkToLastBuild: true,
          keepAll: true,
          reportDir: 'reports',
          reportFiles: 'report.html',
          reportName: 'Test Report'
        ])
      }
    }
  }

  post {
    always {
      echo 'Tearing down containers...'
      sh 'docker-compose down'
    }
  }
}
