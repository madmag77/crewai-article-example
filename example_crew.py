import os
from crewai import Agent, Task, Crew

from langchain_openai import ChatOpenAI
from tools.search_tool import SearchTools
from dotenv import load_dotenv

from llm_response_logger.response_logger import ResponseLogger

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
api_base = os.getenv('OPENAI_API_BASE')
model_name = os.getenv('OPENAI_MODEL_NAME')

llm = ChatOpenAI(
     model = model_name, # use the full name of model with .gguf extension for LM Studio
     base_url = api_base, # "http://localhost:1234/v1/"
     api_key = api_key, # doesn't matter for LM Studio
     temperature=0.01,
     )

# uncomment if want to log raw LLM responses:
# llm.callbacks = []
# llm.callbacks.append(ResponseLogger())

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in AI and data science related to Interior Design',
  backstory="""You work at a leading tech think tank.
  Your expertise lies in identifying emerging trends.
  You have a knack for dissecting complex data and presenting actionable insights.
  You can use internet search tool for search but you CAN'T use any tools for reading articles, 
  so please use ONLY the information from internet search!
  """,
  verbose=True,
  allow_delegation=False,
  tools=[SearchTools.search_internet],
  llm=llm,
)

writer = Agent(
  role='Tech Content Strategist in Interior Design sphere',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.
  You transform complex concepts into compelling narratives.
  """,
  verbose=True,
  allow_delegation=True,
  llm=llm,
  max_iter=3,
)

task = Task(
  description="""Develop an engaging blog
  post that highlights the most interesting cases of using AI in Interior Design in 2024.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI. 
  If you need some actual information ask your collegues.""",
  expected_output="Full blog post of at least 4 paragraphs",
  agent=writer,
  max_iter=3,
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task],
  verbose=2,
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)