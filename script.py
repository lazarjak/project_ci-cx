import json

# Učitaj project_config.json
with open('project_config.json') as f:
    data = json.load(f)

# Izvuci potrebne podatke
project_name = data["project"]["name"]
technology = data["project"]["technology"]
artefacts = data["project"]["artefacts"]
repos = data["project"].get("repos", []) # koristi .get zbog sigurnosti


# Funkcija za generisanje git checkout skripte
def generate_git_checkout_script(repos):
    script = ""
    for repo in repos:
        script += f'''
        	echo "Cloning {repo['name']}..."
        	git clone -b {repo['branch']} {repo['url']} || exit 1
        '''
    return script

# Funkcija za generisanje build skripte
def generate_build_script(artefacts):
    script = ""
    for artefact in artefacts:
        script += f'''
        	echo "Building {artefact['name']}..."
        	# Build komanda za {artefact['type']}
        '''
    return script

# Funkcija za generisanje skripte za pokretanje servisa
def generate_run_script():
    script = '''
    echo "Running core service..."
    cd core
    python3 main.py || exit 1  # Pokreće main.py iz core repozitorijuma

    echo "Running frontend service..."
    cd ../frontend
    python3 app.py || exit 1  # Pokreće app.py iz frontend repozitorijuma
    '''
    return script

# Funkcija za generisanje deploy skripte
def generate_deploy_script():
    script = '''
    // Clean up existing container
    echo "Cleaning up old Docker container..."
    docker rm -f my-app-container || { echo "Failed to remove old container"; exit 1; }

    // Pokreće aplikaciju u Docker kontejneru
    echo "Deploying new container..."
    docker run -d -p 5001:8080 --name my-app-container my-app || exit 1
    '''
    return script

# Sada generiši Groovy skriptu na osnovu tih podataka
groovy_script = f'''
pipeline {{
    agent any

    environment {{
        PROJECT_NAME = "{project_name}"
        TECHNOLOGY = "{technology}"
    }}

    stages {{
	stage('Checkout Repositories') {{
	    steps {{
		script {{
		    {generate_git_checkout_script(repos)}
		}}
	    }}
	}}

        stage('Build Artefacts') {{
            steps {{
                script {{
                    // Generisanje artefakata
                    {generate_build_script(artefacts)}
                }}
            }}
        }}

	stage('Run Tests') {{
            steps {{
                script {{
                    echo "Running core tests..."
                    dir('core') {{
                        sh 'PYTHONPATH=. pytest test_main.py'  // Pokreće testove za core
                    }}

                    echo "Running frontend tests..."
                    dir('frontend') {{
                        sh 'PYTHONPATH=.:$PWD pytest test_app.py'  // Pokreće testove za frontend
                    }}
                }}
            }}
        }}

	stage('Run Services') {{
            steps {{
                script {{
                    // Pokreni core i frontend servise
                    {generate_run_script()}
                }}
            }}
        }}

	stage('Deploy') {{
            steps {{
                script {{
                    {generate_deploy_script()}
                }}
            }}
        }}
    }}
}}

'''


# Spremi generisani Groovy script u fajl
with open('Jenkinsfile', 'w') as f:
    f.write(groovy_script)

print("Jenkinsfile je uspesno generisan!")
