from langchain_milvus import Milvus
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# import getpass
import os

os.environ["ZHIPUAI_API_KEY"] ="<your_zhipu_ai_token>"

def search_in_document(question):
    # 初始化 embedding model
    embeddings_model = ZhipuAIEmbeddings(
        model="embedding-2",
        # With the `embedding-3` class
        # of models, you can specify the size
        # of the embeddings you want returned.
        # dimensions=1024
    )

    # from langchain_community.vectorstores import Milvus
    vector = Milvus(
        embedding_function=embeddings_model, # 设置 embedding modelpip install --upgrade milvus_lite
        collection_name="Contract", # 设置 集合名称
        #  connection_args={"uri": URI},
        connection_args={"host": "127.0.0.1", "port": "19530"},# Milvus连接配置
    )

    docs = vector.similarity_search(question,k=2)

    chat = ChatZhipuAI(
        model="glm-4",
        temperature=0.5,
    )
    prompt = question+".Please find the answer from following context.\""+docs[0].page_content+"\" and \""+docs[1].page_content+"\". Please just give a result without explanation."
    print(prompt)
    messages = [
        SystemMessage(content="Your role is a assistant."),
        HumanMessage(content=prompt),
    ]
    response = chat.invoke(messages)
    print(response.content) 
    return response.content