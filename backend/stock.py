import yfinance as yf

def get_stock_data(ticker: str):
    """
    Lekérdezi egy adott részvény (ticker) aktuális adatait (záróár, árfolyamváltozás, forgalom)
    az utolsó 1 napra vonatkozóan.

    :param ticker: A részvény ticker kódja (pl. 'AAPL' vagy 'GOOG')
    :return: Egy dictionary a részvény adataival
    """
    try:
        # A részvény adatainak lekérése a Yahoo Finance API-n keresztül
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")  # 1 napra lekérjük az adatokat

        if not data.empty:
            # Az utolsó nap (1 nap) záró ára, árfolyamváltozása és forgalma
            price = data['Close'].iloc[0]  # Az első (0. pozíciójú) záróár
            change = data['Close'].iloc[0] - data['Open'].iloc[0]  # Az árfolyamváltozás
            volume = data['Volume'].iloc[0]  # Az első (0. pozíciójú) forgalom

            # Visszatérési adat formátuma
            return {
                "ticker": ticker,
                "price": price,
                "change": change,
                "volume": volume,
            }
        else:
            return {"message": "No data found for ticker."}
    except Exception as e:
        return {"message": f"Error fetching data: {str(e)}"}

# # Tesztelés
# stock_data = get_stock_data("GOOG")  # Például Apple részvény adatai
# print(stock_data)
