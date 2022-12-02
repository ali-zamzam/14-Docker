"""Docker-Compose"""
# https://docs.docker.com/compose/install/linux/

"""Docker Compose is a tool that allows you to launch a set of Docker containers at the same time. 
If an application must use several containers, launching all these containers at once is very practical. 
One of the common uses of Docker Compose is to create test environments: for example, if you have to test a 
script that must interact with an interaction, you can launch a set of containers that will constitute the test set. 
In particular, Docker Compose is not used to create a set of containers on different machines but on a single machine."""
# ---------------------------------------------------------------------------------------------------------------------
"""In a docker-compose.yml file, paste the following lines:"""


# nano docker-compose.yml

# version: "3.9"
# services:
#   jupyter:
#     image: jupyter/minimal-notebook:ubuntu-18.04
#   elasticsearch:
#     image: elasticsearch:7.2.0


"""Save the file, exit it and run the following command
"""
# docker-compose up

"""We can see that we were able to create a container: an instance of jupyter/minimal-notebook. In the docker-compose.yml file, 
we can see two services jupyter and elasticsearch: this file is actually supposed to launch two containers but as we have seen 
before, ElasticSearch images require that we define a variable d 'environment. Environment variables can be specified using 
the environment keyword.

Containers launched by Docker Compose can be stopped by using ctrl + C in the console in which docker-compose up was 
performed or by typing docker-compose down in another console."""

# ---------------------------------------------------------------------------------------------------------------------
"""Stop containers launched by Docker Compose

Replace the contents of the docker-compose.yml file with the following lines"""

# version: "3.9"
# services:
#   jupyter:
#     image: jupyter/minimal-notebook:ubuntu-18.04
#   elasticsearch:
#     image: elasticsearch:7.2.0
#     environment:
#       discovery.type: single-node

"""Exit this file, run the command docker-compose up then list the containers in operation

This time we can see that the containers are both in operation. To be able to use jupyter, port 8888 of the container must be 
forwarded to one of the ports of the host machine."""
# ---------------------------------------------------------------------------------------------------------------------
"""Replace the contents of the docker-compose.yml file with these lines, then restart the Docker Compose services"""

# version: "3.9"
# services:
#   jupyter:
#     image: jupyter/minimal-notebook:ubuntu-18.04
#     ports:
#       - target: 8888
#         published: 4444
#         protocol: tcp
#         mode: host
#   elasticsearch:
#     image: elasticsearch:7.2.0
#     environment:
#       discovery.type: single-node

"""Here we forward port 8888 to port 4444 of the host machine. You can open this port to get to the jupyter GUI. 
Note that there is another way to forward ports. For example, if we want to forward ports 9200 and 9300 of the elasticsearch 
container to those of the host machine, we can do:"""

# version: "3.9"
# services:
#   jupyter:
#     image: jupyter/minimal-notebook:ubuntu-18.04
#     ports:
#       - target: 8888
#         published: 4444
#         protocol: tcp
#         mode: host
#   elasticsearch:
#     image: elasticsearch:7.2.0
#     environment:
#       discovery.type: single-node
#     ports:
#       - "9200:9200"
#       - "9300:9300"

# --------------------------------------------------------------------------------------------------------------------------------
"""You can also specify the networks or give a name to the containers. In the following code, we place the containers on the 
my_network_from_compose network, we rename them my_jupyter_from_compose and my_es_from_compose. Finally, we specify that the 
password to use to use jupyter is bonjour."""

# version: "3.9"
# services:
#   jupyter:
#     image: jupyter/minimal-notebook:ubuntu-18.04
#     container_name: my_jupyter_from_compose
#     networks:
#       - my_network_from_compose
#     ports:
#       - target: 8888
#         published: 4444
#         protocol: tcp
#         mode: host
#     environment:
#       JUPYTER_TOKEN: "bonjour"
#   elasticsearch:
#     image: elasticsearch:7.2.0
#     container_name: my_es_from_compose
#     networks:
#       - my_network_from_compose
#     ports:
#       - "9200:9200"
#       - "9300:9300"
#     environment:
#       discovery.type: single-node
# networks:
#   my_network_from_compose:

"""Once the services are started, go to the browser to your virtual machine's IP address and port 4444, you will need to have 
the jupyter interface."""

# ---------------------------------------------------------------------------------------------------------------------
"""In a new notebook, run the following code:"""

import json
import pprint

import requests

content = json.loads(requests.get("http://my_es_from_compose:9200").content)

pprint.pprint(content)

# -------------------------------------------------------------------------------------------------------------------
"""Finally, you can specify to create mount points by specifying volumes. For example, in the following code, we can link the 
work folder of the container to the local folder:"""

# version: "3.9"
# services:
#   jupyter:
#     image: jupyter/minimal-notebook:ubuntu-18.04
#     container_name: my_jupyter_from_compose
#     networks:
#       - my_network_from_compose
#     volumes:
#       - .:/home/jovyan/work
#     ports:
#       - target: 8888
#         published: 4444
#         protocol: tcp
#         mode: host
#     environment:
#       JUPYTER_TOKEN: "bonjour"
#   elasticsearch:
#     image: elasticsearch:7.2.0
#     container_name: my_es_from_compose
#     networks:
#       - my_network_from_compose
#     ports:
#       - "9200:9200"
#       - "9300:9300"
#     environment:
#       discovery.type: single-node
# networks:
#   my_network_from_compose:

"""Docker Compose therefore makes it easy to launch a set of containers. Here we have seen the main arguments of Docker Compose. 
Note that if we want to launch containers on a distributed system, we will use tools like Docker Swarm or Kubernetes."""
