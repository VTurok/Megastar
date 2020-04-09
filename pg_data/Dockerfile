FROM postgres:10
COPY ./docker-entrypoint-initdb.d/ ./docker-entrypoint-initdb.d/
#ADD dump.pgdata /docker-entrypoint-initdb.d
#RUN chmod a+r /docker-entrypoint-initdb.d/*
#EXPOSE 6666