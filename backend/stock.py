import yfinance as yf
import json

def get_historical_prices_json(symbol, start_date, end_date, interval="1d"):
    stock = yf.Ticker(symbol)
    data = stock.history(start=start_date, end=end_date, interval=interval)
    if not data.empty:
        # Konvertálás JSON objektummá
        json_data = data.reset_index().to_json(orient="records", date_format="iso")
        return json.loads(json_data)
    else:
        return {"error": "Nem található adat a megadott időszakra."}

# Használat
if __name__ == "__main__":
    stock_symbol = "AAPL"  # Apple részvény szimbólum
    start = "2022-01-01"  # Kezdő dátum (ÉÉÉÉ-HH-NN)
    end = "2022-12-31"    # Záró dátum (ÉÉÉÉ-HH-NN)
    interval = "1d"       # Időköz (pl. "1d", "1wk", "1mo")

    historical_data = get_historical_prices_json(stock_symbol, start, end, interval)
    print(json.dumps(historical_data, indent=2, ensure_ascii=False))
