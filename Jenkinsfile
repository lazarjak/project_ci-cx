
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
        	git clone -b main https://github.com/lazarjak/core.git || exit 1
        
        	echo "Cloning frontend..."
        	git clone -b develop https://github.com/lazarjak/frontend.git || exit 1
        
		}
	    }
	}

        stage('Build Artefacts') {
            steps {
                script {
                    // Generisanje artefakata
                    
        	echo "Building core-service..."
        	# Build komanda za py
        
        	echo "Building frontend-bundle..."
        	# Build komanda za zip
        
                }
            }
        }

	stage('Run Tests') {
            steps {
                script {
                    echo "Running core tests..."
                    dir('core') {
                        sh 'PYTHONPATH=. pytest test_main.py'  // Pokreće testove za core
                    }

                    echo "Running frontend tests..."
                    dir('frontend') {
                        sh 'PYTHONPATH=.:$PWD pytest test_app.py'  // Pokreće testove za frontend
                    }
                }
            }
        }

	stage('Run Services') {
            steps {
                script {
                    // Pokreni core i frontend servise
                    
   		    echo "Running core service..."
    		    cd core
    		    python3 main.py || exit 1  # Pokreće main.py iz core repozitorijuma

		    echo "Running frontend service..."
		    cd frontend
		    python3 app.py || exit 1  # Pokreće app.py iz frontend repozitorijuma
    
                }
            }
        }

	stage('Deploy') {
            steps {
                script {
                    
    		// Clean up existing container
	 	   echo "Cleaning up old Docker container..."
 		   docker rm -f my-app-container || { echo "Failed to remove old container"; exit 1; }

 	       // Pokreće aplikaciju u Docker kontejneru
		   echo "Deploying new container..."
    		   docker run -d -p 5001:8080 --name my-app-container my-app || exit 1
    
                }
            }
        }
    }
}

