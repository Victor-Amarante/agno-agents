# create an agent with a temperature search tool and a custom tool to convert Celsius to Fahrenheit
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools import tool
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv
load_dotenv()


@tool
def convert_celsius_to_fahrenheit(temperature_celsius: float) -> float:
  """Converte temperatura em Celsius para Fahrenheit

  Args:
      temperature_celsius (float): Temperatura em graus Celsius

  Returns:
      float: Temperatura convertida para Fahrenheit
  """
  return (temperature_celsius * 9/5) + 32

agent = Agent(
  model=Groq(id='llama-3.3-70b-versatile'),
  tools=[TavilyTools(), convert_celsius_to_fahrenheit],
  description='Você é especialista em pesquisar sobre a temperatura de um local',
  instructions='Forneça apenas a temperatura média do local',
)

agent.print_response('Qual a temperatura de hoje em Recife-PE em Fahrenheit?')
