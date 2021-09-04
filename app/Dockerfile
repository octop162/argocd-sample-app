FROM python:3.9-alpine

ADD . /work
WORKDIR /work
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "app.py"]