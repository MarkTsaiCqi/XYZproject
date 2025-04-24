pipeline {
  agent any

  environment {
    SELENIUM_REMOTE_URL = "http://localhost:4444/wd/hub"
  }

  stages {
    stage('Start Selenium Grid + Report Server') {
      steps {
        sh 'docker-compose up -d --remove-orphans'
      }
    }

    stage('Run Tests') {
      steps {
        sh './run-tests.sh'
      }
    }

    stage('Publish HTML Report') {
      steps {
        publishHTML(target: [
          allowMissing: false,
          alwaysLinkToLastBuild: true,
          keepAll: true,
          reportDir: 'reports',
          reportFiles: 'report.html',
          reportName: 'Selenium Test Report'
        ])
      }
    }
  }

}
