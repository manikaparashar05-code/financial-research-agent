import yfinance as yf

def get_company_data(ticker):

    stock = yf.Ticker(ticker)

    return stock.info