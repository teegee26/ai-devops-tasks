## Jenkins Pipeline Stage Explanations

### 1. Checkout Code
- **What happens:** Retrieves the source code from the version control system (e.g., Git) using the `checkout scm` command.
- **Best practice:** Always start with a clean and up-to-date codebase. Use shallow clones if possible for faster builds.

### 2. Install Dependencies
- **What happens:** Installs all required Node.js dependencies using `npm install`.
- **Best practice:** Use a lock file (`package-lock.json`) to ensure consistent dependency versions. Cache dependencies to speed up builds.

### 3. Run Tests
- **What happens:** Executes the project's test suite with `npm test`.
- **Best practice:** Run tests in isolation and fail the build if any test fails. Collect and archive test reports for visibility.

### 4. Build App
- **What happens:** Builds the application (e.g., compiles code, bundles assets) using `npm run build`.
- **Best practice:** Ensure the build is reproducible and does not rely on external state. Store build artifacts if needed.

### 5. Build Docker Image
- **What happens:** Builds a Docker image using the Dockerfile in the repository, tagging it with the build number.
- **Best practice:** Use meaningful and unique tags (e.g., commit SHA or build number). Keep Dockerfiles clean and minimal.

### 6. Publish Docker Image
- **What happens:** Authenticates with Docker Hub and pushes the built image to the registry.
- **Best practice:** Use credentials securely (never hard-code them). Push images only after successful builds and tests.

### Post Actions
- **What happens:** Cleans up the workspace after the pipeline finishes, regardless of success or failure.
- **Best practice:** Always clean up to avoid disk space issues and ensure a fresh environment for each build.

---

## General Jenkins Pipeline Best Practices

- **Use Declarative Pipelines:** They are easier to read, maintain, and enforce best practices.
- **Keep Stages Modular:** Each stage should have a single responsibility.
- **Fail Fast:** Stop the pipeline early if a critical stage fails.
- **Use Environment Variables:** Store configuration and secrets securely.
- **Archive Artifacts and Reports:** For traceability and debugging.
- **Automate Everything:** From testing to deployment, minimize manual steps.
- **Monitor and Maintain:** Regularly update dependencies and Jenkins plugins.
