FROM gitpod/workspace-full:latest

# Use root user
USER root
RUN apt-get update && apt-get install -y \
    # Install Heroku CLI
    && curl https://cli-assets.heroku.com/install.sh | sh \
    # Install Postgres https://github.com/gitpod-io/workspace-images/blob/master/postgres/Dockerfile
    && sudo apt-get install -y postgresql postgresql-contrib \
    # Clean-up
    && sudo apt-get clean \
    && sudo rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/*

# Setup PostgreSQL server for user gitpod
ENV PATH="$PATH:/usr/lib/postgresql/11/bin"
ENV PGDATA="/home/gitpod/.pg_ctl/data"
RUN mkdir -p ~/.pg_ctl/bin ~/.pg_ctl/data ~/.pg_ctl/sockets \
 && initdb -D ~/.pg_ctl/data/ \
 && printf "#!/bin/bash\npg_ctl -D ~/.pg_ctl/data/ -l ~/.pg_ctl/log -o \"-k ~/.pg_ctl/sockets\" start\n" > ~/.pg_ctl/bin/pg_start \
 && printf "#!/bin/bash\npg_ctl -D ~/.pg_ctl/data/ -l ~/.pg_ctl/log -o \"-k ~/.pg_ctl/sockets\" stop\n" > ~/.pg_ctl/bin/pg_stop \
 && chmod +x ~/.pg_ctl/bin/*
ENV PATH="$PATH:$HOME/.pg_ctl/bin"
ENV DATABASE_URL="postgresql://gitpod@localhost"
ENV PGHOSTADDR="127.0.0.1"
ENV PGDATABASE="postgres"

# This is a bit of a hack. At the moment we have no means of starting background
# tasks from a Dockerfile. This workaround checks, on each bashrc eval, if the
# PostgreSQL server is running, and if not starts it.
RUN printf "\n# Auto-start PostgreSQL server.\n[[ \$(pg_ctl status | grep PID) ]] || pg_start > /dev/null\n" >> ~/.bashrc


# Local environment variables
ENV DEVELOPMENT="true"
ENV IP="0.0.0.0"
ENV GP_HOSTNAME="localhost"
ENV PORT="8080"

ENV DB_NAME="testdb"
ENV DB_USER="gitpod"
ENV DB_PORT="5432"
