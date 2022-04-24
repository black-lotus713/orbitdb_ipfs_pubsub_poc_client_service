FROM python:3.8-alpine3.15
RUN apk update && apk upgrade && mkdir /usr/src/app/

COPY index.py /usr/src/app/
COPY requirements.txt /usr/src/app/

WORKDIR /usr/src/app/

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

EXPOSE 3030
CMD [ "python", "index.py" ]
