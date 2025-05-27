## How to Solve High Memory Usage in a Docker Container

1. **Set Memory Limits**  
    Use the `--memory` flag to restrict container memory:
    ```sh
    docker run --memory="512m" my-image
    ```

2. **Optimize Application Code**  
    - Fix memory leaks.
    - Use efficient data structures.
    - Release unused resources.

3. **Use Alpine or Slim Base Images**  
    Smaller images reduce memory footprint.

4. **Monitor Container Usage**  
    Use `docker stats` to monitor memory:
    ```sh
    docker stats <container_id>
    ```

5. **Tune Garbage Collection (for Java, Node.js, etc.)**  
    Adjust runtime memory settings (e.g., `JAVA_OPTS`, `NODE_OPTIONS`).

6. **Reduce Number of Processes**  
    Limit background tasks and unnecessary services.

7. **Multi-Stage Builds**  
    Remove build-time dependencies from the final image.

8. **Restart Policy**  
    Use `--restart` to automatically recover from OOM errors.

**References:**  
- [Docker Docs: Runtime Options](https://docs.docker.com/config/containers/resource_constraints/)


## Additional Tips

- **Profile Memory Usage**  
    Use tools like `top`, `htop`, or language-specific profilers inside the container to identify memory hotspots.

- **Use Swap Carefully**  
    Configure swap with `--memory-swap` if needed, but avoid relying on swap for production workloads.

- **Update Dependencies**  
    Regularly update libraries and base images to benefit from performance and memory improvements.

- **Container Orchestration**  
    In Kubernetes, set `resources.limits.memory` and use liveness probes to handle unhealthy containers.

- **Documentation and Logging**  
    Enable detailed logging to help trace memory spikes and correlate with application events.