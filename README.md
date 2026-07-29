# 🚀 Two-Tier Flask Application with Docker & MySQL

A beginner-friendly DevOps project demonstrating how to containerize a Python Flask application and connect it with a MySQL database using Docker Compose.

This project was built as part of my DevOps learning journey to understand containerization, multi-container applications, and Docker networking.

---

## 📌 Project Overview

This is a simple Message Management web application built using **Flask** and **MySQL**.

The application follows a **Two-Tier Architecture**:

- **Application Tier:** Python Flask
- **Database Tier:** MySQL 5.7

Both services run inside separate Docker containers and communicate through Docker Compose.

---

# 📖 Why I Built This Project

As a DevOps fresher, I wanted to understand how real-world applications are deployed using containers.

Instead of simply running an application locally, I wanted to learn how to:

- Containerize applications using Docker
- Connect multiple containers
- Use Docker Compose
- Store application data inside MySQL
- Manage environment variables
- Build a project similar to what companies use

This project helped me understand the fundamentals of application deployment before moving towards Kubernetes and CI/CD pipelines.

---


# 📂 Project Structure

```

two-tier-flask-app/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── message.sql
├── Jenkinsfile
├── README.md
│
├── templates/
│     └── index.html
│
└── .gitignore

```

---


# ⚙️ Prerequisites

Before running this project, make sure you have installed:

- Git
- Docker
- Docker Compose
- Python (Optional if running only with Docker)

Verify installation:

```bash
docker --version
docker compose version
git --version
```

---

# 📥 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/two-tier-flask-app.git

cd two-tier-flask-app
```

Replace:

```
YOUR_USERNAME
```

with your GitHub username.

---

# ▶️ Running the Application

Build and start the containers:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d --build
```

---

# 🌐 Access the Application

Once the containers are running, open:

```
http://localhost:5000
```

The Flask application should now be accessible in your browser.

---

# 🐳 Docker Containers

Check running containers:

```bash
docker ps
```

Expected output:

```
flask-app
mysql
```

---

# 📝 Useful Docker Commands

### Stop Containers

```bash
docker compose down
```

---

### Restart Containers

```bash
docker compose restart
```

---

### Rebuild Containers

```bash
docker compose up --build
```

---

### View Logs

```bash
docker compose logs
```

or

```bash
docker logs flask-app

docker logs mysql
```

---

### Remove Containers

```bash
docker compose down
```

---

# 🗄️ Database

The MySQL database is initialized using:

```
message.sql
```

This file creates the required database objects during the first startup.

---

# 🔐 Environment Variables

The Flask application reads the following environment variables:

| Variable | Description |
|-----------|-------------|
| MYSQL_HOST | MySQL Container |
| MYSQL_USER | Database Username |
| MYSQL_PASSWORD | Database Password |
| MYSQL_DB | Database Name |

Docker Compose automatically passes these variables to the Flask container.

---


# 🚀 Future Improvements

I plan to continue improving this project by adding:

- Jenkins CI/CD Pipeline
- Docker Hub Integration
- GitHub Webhooks
- Automated Testing
- Kubernetes Deployment
- AWS EC2 Deployment
- Nginx Reverse Proxy
- Monitoring with Prometheus & Grafana

