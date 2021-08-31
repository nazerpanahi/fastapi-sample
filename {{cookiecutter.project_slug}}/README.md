# {{cookiecutter.project_name}}

{{cookiecutter.short_description}}

## ENVIRONMENTS
- DEBUG
- SENTRY_DSN

## Up&Running
### Using Docker
```shell
docker build -t fastapi-sample:python3.7 .
docker run -it -d -e DEBUG=0 fastapi-sample:python3.7
```

### Local Running
```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
cd src
uvicorn app:app --host 127.0.0.1 --port 8000
```
