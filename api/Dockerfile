FROM python:3.9-slim

WORKDIR /api

COPY . /api

RUN pip install --no-cache-dir -r requirements.txt

# Set the Flask environment to development
ENV FLASK_ENV=development
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1

EXPOSE 5174

# Run the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5174"]