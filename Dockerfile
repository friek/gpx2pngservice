FROM python:3.7

COPY requirements.txt /usr/src

ENV DEBIAN_FRONTEND=noninteractive
ENV FLASK_APP=gpx2pngservice.py

RUN pip install -r /usr/src/requirements.txt && \
    apt-get update && \
    apt-get -y install perl imagemagick libimage-magick-perl libimage-magick-q16-perl libwww-perl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists

RUN chmod 1777 /tmp
VOLUME /tmp

COPY gpx2pngservice.py /usr/src
COPY converter.pl /usr/src

EXPOSE 5000

USER nobody
WORKDIR /usr/src
CMD flask run --host=0.0.0.0