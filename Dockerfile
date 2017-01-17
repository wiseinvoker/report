# Start with a Python image.
FROM python:3.4

# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1

# Install some necessary things.
RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat

# Copy all our files into the image.
RUN mkdir /code
WORKDIR /code
COPY . /code/

# Install our requirements.
RUN pip install -U pip
RUN pip install -Ur requirements.txt

# Collect our static media.
RUN /code/manage.py collectstatic --noinput

# Perform database migration
RUN /code/manage.py migrate

# Run uWSGI server
RUN uwsgi --ini /code/config/uwsgi.ini
