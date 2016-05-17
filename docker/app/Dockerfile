FROM django:python3

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/volatile/static
RUN mkdir -p /usr/src/persistent/media
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/


# move files from present dir to container
COPY . /usr/src


# install all necessary tools & packages
RUN apt-get update && apt-get install -y \
		build-essential git \
		python3 python3-dev python3-setuptools \
		nginx supervisor \
		postgresql-client libpq-dev \
		sqlite3 libjpeg62-turbo-dev \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install uwsgi
RUN apt-get update
RUN apt-get install -y software-properties-common python3-software-properties

RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get install -y sqlite3

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN export DJANGO_SETTINGS_MODULE="rcrfbackend.settings"
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /usr/src/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s /usr/src/supervisor-app.conf /etc/supervisor/conf.d/
RUN pip install -r /usr/src/app/requirements.txt

EXPOSE 80 443
CMD ["supervisord", "-n"]