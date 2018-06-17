FROM python:3.6-alpine
RUN apk add --update build-base libffi-dev
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "oauth_redir.py"]
