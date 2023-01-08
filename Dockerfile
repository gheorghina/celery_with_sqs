FROM python:3.9

ARG CA_USER="ca_user"

RUN addgroup --gid 1000 ${CA_USER} && adduser --system --disabled-password --uid 1000 ${CA_USER}
COPY ./src ./requirements.txt ./run.sh /home/${CA_USER}

WORKDIR /home/${CA_USER}

RUN apt-get update && apt-get install libpq-dev curl libcurl14-openssql-dev -y && apt-get clean && \
    pip install -r requirements.txt && \
    chmod +x /home/${CA_USER}/run.sh

ENV PYTHONPATH=/home/${CA_USER}
ENV DD_VERSION=$COMMIT_SHA

USER ${CA_USER}
CMD [ "run.sh" ]
