from langchain_milvus import Milvus
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# import getpass
import os

os.environ["ZHIPUAI_API_KEY"] ="<your_zhipu_ai_token>"

file_path='../data/Contract.pdf'
 # 初始化pdf 文档加载器
loader = PyPDFLoader(file_path=file_path)
 # 将pdf中的文档解析为 langchain 的document对象
documents = loader.load()
 # 将文档拆分为合适的大小
text_splitter = RecursiveCharacterTextSplitter(chunk_size=150, chunk_overlap=20)
docs = text_splitter.split_documents(documents)

# 初始化 embedding model
embeddings_model = ZhipuAIEmbeddings(
    model="embedding-2",
    # With the `embedding-3` class
    # of models, you can specify the size
    # of the embeddings you want returned.
    # dimensions=1024
)

vector = Milvus.from_documents(
     documents=docs, # 设置保存的文档
     embedding=embeddings_model, # 设置 embedding modelpip install --upgrade milvus_lite
     collection_name="Contract", # 设置 集合名称
     drop_old=True,
    #  connection_args={"uri": URI},
     connection_args={"host": "127.0.0.1", "port": "19530"},# Milvus连接配置
 )

##Test code once document is loaded into DB
# query = "What is the purchase price?"
# docs = vector.similarity_search(query,k=2)

# chat = ChatZhipuAI(
#     model="glm-4",
#     temperature=0.5,
# )
# messages = [
#     SystemMessage(content="Your role is a assistant."),
#     HumanMessage(content="Please find the purchase price from following context"+docs[0].page_content+". Please just give a result without explanation."),
# ]
# response = chat.invoke(messages)
# print(response.content) 