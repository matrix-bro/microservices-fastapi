# Microservices using FastAPI

In this project, I am trying to implement microservices architecture using FastAPI and Docker.

## Project Setup

- Clone the repository:

```bash
git clone https://github.com/matrix-bro/microservices-fastapi.git
```

- Then, create a network

```bash
docker network create my-default-rabbit
```

- Create and Start RabbitMQ container

```bash
docker run -d --network my-default-rabbit --hostname rabbitmqhost --name rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3-management-alpine

# Now the container has been created and is running.
# To stop:
docker stop rabbitmq

# To run it next time,
docker start rabbitmq

# Or, you can also start and stop it directly from Docker Desktop.
```

- Go inside `blog-service` directory
- Build and run the `blog-service` by running the following command:

```bash
docker compose up -d --build

# To stop:
docker compose down
```

- Go inside `auth-service` directory
- Build and run the `auth-service` by running the following command:

```bash
docker compose up -d --build

# To stop:
docker compose down
```

- List running containers

```bash
docker ps
```

- Access `blog-service` in `http://localhost:8000`

- Access `auth-service` in `http://localhost:5000`
