FROM gitpod/workspace-full:latest

# Use root user
USER root
RUN apt-get update && apt-get install -y \
    # Install Heroku CLI
    #&& curl https://cli-assets.heroku.com/install.sh | sh \
    && curl https://cli-assets.heroku.com/install-ubuntu.sh | sh \
    && sudo chown gitpod:gitpod /home/gitpod/.cache/heroku
    # && curl https://cli-assets.heroku.com/install.sh | sh \
    # && sudo chown gitpod:gitpod /home/gitpod/.cache/heroku
    # Install Postgres CLI psql
    && sudo apt-get install -y postgresql postgresql-contrib \
    # Clean-up
    && sudo apt-get clean \
    && sudo rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/*


# Local environment variables
ENV DEVELOPMENT="true"
ENV IP="0.0.0.0"
ENV GP_HOSTNAME="localhost"
ENV PORT="8080"

ENV DB_NAME="testdb"
ENV DB_USER="postgres"
ENV DB_PORT="5432"
