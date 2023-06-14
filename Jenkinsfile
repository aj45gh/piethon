pipeline {
  agent any
  stages {
    stage('Checkout') {
      agent any
      steps {
        git(url: 'https://github.com/aj45gh/piethon.git', branch: 'main', credentialsId: 'github_pat')
      }
    }

  }
}