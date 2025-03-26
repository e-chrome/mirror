ARG DOCKER_PROXY=harbor.megamarket.tech/docker.io
FROM ${DOCKER_PROXY}/python:3.11-slim-bookworm as builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONBUFFERED=1 \
    PIP_NO_CACHE_DIR=OFF \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONPATH=/opt/app \
    PDM_VERSION=2.8.*

RUN apt-get update && apt-get install gcc -y && rm -rf /var/lib/apt/lists/*

# Setup pdm
RUN pip install --no-cache-dir "pdm==$PDM_VERSION" pip==23.0.1 && \
    pdm config venv.in_project false && \
    pdm config check_update false && \
    pdm config python.use_venv false

COPY pyproject.toml pdm.lock README.md /opt/app/

WORKDIR /opt/app

# Setup prod dependency
RUN mkdir __pypackages__ && pdm install -v --prod --no-lock --no-editable

FROM builder as tester

ENV PYTHONPATH=/opt/app/__pypackages__/3.11/lib

# Setup dev dependency
RUN pdm install --dev

CMD ["python"]

FROM ${DOCKER_PROXY}/python:3.11-slim-bookworm as runner

ENV TZ=Europe/Moscow \
    PYTHONPATH=/opt/app/pkgs

COPY --from=builder /opt/app/__pypackages__/3.11/lib /opt/app/pkgs

WORKDIR /opt/app
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
