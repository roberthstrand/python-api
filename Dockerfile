FROM python:3.8-slim
RUN pip install --no-cache-dir uvicorn fastapi typing pydantic

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

LABEL maintainer="RoberthStrand" \
  org.label-schema.build-date=$BUILD_DATE \
  org.label-schema.name="Python-TODO-API" \
  org.label-schema.description="Python API, demonstration project" \
  org.label-schema.url="https://robstr.dev" \
  org.label-schema.vcs-ref=$VCS_REF \
  org.label-schema.vcs-url="https://github.com/roberthstrand/python-api" \
  org.label-schema.version=$VERSION \
  org.label-schema.schema-version="1.0"

COPY src/api /api

WORKDIR /api
ENTRYPOINT [ "uvicorn", "main:app" ]