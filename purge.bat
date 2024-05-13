@echo off
REM Stop and remove all running Docker containers
for /f "tokens=*" %%i in ('docker ps -aq') do (
    docker rm -f %%i
)

REM Prune all Docker images
docker image prune -a
