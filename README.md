# Market AI Trading India

This repository contains a starter MVP for an automated market analysis and trading software focused on the Indian market. It includes:

- market scanning for Indian symbols
- trend and signal evaluation logic
- position sizing and risk rules
- paper trading bot simulation
- backend API for analysis
- minimal dashboard UI

Default rule used in the project:
- Buy signal when trend is confirmed
- Position size: 0.01
- Take profit: 0.50%
- Stop loss: 0.10%

## Tech stack

- Frontend: Next.js
- Backend: FastAPI (Python)
- Market analysis: Python strategy engine
- Data layer: PostgreSQL schema included
- Optional live market access: CCXT

## Project structure

```text
market-ai-trading-india/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── market_data.py
│   │   ├── schemas.py
│   │   └── strategy.py
│   ├── .env.example
│   └── requirements.txt
├── bot/
│   ├── execution.py
│   └── risk_manager.py
├── database/
│   └── schema.sql
├── frontend/
│   ├── app/
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── .gitignore
│   ├── next-env.d.ts
│   ├── next.config.js
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
├── .gitignore
├── README.md
└── LICENSE
```

## Run backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Run frontend

```bash
cd frontend
npm install
npm run dev
```

Then open:
- Frontend: http://localhost:3000
- API Docs: http://localhost:8000/docs

## Default signal logic

```python
POSITION_SIZE = 0.01
TP_PERCENT = 0.50
SL_PERCENT = 0.10
```

Buy condition (example):
- trend score > 0.6
- RSI in range
- EMA alignment positive
- volume valid

## Indian market examples

Sample data includes Indian symbols such as:
- RELIANCE.NS
- TCS.NS
- INFY.NS
- HDFCBANK.NS
- SBIN.NS

## Disclaimer

This project is for education and prototype development. It does not guarantee profits and should not be treated as financial advice.
