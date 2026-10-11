const marketData = [
  { symbol: 'RELIANCE.NS', price: 3012.45, signal: 'BUY', confidence: '78%' },
  { symbol: 'TCS.NS', price: 3874.15, signal: 'BUY', confidence: '66%' },
  { symbol: 'INFY.NS', price: 1518.65, signal: 'BUY', confidence: '81%' },
  { symbol: 'HDFCBANK.NS', price: 1741.9, signal: 'HOLD', confidence: '62%' },
  { symbol: 'SBIN.NS', price: 862.75, signal: 'BUY', confidence: '74%' },
];

export default function Home() {
  return (
    <main className="main">
      <div className="container">
        <header className="header">
          <h1 className="title">Market AI Trading India</h1>
          <p className="subtitle">Automated market analysis and paper trading dashboard for Indian markets.</p>
        </header>

        <section className="grid">
          <div className="card">
            <div className="card-label">Market</div>
            <div className="card-value">NSE / BSE</div>
          </div>
          <div className="card">
            <div className="card-label">Position size</div>
            <div className="card-value">0.01</div>
          </div>
          <div className="card">
            <div className="card-label">Take Profit</div>
            <div className="card-value">0.50%</div>
          </div>
          <div className="card">
            <div className="card-label">Stop Loss</div>
            <div className="card-value">0.10%</div>
          </div>
        </section>

        <section className="rule-list">
          <h3>Signal Watchlist</h3>
          <ul>
            {marketData.map((item) => (
              <li key={item.symbol}>
                {item.symbol}: ₹{item.price} | Signal: <span className={item.signal === 'BUY' ? 'signal-buy' : 'signal-hold'}>{item.signal}</span> | Confidence: {item.confidence}
              </li>
            ))}
          </ul>
        </section>

        <section className="rule-list" style={{ marginTop: 24 }}>
          <h3>Strategy Rules</h3>
          <ul>
            <li>Buy when market trend is confirmed.</li>
            <li>Use RSI and EMA alignment.</li>
            <li>Fixed position size is 0.01.</li>
            <li>Take profit at 0.50%.</li>
            <li>Stop loss at 0.10%.</li>
            <li>Paper trading mode is enabled.</li>
          </ul>
        </section>
      </div>
    </main>
  );
}
