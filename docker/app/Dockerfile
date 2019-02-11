FROM django:python3

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/volatile/static
RUN mkdir -p /usr/src/persistent/media
RUN mkdir -p /usr/src/tmp

RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install -y wget
RUN apt-get install -y nano
RUN pip3 install --upgrade pip

RUN apt-get install -y build-essential
RUN apt-get install -y libpq-dev
RUN apt-get install -y libssl-dev
RUN apt-get install -y openssl
RUN apt-get install -y libffi-dev
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y software-properties-common
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-dev python3-setuptools python3-software-properties
RUN apt-get install -y python3-pip
RUN add-apt-repository -y ppa:nginx/stable

RUN apt-get update && apt-get install -y nginx supervisor postgresql-client sqlite3

# USE WHEN INSTALLER HAS ISSUES:
#	--no-install-recommends

RUN rm -rf /var/lib/apt/lists/*








WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY . /usr/src

#RUN pip3 install django==1.11.18
RUN pip3 install wheel
RUN pip3 install setuptools
#RUN pip3 install uwsgi
RUN pip3 install django-extensions
#RUN pip3 install django-redis
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt






RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN export DJANGO_SETTINGS_MODULE="jawn.settings"
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /usr/src/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s /usr/src/supervisor-app.conf /etc/supervisor/conf.d/

#RUN pip3 install -r /usr/src/app/requirements.txt
#RUN rm -R /usr/src/app/krogoth_chat/migrations
#RUN rm -R /usr/src/app/krogoth_3rdparty_api/migrations
#RUN rm -R /usr/src/app/krogoth_examples/migrations
#RUN rm -R /usr/src/app/krogoth_admin/migrations
#RUN rm -R /usr/src/app/krogoth_social/migrations
#RUN rm -R /usr/src/app/moho_extractor/migrations
#RUN rm -R /usr/src/app/kbot_lab/migrations

EXPOSE 80 443 22
CMD ["supervisord", "-n"]