This project serves as an example for writing Automation(Selenium, Rest Api and Web-socket) using Gauge
Installation Help Documentation - https://docs.gauge.org/getting_started/installing-gauge.html?os=windows&language=python&ide=vscode

**Pre-requisites (Install the following softwares)** -

	pip install getgauge==0.3.17 –user
	pip3 install --upgrade protobuf==3.20.0
	pip install selenium
	pip3 install websocket-client
	python -m pip install requests
	pip install webdriver-manager<br>
  
**To generate reports** - 

	gauge install html-report
	gauge install json-report
	gauge install xml-report
	gauge install spectacle
	gauge install flash

**To generate spectacle report** -

	gauge docs spectacle

**Run specific features with environment files** –  

	gauge run --env="default" specs
	
**Run specific feature file** – 

	gauge run .\specs\login_csv.spec


**Suppose that you have a specification file, called let say Login.spec, and you want to list all the scenarios or tags. Below command can be used :**

	gauge list --tags specs/login.spec
	gauge list --scenarios specs/login.spec

**Gauge Tests Dockerization** -

This is an example project that demonstrates how to Dockerize a Gauge project with Python and Requests.

**Prerequisites**:

To run this project, you will need to Docker installed on your machine.
	
**Building the Docker Image** -

To build the Docker image for this project, run the following command:

	docker build -t gauge-tests .
	
This command will create a Docker image with the name gauge-tests based on the instructions in the Dockerfile in the root directory of the project.

**Running the Tests**
To run all the specs in the project, use the following command:

	docker run --rm -v <project root directory>:/app gauge-tests gauge run app/demo/features/specs
	Example:
	docker run --rm -v C:\Project\Python\gauge-tests:/app gauge-tests gauge run app/demo/features/specs

This command will start a Docker container with the gauge-tests image and run the Gauge tests in the app/demo/features/specs directory inside the container.

**To run a specific spec file, use the following command**

	docker run --rm -v C:\Project\Python\gauge-tests:/app -w /app/demo gauge-tests gauge run features/specs/rest_api.spec
	
This command will start a Docker container with the gauge-tests image, set the working directory to app/demo, and run the rest_api.spec file inside the container.

**Conclusion**

With Docker, you can easily package and run Gauge projects in a consistent and isolated environment. By following the steps in this README, you should be able to Dockerize your own Gauge projects and run them anywhere with minimal setup.



