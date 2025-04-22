import json

# Učitaj project_config.json
with open('project_config.json') as f:
    data = json.load(f)

# Izvuci potrebne podatke
project_name = data["project"]["name"]
technology = data["project"]["technology"]
repos = data["project"]["repos"]
artefacts = data["project"]["artefacts"]


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

# Sada generiši Groovy skriptu na osnovu tih podataka
groovy_script = f'''
pipeline {{
    agent any

    environment {{
        PROJECT_NAME = "{project_name}"
        TECHNOLOGY = "{technology}"
    }}

    stages {{
        stage('Build Artefacts') {{
            steps {{
                script {{
                    // Generisanje artefakata
                    {generate_build_script(artefacts)}
                }}
            }}
        }}
    }}
}}

'''


# Spremi generisani Groovy script u fajl
with open('Jenkinsfile', 'w') as f:
    f.write(groovy_script)
