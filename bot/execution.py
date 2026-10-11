from __future__ import annotations

from bot.risk_manager import RiskManager


class PaperTradingBot:
    def __init__(self) -> None:
        self.risk_manager = RiskManager()

    def evaluate(self, action: str, confidence: float) -> dict:
        valid = self.risk_manager.validate_trade(action, confidence)
        trade_rule = self.risk_manager.get_rule()

        return {
            "action": action,
            "allowed": valid,
            "position_size": trade_rule.position_size,
            "take_profit_percent": trade_rule.take_profit_percent,
            "stop_loss_percent": trade_rule.stop_loss_percent,
            "status": "executed" if valid else "blocked",
        }
