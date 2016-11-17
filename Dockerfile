FROM debian:jessie
MAINTAINER Derek Vance <dvance@cerb-tech.com>


ENV APP_USER=web
ENV APP_PATH=/opt/PowerDNS-Admin
RUN useradd -s /bin/bash -d $APP_PATH -m $APP_USER

VOLUME $APP_PATH
WORKDIR $APP_PATH

RUN apt-get update && \
    apt-get install -y sudo curl git python libpython2.7 python-dev libsasl2-dev \
        build-essential libmysqlclient18 libmysqlclient-dev libssl-dev \
        libldap2-dev && \
    curl https://bootstrap.pypa.io/get-pip.py | python 

RUN chown -R $APP_USER:$APP_USER /opt/PowerDNS-Admin

RUN pwd

RUN sudo -u $APP_USER git clone https://github.com/ngoduykhanh/PowerDNS-Admin.git .
COPY setup.py .

RUN ./setup.py ;\
    pip install -r requirements.txt

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

USER $APP_USER
ENTRYPOINT ["entrypoint.sh"]
EXPOSE 9393

CMD ["./run.py"]
