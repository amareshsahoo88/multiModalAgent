from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground

#web search agent 
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model =Groq(id="llama3-70b-8192"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

#Finance agent
financial_agent = Agent(
    name="Financial AI Agent",
    role="Analyze financial data and provide insights",
    model=Groq(id="llama3-70b-8192") ,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news =True)],
    instructions=["Use Tables to dsplay the data"],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    model=Groq(id="llama3-70b-8192") ,
    team=[web_search_agent, financial_agent],
    instructions=["Always include sources","use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)


