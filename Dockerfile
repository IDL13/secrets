FROM python:latest

WORKDIR /app

COPY /. /app

SHELL ["/bin/bash", "-c"] 

RUN source venv/bin/activate

RUN pip install --upgrade pip

RUN pip install poetry

COPY ./poetry.lock pyproject.toml ./

RUN poetry install

RUN python3 toml_parser.py

RUN pip install -r requirements.txt

# CMD ["uvicorn", "main:app"]
CMD ["fastapi", "run", "main.py"]