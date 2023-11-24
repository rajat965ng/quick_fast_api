
## Create a New Project
`
poetry new phone-number-validator
`

## Create a New Virtual Environment
`
poetry env use $(which python3.11)
`

## Verify Virtual Environment
`
poetry env info
`

## Configure Project Dependencies
`
poetry add requests
`

### To create a requirements.txt file from the poetry.lock file, you can use the following command:
`
poetry export --output requirements.txt
`

## Add FastAPI and Uvicorn
`
pip3.11 install fastapi   
pip3.11 install "uvicorn[standard]" 
`

**To run fastAPI app using poetry add start() method in proj2/main.py followed by configure [tool.poetry.scripts] in pyproject.toml**

`
poetry run start  
`

## Important Links
`
NFO:     127.0.0.1:56920 - "GET /items/5?q=somequery HTTP/1.1" 200 OK
INFO:     127.0.0.1:56920 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:56920 - "GET /openapi.json HTTP/1.1" 200 OK
INFO:     127.0.0.1:56920 - "GET /redoc HTTP/1.1" 200 OK
INFO:     127.0.0.1:56920 - "GET /openapi.json HTTP/1.1" 200 OK
`


## Basic Commands (Poetry)
`
https://python-poetry.org/docs/cli/
`