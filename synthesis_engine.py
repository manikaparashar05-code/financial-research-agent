def synthesize(info):

    print("\n========== SYNTHESIS ==========")

    company = info.get("longName")
    sector = info.get("sector")
    market_cap = info.get("marketCap")

    print(f"Company: {company}")
    print(f"Sector: {sector}")

    if market_cap:

        if market_cap > 100000000000:
            print("Assessment: Strong large-cap company")

        elif market_cap > 10000000000:
            print("Assessment: Medium-sized company")

        else:
            print("Assessment: Smaller company")

    print("Data combined from multiple sources.")