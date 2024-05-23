FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /backend

COPY . .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r ./requirements.txt

FROM builder as dev-envs

RUN <<EOF
apt-get update nano
apt-get install -y --no-install-recommends git
alembic init alembic
EOF

RUN <<EOF
useradd -s /bin/bash -m vscode
groupadd docker
usermod -aG docker vscode
EOF

COPY --from=gloursdocker/docker / /

CMD [ "python3", "main.py" ]