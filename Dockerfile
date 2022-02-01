### 1. Get Linux
FROM python:3.7

### 2. Get Java via the package manager
# Install OpenJDK-8
RUN apt-get update && \
    apt-get install software-properties-common && \
    add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;
    
# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

### 3. Get Python, PIP

# RUN apk add --no-cache python3 \
# && python3 -m ensurepip \
# && pip3 install --upgrade pip setuptools \
# && rm -r /usr/lib/python*/ensurepip && \
# if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
# if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
# rm -r /root/.cache

ENV FLASK_APP main.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_RUN_PORT 8080
### Get Flask for the app
# RUN pip install --trusted-host pypi.python.org flask
ADD requirements.txt /
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

####
#### OPTIONAL : 4. SET JAVA_HOME environment variable, uncomment the line below if you need it

#ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

####

EXPOSE 8080
ADD main.py /
CMD ["flask", "run"]