pipeline {
  agent any

  environment {
    SELENIUM_REMOTE_URL = "http://mark-i7:4444/wd/hub"
  }

  stages {
    stage('Run in Docker Agent') {
      steps {
        script {
          docker.image('marktw75/xyzproject-runner:latest').inside {
            sh './run-tests.sh'
          }
        }
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
