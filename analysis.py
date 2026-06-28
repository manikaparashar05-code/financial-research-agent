def analyze_company(info):

    print("\n========== BASIC ANALYSIS ==========")

    market_cap = info.get("marketCap")
    current_price = info.get("currentPrice")

    if market_cap:

        if market_cap > 100000000000:
            print("Large Cap Company")

        elif market_cap > 10000000000:
            print("Mid Cap Company")

        else:
            print("Small Cap Company")

    else:
        print("Market Cap Data Not Available")

    if current_price:

        if current_price > 200:
            print("Stock Price is High")

        else:
            print("Stock Price is Moderate")

    else:
        print("Current Price Data Not Available")