FROM python:slim
RUN apt-get update && apt-get install -y libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev
RUN apt install -y curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
WORKDIR /skin_trader
COPY ./pyproject.toml /skin_trader/pyproject.toml
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry install 
COPY . /skin_trader
RUN poetry run python manage.py collectstatic
CMD bash -c "poetry run python manage.py migrate && poetry run gunicorn config.wsgi -b 0.0.0.0:8000"


