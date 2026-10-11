from __future__ import annotations

from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.market_data import MarketDataSource
from app.schemas import SignalRequest
from app.strategy import analyze_market_snapshot, evaluate_signal

app = FastAPI(title="Market AI Trading India", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

market_source = MarketDataSource()


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "market-ai-trading-india",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/")
def root() -> dict:
    return {"message": "Welcome to Market AI Trading India"}


@app.get("/market")
def list_market() -> dict:
    return {
        "markets": ["NSE", "BSE", "Crypto"],
        "symbols": ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "SBIN.NS"],
    }


@app.get("/market/analyze")
def analyze_market() -> dict:
    snapshot = market_source.list_symbols()
    signals = analyze_market_snapshot(snapshot)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "signals": signals,
    }


@app.post("/signal")
def create_signal(payload: SignalRequest) -> dict:
    result = evaluate_signal(
        symbol=payload.symbol,
        price=payload.price,
        trend_score=payload.trend_score,
        rsi=payload.rsi,
        ema_short=payload.ema_short,
        ema_long=payload.ema_long,
        volume=payload.volume or 0,
    )
    return result
