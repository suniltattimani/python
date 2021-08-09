pipeline {
  
  agent any
  
  stages {
    stage ( "Build") {
      
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
    
  }
  
}

    
    
