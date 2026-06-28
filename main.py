from news_tool import get_news
from Planner import create_plan
from financial_tool import get_company_data
from analysis import analyze_company
from report_generator import generate_report, save_report
from tool_registry import show_tools
from react_loop import react_loop
from memory import add_short_term
from memory import add_episode
from memory import show_memory
from long_term_memory import save_research
from long_term_memory import show_long_term_memory
from synthesis_engine import synthesize
from evaluation import evaluate_report
from sec_tool import get_sec_info
from earnings_tool import get_earnings_call
from conflict_resolution import resolve_conflicts
from research_challenges import show_research_challenges
from project_summary import show_project_summary
try:

    ticker = input("Enter stock ticker: ")
    show_tools()
    react_loop(ticker)
    create_plan(ticker)
    add_episode(ticker)

    info = get_company_data(ticker)
    add_short_term("Financial data collected")
    get_news(ticker)
    get_sec_info(ticker)
    get_earnings_call(ticker)
    add_short_term("News collected")
    save_research(ticker)

    print("\n========== COMPANY DATA ==========")

    print("Company Name:", info.get("longName"))
    print("Current Price:", info.get("currentPrice"))
    print("Market Cap:", info.get("marketCap"))
    print("Sector:", info.get("sector"))

    analyze_company(info)
    synthesize(info)
    resolve_conflicts()
    generate_report(info)
    save_report(info)
    show_memory()
    show_long_term_memory()
    show_research_challenges()
    evaluate_report()
    show_project_summary()
except:

    print("Invalid ticker or data not found")