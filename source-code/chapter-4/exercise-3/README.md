### README

This directory contains the source code for the third exercise of chapter 4. In this exercise, we compose a Dockerfile for Newsbot and then use the Dockerfile to build a Docker image and run the container.


### Building the Docker image

Build the image using the below command

```
docker build -t sathyabhat/newsbot
```

Run the container using 

```
docker run -e NBT_ACCESS_TOKEN=<token> sathyabhat/newsbot
```

Replace `<token>` with the Telegram API Token that was generated. 