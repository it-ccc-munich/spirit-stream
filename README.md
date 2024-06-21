# Make sure the submodule is configured and pulled
```commandline
git submodule init
git submodule update --recursive --remote
```

There is a folder named "Security", that comes with the submodule. It contains sensitive account and authorization information that is separated in to different private github repository.

These sensitive information is injected in the runtime. If you want to run all the functions and use tools with authorization information from our provided source. Please contact contributors and our church managers. 

# Test

### Build the docker image
```commandline
docker build -f "Dockerfile_test" -t europe-west9-docker.pkg.dev/church-service-automation/ccc-church-automation/spirit-stream-test-py:latest .
```
### Run the container for testing
This is designed to run the **test.py** file within this repository. 
```commandline
docker run -it --rm europe-west9-docker.pkg.dev/church-service-automation/ccc-church-automation/spirit-stream-test-py:latest
```

# Production

### Build the docker image for main automation functions
```commandline
docker build -f "Dockerfile_main" -t europe-west9-docker.pkg.dev/church-service-automation/ccc-church-automation/spirit-stream-main-py:latest .
```

### Run the container for main automation functions (should not be manually triggered)
This is designed to run the **main.py** file within this repository. 
```commandline
docker run -it --rm europe-west9-docker.pkg.dev/church-service-automation/ccc-church-automation/spirit-stream-main-py:latest
```

# Push Built Images

The CI/CD steps should be automatically configured by pushing an update to the main branch soon. 

It has to be manually done for now. 

To push the built images: 
1. Make sure google cloud cli is installed by following https://cloud.google.com/sdk/docs/install-sdk
2. Run ```gcloud auth configure-docker europe-west9-docker.pkg.dev```
3. Run ```gcloud auth login``` and login with your credentials. (make sure your account is allowed to use the resources by talking to our contributor or project administrator)
4. Run ```docker push europe-west9-docker.pkg.dev/church-service-automation/ccc-church-automation/spirit-stream-test-py:latest``` to push the built test image with `latest` tag.
5. Run ```docker push europe-west9-docker.pkg.dev/church-service-automation/ccc-church-automation/spirit-stream-main-py:latest``` to push the built main image with `latest` tag.
6. The automatic triggers and execution should be configured on Google cloud platform. https://console.cloud.google.com/run/jobs?project=church-service-automation

For any further questions, please contact project contributors and administrators. 