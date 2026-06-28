import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="financial_research"
)

def save_research(company):

    collection.add(
        documents=[company],
        ids=[company]
    )

def show_long_term_memory():

    print("\n========== LONG TERM MEMORY ==========")

    results = collection.get()

    for doc in results["documents"]:
        print("-", doc)