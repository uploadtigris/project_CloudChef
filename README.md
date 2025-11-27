\# ChefTec Modern Rebuild

A full, modern recreation of the **ChefTec** application using cloud-native patterns, Infrastructure-as-Code, containerization, and automated deployments.

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

🟦--> Terraform Managed

🟥--> Ansible Managed
```mermaid
graph LR

    %% ============================================================
    %% Client Layer
    %% ============================================================
    Client[User Browser / Mobile App] --> ALB["Application Load Balancer - HTTPS 443"]

    %% ============================================================
    %% Frontend + API (Grouped Tightly)
    %% ============================================================
    subgraph Frontend and API Tiers
        direction LR

        %% Frontend Tier
        subgraph Frontend Tier
            FTG1["EC2 Frontend 1<br>Ubuntu + Docker + Web Container"]
            FTG2["EC2 Frontend 2<br>Ubuntu + Docker + Web Container"]
        end

        %% API Tier
        subgraph API Tier
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
    subgraph Database Private Subnet
        RDS["RDS Database"]
    end

    FTG1 --> RDS
    FTG2 --> RDS
    APITG1 --> RDS
    APITG2 --> RDS

    %% ============================================================
    %% Monitoring Layer
    %% ============================================================
    subgraph Monitoring and Logging
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

## Why This Architecture

This project is designed for **modularity, scalability, and automation**, reflecting modern cloud and DevOps practices.

### **1. Terraform – Infrastructure as Code**

Manages **persistent cloud resources**: VPC, subnets, ALB, EC2 Auto Scaling Groups, and RDS.

* Ensures reproducible, version-controlled infrastructure
* Serves as a **single source of truth** for all environments

### **2. Ansible – Host Configuration**

Configures EC2 hosts after provisioning:

* Installs packages, Docker, Nginx
* Deploys containers and system-level settings
* Ensures consistent, identical hosts across environments

### **3. CI/CD – Automated Application Delivery**

Pipelines handle **building, testing, and deploying code**:

* CI: Runs tests, builds Docker images, stores them in ECR
* CD: Deploys containers to EC2 hosts via Ansible
* Keeps development, staging, and production consistent

### **4. Containers – Runtime Consistency**

Frontend and API services run in Docker containers:

* Isolated environments, same runtime in dev/prod
* Faster, predictable deployments
* Eliminates “works on my machine” issues

### **5. Multi-Tier Layout**

**Frontend → API → Database** separation:

* Frontend: handles user interaction
* API: handles business logic and database operations
* Database: internal-only access, secure
  **Benefits:** independent scaling, fault isolation, and maintainable architecture

### **6. Private Database**

RDS runs in **private subnets**, accessible only by API/frontend containers, ensuring security and internal-only access.

---

## Tech Stack (Planned)

| Layer              | Tools                                |
| ------------------ | ------------------------------------ |
| Infrastructure     | Terraform                            |
| Host Configuration | Ansible                              |
| Runtime            | Docker                               |
| Cloud Provider     | AWS / Azure / GCP                    |
| CI/CD              | GitHub Actions / GitLab CI / Jenkins |
| Monitoring         | Prometheus, ELK/OpenSearch           |
| App Framework      | Python CLI / GTK / FastAPI / Flask   |
| Database           | SQLite (MVP) / RDS (Cloud)           |

---

## Status

**Active development** – infrastructure, automation, and Python MVP are in progress.

---

## Purpose

This repository is a **learning platform and real-world rebuild** to strengthen:

* Cloud engineering
* DevOps workflows and automation
* Multi-tier application design
* Infrastructure-as-Code practices

---
