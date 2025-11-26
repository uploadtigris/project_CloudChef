# ChefTec Modern Rebuild

A full, modern recreation of the **ChefTec** application using cloud-native patterns, Infrastructure-as-Code, containerization, and automated deployments.

---

## Table of Contents

1. [Project Goals](#project-goals)
2. [Scope](#scope)
3. [Cloud Deployment Diagram](#cloud-deployment-diagram)
4. [Why This Architecture? (Concise Explained)](#why-this-architecture-concise-explained)
5. [Tech Stack (Planned)](#tech-stack-planned)
6. [Status](#status)
7. [Purpose](#purpose)

---

## Project Goals

* Build separate **development** and **production** cloud environments
* Implement **authentication**, **user roles**, and **account management**
* Establish **Git-based workflows** for consistent development
* Deploy **scalable, secure, automated** cloud infrastructure
* Ensure long-term maintainability with Infrastructure-as-Code

---

## Scope

* Full **frontend + backend rebuild**
* **CI/CD automation** for building and deploying containers
* **Terraform-based Infrastructure-as-Code**
* **Ansible automation** for provisioning VMs and Docker services
* Standardized **environment configuration** across Dev/Prod
* Clear **architecture diagrams and documentation**

---

## Cloud Deployment Diagram

High-level view of ChefTec’s cloud deployment:

```mermaid
graph LR

    %% ─────────────────────────────────────
    %% Client Layer
    %% ─────────────────────────────────────
    Client[User Browser / Mobile App] --> ALB["Application Load Balancer (HTTPS 443)"]

    %% ─────────────────────────────────────
    %% Terraform Layer (Infra Provisioning)
    %% ─────────────────────────────────────
    Terraform["Terraform (Infrastructure Provisioning)"]

    Terraform --> ALB
    Terraform --> VPC[VPC, Subnets, Routes, Security Groups]
    Terraform --> RDS[(RDS Database)]
    Terraform --> FTG["Frontend EC2 Auto Scale Group"]
    Terraform --> APITG["API EC2 Auto Scale Group"]

    %% ─────────────────────────────────────
    %% Ansible Layer (Host Configuration)
    %% ─────────────────────────────────────
    Ansible["Ansible (OS + Packages + Docker Config)"]

    Ansible --> FTG
    Ansible --> APITG

    %% ─────────────────────────────────────
    %% Frontend Tier
    %% ─────────────────────────────────────
    subgraph "Frontend Tier"
        FTG1[EC2 Frontend 1]
        FTG2[EC2 Frontend 2]
        Web1[Frontend Container]
        Web2[Frontend Container]
    end

    ALB --> FTG1
    ALB --> FTG2

    FTG1 --> Web1
    FTG2 --> Web2

    %% ─────────────────────────────────────
    %% API Tier
    %% ─────────────────────────────────────
    subgraph "API Tier"
        APITG1[EC2 API 1]
        APITG2[EC2 API 2]
        API1[API Container]
        API2[API Container]
    end

    ALB --> APITG1
    ALB --> APITG2

    APITG1 --> API1
    APITG2 --> API2

    %% ─────────────────────────────────────
    %% Database Tier
    %% ─────────────────────────────────────
    subgraph "Database (Private Subnet)"
        RDS
    end

    Web1 --> RDS
    Web2 --> RDS
    API1 --> RDS
    API2 --> RDS

    %% ─────────────────────────────────────
    %% CICD Layer (App Build & Deployment)
    %% ─────────────────────────────────────
    subgraph "Application Code & CI/CD"
        Git[Git Repository]
        Pipeline[CI/CD Pipeline - Build & Push Images]
        AppConfig["App Config (.env, docker-compose.yml, nginx.conf)"]
    end

    Git --> Pipeline
    Pipeline --> Web1
    Pipeline --> Web2
    Pipeline --> API1
    Pipeline --> API2

    AppConfig --> Web1
    AppConfig --> Web2
    AppConfig --> API1
    AppConfig --> API2

    %% ─────────────────────────────────────
    %% Monitoring Layer
    %% ─────────────────────────────────────
    subgraph "Monitoring & Logging"
        Prometheus[Prometheus Metrics]
        ELK[ELK Stack / OpenSearch Logs]
    end

    FTG1 --> Prometheus
    FTG2 --> Prometheus
    APITG1 --> Prometheus
    APITG2 --> Prometheus

    FTG1 --> ELK
    FTG2 --> ELK
    APITG1 --> ELK
    APITG2 --> ELK
```

---

## Why This Architecture? (Concise Explained)

### **1. Terraform for Infrastructure**

Terraform handles **everything that should persist**: VPC, subnets, ALB, EC2 ASGs, RDS.

* Cloud infra must be reproducible
* Terraform produces a **single source of truth**
* Changes are versioned and safely previewed

**Why:** Infra should never be manually created.

---

### **2. Ansible for Host Configuration**

Ansible configures each EC2 instance after Terraform creates them:

* Installs packages, Docker, Nginx
* Deploys system-level settings
* Ensures servers are identical

**Why:** Configuring hosts is not Terraform’s job.

---

### **3. CI/CD for Application Delivery**

CI/CD builds container images and deploys them to the provisioned hosts:

* Separate from infra provisioning
* Automatically pushes updates
* Keeps environments consistent

**Why:** Code should deploy automatically—not tied to infra state.

---

### **4. Containers for Runtime Consistency**

The frontend and API run in containers on each EC2 instance:

* Isolates application behavior
* Same runtime in dev/prod
* Faster deployments

**Why:** No “works on my machine” problems.

---

### **5. 3-Tier Layout for Scalability & Clarity**

**Frontend → API → Database** tiers

* Each tier can scale independently
* Better fault isolation
* Industry standard architecture

**Why:** Clean separation of concerns.

---

### **6. RDS in Private Subnets**

Database stays private, never exposed to the internet:

* Most secure design
* Only app/API containers can reach it

**Why:** Databases must not be on public networks.

---

## Tech Stack (Planned)

| Layer                 | Tools                                |
| --------------------- | ------------------------------------ |
| **Infrastructure**    | Terraform                            |
| **Config Management** | Ansible                              |
| **Runtime**           | Docker containers                    |
| **Cloud Provider**    | AWS / Azure / GCP                    |
| **CI/CD**             | GitHub Actions / GitLab CI / Jenkins |
| **Monitoring**        | Prometheus, ELK/OpenSearch           |
| **App Framework**     | TBD                                  |
| **Database**          | TBD                                  |

---

## Status

**Active development**
Architecture, IaC layout, and base automation are being built.

---

## Purpose

This repository serves as a **learning platform** and **real-world rebuild** to strengthen skills in:

* Cloud engineering
* DevOps workflows
* Infrastructure automation
* Multi-tier architecture design
