from agents.tool import tools
from chains.memory import get_llm, get_user_memory
from langchain.agents import AgentType, initialize_agent

agent_cache = {}

def get_agent(user_id: str):
    if user_id not in agent_cache:
        llm = get_llm()
        memory = get_user_memory(user_id)
        agent = initialize_agent(
            tools = tools,
            llm = llm,
            memory = memory,
            agent = AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            verbose =True
        )
        agent_cache[user_id] = agent
    return agent_cache[user_id]

def run_agent(user_id:str, prompt:str):
    return get_agent(user_id).invoke(prompt)