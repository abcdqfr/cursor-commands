# docker-logs

Tail logs from Docker containers to check for errors and monitor application behavior.

1. **Discover running containers** - List all running containers to see what's available using `docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Image}}"`
2. **Ask user which container(s)** - Present the list and ask which container(s) they want to monitor
3. **Use appropriate command** - Run `docker logs` with suitable flags based on their needs (follow, timestamps, tail, since time, filters)

Focus on:
- Container discovery and selection
- Appropriate log command selection
- Error filtering and monitoring
- Timestamp and tail options
- Follow mode for real-time monitoring

Consider both:
- Single container monitoring
- Multiple container monitoring (docker compose)

Format the output as:
- List of available containers
- Selected container(s) and command used
- Log output with appropriate formatting
- Error highlights if filtering for errors

Common commands:
- `docker ps` - List running containers
- `docker logs -f <container>` - Follow logs
- `docker logs -f --timestamps <container>` - Follow with timestamps
- `docker logs -f --tail 100 <container>` - Follow last 100 lines
- `docker logs -f --since 5m <container>` - Follow since 5 minutes ago
- `docker compose logs -f` - Follow all compose services
- `docker logs <container> 2>&1 | grep -i error` - Filter for errors

Tail Docker container logs with appropriate options for effective debugging and monitoring.
