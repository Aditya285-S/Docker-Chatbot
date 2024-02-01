
# Deploying Chatbot on AWS EC2 using 


## Project Overview

The interactive chatbot is a sophisticated conversational agent designed for seamless communication. Its source code is stored in a GitHub repository, allowing for version control and collaborative development. To deploy the chatbot on an AWS EC2 instance, the user clones the repository to the instance using Git Bash terminal on an Ubuntu operating system. Leveraging Docker, the user creates a container image encapsulating the chatbot's files and dependencies, ensuring portability and reproducibility. The Docker container is then launched on the EC2 instance, with communication facilitated through a specified port address, enabling users to interact with the chatbot in a scalable and efficient manner.


## Requirements
AWS account with an EC2 instance\
SSH key pair for accessing the EC2 instance

## Commands

1.Giving access of key pair

    chmod 400Docker-chatbot.pem

2.Switch to Ubuntu environment

3.Clone the repository

    git clone https://github.com/yourusername/chatbot-docker-aws.git

    cd Docker-chatbot

    sudo apt-get update

3.Install Docker

    sudo apt install docker.io

    docker --version

    sudo usermod -aG docker $User

3.Create Docker image

    docker build -t chatbot

4.Run image on container

    docker run -d -p 3000:3000 --name chatbot-app chatbot

    docker ps


### Notes
Make sure to update the security group settings on your EC2 instance to allow traffic on port 80.

For a production environment, consider using a reverse proxy (e.g., Nginx) and securing your application with HTTPS.
