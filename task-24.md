## API Server Metrics (Last 24h)

| Metric                | Value                |
|-----------------------|---------------------|
| Average response time | 230ms               |
| 95th percentile       | 450ms               |
| 99th percentile       | 1200ms              |
| Request count         | 15,000              |
| 5xx errors            | 120                 |
| CPU usage (avg / max) | 45% / 80%           |
| Memory usage (avg / max) | 2.1GB / 3.5GB (of 4GB) |

---

**Observations:**
- Response times are generally good, but 99th percentile spikes to 1200ms.
- 5xx errors (120) may indicate stability or reliability issues.
- CPU and memory usage are within limits, but memory is approaching the maximum.
- Consider investigating error causes and optimizing for high-percentile latency.
- Monitor resource usage to avoid hitting hardware limits.