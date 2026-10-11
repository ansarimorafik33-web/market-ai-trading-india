from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TradeRule:
    position_size: float = 0.01
    take_profit_percent: float = 0.50
    stop_loss_percent: float = 0.10


class RiskManager:
    def __init__(self) -> None:
        self.rule = TradeRule()

    def validate_trade(self, action: str, confidence: float) -> bool:
        if action == "BUY" and confidence >= 0.55:
            return True
        return False

    def get_rule(self) -> TradeRule:
        return self.rule
