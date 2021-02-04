FROM ubuntu 
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --assume-yes apt-utils


# 安装pytnon环境
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip


WORKDIR /programs
ADD . .

# 安装依赖
RUN pip3 install --requirement requirements.txt


