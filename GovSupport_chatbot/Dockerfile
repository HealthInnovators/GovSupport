FROM python:3.12.3

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml GovSupport_chatbot/src ./GovSupport_chatbot/

WORKDIR /GovSupport_chatbot

RUN poetry install

RUN spacy download en_core_web_sm

ENTRYPOINT ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]
