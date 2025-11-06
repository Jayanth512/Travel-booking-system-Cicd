# Travel Booking System - Fullstack Application

## Overview
A cloud-native Travel Booking System that enables users to search, compare, and book flights, hotels, and tour packages. The application is containerized using Docker and orchestrated with Kubernetes for scalability and high availability.

## Project Structure
```
travel-booking-system/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── kubernetes/
│       └── backend-deployment.yaml
├── frontend/
│   ├── index.html
│   ├── app.js
│   ├── Dockerfile
│   └── kubernetes/
│       └── frontend-deployment.yaml
├── .gitignore
└── README.md
```

## Backend (Flask API)
- Python Flask-based REST API
- Provides flight search and booking endpoints
- Containerized with Docker
- Deployed on Kubernetes with 2 replicas

## Frontend (HTML + JavaScript)
- Simple HTML interface with JavaScript
- Served via Nginx
- Containerized with Docker
- Deployed on Kubernetes with LoadBalancer service

## Deployment Instructions

### Prerequisites
- Docker installed
- Kubernetes cluster (Minikube, EKS, GKE, or AKS)
- kubectl configured
- DockerHub account

### Step 1: Build Docker Images
```bash
# Build backend image
docker build -t your-dockerhub-username/travel-backend:latest ./backend

# Build frontend image
docker build -t your-dockerhub-username/travel-frontend:latest ./frontend
```

### Step 2: Push Images to DockerHub
```bash
docker push your-dockerhub-username/travel-backend:latest
docker push your-dockerhub-username/travel-frontend:latest
```

### Step 3: Deploy to Kubernetes
```bash
# Deploy backend
kubectl apply -f backend/kubernetes/backend-deployment.yaml

# Deploy frontend
kubectl apply -f frontend/kubernetes/frontend-deployment.yaml
```

### Step 4: Access the Application
```bash
# Get services
kubectl get svc

# Access the frontend using the LoadBalancer EXTERNAL-IP
```

## API Endpoints

- `GET /` - Health check
- `GET /flights` - Get list of available flights
- `POST /book` - Book a flight

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML, JavaScript
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Web Server**: Nginx (for frontend)

## Features

- RESTful API design
- Containerized microservices
- Kubernetes orchestration
- High availability with replicas
- LoadBalancer for external access
- Scalable architecture

## License
MIT License
