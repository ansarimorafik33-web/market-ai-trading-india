from __future__ import annotations

from typing import Any, Dict, List

POSITION_SIZE = 0.01
TAKE_PROFIT_PERCENT = 0.50
STOP_LOSS_PERCENT = 0.10


def evaluate_signal(symbol: str, price: float, trend_score: float, rsi: float, ema_short: float, ema_long: float, volume: int = 0) -> Dict[str, Any]:
    buy_signal = False
    action = "HOLD"
    reason = "No valid trade condition detected."
    confidence = 0.0

    bullish = trend_score > 0.6
    ema_alignment = price > ema_short > ema_long
    rsi_ok = 45 <= rsi <= 70
    volume_ok = volume > 0

    if bullish and ema_alignment and rsi_ok and volume_ok:
        buy_signal = True
        action = "BUY"
        confidence = round(min(0.95, 0.55 + (trend_score * 0.4) + ((70 - rsi) / 100) * 0.2), 3)
        reason = "Trend confirmed with bullish EMA alignment and RSI within range."
    elif trend_score < 0.4:
        action = "SELL"
        reason = "Momentum is weak; caution recommended."

    return {
        "symbol": symbol,
        "action": action,
        "buy_signal": buy_signal,
        "position_size": POSITION_SIZE,
        "take_profit_percent": TAKE_PROFIT_PERCENT,
        "stop_loss_percent": STOP_LOSS_PERCENT,
        "confidence": confidence,
        "reason": reason,
    }


def analyze_market_snapshot(snapshot: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    results: List[Dict[str, Any]] = []
    for row in snapshot:
        result = evaluate_signal(
            symbol=row.get("symbol", "UNKNOWN"),
            price=float(row.get("price", 0)),
            trend_score=float(row.get("trend_score", 0)),
            rsi=float(row.get("rsi", 0)),
            ema_short=float(row.get("ema_short", 0)),
            ema_long=float(row.get("ema_long", 0)),
            volume=int(row.get("volume", 0)),
        )
        results.append(result)
    return results
