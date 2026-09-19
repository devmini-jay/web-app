#instructions for creating image

#base image
FROM python:3.12

#working directory inside cimage & ontainer
WORKDIR /app

#copy local requirements inside the image
COPY requirements.txt .

#install flask inside the image
RUN pip install --no-cache-dir -r requirements.txt

#copy flask app into image
COPY app.py .

#exposing port the app will use
EXPOSE 5000

#command to run when container starts
CMD ["python", "app.py"]