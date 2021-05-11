FROM python:3.9

ARG arg_http_proxy
ARG arg_https_proxy
ARG arg_django_project_name

ENV http_proxy=${arg_http_proxy}
ENV https_proxy=${arg_https_proxy} 
ENV django_project_name=${arg_django_project_name}

ENV PYTHONNUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD ./${django_project_name} /code/${django_project_name}
WORKDIR /code/${django_project_name}
RUN pip install pipenv
RUN pipenv sync --system
ADD ./wait-for-it.sh /usr/wait-for-it.sh
RUN chmod 755 /usr/wait-for-it.sh
