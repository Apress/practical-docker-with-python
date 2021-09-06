In this exercise, we will set up a Continuous Integration workflow for Newsbot that will run flake8, build the Docker image, and push the resulting image to Docker Hub. The Continuous Integration workflow will be set up using GitHub Actions, but the same principle could be applied using any Continuous Integration tool.

This exercise also assumes that we will be working with the Newsbot source code and the Dockerfile from Chapter 7, Exercise 2. You can find the GitHub Actions Workflow file in [.github/workflows/build-newsbot.yaml](../../../.github/workflows/build-newsbot.yaml)

