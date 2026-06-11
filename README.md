# 🤖 AIVA.AI – Self-Hosted AI Assistant Platform

AIVA.AI is a self-hosted AI chatbot platform that provides a ChatGPT-style web interface powered by local Large Language Models (LLMs) running through Ollama. The platform is containerized using Docker, deployed on AWS EC2, and automated using Jenkins and GitLab CI/CD pipelines.

---

## 🚀 Features

- ChatGPT-style responsive web interface
- Local AI model execution using Ollama
- Dockerized microservice architecture
- AWS EC2 deployment
- Jenkins CI/CD automation
- GitLab CI/CD automation
- Docker Hub image management
- Automated deployment and health checks
- Nginx reverse proxy integration
- Production-ready DevOps workflow

---

## 🏗️ Architecture

```text
Browser
   │
   ▼
┌─────────────────────┐
│ Frontend (Nginx)    │
│ Port 80             │
└──────────┬──────────┘
           │ /api/chat
           ▼
┌─────────────────────┐
│ Backend (Flask API) │
│ Port 5000           │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Ollama + TinyLlama  │
│ Port 11434          │
└─────────────────────┘
```

---

## ☁️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Nginx

### Backend
- Python
- Flask
- Requests

### AI Layer
- Ollama
- TinyLlama

### DevOps & Automation
- Docker
- Docker Compose
- Jenkins
- GitLab CI/CD
- Docker Hub

### Cloud Platform
- AWS EC2
- Ubuntu 22.04 LTS

---

## 📁 Project Structure

```text
aiva-ai/
│
├── frontend/
│   ├── Dockerfile
│   ├── nginx.conf
│   └── index.html
│
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── docker-compose.yml
├── Jenkinsfile
├── .gitlab-ci.yml
├── setup.sh
├── README.md
└── .gitignore
```

---

## 🔄 CI/CD Workflow

### Jenkins Pipeline

1. Push code to GitHub
2. Jenkins automatically triggers
3. Build Docker images
4. Push images to Docker Hub
5. Connect to AWS EC2 via SSH
6. Pull latest images
7. Restart containers
8. Run health checks

### GitLab Pipeline

1. Push code to GitLab
2. GitLab Runner triggers pipeline
3. Build Docker images
4. Push images to Docker Hub
5. Deploy to AWS EC2
6. Verify deployment through health checks

---

## 🐳 Local Setup

### Clone Repository

```bash
git clone https://github.com/amanevolve/aiva-ai.git
cd aiva-ai
```

### Start Application

```bash
chmod +x setup.sh
./setup.sh
```

or

```bash
docker compose up -d
```

### Verify Containers

```bash
docker compose ps
```

---

## ☁️ AWS Deployment

### EC2 Configuration

- Ubuntu 22.04 LTS
- t2.small or higher
- Docker Installed
- Docker Compose Installed

### Required Ports

| Port | Purpose |
|--------|---------|
| 22 | SSH |
| 80 | Frontend |
| 5000 | Backend API |
| 8080 | Jenkins |
| 11434 | Ollama |

---

## 🧪 Verification Commands

### Check Running Containers

```bash
docker compose ps
```

### Backend Health Check

```bash
curl http://SERVER-IP:5000/health
```

### View Logs

```bash
docker compose logs -f
```

### Test API

```bash
curl -X POST http://SERVER-IP:5000/api/chat \
-H "Content-Type: application/json" \
-d '{"messages":[{"role":"user","content":"Hello"}]}'
```

---

## 📊 Skills Demonstrated

- AWS EC2
- Docker
- Docker Compose
- Jenkins
- GitLab CI/CD
- Linux Administration
- Nginx Reverse Proxy
- SSH Automation
- Infrastructure Deployment
- AI Model Hosting
- DevOps Automation
- Cloud Computing

---

## 🎯 Project Outcome

Successfully built and deployed a complete self-hosted AI assistant platform with:

- Containerized Architecture
- Automated CI/CD Pipelines
- Cloud Deployment on AWS
- AI Model Integration via Ollama
- Jenkins & GitLab Automation
- Production-Ready Deployment Workflow

This project demonstrates hands-on experience in DevOps, Cloud Computing, Docker, CI/CD, Linux Administration, and AI Infrastructure.

---

## 👨‍💻 Author

**Aman Kumar**

DevOps Engineer | AWS | Docker | Jenkins | GitLab CI/CD | AI Infrastructure

⭐ If you found this project useful, consider starring the repository.
