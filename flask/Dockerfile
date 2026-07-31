FROM python:3.14.6-slim

WORKDIR /backend

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "--app", "src.main", "run", "--port", "5000"]

