"""import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient

embeddings = SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")

client = QdrantClient(
    url=os.getenv("QDRANT_URL", "https://868005ec-814c-4a06-b5f5-f4051fdf2a5d.europe-west3-0.gcp.cloud.qdrant.io"),
    #api_key=os.getenv("QDRANT_API_KEY"),
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzQ2MTE5OTc1fQ.MxRF1I8LOx3Oio3ChLmffHsj7lxn1ekl9fuAb-4iSBU",

    prefer_grpc=False
)



loader = DirectoryLoader('data/', glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

qdrant = Qdrant.from_documents(
    texts,
    embeddings,
    client=client,
    collection_name="vector_db"
)

#print("Vector DB Successfully Created!")



"""




import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.vectorstores import Qdrant

# Initialize embeddings
embeddings = SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")

# Load documents
loader = DirectoryLoader('data/', glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)
documents = loader.load()

# Split documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

# Create Qdrant collection
qdrant = Qdrant.from_documents(
    texts,
    embeddings,
    #url=os.getenv("QDRANT_URL"),
    url = "https://868005ec-814c-4a06-b5f5-f4051fdf2a5d.europe-west3-0.gcp.cloud.qdrant.io",
    #api_key=os.getenv("QDRANT_API_KEY"),
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzQ2MTE5OTc1fQ.MxRF1I8LOx3Oio3ChLmffHsj7lxn1ekl9fuAb-4iSBU",
    collection_name="vector_db",
    prefer_grpc=False
)

print("Vector DB Successfully Created!")