# Yara Malware Regex Detection
Detect malware in a string with malware rules and Yara

## Development

Build the development container with
```bash
# Create a user-defined network locally
docker network create -d bridge my-net

# build development container
docker build -t yara:dev -f Dockerfile.dev .

# build production container
docker build -t yara:latest -f Dockerfile.prod .

# -t tag
# yara:dev container_name: yara, tag: dev
# Dockerfile.dev development dockerfile
```

Run Jupyter Lab automatically on container start (expose ports)
```bash
docker run -p 8888:8888 --network=my-net yara:dev
```

Run Production Container with Uvicorn Command to Up Backend
```bash
docker run -d -p 5000:5000 --network=my-net yara:dev uvicorn src.app.main:app --reload --host 0.0.0.0 --port 5000
```

## References
https://github.com/Yara-Rules/rules

