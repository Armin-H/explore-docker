FROM python:3.14


# docker build -f Dockerfile -t myfirstapp .
# docker run -it myfirstapp

WORKDIR /app
# RUN mkdir -p /static_files
COPY ./src .

# docker run -it -p 3000:8000 myfirstapp
CMD ["python", "-m", "http.server", "8000"]