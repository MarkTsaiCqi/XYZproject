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
  }

  post {
    always {
      // 無論成功或失敗都發布 report（截圖才能在 report 中看到）
      publishHTML(target: [
        allowMissing: true,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'reports',
        reportFiles: 'report.html',
        reportName: 'Selenium Test Report'
      ])
      emailext(
        subject: "[XYZproject] 測試報告 - Build #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
        body: """Hi Team,

自動化測試完成，結果：${currentBuild.currentResult}

🔗 Report: ${env.BUILD_URL}Selenium_20Test_20Report/

Regards,
Jenkins
""",
        recipientProviders: [[$class: 'DevelopersRecipientProvider']],
      )
    }
  }
}
