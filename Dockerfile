FROM python:3.11-slim-bookworm

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock*
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . .

# Command to run the application
CMD ["poetry", "run", "python", "main.py"]