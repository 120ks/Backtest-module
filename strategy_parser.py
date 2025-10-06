class StrategyParser:
    def __init__(self, config=None):
        self.config = config or {}

    # Example placeholder for other parsing methods
    def parse(self, text: str):
        tokens = text.split()
        # simplified mock example for demonstration
        symbol = self._extract_symbol(text)
        return {"symbols": symbol}

    
    
    def _extract_symbol(self, text: str) -> list[str]:
        """Extract all ticker symbols (case-insensitive) from text."""
        import re

        # Normalize text to uppercase
        text_upper = text.upper()

        # Capture all ticker-like sequences (1–5 letters, optional dash, separated by commas/and/spaces)
        potential = re.findall(r"[A-Z]{1,5}(?:-[A-Z])?", text_upper)

        # Expanded known tickers list
        known_tickers = [
            "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA",
            "META", "NVDA", "JPM", "V", "BRK-B", "NFLX",
            "INTC", "AMD", "BAC", "XOM", "KO", "PEP"
        ]

        # Filter only known tickers
        tickers = [t for t in potential if t in known_tickers]

        # Return unique list if found, else fallback
        if tickers:
            return sorted(set(tickers))

        default_symbol = self.config.get("backtest", {}).get("default_symbol", "AAPL")
        return [default_symbol]
