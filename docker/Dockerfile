FROM continuumio/miniconda3

USER root

ENV SERVICE_HOME /opt/arlo
RUN mkdir -p /opt/arlo/videos

# set local docker resources relative path
ENV DOCKER_RESOURCES docker/resources

# Set the working directory to SERVICE_HOME
WORKDIR $SERVICE_HOME

RUN apt-get update --fix-missing && \
    apt-get install -y unzip libaio1 libaio-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# copy service code to SERVICE_HOME
#COPY .env $SERVICE_HOME/
COPY setup.cfg $SERVICE_HOME/
COPY setup.py $SERVICE_HOME/
COPY requirements.txt $SERVICE_HOME/
COPY $DOCKER_RESOURCES/arlo.sh $SERVICE_HOME/
COPY arlo.py $SERVICE_HOME/

# configure python environment
RUN cd $SERVICE_HOME \
    && python -m venv venv \
    && . venv/bin/activate \
    && pip install -r requirements.txt \
    && python setup.py develop

# Run cmd
#CMD ["/bin/bash", "-c", "$SERVICE_HOME/arlo.sh"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["/bin/bash", "-c", "$SERVICE_HOME/arlo.sh"]
