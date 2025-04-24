# Koristimo zvaničnu Jenkins sliku
FROM jenkins/jenkins:lts

# Instaliraj potrebne zavisnosti za tvoj pipeline (npr. Git, Python, Java)
USER root
RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-venv \
    openjdk-17-jdk \
    curl

# Eksponuj portove Jenkins-a
EXPOSE 8080
EXPOSE 50000

# Pokreni Jenkins
CMD ["java", "-jar", "/usr/share/jenkins/jenkins.war"]

