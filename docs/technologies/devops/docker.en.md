---
description: "Docker for testers: images and containers, the most useful commands, reading logs and building a repeatable test environment with Docker Compose."
---

# Docker

**Docker** is an open-source platform for building, running and managing applications in **containers**. It isolates environments, so an application behaves the same regardless of the operating system and server configuration, without the “works on my machine” problem.

## Basic concepts

| Concept | Description |
|---|---|
| **Container** | a lightweight, isolated environment with the application and its dependencies, runs like a process in the system |
| **Image** | a template from which containers are created |
| **Dockerfile** | a file with instructions for building an image (base system, commands, ports) |
| **Docker Hub** | public image repository (nginx, mysql, python, jenkins…) |
| **Volume** | persistent storage for data outside the container's lifecycle |

## Most important commands

| Command | What it does |
|---|---|
| `docker ps` | running containers |
| `docker ps -a` | all containers (including stopped ones) |
| `docker images` | list of local images |
| `docker pull <image>` | download an image from Docker Hub |
| `docker run <image>` | start a new container |
| `docker stop <id>` | stop a container |
| `docker rm <id>` / `docker rmi <image>` | remove a container / an image |
| `docker exec -it <container> bash` | get a shell inside a container (`sh` on images without bash, e.g. Alpine) |
| `docker logs <container>` | container logs |

## Docker Compose

A tool for defining and running **multiple containers as one application** (e.g. app + database + cache) in a `docker-compose.yml` file.

```yaml
services:
  app:
    image: my-app:1.4.2          # a fixed version, so every run tests the same build
    ports: ["8080:8080"]
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: test    # test environment only
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      retries: 10
```

```bash
docker compose up -d     # start in the background
docker compose down      # stop and remove the containers
docker compose down -v   # the same, plus remove volumes (clean database)
```

!!! warning "`depends_on` does not wait for the service to be ready"
    A plain `depends_on: [db]` only waits for the container to start, not for the database to accept connections, which causes flaky "connection refused" errors. That is why the database in the example has a `healthcheck` and the app waits for `service_healthy`.

## Docker in a tester's work

- quickly setting up a **test environment** or a database with test data,
- running tests in a reproducible environment in CI (e.g. the `cypress/included` image),
- **Selenium Grid** in containers for testing on many browsers,
- investigating failures with `docker logs` and `docker exec`.
