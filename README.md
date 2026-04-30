# MSIT 3404 — Cloud & DevOps Group Project

> A containerized full-stack web application deployed on Kubernetes, built for the MSIT 3404 Cloud & DevOps course at Clark University.

---

## Team

| Name | Role |
|------|------|
| **Adnan Nazir** | Backend · DevOps · K8s |
| **Shirish** | Frontend · DevOps · K8s |

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│                  Kubernetes Cluster              │
│                                                  │
│   ┌─────────────────────┐                        │
│   │   Frontend Service  │  NodePort :30002       │
│   │   (nginx:alpine)    │◄──── Browser           │
│   │   4 Replicas        │                        │
│   └─────────────────────┘                        │
│                                                  │
│   ┌─────────────────────┐                        │
│   │   Backend Service   │  Port :5000            │
│   │   (Flask / Python)  │                        │
│   └─────────────────────┘                        │
└─────────────────────────────────────────────────┘
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML · Nginx (Alpine) |
| **Backend** | Python 3.10 · Flask 3.0 |
| **Containerization** | Docker |
| **Orchestration** | Kubernetes |
| **Image Registry** | Docker Hub (`zangoo/msit-frontend`) |

---

## Project Structure

```
MSIT-3404-Project/
├── backend/
│   ├── app.py               # Flask application
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile           # Backend container image
│   └── static/
│       └── sample.jpg       # Served static asset
├── frontend/
│   ├── index.html           # Frontend HTML page
│   └── Dockerfile           # Frontend container image (nginx)
└── k8s/
    ├── frontend-deployment.yaml   # Deployment (4 replicas) + NodePort Service
    └── node.yaml                  # Node configuration
```

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) installed
- [Kubernetes](https://kubernetes.io/) cluster (Minikube, kubeadm, or cloud provider)
- `kubectl` configured

---

### Run Locally with Docker

**Backend**
```bash
cd backend
docker build -t msit-backend .
docker run -p 5000:5000 msit-backend
```
Visit: `http://localhost:5000`

**Frontend**
```bash
cd frontend
docker build -t msit-frontend .
docker run -p 8080:80 msit-frontend
```
Visit: `http://localhost:8080`

---

### Deploy to Kubernetes

```bash
# Apply all manifests
kubectl apply -f k8s/

# Verify pods are running
kubectl get pods

# Check services
kubectl get svc
```

The frontend will be accessible on **NodePort 30002**:
```
http://<node-ip>:30002
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Returns a hello message |
| `GET` | `/image` | Serves `sample.jpg` from static folder |

---

## Kubernetes Configuration

| Resource | Detail |
|----------|--------|
| Deployment | `frontend` — 4 replicas |
| Image | `zangoo/msit-frontend:latest` |
| Container Port | `80` |
| Service Type | `NodePort` |
| Node Port | `30002` |

---

## Course Info

| Field | Detail |
|-------|--------|
| **Course** | MSIT 3404 — Cloud & DevOps |
| **Institution** | Clark University |
| **Semester** | Spring 2026 |
