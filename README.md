# My App (CI Pipeline)

This repository serves as the Application Source Code and **Continuous Integration (CI)** component of my sample CI/CD GitOps pipeline.

This is an educational project I built to demonstrate a modern, automated software delivery workflow.

## Overview

It contains the application source code, Dockerfile, and the automated pipeline logic defined in the `Jenkinsfile`.

### How the CI Pipeline Works:

1. **Automated Testing**: On every code change, Jenkins spins up a temporary Docker container to run isolated tests (e.g., Pytest), ensuring code quality without polluting the Jenkins host.
2. **Containerization**: If the tests pass and the branch is designated for release (`staging` or a production tag), Jenkins builds the application into a Docker Image and pushes it to Docker Hub.
3. **GitOps Handover**: The pipeline's final step automatically updates the Kubernetes deployment manifests in a separate GitOps repository ([my-app-gitops](https://github.com/bunnywkwk/my-app-gitops)) with the newly generated image tag.

By separating the CI (this repo) from the CD (the GitOps repo), we achieve a clean separation of concerns and higher security, which is a best practice in modern DevOps!
