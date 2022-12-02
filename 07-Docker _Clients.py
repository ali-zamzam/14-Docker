"""Docker - Clients"""

"""1. Docker Desktop
Docker Desktop is an application for MacOS or Windows that offers a graphical interface to manipulate the various objects created 
by Docker. If you want to learn more, you can go to this link.
"""
"""2.Portainer
Portainer is an Open Source Docker GUI, which runs in a container. Its handling is quite intuitive and its launch is rather 
simple:"""

# docker volume create portainer_data

# docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce

"""You can then go to port 9000 of the machine and explore the different menus."""
# ------------------------------------------------------------------------------------------------------------------
"""3.Python client
Python is the most used language in the world of Data Science. You can use the docker library (pip3 install docker) to create, 
list, launch or delete different objects.

For example, we can launch a container using the following code:"""

from docker import DockerClient

client = DockerClient()

client.containers.run(
    image="datascientest/neo4j:latest",
    name="my_neo4j",
    detach=True,
    auto_remove=True,
    ports={"7474/tcp": 7474, "7687/tcp": 7687},
    network="bridge",
)

# printing names of active containers
for c in client.containers.list():
    print(c.name, c.image)


# https://docker-py.readthedocs.io/en/stable/index.html
