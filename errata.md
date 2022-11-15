# Errata for *Book Title*

On **page 6** [Figure captions interchanged]:
 
On page 6 and page 7, the captions for **Figure 1-1 and Figure 1-2 are interchanged**. The caption for Figure 1-1 should read _Representation of three apps running on three different virtual machines_ and the caption for Figure 1-2 should read _Representation of three apps running on three different containers_.

***

On **page 27** [Extra word on the sentence about inter-daemon communication]:
 
On page 27, in the chapter paragraph about Docker daemon, the example sentence mentions _Some examples of inter-daemon communication include communication Datadog for container metrics monitoring and Aqua for container security monitoring_. This should **actually read** _Some examples of inter-daemon communication include Datadog for container metrics monitoring and Aqua for container security monitoring_

***


For the **Telegram chat bot exercises** [Docker image has been updated]: 
 
The exercises refer to Docker iamge to be used as `FROM python:3-alpine`. Due to some breaking changes in Python versions and dependencies, this causes **Docker image to not build**. 
For this reason, the Docker images have been **updated** to refer to **Python 3.9** image and as a result, the FROM line has been updated to `FROM python:3.9-alpine` in place of the existing `FROM python:3-alpine`.
