FROM python:3.6.1

# Create working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Copy source code into container
COPY . /app

CMD ["flask", "run"]
