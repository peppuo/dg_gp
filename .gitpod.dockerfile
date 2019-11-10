FROM gitpod/workspace-full:latest

# Use root user
USER root
RUN apt-get update && apt-get install -y \
    # Setup Heroku CLI
    && curl https://cli-assets.heroku.com/install.sh | sh \
    # Clean up
    && apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*


# Local environment variables
ENV DEVELOPMENT="true"
ENV IP="0.0.0.0"
ENV GP_HOSTNAME="localhost"
ENV PORT="8080"
