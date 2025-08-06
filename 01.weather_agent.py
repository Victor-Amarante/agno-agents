from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
load_dotenv()


agent = Agent(
  model=Groq(id='llama-3.3-70b-versatile'),
  tools=[TavilyTools()]
)

agent.print_response('Quantos estados tem o estado de Pernambuco no Brasil?')
