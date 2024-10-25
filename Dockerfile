# Használjunk egy alapértelmezett Python képet
FROM python:3.8-slim

# Telepítsük a függőségeket
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Másoljuk át a kódot
COPY . .

# Indítsuk el az alkalmazást
CMD ["python", "app.py"]
