pipeline {
  
  agent { label 'slave1' }
  
  stages {
    stage ( "Build") {
// Step is for building the application
      
/* This is for multiple comment syntax
entering second line of comment */
      steps {
        echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
        echo 'Building the application...'
      }
      
    }
    
    stage ( "Test") {
      
      steps {
        echo 'Testing the application...'
        sh '''#!/bin/bash

                    echo "Hello from bash"
                    echo "Who I'm $SHELL"
                    pwd
                    ls
                 
                 '''
      }
      
    }
    
    stage ( "Deploy") {
      
      steps {
        echo 'Deploying the application...'
      }
      
    }
    post {
        always {
            sh 'sudo rm -rf *@tmp'
            cleanWs()
        }
    }
    
  }
  
}

    
    
