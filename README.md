# Docker-Learning  

Installed Docker Desktop + needed to install WSL (Ubuntu on Windows)  
- Docker installed, used `docker --version` on PowerShell to check if it has installed.  
- Used `docker info` - showed info about system, detailed  

Ran `docker hello world`  
- `docker ps -a` showed all containers (historical too)    

Had an error, whilst trying to run a python script ‒ found out, I wasn't in the right directory 🤦🏻‍♂️  

ran a hello world python script ‒ web page server on local port  
> - Used flask ‒ Flask, easy web-app builder in Python.  
> - POINT= To understand how a web application works (before we try to containerise it in docker)  

- use `touch Dockerfile` to  create Dockerfile.  

tried to run `docker build -t flaskImage .`  
> - ERROR: failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine; check if the path is correct and if the daemon is running: open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.  
> - I had to open the DockerDesktop app on my PC then  it started to work.  
- Next Error: I used a capital letter for the image name.  
> - repository name must be lowercase

CMD command in Dockerfile= run our "python" application "app.py", (web  app built using flask) ‒ it links with our script  
Ran, worked Alhamdulillah (used, `docker run -d -p 5000:5000 flask-image`). docker ps, showed it running. docker stop (ID), stopped the container.  
- Can set name/ custom identifier, to containers, with --name  
- Can connect container to a network, using --network <net_name>, so containers can connect to other services, like a mySQL database.  
- > Can also use --network <net_name>, to use container names, as host names, instead of IP addresses (in other services, like mySQL db)    

-p 5000:5000, maps port 5000 in host machine With port 5000 in container. ‒ Exposes Flask app to outside world, allowing access by http://localhost:5000  
  
  <br>
- image contains flask application code & necessary depc'ies  

