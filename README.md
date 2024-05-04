# mlops-template
A simple and flexible project template for MLOps.


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![Railway](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

Loguru, Pydantic, Railway, FastAPI, CircleCI
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
We use [CircleCI](https://circleci.com/product/) as the CI/CD platform in the project. The other alternatives for CI/CD platfforms include Jenkins, GitLab CI and Travis CI, which are equally good. 