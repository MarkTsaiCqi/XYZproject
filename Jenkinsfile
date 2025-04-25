pipeline {
  agent any

  environment {
    SELENIUM_REMOTE_URL = "http://mark-i7:4444/wd/hub"
  }

  stages {
    stage('Run Tests') {
      steps {
        echo '🔍 Running tests on remote Selenium Grid...'
        sh './run-tests.sh'
      }
    }

    stage('Publish HTML Report') {
      steps {
        echo '📄 Publishing pytest HTML report...'
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
