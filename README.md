# Monitoring Tool
### This is a monitoring tool that allows you to monitor your logs in real-time, fetch and analyze logs, and generate reports, and visualizations.

## Requirements
- Docker
- Docker Compose

## How To Use
- Create a docker-compose.yml file
- Copy content from my docker-compose.yml file to your docker-compose.yml file
- Run `docker compose pull` to pull the latest images
- Run `docker compose up -d` to start the containers

## Docker Compose File
- [docker-compose.yml](https://github.com/MawuliB/monitor-tool/blob/main/docker-compose.yml)

## Note
- This is a work in progress
- This app uses port 8000 and 4200
- For Local logs the app uses the /var/log directory
- For AWS logs the app uses the CloudWatch logs (Log Groups)
