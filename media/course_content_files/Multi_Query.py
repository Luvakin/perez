from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaLLM,OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableMap
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.load import dumps, loads
import os
from operator import itemgetter

os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = 'Multi_query'
os.environ['LANGCHAIN_API_KEY'] = '<>API'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'

os.environ["GROQ_API_KEY"] = "<api>"


# llm = OllamaLLM(
#      model= "llama3:8b", 
#      temperature= 0
#  )


llm = ChatGroq(
     model="deepseek-r1-distill-llama-70b", 
     temperature=0.0,
 )

embedding_model = OllamaEmbeddings(model = 'nomic-embed-text')

file_path = "C:\\Users\\HP\\Documents\\400leve\\Data-Structure-Final-.pdf"
loader = PyPDFLoader(file_path)
docs_book = loader.load()



print(docs_book)
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 300, chunk_overlap= 50)


splits = text_splitter.split_documents(docs_book)

vectorstore = Chroma.from_documents(documents=splits, embedding=embedding_model, persist_directory="C:\\Users\\HP\\Documents\\400leve\\CPE401\\rag_from_scratch\\vectorstore")

retriever = vectorstore.as_retriever()


template  = """ You are an AI language model assistant. Your task is to generate five different versions of the given user question to retrieve relevant documents from a vector database. By generating multiple perspective on the user question, your goal is to help the user study more efficiently and answer question related to the context of the document """

prompt_perspectives = ChatPromptTemplate.from_template(template)


generate_queries = (prompt_perspectives
                    |llm
                    |StrOutputParser()
                    |(lambda x: x.split("n/")))


def get_unique_union(documents: list[list]):
    """ Union of retrieved docs"""

    flattened_docs = [dumps(doc) for sublist in documents for doc in sublist]
    unique_docs = list(set(flattened_docs))

    return [loads(doc) for doc in unique_docs]



question = "what are the features for data structures"


retrieval_chain = generate_queries | retriever.map() | get_unique_union

docs = retrieval_chain.invoke({"question":question})



template = """Answer the following question based on this context:

{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)



final_rag_chain = (
    {"context": retrieval_chain, 
     "question": itemgetter("question")} 
    | prompt
    | llm
    | StrOutputParser()
)

print(final_rag_chain.invoke({"question":question}))