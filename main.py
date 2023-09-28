from langchain.agents import load_tools
from langchain.agents import initialize_agent
import os
from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI

_ = load_dotenv('config.env')
llm = OpenAI(temperature = 0)

tools = load_tools(["wikipedia", "llm-math"], llm = llm)
agent = initialize_agent(tools, llm, agent = 'zero-shot-react-description', verbose = True)

input = ("Ask a question, any question :)")
agent.run(input)