FROM python:3.9-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files
COPY poetry.lock pyproject.toml ./

# Install the project dependencies
RUN poetry install --no-dev --no-interaction --no-ansi --verbose

# Copy the rest of the project files
COPY . .

# Set the entrypoint
ENTRYPOINT ["poetry", "run", "python", "main.py"]