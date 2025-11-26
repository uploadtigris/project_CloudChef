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

