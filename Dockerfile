FROM python:3.14


# docker build -f Dockerfile -t myfirstapp .
# docker run -it myfirstapp

WORKDIR /app
RUN echo "Hello World" > index.html

# docker run -it -p 3000:8000 myfirstapp
CMD ["python", "-m", "http.server", "8000"]