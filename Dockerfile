FROM python:3.13.0a2-bookworm

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["behave", "features/business.feature"]
