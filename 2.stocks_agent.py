# create an agent that get stocks information
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
load_dotenv()


system_prompt = '''
You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.
'''

stock_agent = Agent(
  model=Groq(id='llama-3.3-70b-versatile'),
  tools=[YFinanceTools()],
  description=system_prompt,
  instructions='Use tables to display the final answer. Do not include any other text.',
  debug_mode=True
)

stock_agent.print_response('Qual a cotação atual do Dólar Canadense em relação ao Real Brasileiro (BRL)?', stream=True)
