# Assignment Submission: Dockerized Text Analyzer

**Author:** Randy Hucker
**Date:** March 1 2026

---

## 1. Environment Setup (Requirement 1)

- **Action:** Installed **Docker Desktop** on a personal machine.
- **Status:** Docker Engine is running, and the containerized environment is configured.

> **![image](images/DockerDesktop.png)**

---

## 2. Docker Implementation (Requirement 2 & 5)

### Lightweight Base Image Selection

For this assignment, I utilized `python:3.9-slim` as the base image as directed.

---

## 3. Python Script Logic (Requirement 3 & 4)

The `scripts.py` file is designed to be fully automated. It handles text cleaning, frequency analysis, and system networking.

### Addressing Text Challenges:

- **Requirement 4c/4d (Special Characters):** * **Hyphens (`-`) & Em-dashes (`—`):** In the poem *If\*, certain words are joined by these characters (e.g., `pitch-and-toss`, `And—which`). The script replaces these characters with spaces to ensure words like "and" are isolated and counted individually, reaching the target count of **20**.
  - **Contractions:** For `AlwaysRememberUsThisWay.txt`, apostrophes are replaced with spaces to split words like "don't" into "don" and "t" as required.
- **Requirement 4e (IP Address):** The script uses `socket.gethostbyname(socket.gethostname())` to retrieve the internal IP assigned to the container by the Docker bridge network.

---

## 4. Execution & Usage Instructions

To build and run this project from the source files, use the following commands:

### Build the Image

```bash
docker build -t word-counter-app .
```

### Run the Container (Requirement 4f)

```bash
docker run --rm --name docker-project word-counter-app
```

_This command will execute the script, print the results to the console, and save them to /home/data/output/result.txt._

> **![image](images/ProjectContainer.png)**

### Export for Evaluation (Requirement 6)

To generate the .tar file for submission:

```bash
docker save -o HUCKERRE.tar word-counter-app
```

## 5. Extra Credit: Orchestration

### Kubernetes Manifest

A `deployment.yaml` was created to orchestrate the container using Kubernetes.

- Replicas: Set to 2 to ensure high availability and demonstrate scaling.
- Verification: The output of the pod status was captured using:

### 1. Deployment Command:

This triggers Kubernetes to pull our Docker image and start the two replicas we defined.

```bash
kubectl apply -f deployment.yaml
```

### 2. Status & Redirect command:

This command checks the status of the pods and redirects the output to a text file for review.

```bash
kubectl get pods > kube_output.txt
```

> **![image](images/KubeOutput.png)**

## 6. Expected Assignment Results Summary

> **![image](images/ResultsScreenshot.png)**
