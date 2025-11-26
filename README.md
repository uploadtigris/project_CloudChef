# ChefTec Modern Rebuild

A full, modern recreation of the **ChefTec** application, rebuilt from the ground up using modern development practices, automation, and cloud-native architecture.

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
* Implement **user account creation, authentication, and role-based management**
* Establish **clean Git-based version control workflows**
* Architect and deploy **cloud infrastructure** with scalability, security, and automation in mind

---

## Scope

* **Backend and frontend application redesign**
* **CI/CD automation** for testing, building, and deployment
* **Infrastructure-as-Code (IaC)** for cloud deployments
* Ensure **environment consistency** using containers or VMs
* Provide **documentation and diagrams** for architecture, workflows, and operations

---

## Cloud Deployment Diagram

A high-level view of the planned cloud deployment for ChefTec:

*This diagram represents the flow from client requests through the load balancer, web and application tiers, to the database, with CI/CD, IaC, and monitoring included.*

```mermaid
graph TD
    subgraph Client
        Browser[User Browser / Mobile App]
    end

    subgraph "Cloud Environment"
        LB[Load Balancer]
        subgraph "Web Tier"
            WebApp[Web Application Servers]
        end
        subgraph "Application Tier"
            API[API Servers / Backend]
        end
        subgraph "Database Tier"
            DB[(Database)]
        end
        subgraph "Monitoring & Logging"
            Prometheus[Monitoring]
            ELK[Logging - ELK Stack]
        end
    end

    subgraph "DevOps / Infrastructure"
        Git[Git Repository]
        Pipeline[CI/CD Pipeline]
        Terraform["Infrastructure as Code"]
    end

    Browser --> LB --> WebApp --> API --> DB
    Git --> Pipeline --> WebApp
    Terraform --> LB
    Terraform --> WebApp
    Terraform --> API
    WebApp --> Prometheus
    WebApp --> ELK
```

This diagram illustrates the ChefTec cloud deployment architecture. Client requests enter through an Application Load Balancer (ALB), which routes traffic to separate target groups for frontend and API servers. Each target group consists of EC2 instances running Ubuntu and Docker containers. The containers host the actual application code, while all backend services connect securely to an RDS/Aurora database in private subnets. The architecture emphasizes scalability, high availability, and security.

```mermaid
graph TD
    Client[User Browser / Mobile App] --> ALB["Application Load Balancer - HTTPS 443"]

    subgraph "Frontend Target Group"
        FTG1[EC2 Instance 1 - Ubuntu + Docker]
        FTG2[EC2 Instance 2 - Ubuntu + Docker]
    end

    subgraph "API Target Group"
        APITG1[EC2 Instance 3 - Ubuntu + Docker]
        APITG2[EC2 Instance 4 - Ubuntu + Docker]
    end

    ALB --> FTG1
    ALB --> FTG2
    ALB --> APITG1
    ALB --> APITG2

    subgraph "Containers on EC2"
        Web1[Frontend Web App Container]
        Web2[Frontend Web App Container]
        API1[API Container]
        API2[API Container]
    end

    FTG1 --> Web1
    FTG2 --> Web2
    APITG1 --> API1
    APITG2 --> API2

    subgraph "Database Tier - Private Subnet"
        RDS[(RDS / Aurora Database)]
    end

    Web1 --> RDS
    Web2 --> RDS
    API1 --> RDS
    API2 --> RDS
```

**Client**: User browser or mobile app accessing ChefTec

**ALB (Load Balancer)**: Routes HTTPS traffic to the right target group, handles health checks and SSL termination

**Target Groups**: Groups of EC2 instances for frontend or API, checked for health

**EC2 Instances (Ubuntu + Docker)**: Hosts frontend and API containers in private subnets

**Containers**: Run the actual app code, isolated and portable

**Database (RDS/Aurora)**: Stores app data securely in private subnets

```mermaid
graph TD
    %% Clients
    Client[User Browser / Mobile App] --> ALB["Application Load Balancer - HTTPS 443"]

    %% Target Groups
    subgraph "Frontend Target Group"
        FTG1[EC2 Instance 1 - Ubuntu + Docker]
        FTG2[EC2 Instance 2 - Ubuntu + Docker]
    end

    subgraph "API Target Group"
        APITG1[EC2 Instance 3 - Ubuntu + Docker]
        APITG2[EC2 Instance 4 - Ubuntu + Docker]
    end

    ALB --> FTG1
    ALB --> FTG2
    ALB --> APITG1
    ALB --> APITG2

    %% Containers
    subgraph "Containers on EC2"
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
    subgraph "Database Tier - Private Subnet"
        RDS[(RDS / Aurora Database)]
    end

    Web1 --> RDS
    Web2 --> RDS
    API1 --> RDS
    API2 --> RDS

    %% DevOps / Infrastructure (IaC) - Removed inline style
    subgraph "DevOps / IaC"
        Git[Git Repository - Config & Terraform]
        Pipeline[CI/CD Pipeline]
        Terraform["Terraform IaC Scripts"]
    end

    Git --> Pipeline
    Pipeline --> FTG1
    Pipeline --> FTG2
    Pipeline --> APITG1
    Pipeline --> APITG2
    Terraform --> FTG1
    Terraform --> FTG2
    Terraform --> APITG1
    Terraform --> APITG2

    %% Application Config
    subgraph "Application Configuration"
        AppConfig[".env, docker-compose.yml, nginx.conf, API keys"]
    end

    AppConfig --> Web1
    AppConfig --> Web2
    AppConfig --> API1
    AppConfig --> API2

    %% Monitoring & Logging
    subgraph "Monitoring & Logging"
        Prometheus[Prometheus - Metrics]
        ELK[ELK Stack - Logs]
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

This repository is both a **learning project** and a **practical rebuild** designed to deepen skills in:

* Software architecture
* DevOps workflows
* Cloud engineering
* Infrastructure design and automation

Do you want me to add that too?
