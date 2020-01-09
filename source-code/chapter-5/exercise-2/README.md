### README

This exercise contains the source code for the second exercise of chapter 5. In the previous chapters’ exercises, we wrote a Dockerfile for our project. However, as you might have noticed, killing the container would reset the state and we need to customize our bot all over again.

For this exercise, we will be working on a slightly modified codebase that has support for saving the preferences to a SQLite DB. We would use Docker Volumes to persist the database across containers.
