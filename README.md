# 🚀 Two-Tier Flask Application with Docker, MySQL & Jenkins CI/CD

A containerized two-tier web application built with **Flask** (application layer) and **MySQL** (database layer), orchestrated using **Docker Compose**. This project was built to understand real-world multi-container deployment patterns — networking, persistent storage, and environment-based configuration — the same fundamentals used in production DevOps workflows.

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white)


---

## 📌 Project Overview

This is a simple **Message Management** web application demonstrating a classic **two-tier architecture**:

| Tier | Technology | Responsibility |
|------|-----------|-----------------|
| Application Tier | Python (Flask) | Serves the web UI and handles request logic |
| Database Tier | MySQL 5.7 | Stores and persists message data |

Both services run as separate containers and communicate over a Docker Compose network, with MySQL data persisted via a Docker volume.

---

## 🏗️ Architecture

```
┌─────────────┐        Docker Network        ┌─────────────┐
│   Browser   │ ─────────────────────────────▶│   Flask     │
│  (Client)   │        http://localhost:5000  │  Container  │
└─────────────┘                                └──────┬──────┘
                                                        │
                                                        │ MySQL Connector
                                                        ▼
                                                 ┌─────────────┐
                                                 │   MySQL     │
                                                 │  Container  │
                                                 │ (Volume-    │
                                                 │  backed)    │
                                                 └─────────────┘
```



## 🧰 Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL 5.7
- **Containerization:** Docker, Docker Compose
- **CI/CD:** Jenkins (pipeline defined in `Jenkinsfile`)

---

## 📂 Project Structure

```
two-tier-flask-app/
│
├── app.py                 # Flask application entry point
├── Dockerfile              # Image definition for the Flask app
├── docker-compose.yml       # Multi-container orchestration
├── requirements.txt         # Python dependencies
├── message.sql              # Initial DB schema/data
├── Jenkinsfile               # CI/CD pipeline definition
├── templates/
│   └── index.html           # Frontend template
└── .gitignore
```

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- [Git](https://git-scm.com/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

Verify installation:

```bash
docker --version
docker compose version
git --version
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Md-Khursheed/two-tier-flask-app.git
cd two-tier-flask-app
```

### 2. Build and run the containers

```bash
docker compose up --build
```

Or run in detached mode:

```bash
docker compose up -d --build
```

### 3. Access the application

Open your browser and navigate to:

```
http://localhost:5000
```


### 4. Verify containers are running

```bash
docker ps
```

Expected containers:
- `flask-app`
- `mysql`


---

## 🗄️ Database Initialization

The MySQL database is initialized on first startup using `message.sql`, which creates the required schema and seed data automatically via Docker's entrypoint init mechanism.

---

## 🔐 Environment Variables

The Flask app connects to MySQL using the following environment variables (configured in `docker-compose.yml`):

| Variable | Description |
|-----------|-------------|
| `MYSQL_HOST` | Hostname of the MySQL container |
| `MYSQL_USER` | Database username |
| `MYSQL_PASSWORD` | Database password |
| `MYSQL_DB` | Database name |

---

## 📝 Useful Docker Commands

| Action | Command |
|--------|---------|
| Stop containers | `docker compose down` |
| Restart containers | `docker compose restart` |
| Rebuild containers | `docker compose up --build` |
| View all logs | `docker compose logs` |
| View Flask logs | `docker logs flask-app` |
| View MySQL logs | `docker logs mysql` |
| Remove containers | `docker compose down` |

---

## 🔄 CI/CD Pipeline

This project includes a Jenkinsfile that fully automates the build, scan, push, and deploy process using a declarative pipeline (with shared-library steps for cloning, scanning, and pushing).

Pipeline stages:

Code Clone — Pulls the latest source from this repository
Trivy File System Scan — Scans the codebase for known vulnerabilities before building
Build — Builds the Docker image (docker build -t two-tier-flask-app .)
Test — Placeholder stage reserved for automated tests
Push to Docker Hub — Pushes the built image to Docker Hub using stored Jenkins credentials
Deploy — Redeploys the app with docker compose up -d --build

On completion, the pipeline sends an email notification reporting build success or failure.
---


## 👤 Author

**Mohammad Khursheed**
DevOps Engineer 
[GitHub](https://github.com/Md-Khursheed) • [LinkedIn](https://linkedin.com/in/2-md-khursheed)
