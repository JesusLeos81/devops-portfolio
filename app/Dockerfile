FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.12-slim
WORKDIR /app

RUN useradd -m appuser
COPY --from=builder /root/.local /home/appuser/.local
COPY main.py .

USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]