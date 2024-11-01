FROM python:3.11

# Install poetry
RUN pip install poetry

# Configure poetry to use global virtualenv
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --with api

COPY asi_labs/ /app/asi_labs/

COPY .assets/CollegeDistance.csv /app/.assets/CollegeDistance.csv

COPY .models/output_model.pkl /app/.models/output_model.pkl

CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000", "asi_labs/lab4/api.py"]
