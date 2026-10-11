from __future__ import annotations

from pydantic import BaseModel
from typing import Optional


class SignalRequest(BaseModel):
    symbol: str
    price: float
    trend_score: float
    rsi: float
    ema_short: float
    ema_long: float
    volume: Optional[int] = 0


class StrategyResult(BaseModel):
    symbol: str
    action: str
    buy_signal: bool
    position_size: float
    take_profit_percent: float
    stop_loss_percent: float
    confidence: float
    reason: str
