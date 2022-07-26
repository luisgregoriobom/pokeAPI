FROM python:3.8

WORKDIR /trainerapp
COPY . .

RUN pip install -r requirements.txt

# ENTRYPOINT ["python"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]