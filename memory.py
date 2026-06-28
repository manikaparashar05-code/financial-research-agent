short_term_memory = []

episodic_memory = []

def add_short_term(data):

    short_term_memory.append(data)

def add_episode(company):

    episodic_memory.append(company)

def show_memory():

    print("\n========== MEMORY ==========")

    print("Short Term Memory:")

    for item in short_term_memory:
        print("-", item)

    print("\nEpisodic Memory:")

    for item in episodic_memory:
        print("-", item)