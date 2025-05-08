pipeline {
  agent {
    docker {
      image 'marktw75/xyzproject-runner:latest'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }

  environment {
    SELENIUM_REMOTE_URL = "http://mark-i7:4444/wd/hub"
  }

  stages {
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

  post {
    always {
emailext(
      subject: " [XYZproject] 測試報告 - Build #${env.BUILD_NUMBER}",
      body: """Hi Team,

自動化測試完成，請查閱以下測試報告：

🔗 Report: ${env.BUILD_URL}Selenium_20Test_20Report/

Regards,
Jenkins
""",
      recipientProviders: [[$class: 'DevelopersRecipientProvider']],
    )
    }
  }
}
