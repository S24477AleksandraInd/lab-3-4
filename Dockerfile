FROM python:3.11 AS learner

RUN apt update && apt install -y libgomp1 wkhtmltopdf
# Install poetry
RUN pip install poetry

# Configure poetry to use global virtualenv
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --with learning

COPY asi_labs/ /app/asi_labs/

COPY assets/CollegeDistance.csv /app/assets/CollegeDistance.csv

RUN python3 -m asi_labs.lab3.learn

FROM python:3.11 AS api

# Install poetry
RUN pip install poetry

# Configure poetry to use global virtualenv
RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --with api

COPY asi_labs/ /app/asi_labs/

COPY assets/CollegeDistance.csv /app/assets/CollegeDistance.csv

COPY --from=learner /app/models/ /app/models/

CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000", "asi_labs/lab4/api.py"]
