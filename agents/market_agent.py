import yfinance as yf
 
 
SYMBOL_MAP = {
    "TESLA": "TSLA", "TSLA": "TSLA",
    "APPLE": "AAPL", "AAPL": "AAPL",
    "GOOGLE": "GOOGL", "GOOGL": "GOOGL", "ALPHABET": "GOOGL",
    "MICROSOFT": "MSFT", "MSFT": "MSFT",
    "AMAZON": "AMZN", "AMZN": "AMZN",
    "NVIDIA": "NVDA", "NVDA": "NVDA",
    "META": "META", "FACEBOOK": "META",
    "NETFLIX": "NFLX", "NFLX": "NFLX",
}
 
 
class MarketAgent:
    """
    Fetches real market data from Yahoo Finance via yfinance.
    Returns OHLCV prices, volume, and daily change.
    """
 
    def __init__(self):
        self.name = "MarketAgent"
 
    def extract_symbol(self, query: str) -> str:
        """
        Extract ticker symbol from natural language query.
        Handles: 'TSLA', 'Tesla', 'Should I buy NVDA?', etc.
        """
        query_upper = query.upper()
        for keyword, symbol in SYMBOL_MAP.items():
            if keyword in query_upper:
                return symbol
 
        # Fallback: look for a 2-5 letter all-caps word (likely a ticker)
        import re
        matches = re.findall(r'\b[A-Z]{2,5}\b', query_upper)
        for match in matches:
            if match not in {"THE", "AND", "FOR", "BUY", "SELL", "WHAT", "IS", "ARE"}:
                return match
 
        return "UNKNOWN"
 
    def fetch_market_data(self, symbol: str) -> dict:
        """
        Fetch real OHLCV data from Yahoo Finance.
        Returns price, change, volume, and 5-day history.
        """
        ticker = yf.Ticker(symbol)
 
        # Get latest info
        info = ticker.info
 
        # Get last 5 days of price history
        hist = ticker.history(period="5d")
 
        if hist.empty:
            return {"error": f"No data found for symbol: {symbol}"}
 
        latest = hist.iloc[-1]
        prev   = hist.iloc[-2] if len(hist) > 1 else latest
 
        current_price  = round(float(latest["Close"]), 2)
        previous_close = round(float(prev["Close"]), 2)
        change         = round(current_price - previous_close, 2)
        change_pct     = round((change / previous_close) * 100, 2) if previous_close else 0
 
        return {
            "symbol":         symbol,
            "current_price":  current_price,
            "previous_close": previous_close,
            "change":         change,
            "change_pct":     change_pct,
            "volume":         int(latest["Volume"]),
            "day_high":       round(float(latest["High"]), 2),
            "day_low":        round(float(latest["Low"]), 2),
            "market_cap":     info.get("marketCap", "N/A"),
            "pe_ratio":       info.get("trailingPE", "N/A"),
            "week_52_high":   info.get("fiftyTwoWeekHigh", "N/A"),
            "week_52_low":    info.get("fiftyTwoWeekLow", "N/A"),
            "company_name":   info.get("longName", symbol),
            "sector":         info.get("sector", "N/A"),
        }
 
    def run(self, query: str) -> dict:
        """
        Main method called by Orchestrator.
        """
        symbol = self.extract_symbol(query)
 
        if symbol == "UNKNOWN":
            return {
                "status": "skipped",
                "reason": "Could not identify a stock symbol in your query.",
                "hint":   "Try mentioning a company name or ticker, e.g. 'Analyze Tesla' or 'What is NVDA doing?'"
            }
 
        try:
            data = self.fetch_market_data(symbol)
 
            if "error" in data:
                return {"status": "error", "message": data["error"]}
 
            # Add human-readable sentiment
            if data["change_pct"] > 2:
                sentiment = "strongly bullish"
            elif data["change_pct"] > 0:
                sentiment = "slightly bullish"
            elif data["change_pct"] < -2:
                sentiment = "strongly bearish"
            else:
                sentiment = "slightly bearish"
 
            return {
                "status":    "success",
                "agent":     self.name,
                "symbol":    data["symbol"],
                "company":   data["company_name"],
                "sector":    data["sector"],
                "price":     data["current_price"],
                "change":    data["change"],
                "change_pct": data["change_pct"],
                "sentiment": sentiment,
                "volume":    data["volume"],
                "day_high":  data["day_high"],
                "day_low":   data["day_low"],
                "pe_ratio":  data["pe_ratio"],
                "market_cap": data["market_cap"],
                "52w_high":  data["week_52_high"],
                "52w_low":   data["week_52_low"],
            }
 
        except Exception as e:
            return {
                "status": "error",
                "agent":  self.name,
                "symbol": symbol,
                "message": f"Failed to fetch market data: {str(e)}"
            }
