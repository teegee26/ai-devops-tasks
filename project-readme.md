# Simple Task API

## Description

Simple Task API is a RESTful service for task management, built with Node.js, Express, and MongoDB. It allows users to create, read, update, and delete tasks, filter them by status and priority, and includes basic user authorization.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd simple-task-api
    ```
2. Install dependencies:
    ```bash
    npm install
    ```
3. Set up environment variables (see `.env.example`).
4. Start the server:
    ```bash
    npm start
    ```

## Usage

- Ensure MongoDB is running.
- Use tools like Postman or curl to interact with the API.
- Register or log in to obtain an authorization token.

## API Endpoints

| Method | Endpoint           | Description                  |
|--------|--------------------|-----------------------------|
| POST   | `/tasks`           | Create a new task           |
| GET    | `/tasks`           | Get all tasks (with filters)|
| GET    | `/tasks/:id`       | Get a specific task         |
| PUT    | `/tasks/:id`       | Update a task               |
| DELETE | `/tasks/:id`       | Delete a task               |

**Filtering:**  
Use query parameters `status` and `priority` with `GET /tasks`.

**Authorization:**  
Include your token in the `Authorization` header for protected routes.
