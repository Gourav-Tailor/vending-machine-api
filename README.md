# Vending Machine API

FastAPI implementation of the provided OpenAPI specification.

## Requirements

* Python 3.11+
* pip

---

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API runs at:

```
http://localhost:8000
```

Swagger docs:

```
http://localhost:8000/docs
```

---

## Run with Docker

```bash
docker build -t vending-machine-api .
docker run -p 8000:8000 vending-machine-api
```

Or:

```bash
docker-compose up --build
```

---

## Notes

* All endpoints require header: `X-Machine-Id`
* Money is handled in integer cents (`price_cents`, `payment_cents`)
* Special rule: insufficient funds for item `A1` returns `A1_BROKE`
* Data is stored in-memory
