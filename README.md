# Git & GitHub Learning Guide

A comprehensive guide documenting the journey of learning Git, GitHub, and local development environments through CS50 resources.

## Overview

This repository serves as a learning resource for developers transitioning from cloud-based development environments to local development workflows. The guide focuses on two primary objectives:

1. **Setting Up Local Development Environment**
2. **Mastering Git and GitHub Workflows**

## 1. Local Development Setup

### Windows Subsystem for Linux (WSL)

**Resource:** [Microsoft WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/about)

**Key Takeaway:** WSL requires a Linux distribution (such as Ubuntu) to function properly. Both WSL and Ubuntu need to be installed to create a complete development environment.

### VS Code Configuration for Local Development

**Resource:** [Developing Your Project Locally with VS Code (Windows) - CS50 Seminars 2021](https://youtu.be/9yzQCgIdL-Y)

**Key Takeaways:**
- Configure Windows Subsystem for Linux with Ubuntu to access the Linux terminal environment used in CS50
- Understand package managers: `apt-get` serves as the general package manager for Linux, while language-specific managers like `pip3` handle Python packages
- Install and configure relevant VS Code extensions to enhance your development workflow

## 2. Git and GitHub Fundamentals

### Creating a GitHub Repository

**Resource:** [Collaboration and Version Control with Git - CS50 Seminars 2021](https://youtu.be/S-gBbnBDUhA) (Timestamp: 16:49 - 30:36)

### Git and GitHub Basics

**Resource:** [An Introduction to Git and GitHub by Brian Yu](https://youtu.be/MJUJ4wbFm_A)

**Key Takeaway:** Git operates locally and requires initialization with `git init` for new projects. GitHub serves as a remote repository hosting service. When cloning an existing repository with `git clone`, local Git setup is handled automatically.

### Pull Requests and Collaboration

**Resource:** [Collaboration and Version Control with Git - CS50 Seminars 2021](https://youtu.be/S-gBbnBDUhA) (Timestamp: 49:43 - 57:06)

**Key Takeaway:** Pull requests enable collaborative development by allowing code review and approval before merging branches or forks into the main branch. This workflow is essential for open-source collaboration and team-based development.

## Purpose

This guide was created as part of a CS50 final project to document the learning process and serve as a reference for others transitioning to professional development workflows.
