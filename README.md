## RAG sample

This is a sample project demonstrate build a RAG service with a client UI built by VUE. User can ask questions related to the sample contract document using current project. 

TODO: Based on this sample, your can extend this project to a knowledge base by loading more PDF documents.

The RAG project is built with 
- VUE
- Python
- Django Rest Framework
- Milvus
- Langchain
- Zhipu AI

## Deployment Guide

1. install Python
2. Create a Python virtual envrinoment.
```
python3 -m venv ~/.venv
source ~/.venv/bin/activate
```
3.Install required dependencies
```
cd .venv 
pip install Milvus
pip install pypdf
pip install zhipuai
pip install langchain langchain-community langchain_milvus
pip install django djangorestframework django-cors-headers
```

4. Install Milvus standalone
4.1 Create a 'Milvus" folder with following subfolders. /conf /db /logs /pic /volumes /wal
4.2 Get milvus-standalone-docker-compose.yml
from https://github.com/milvus-io/milvus/releases  (v2.4.14 or later)
4.3 Rename the milvus-standalone-docker-compose.yml to docker-compose.yml and put it in /Milvus
https://blog.csdn.net/m0_52424297/article/details/140796305
4.4 Start/Stop Milvus
```
docker compose up -d
docker compose down
```
5. Install Attu(Optional)
Attu is a client tool allow you view data in Milvus. Download the installer package from the "Assets" section.
https://github.com/zilliztech/attu/releases/

6. Add Zhipu AI token
   6.1 Get token from https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys
   6.2 Search "ZHIPUAI_API_KEY" in code and input the Zhipu AI token. There should be 2 places need the token.
7. Load Data into Milvus
```
cd src
python3 LoadPDF.py
```
Open Attu and connnect to Milvus. You should be able to see a "Contact" collection

8. Start Django rest framework
```
cd server/restapi
python3 manage.py runserver
```

Verify if API work
Open http://localhost:8000/api/chat/ and send a POST with content 
```
{
    "text": "What is the total price"
}
```
The response looks like "The total purchase price is $20,000.00."

9. Start VUE App
```
cd /client
npm install
npm run dev
```
The client app is opened at http://localhost:5173/

Try ask question like "What is the total price" or "What is the address"