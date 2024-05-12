
# Cloud Computing Project - 02-24-00204
## Overview
Welcome to Cloud Computing Project 02-24-00204! This project focuses on creating a web server that serves HTML files in a containerized environment. Additionally, it involves setting up another container for the database, which will contain student information.

# Project Structure
The project consists of two main components:

1. **Web Server Container**: This container hosts the web server responsible for serving HTML files. It handles incoming requests and responds with the appropriate HTML content. The web server is designed to run efficiently within a containerized environment.

2. **Database Container**: This container houses the database containing student information. It stores data related to students, such as their names, grades, and other relevant details. The database container ensures data persistence and provides a reliable storage solution for the application.

## Installation

To install and run the project, follow these steps:

1. **Clone the Repository**: Clone the project repository to your local machine.

    ```bash
    git clone https://github.com/TortoiseShell04/Cloud-Computing-Project---02-24-00204-
    ```

2. **Build and Run Containers**: Navigate to the project directory and use Docker Compose to build and run the containers.

    ```bash
    cd Cloud-Computing-Project---02-24-00204-
    docker-compose up --build
    ```
## Usage
1. **Access the Web Server**: Once the containers are up and running, you can access the web server by visiting `http://localhost:8080` in your web browser.s Web Pages: Navigate to the web server URL (http://localhost:8080) to view the served HTML files. You can interact with the web pages as intended.

2. **Database Interaction**: The database container is set up to handle student information. You can perform CRUD operations on the database using the appropriate APIs or interfaces provided by your chosen database management system (DBMS).
