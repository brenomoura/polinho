FROM pypy:3.9-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update
RUN apt install libuv1-dev libssl-dev libpq-dev  gcc -y
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "pypy3", "./src/main.py" ]