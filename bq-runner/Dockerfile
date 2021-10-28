FROM python:3.9
WORKDIR /opt/stoix/bq-runner
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY src src
CMD python src/main.py
