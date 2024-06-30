FROM ubuntu:22.04

RUN apt update && apt install -y python3 python3-pip gcc g++ curl wget

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN /root/.cargo/bin/uv pip install --system --no-cache -r requirements.txt

COPY . /app

RUN bash ./talib_setup.sh

EXPOSE 8082

CMD ["python3", "server.py"]