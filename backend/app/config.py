from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Settings:
    app_name: str = "market-ai-trading-india"
    environment: str = "development"
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    log_level: str = "INFO"

    def load_env(self) -> None:
        import os

        self.app_name = os.getenv("APP_NAME", self.app_name)
        self.environment = os.getenv("ENVIRONMENT", self.environment)
        self.api_host = os.getenv("API_HOST", self.api_host)
        self.api_port = int(os.getenv("API_PORT", str(self.api_port)))
        self.log_level = os.getenv("LOG_LEVEL", self.log_level)


settings = Settings()
settings.load_env()
