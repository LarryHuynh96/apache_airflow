# Apache Airflow Study

# Docker Compose Setup and Run

This guide explains how to use Docker Compose to set up and run your services.

## Prerequisites

- **Docker**: Ensure Docker is installed and running on your machine.
- **Docker Compose**: Ensure Docker Compose is installed.

If you do not have Docker or Docker Compose installed, you can follow the official installation guide:

- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

## Clone the Project

If you are using a Git repository, clone the project to your local machine.

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

## Running Docker Compose

### 1. **Build and Start Services**

If you have a `docker-compose.yml` file in your project folder, run the following command to build and start the services defined in the `docker-compose.yml` file:

```bash
docker compose up --build
```

- `--build` ensures that any changes to Dockerfiles are considered during the process.
- The command will pull the necessary images and start the services in detached mode.

### 2. **Start Docker Compose in Detached Mode**

To start Docker Compose and run it in the background (detached mode):

```bash
docker compose up -d
```

This will start your services in the background, allowing you to continue working in the terminal.

### 3. **View Running Containers**

To check if the services are running, use the following command:

```bash
docker compose ps
```

This will show you the status of the running containers defined by the `docker-compose.yml` file.

### 4. **Stop the Running Containers**

To stop the containers that were started by Docker Compose, use:

```bash
docker compose down
```

This will stop and remove the containers, networks, and volumes associated with the project.

### 5. **View Logs for a Specific Service**

To view the logs for a specific service defined in the `docker-compose.yml` file:

```bash
docker compose logs <service-name>
```

Replace `<service-name>` with the name of the service whose logs you want to check.

---

## Example Docker Compose Commands

1. **Build and start services in the background:**

   ```bash
   docker compose up --build -d
   ```

2. **Stop and remove services:**

   ```bash
   docker compose down
   ```

3. **View logs for a specific service:**
   ```bash
   docker compose logs <service-name>
   ```

---

## Additional Information

For more advanced options, refer to the official Docker Compose documentation:

- [Docker Compose CLI Reference](https://docs.docker.com/compose/reference/)

---

**🚀 That's it! You are ready to use Docker Compose to manage your services.**
