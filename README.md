# ChefTec Modern Rebuild

A full, modern recreation of the **ChefTec** application using modern development practices, automation, and cloud-native architecture.

---

## Table of Contents

1. [Project Goals](#project-goals)
2. [Scope](#scope)
3. [Cloud Deployment Diagram](#cloud-deployment-diagram)
4. [Tech Stack (Planned)](#tech-stack-planned)
5. [Status](#status)
6. [Purpose](#purpose)

---

## Project Goals

* Build **development** and **production** environments
* Implement **user accounts, authentication, and role-based management**
* Establish **Git-based version control workflows**
* Deploy **cloud infrastructure** with scalability, security, and automation

---

## Scope

* **Backend & frontend redesign**
* **CI/CD automation** for testing, building, and deployment
* **Infrastructure-as-Code (IaC)** for cloud deployments
* Ensure **environment consistency** using containers or VMs
* Provide **documentation and architecture diagrams**

---

## Cloud Deployment Diagram

High-level view of ChefTec’s cloud deployment:

```mermaid
graph LR
    %% Client
    Client[User Browser / Mobile App] --> ALB["Application Load Balancer - HTTPS 443"]

    %% Target Groups
    subgraph "Frontend Target Group"
        FTG1[EC2 1 - Ubuntu + Docker]
        FTG2[EC2 2 - Ubuntu + Docker]
    end

    subgraph "API Target Group"
        APITG1[EC2 3 - Ubuntu + Docker]
        APITG2[EC2 4 - Ubuntu + Docker]
    end

    ALB --> FTG1
    ALB --> FTG2
    ALB --> APITG1
    ALB --> APITG2

    %% Containers
    subgraph "Containers"
        Web1[Frontend Web App Container]
        Web2[Frontend Web App Container]
        API1[API Container]
        API2[API Container]
    end

    FTG1 --> Web1
    FTG2 --> Web2
    APITG1 --> API1
    APITG2 --> API2

    %% Database
    subgraph "Database - Private Subnet"
        RDS[(RDS Database)]
    end

    Web1 --> RDS
    Web2 --> RDS
    API1 --> RDS
    API2 --> RDS

    %% Terraform Node (No grey box)
    Terraform["Terraform IaC Scripts"]
    Terraform --> FTG1
    Terraform --> FTG2
    Terraform --> APITG1
    Terraform --> APITG2
    Terraform --> ALB
    Terraform --> RDS

    %% Application Code / Config
    subgraph "Application Code & Config"
        Git[Git Repository - App Code & Config]
        Pipeline[CI/CD Pipeline]
        AppConfig[".env, docker-compose.yml, nginx.conf, API keys"]
    end

    Git --> Pipeline --> Web1
    Git --> Pipeline --> Web2
    Git --> Pipeline --> API1
    Git --> Pipeline --> API2
    AppConfig --> Web1
    AppConfig --> Web2
    AppConfig --> API1
    AppConfig --> API2

    %% Monitoring & Logging
    subgraph "Monitoring & Logging"
        Prometheus[Prometheus Metrics]
        ELK[ELK Stack Logs]
    end

    FTG1 --> Prometheus
    FTG2 --> Prometheus
    APITG1 --> Prometheus
    APITG2 --> Prometheus
    FTG1 --> ELK
    FTG2 --> ELK
    APITG1 --> ELK
    APITG2 --> ELK

    %% Environments
    subgraph "Development Environment"
        DevFTG1[Dev Frontend EC2 + Docker]
        DevAPITG1[Dev API EC2 + Docker]
    end

    subgraph "Production Environment"
        ProdFTG1["Prod Frontend Target Group 1"]
        ProdFTG2["Prod Frontend Target Group 2"]
        ProdAPITG1["Prod API Target Group 1"]
        ProdAPITG2["Prod API Target Group 2"]
    end
```

**Components**:

* **Client**: Browser or mobile app
* **ALB**: Routes HTTPS traffic to frontend/API target groups
* **Target Groups**: EC2 instances hosting frontend/API containers
* **Containers**: Run application code in isolated environments
* **Database (RDS)**: Stores app data in private subnets
* **DevOps / IaC**: Git repository, CI/CD pipeline, Terraform scripts
* **Application Config**: `.env`, container and web server config
* **Monitoring & Logging**: Prometheus metrics, ELK stack logs
* **Dev / Prod Environments**: Separate EC2 instances for safe development and production

---

## Tech Stack (Planned)

* **Application Framework:** TBD
* **Database:** TBD
* **Infrastructure-as-Code / Automation:** Terraform, Ansible
* **Cloud Provider:** AWS / Azure / GCP
* **CI/CD Tools:** GitHub Actions / Jenkins / GitLab CI

---

## Status

* **Active development**

---

## Purpose

This repository is a **learning project** and **practical rebuild** designed to deepen skills in:

* Software architecture
* DevOps workflows
* Cloud engineering
* Infrastructure design and automation

