

FROM django:python3

RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              FROM django:python3         \033[0m')"



RUN mkdir -p /usr/src/app
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              FROM django:python3         \033[0m')"
RUN mkdir -p /usr/src/volatile/static
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              FROM django:python3         \033[0m')"
RUN mkdir -p /usr/src/persistent/media
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              FROM django:python3         \033[0m')"
WORKDIR /usr/src/app
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              FROM django:python3         \033[0m')"

COPY requirements.txt /usr/src/app/
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              FROM django:python3         \033[0m')"



# move files from present dir to container
COPY . /usr/src
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              FROM django:python3         \033[0m')"

# install all necessary tools & packages
RUN apt-get update && apt-get install -y -qq \
		build-essential git \
		python3 python3-dev python3-setuptools \
		nginx supervisor \
		postgresql-client libpq-dev \
		sqlite3 libjpeg62-turbo-dev \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[35m          apt-get update && apt-get install -y          build-essential        libpq-dev   \033[0m')"
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[35m              python3             python3-dev           python3-setuptools        \033[0m')"
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[35m              nginx               supervisor            postgresql-client           \033[0m')"
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[35m              postgresql-client   libpq-dev        \033[0m')"
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[35m              sqlite3             libjpeg62-turbo-dev   git      \033[0m')"


RUN pip install -q --no-cache-dir -r requirements.txt
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN pip install --no-cache-dir -r requirements.txt         \033[0m')"


RUN pip install --upgrade pip
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN pip install --upgrade pip         \033[0m')"


RUN pip install -q wheel
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN pip install wheel         \033[0m')"

RUN pip install -q setuptools==36.6.0
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN pip install setuptools==36.6.0         \033[0m')"



RUN pip install -q uwsgi
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN pip install uwsgi         \033[0m')"


RUN apt-get update
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN apt-get update         \033[0m')"


RUN apt-get install -y -qq software-properties-common python3-software-properties
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN apt-get install -y software-properties-common python3-software-properties         \033[0m')"



RUN add-apt-repository -y ppa:nginx/stable
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN add-apt-repository -y ppa:nginx/stable         \033[0m')"


RUN apt-get install -y -qq sqlite3
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN apt-get install -y sqlite3         \033[0m')"


# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN echo "daemon off;" >> /etc/nginx/nginx.conf         \033[0m')"


RUN export DJANGO_SETTINGS_MODULE="rcrfbackend.settings"
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN export DJANGO_SETTINGS_MODULE="rcrfbackend.settings"         \033[0m')"


RUN rm /etc/nginx/sites-enabled/default
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN rm /etc/nginx/sites-enabled/default         \033[0m')"


RUN ln -s /usr/src/nginx-app.conf /etc/nginx/sites-enabled/
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN ln -s /usr/src/nginx-app.conf /etc/nginx/sites-enabled/         \033[0m')"


RUN ln -s /usr/src/supervisor-app.conf /etc/supervisor/conf.d/
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN ln -s /usr/src/supervisor-app.conf /etc/supervisor/conf.d/         \033[0m')"


RUN pip install -q -r /usr/src/app/requirements.txt
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              RUN pip install -r /usr/src/app/requirements.txt         \033[0m')"


EXPOSE 80 443
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              EXPOSE 80 443         \033[0m')"


CMD ["supervisord", "-n"]
RUN python -c "print('\033[31m[\033[0m\033[92mAPP_DOCKERFILE\033[0m 🐳 \033[31m]\033[0m\033[34m>>> \033[0m\033[0m\033[32m              CMD ['supervisord', '-n']         \033[0m')"