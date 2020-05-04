FROM python:3.6-alpine

RUN adduser -D forbearance

WORKDIR /home/forbearance

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY migrations migrations
COPY forbearance.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP microblog.py

RUN chown -R microblog:microblog ./
USER forbearance

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]