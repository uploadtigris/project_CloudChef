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

    %% ============================================================
    %% Client Layer
    %% ============================================================
    Client[User Browser / Mobile App] --> ALB["Application Load Balancer - HTTPS 443"]

    %% ============================================================
    %% Frontend + API (Grouped Tightly)
    %% ============================================================
    subgraph Frontend_and_API_Tiers
        direction LR

        %% Frontend Tier
        subgraph Frontend_Tier
            FTG1["EC2 Frontend 1<br>Ubuntu + Docker + Web Container"]
            FTG2["EC2 Frontend 2<br>Ubuntu + Docker + Web Container"]
        end

        %% API Tier
        subgraph API_Tier
            APITG1["EC2 API 1<br>Ubuntu + Docker + API Container"]
            APITG2["EC2 API 2<br>Ubuntu + Docker + API Container"]
        end
    end

    %% Connections to ALB
    ALB --> FTG1
    ALB --> FTG2
    ALB --> APITG1
    ALB --> APITG2

    %% ============================================================
    %% Database Layer
    %% ============================================================
    subgraph Database_Private_Subnet
        RDS["RDS Database"]
    end

    FTG1 --> RDS
    FTG2 --> RDS
    APITG1 --> RDS
    APITG2 --> RDS

    %% ============================================================
    %% Monitoring Layer
    %% ============================================================
    subgraph Monitoring_and_Logging
        Prometheus["Prometheus Metrics"]
        ELK["ELK Stack / OpenSearch Logs"]
    end

    FTG1 --> Prometheus
    FTG2 --> Prometheus
    APITG1 --> Prometheus
    APITG2 --> Prometheus

    FTG1 --> ELK
    FTG2 --> ELK
    APITG1 --> ELK
    APITG2 --> ELK

    %% ============================================================
    %% CI/CD Layer
    %% ============================================================
    subgraph Application Code and CI/CD
        direction LR

        Git["Git Repository<br>- App Code<br>- Dockerfiles<br>- Ansible Playbooks"]
        Pipeline["CI/CD Pipeline<br>Build Images → Push → Deploy"]
        ECR["ECR Registry<br>Stores Docker Images"]
        Ansible["Ansible Automation<br>Deploys Containers on EC2"]
        AppConfig["App Config<br>.env, compose files, nginx.conf"]
    end

    Git --> Pipeline
    Pipeline --> ECR
    ECR --> Ansible

    Ansible --> FTG1
    Ansible --> FTG2
    Ansible --> APITG1
    Ansible --> APITG2

    AppConfig --> FTG1
    AppConfig --> FTG2
    AppConfig --> APITG1
    AppConfig --> APITG2

    %% ============================================================
    %% Class Assignments
    %% ============================================================

    %% Terraform-only resources
    class ALB,RDS,ECR terraform;

    %% Ansible-only resources
    class AppConfig,Ansible ansible;

    %% Dual-managed resources
    class FTG1,FTG2,APITG1,APITG2 dual;

    %% Neutral
    class Git,Pipeline neutral;

    %% ============================================================
    %% Color Definitions
    %% ============================================================

    classDef terraform stroke:#1E90FF,stroke-width:3px,color:#fff;
    classDef ansible stroke:#FF4C4C,stroke-width:3px,color:#fff;
    classDef dual stroke:#1E90FF,stroke-width:5px,color:#fff;
    classDef neutral stroke:#666,stroke-width:2px,color:#fff;
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
