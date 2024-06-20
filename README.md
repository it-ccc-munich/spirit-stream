# Make sure the submodule is pulled
```commandline
git submodule update --recursive --remote
```

There is a folder named "Security", containing sensitive account and authorization information that is separated in to different github repo.

These sensitive information is injected in the runtime. If you want to run all the functions and use tools with authorization information from our provided source. Please contact contributors and our church managers. 

# Build the docker image for testing
```commandline
docker build -f "./Dockerfile_tests" -t my-python-app-tests .
```

# Run the container for testing
```commandline
docker run -it --rm my-python-app-tests
```

# Build the docker image for main functions
```commandline
docker build -f "./Dockerfile_main" -t my-python-app .
```

# Run the container for main functions
```commandline
docker run -it --rm my-python-app
```
