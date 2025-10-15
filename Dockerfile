FROM python:3.12-slim

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY app /code/app

ENV USER_DB=lameque
ENV PASSWORD_DB=lameque123
ENV HOST_DB=db
ENV PORT_DB=3306
ENV DATABASE=oficina_fase1
ENV SECRET_KEY='fc05c7570c34597ddbf3a010cedd9247d5839bd74b6c5f96f770ed4b0f4dc8ff'
ENV ALGORITHM=HS256

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
