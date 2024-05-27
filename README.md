# mlops-template
MLOps project template to integrate robust and reliable machine learning pipelines in production.


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![Railway](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)




Loguru, Pydantic, Railway, FastAPI, CircleCI, Gemfurry

## Observability (Tracking the logs)
Python based [logging](https://docs.python.org/3/library/logging.html) module is a common way to to track events that happen when some software runs to provide observability about the code running. 

In this project template, we use [Loguru](https://loguru.readthedocs.io/en/stable/) which is a Python module built-in with the `logger`functionalities. It is intended to make Python logging less painful by adding a bunch of useful functionalities that solve caveats of the standard loggers. 

## Portability (Building the ML model package)
To generate the distribution package for the model, we use [PyPA](https://packaging.python.org/en/latest/). It would create a versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a release. Later, this distribution package could be installed via `pip` to import it as a module.

#### Steps to build the model package:
##### 1. Make sure you have the latest version of PyPA’s build installed:

```
  python3 -m pip install --upgrade build  # for Unix/macOS
  py -m pip install --upgrade build     # for Windows
```

##### 2. Run this command from the same directory where `pyproject.toml` is located:

```
  python3 -m build  (for Unix, macOS)
  py -m build     (for Windows)
```
## Scalibility
Machine learning models deployed in production often need to handle numerous inference requests simultaneously, especially in high-traffic environments. In this project, we use [Uvicorn](https://www.uvicorn.org/) as the ASGI web server. Uvicorn's asynchronous architecture makes it well-suited for this task, ensuring that the model serving infrastructure can scale effectively to meet demand. It is used in conjunction with a PaaS provider (like Railway) in order to get and post requests from/to the server. 

## Deployment
We deploy our Titanic Survival Predictor app on Platform as a Service (PaaS) using [Railway App](https://railway.app/). There are other PaaS providers like Microsoft Azure, Heroku, AWS etc. In this MLOps project template, we use Railway for simplicity because its free of charge for first 500 hours.


#### Installation of Railway App to local machine using Shell terminal

```
  bash <(curl -fsSL cli.new)  (for macOS, Linux, Windows)
```

Once installed, run following commands in current project working directory (`api`) to start the project deployment on Railway:

```
# authenticate CLI to your Railway account
railway login

# Link to a project (in current project directory)
railway link

# Deploy the linked project directory
railway up --detach
```

_More information on the CLI commands for Railway can be found [here](https://docs.railway.app/guides/cli#authenticating-with-the-cli)._

As soon as the project is deployed to Railway, the build is started which could be seen in the Railway App web interface. Once the build is completed, we need to create a general domain to view our deployed model on the server. This could be done by opening the service being used in the Railway App web interface: `Settings -> Generate Domain (in Environment section)`. 

At the end, we get a server of our own (eg. `https://luminous-eagerness-production.up.railway.app/docs`) which could be accessed to run the ML app via web interface. 

## CI/CD 
We use [CircleCI](https://circleci.com/product/) as the CI/CD platform in the project. This tool helps in automating the training, testing and deployment of the model in the cloud. It provides a seemless CI/CD by avoiding the use of commands via local terminal, instead runs the commands using the CircleCI configuration file. This leads to a minimal usage of manual labor in integration and deployment, ultimately reducing the chances of error. (The other alternatives for CI/CD platfforms include Jenkins, GitLab CI and Travis CI, which are equally good.)

## Publishing Python Packages
In order to publish python packages, we have free servers like [PyPI](https://pypi.org/). However, there are scenarios where the packages shall be privately kept in servers to avoid public access. In such cases, we need private servers wherein we could publish the packages. [Gemfurry](https://gemfury.com/) is one such cloud package repository which provides free service to publish our packages publicly as well as privately. 

We use this hosted repository by providing the index URL of the repository to our `requirements.txt` file, which is used by the `pip` module to install the our python package.

## Differential test
A differential test compares the predictions between two different versions of a machine learning model. In cases where accuracy is really important, these type of tests are crucial in detecting subtle and insidious issues that do not cause any exceptions or failures in the code, but vcould be ignored in the usual testing scenario where the predcitions for the same input have been affected. A naive example for such a scenrio could be that the new machine learning model migth be missing a preprocessing step, or missing out a feature etc. Differential testing is all about catching such issues in the model before it goes into production. 

We perform differetnial test in this rpoject using [PyTest](https://docs.pytest.org/en/latest/how-to/mark.html).

## Docker
![Docker in Practise](https://drek4537l1klr.cloudfront.net/miell/Figures/01fig02_alt.jpg)

Docker provides the ability to package and run an application in a loosely isolated environment called a container. The isolation and security lets you run many containers simultaneously on a given host. Containers are lightweight and contain everything needed to run the application, so you don't need to rely on what's installed on the host. You can share containers while you work, and be sure that everyone you share with gets the same container that works in the same way.

If you want to dig deep into the usage of Docker, I would suggest you to have a look at these two books:
  - [Docker in Action](https://livebook.manning.com/book/docker-in-action-second-edition/) (for basics)
  - [Docker in Practise](https://livebook.manning.com/book/docker-in-practice/) (for advanced usage)

#### Docker v/s Virtual Machine
Unlike virtual machines, Docker containers don’t use any hardware virtualization. Programs running inside Docker containers interface directly with the host’s Linux kernel. Many programs can run in isolation without running redundant operating systems or suffering the delay of full boot sequences. This is an important distinction. Docker is not a hardware virtualization technology. Instead, it helps you use the container technology already built into your operating system kernel.

Virtual machines provide hardware abstractions so you can run operating systems. Containers are an operating system feature. So you can always run Docker in a virtual machine if that machine is running a modern Linux kernel. Docker for Mac and Windows users, and almost all cloud computing users, will run Docker inside virtual machines. **So these are really complementary technologies.**

#### Deploying with Docker Container
Follow below steps to use a Dcoker container to deploy the application. The `requirements.txt` of the applicaiton contains the `PIP_EXTRA_INDEX_URL` which serves as the link to the Gemfury private repository where our model package is located. The dcoker image is designed such that it first fetches all the required packages to run the application, and then runs the application. 

```
# add Docker path to local directory
export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"

# build docker image
docker build --build-arg PIP_EXTRA_INDEX_URL=<Your-Gemfury-Token-Here> -t api:latest .

# run docker container
docker run -p 8001:8001 -e PORT=8001 api 
```