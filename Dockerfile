FROM python:3.13.1-bookworm


RUN mkdir /code
WORKDIR /code

# Installing apps
RUN apt-get update && apt-get install -y postgresql netcat-traditional gettext
# Install dependencies:
COPY ./requirements .

RUN pip install -r requirements.txt

COPY . .

COPY wait.sh /wait.sh
RUN sed -i 's/\r$//g' /wait.sh
RUN chmod +x /wait.sh

COPY start.sh /start.sh
RUN sed -i 's/\r$//g' /start.sh
RUN chmod +x /start.sh

COPY entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]