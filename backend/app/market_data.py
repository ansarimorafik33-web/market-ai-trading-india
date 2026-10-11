from __future__ import annotations

from typing import Any, Dict, List


def get_india_market_samples() -> List[Dict[str, Any]]:
    return [
        {
            "symbol": "RELIANCE.NS",
            "exchange": "NSE",
            "price": 3012.45,
            "rsi": 58.4,
            "ema_short": 2988.2,
            "ema_long": 2912.7,
            "trend_score": 0.78,
            "volume": 1350000,
        },
        {
            "symbol": "TCS.NS",
            "exchange": "NSE",
            "price": 3874.15,
            "rsi": 52.9,
            "ema_short": 3845.5,
            "ema_long": 3798.4,
            "trend_score": 0.66,
            "volume": 980000,
        },
        {
            "symbol": "INFY.NS",
            "exchange": "NSE",
            "price": 1518.65,
            "rsi": 61.2,
            "ema_short": 1494.3,
            "ema_long": 1450.8,
            "trend_score": 0.81,
            "volume": 2200000,
        },
        {
            "symbol": "HDFCBANK.NS",
            "exchange": "NSE",
            "price": 1741.9,
            "rsi": 49.3,
            "ema_short": 1718.2,
            "ema_long": 1690.5,
            "trend_score": 0.62,
            "volume": 1100000,
        },
        {
            "symbol": "SBIN.NS",
            "exchange": "NSE",
            "price": 862.75,
            "rsi": 64.7,
            "ema_short": 851.2,
            "ema_long": 833.1,
            "trend_score": 0.74,
            "volume": 2900000,
        },
    ]


class MarketDataSource:
    def __init__(self) -> None:
        self.snapshot = get_india_market_samples()

    def list_symbols(self) -> List[Dict[str, Any]]:
        return self.snapshot

    def get_symbol(self, symbol: str) -> Dict[str, Any]:
        for item in self.snapshot:
            if item["symbol"].lower() == symbol.lower():
                return item
        raise ValueError(f"Symbol not found: {symbol}")
