FROM python:3.8
ENV PYTHONNUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./backend /code/backend
WORKDIR /code/backend
RUN pip install pipenv
RUN pipenv install --system
ADD ./wait-for-it.sh /usr/wait-for-it.sh
RUN chmod 755 /usr/wait-for-it.sh