- 'docker build', reads instructions from Dockerfile, initiates image creation process (builds image)  
- Dockerfile **builds image**.  
- -t command in docker build assigns a **name** (tag) to the image coming out from this Dockerfile.  
> - A **name**/ ref, for the docker image, Can be useful when knowing what image, a container is using ‒ could possibly use image in future too.  
Eg, `docker build -t flask-image-mysql .`, creates a new image, calls it: flask-image-mysql, attaches default tag: `latest`, constructs a Docker image (takes depc'ies/ code from here, ie.) **from the Dockerfile** in the current directory  
  
Quick-fire: What's the difference between RUN and CMD in a Dockerfile?   
> `RUN` is used to **build** the **image**. `CMD` is used when we actually wanna **start**/ execute the **container** (program.)  
> Fun fact: You can Only Have ONE `CMD` command in a Dockerfile.  

Whilst trying to make a web app in Docker (using flask and mySQL db),  
- encountered problem with building image (ERROR: failed to build: failed to solve: process "/bin/sh -c pip install flask mysqlclient" did not complete successfully: exit code: 1)  
**Purpose of project:** working with Docker Networking (which enables containers  to communicate with each other.)  
- Some steps I did were:  
> - Created a new **network** with: `docker network create my-customnet`  
> - Created a -d; **detached** (background ) container, assigned --name; `mydb`, used image; `mysql`, version, 5.7, connected container to --network; my-customnet (Allows COMMUNICATION w/ other containers on that network), set root password  
> > - docker run -d --name mydb --network my-customnet -e MYSQL_ROOT_PASSWORD=the-password mysql:5.7  
> > - MySQL:5.7 ‒ if not found locally, (image) to be pulled from Docker Hub.  
- When I tried to build flask image, I encountered an error with my Dockerfile command, `RUN pip install flask mysqlclient`  
> - Could not build image, led to could not create background container (myapp)  
> - Needed to add code,  
> `RUN apt-get update && apt-get install -y \`  
    `gcc \`  
    `python3-dev \`  
    `libmariadb-dev \`  
    `pkg-config`  
>   - tried to build image again, Alhamdulillah, worked.  

Just a quick, Why do Containers start in detached mode (-d, background)?  
> Allows terminal to be used for other commands.  

- When trying to run the web app, on localhost:5000, Ran into the error, Internal Service Error, checked Docker logs for myapp container, saw, 'MySQLdb.OperationalError: (2005, "Unknown server host 'mydb' (-2)")' ‒ checked to see if container mydb was running (on Docker Desktop) and it was not!    
- I realised that, the container, myapp, connects to the, mydb, container (they work with each other) and More Specifically, mydb is a dependency of the myapp container.  
> - To fix the problem, I deleted the offline, mydb, container (realised later I could've just re-started it 🤦‍♂️), ran the command, "docker run -d --name mydb --network my-customnet -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:5.7", in VSCode, checked if the container/s were running with, docker ps, and they were, Alhamdulillah.   
> - <img width="1024" height="178" alt="image" src="https://github.com/user-attachments/assets/9eb374d4-9cdb-454e-9c89-83e31d7bd693" />  
> - <img width="989" height="450" alt="image" src="https://github.com/user-attachments/assets/ef60ede2-8d10-4d86-a0ef-d48980735403" />  
> - Web app working on localhost:5000  
> - <img width="406" height="109" alt="image" src="https://github.com/user-attachments/assets/40fbf95a-0ec7-4929-8e60-4df35d2c4605" />  
  
    
If I wanted to make a database container, I'll need to use a base Image (think foundations of a building can be same; base image being same, but different buildings could be built on top, ie. different containers could have, same image..)  
- The baseimage may require setting/ config. of Environment Variables like mySQL  (setting a Password)  
- A Docker Compose Volume is like a shared storage drive for containers, so Data isn't lost . Think RAM, is before a Volume, HDD, is after creating a volume.  
> - Solves issue of, Closing Container and Losing All Data in it. + not being able to share data b/w containers.    
> - One could share Volume/ Data, across containers.  

- Could also use docker init creates the files; readme, Dockerfile, .dockerignore etc..  
  
- Use docker push/ pull to upload/ download images to/ from Docker Hub, respectively.   
  
- Practiced Docker push/ pull of images to DockerHub (had to docker build -t username/repo ., looks for Dockerfile)  
<Br>
Amazon ECR= Private Docker Reigstry (widely used in prod. env's)

- Used Amazon ECR to manage Docker image; try imitate a production environment.    
> - Used Docker Networking so containers could interact with each other; docker push/ pull commands from Amazon AWS ECR  
- Docker Registry is a system for 'storing' and sharing Docker "Images".  
  
We are getting ("pulling") the image from AWS ECR and using that, instead of building the Docker image locally ‒ in Docker-compose file, replace, `build: .`, with, `image: <ECR Repo link from AWS with :tag>` AND USE **docker compose up**  
> Using an Docker image repo link from the cloud (our case, AWS ECR) Instead of building our own ‒ can be helpful in Collaboration projects  

What to do If Image too big, taking up lots of space? Use multi-stage builds    

## Making Our Image Lighter: Multistage Builds (we optimise our Dockerfile)  
- Removed build tools, only kept what was needed for runtime environment; Image build reduced from **724MB**  
- <img width="611" height="73" alt="image" src="https://github.com/user-attachments/assets/d8828ab0-b4a4-48ca-a751-c4a1b14f5a6f" />  
- With the Code:  
`FROM python:3.8-slim`  
`WORKDIR /app`  
`COPY . .`  
`RUN apt-get update && apt-get install -y \`  
    `gcc \`  
    `python3-dev \`  
    `libmariadb-dev \`  
    `pkg-config`  
`RUN pip install flask mysqlclient`  
`EXPOSE 5000`  
`CMD ["python", "app.py"]`  
- To **189MB** with the Multistage Build -- a 73+% decrease in image size!    
- <img width="592" height="75" alt="image" src="https://github.com/user-attachments/assets/32ad9a16-cb57-4a61-8d62-a197665f3e29" />  
- > Code:  
- > <img width="458" height="541" alt="image" src="https://github.com/user-attachments/assets/38516f2f-ff38-4587-9f88-0097b88175ed" />  
  
> When app grows larger in scale (multi container situation..), we look at Kubernetes (k8s)  

<Br>

**k8s:** hundreds/thousands container mgmt./ orchestration ‒ helps developer's manage code ‒ helps microservice architechture mgmt.  
> docker swarm no auto scaling, k8s has auto-scaling.  
> when grows larger in scale ‒ useful   
