
pipeline {
    agent any

    environment {
        PROJECT_NAME = "MyProject"
        TECHNOLOGY = "Python"
    }

    stages {

	stage('Checkout Repositories') {
	    steps {
		script {
		    
        	echo "Cloning core..."
        	sh 'rm -rf core'
		sh 'git clone -b master https://github.com/lazarjak/core.git || exit 1'
        
        	echo "Cloning frontend..."
        	sh 'rm -rf frontend'
		sh 'git clone -b master https://github.com/lazarjak/frontend.git || exit 1'
        
		}
	    }
	}

        stage('Build Artefacts') {
            steps {
                script {
                    // Generisanje artefakata
                    
        	    echo "Building core-service..."
        
        	    echo "Building frontend-bundle..."
        	
        
                }
            }
        }

	stage('Run Tests') {
            steps {
                script {
                    echo "Running core tests..."
                    dir('core') {
                        sh 'pytest privremeni/test_main.py'  // Pokreće testove za core
                    }

                    echo "Running frontend tests..."
                    dir('frontend') {
                        sh 'pytest privremeni1/test_app.py'  // Pokreće testove za frontend
                    }
                }
            }
        }

	stage('Run Services') {
            steps {
                script {
                    // Pokreni core i frontend servise
                    
    		    echo "Running core service..."
   		    sh '''
			 cd core
   			 python3 main.py || exit 1  # Pokreće main.py iz core repozitorijuma

   		    '''


    		    echo "Running frontend service..."
   		    sh '''	
			 cd frontend
   			 python3 app.py || exit 1  # Pokreće app.py iz frontend repozitorijuma
    		    '''
                }
            }
        }
    }
}

