FROM django:python3



RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/volatile/static
RUN mkdir -p /usr/src/persistent/media
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
COPY . /usr/src
RUN apt-get update && apt-get install -y \
		build-essential git \
		python3 python3-dev python3-setuptools \
		nginx supervisor \
		postgresql-client libpq-dev \
		sqlite3 libjpeg62-turbo-dev \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install setuptools
RUN pip install uwsgi
RUN apt-get update
RUN apt-get install -y software-properties-common python3-software-properties
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get install -y sqlite3
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN export DJANGO_SETTINGS_MODULE="rcrfbackend.settings"
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /usr/src/nginx-app.conf /etc/nginx/sites-enabled/
RUN ln -s /usr/src/supervisor-app.conf /etc/supervisor/conf.d/
RUN pip install -r /usr/src/app/requirements.txt

RUN apt install -y wget
RUN apt install -y zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

RUN pip install django-redis==4.8.0

RUN rm -R /usr/src/app/chat/migrations
RUN rm -R /usr/src/app/krogoth_3rdparty_api/migrations
RUN rm -R /usr/src/app/krogoth_examples/migrations
RUN rm -R /usr/src/app/krogoth_admin/migrations
RUN rm -R /usr/src/app/krogoth_apps/migrations
RUN rm -R /usr/src/app/krogoth_social/migrations
RUN rm -R /usr/src/app/moho_extractor/migrations
RUN rm -R /usr/src/app/kbot_lab/migrations

RUN sed -i -e 's/miloshadzic/tonotdo/g' ~/.zshrc

EXPOSE 80 443 22
CMD ["supervisord", "-n"]