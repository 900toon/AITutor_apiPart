from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain_community.llms import OpenAI
from langchain_openai import ChatOpenAI

import os

os.environ['OPENAI_API_KEY'] = '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'

api_key = "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"

llm = ChatOpenAI(
    openai_api_key = api_key,
    temperature = 0,
    model_name = "gpt-3.5-turbo"
)

ConversationEntityMemory(llm = llm, k=10)
