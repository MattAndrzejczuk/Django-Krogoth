FROM postgres:latest
COPY . /var/data/
WORKDIR /var/data
#RUN sh entrypoint.sh
RUN chmod -R 777 /var/lib/postgresql
EXPOSE 5432
CMD ["postgres"]