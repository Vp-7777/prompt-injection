FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies from pyproject
RUN pip install .

# Expose port
EXPOSE 8000

# Run server
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]