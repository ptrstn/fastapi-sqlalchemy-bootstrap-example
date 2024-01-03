[![Python package](https://github.com/ptrstn/fastapi-sqlalchemy-bootstrap-example/actions/workflows/python-package.yml/badge.svg)](https://github.com/ptrstn/fastapi-sqlalchemy-bootstrap-example/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/github/ptrstn/fastapi-sqlalchemy-bootstrap-example/graph/badge.svg)](https://codecov.io/gh/ptrstn/fastapi-sqlalchemy-bootstrap-example)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-darkblue.svg)](http://unlicense.org/)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

# FastAPI + SQLAlchemy + Bootstrap + Pytest Example

This application is a simple REST API built with FastAPI, SQLAlchemy and Bootstrap and tested with pytest. 
It allows for basic operations for managing users and items.

This code is in the public domain, so feel free to do with it whatever you want.

## Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/ptrstn/fastapi-sqlalchemy-bootstrap-example/
cd fastapi-sqlalchemy-bootstrap-example
python -m venv venv
. venv/bin/activate
```

Then install the package (and the optional testing dependencies) with:

```bash
pip install -e .[test]
```

## Usage

```bash
uvicorn src.mypackage.main:app --reload
```

### Docker

If you want to run the application inside a Docker container you have two options.

#### docker-compose.yml

With an applicable ```docker-compose.yml``` file in the project directory, 
you only need to run one command to build and start all the services:

```bash
docker-compose up --build
```

By default, docker-compose will look for files named ```docker-compose.yml``` in the project directory.

Get a shell inside the Docker container:

```bash
docker-compose exec web sh
```

#### Dockerfile

Build the Docker image using the ```Dockerfile```. Replace ```my-image-name``` with the name you want to give to your Docker image.

```bash
docker build --tag my-image-name .
```

Run the Docker image as a container. Replace ```my-image-name``` with the name of your Docker image. 
This command will run your container and map port ```8080``` in the container to port ```80``` on your host machine.

```bash
docker run --detach --name my-container-name --publish 80:8080 my-image-name
```

Optional: To attach it use: 

```bash
docker attach my-container-name
```

Get a shell inside the Docker container:

```bash
docker exec -it my-container-name /bin/bash
```

To stop and remove the container do:

```bash
docker stop my-container-name
docker rm my-container-name
```

## Endpoints

### User Endpoints

- **POST /users/**  
  This endpoint creates a new user. 
  It accepts a JSON body with email and password fields and creates a new user record in the database. 
  If successful, it returns the details of the created user. 
  If a user with the specified email already exists, it returns a 422 Unprocessable Entity error with a message indicating that the email is already registered.
- **GET /users/**  
  This endpoint retrieves a list of all users. 
  When a GET request is sent to this endpoint, it will return a list of all users in the database.

### Item Endpoints:
- **POST /items/**  
  This endpoint creates a new item. 
  It accepts a JSON body with required item details. 
  Upon successful creation, it returns a response with the details of the created item.
- **GET /items/**  
  This endpoint retrieves a list of all items. 
  When a GET request is sent to this endpoint, it will return a list of items existing in the database.


For more details proceed to the built-in docs at http://127.0.0.1:8000/docs

## Testing

The tests for this application use an in-memory SQLite database. 
Before each test module, a new database is created. 
This approach keeps the tests isolated, ensuring that changes made in one test do not affect any others.
The application's main database connection is overwritten in the testing environment to use the in-memory SQLite database instead. 
This is done by overriding the get_db dependency in the tests [conftest.py](/tests/conftest.py), which supplies the FastAPI application with the database session. 
We replace the standard application database with the session of our in-memory SQLite database instead.
By doing this, we can test the application's interaction with the database, without modifying the actual database. 
Also, using an in-memory SQLite database makes these tests much faster to run compared to if they were to use a standard SQL database.

To run the tests, execute the pytest command from the project's root directory:

```bash
pytest
```
