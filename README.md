# Readable Password Generator
### - generates a password which can be remembered easily

- minimum password length 8
- deployable 
- fast API
- docker enabled
- can turn on the log

## requirements
- python 3.8 or above

## on local system
- `git clone https://github.com/alvonx/readable-password-generator.git`
- `pip install -r requirements.txt`
- `uvicorn app.main:app --reload --host 0.0.0.0 --port 5000`
- &nbsp;&nbsp;welcome message http://localhost:5000/
- &nbsp;&nbsp;generate password http://localhost:5000/generate
- &nbsp;&nbsp;custom length password (10 here) http://localhost:5000/generate?plen=10

## on server (docker must be installed)
- `git clone https://github.com/alvonx/readable-password-generator.git`
- `cd readable-password-generator`
- `docker build -t password-generator:v1 .`
- `docker run --restart='always' -dp <externalport>:5000 password-generator:v1`
- &nbsp;&nbsp;welcome message `http://<server-ip>:<externalport>/`
- &nbsp;&nbsp;generate password `http://<server-ip>:<externalport>/generate`
- &nbsp;&nbsp;custom length password (10 here) `http://<server-ip>:<externalport>/generate?plen=10`
- externalport = port on which you want to run the docker container
- port must be open than only you can access it from outside world