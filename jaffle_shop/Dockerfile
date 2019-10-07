FROM python:3.6
MAINTAINER Peter Hanssens <phanssens1@gmail.com>

RUN apt-get update

RUN apt-get install -y python-pip netcat
RUN apt-get install -y python-dev python3-dev

RUN pip install pip --upgrade
RUN pip install virtualenv
RUN pip install virtualenvwrapper
RUN pip install tox
RUN pip install awscli
# RUN pip install boto3==1.7.84
RUN pip install dbt

ENV INSTALL_PATH /usr/src/app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

# Copy the source from your workstation to the image at the WORKDIR path.
COPY . .

RUN dbt init new_folder 
RUN cat ./sample.profiles.yml > ~/.dbt/profiles.yml
RUN rm -rf ./new_folder
RUN ls -la
CMD ./dbt_run.sh