FROM tiangolo/uwsgi-nginx-flask:latest
RUN apt-get update
Run apt-get -y install bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
