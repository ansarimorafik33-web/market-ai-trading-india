CREATE TABLE IF NOT EXISTS market_symbols (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(50) NOT NULL,
    exchange VARCHAR(20) NOT NULL,
    price NUMERIC(18, 4),
    rsi NUMERIC(10, 2),
    ema_short NUMERIC(18, 4),
    ema_long NUMERIC(18, 4),
    trend_score NUMERIC(10, 4),
    volume BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS trade_signals (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(50) NOT NULL,
    action VARCHAR(10) NOT NULL,
    buy_signal BOOLEAN NOT NULL,
    position_size NUMERIC(10, 4) NOT NULL,
    take_profit_percent NUMERIC(10, 4) NOT NULL,
    stop_loss_percent NUMERIC(10, 4) NOT NULL,
    confidence NUMERIC(10, 4),
    reason TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
