
FROM python:3.13.0a2-bookworm

WORKDIR /app

RUN python -m venv venv

RUN /bin/bash source .venv/bin/activate

RUN pip install --upgrade pip

COPY requirements.txt ./
  
RUN pip install -r requirements.txt

COPY . .

CMD ["behave", "features/business.feature"]
