"""from langchain.vectorstores import Qdrant
from langchain.embeddings import SentenceTransformerEmbeddings
from qdrant_client import QdrantClient

embeddings = SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")

url = "http://localhost:6333"

client = QdrantClient(
    url=url, prefer_grpc=False
)

print(client)
print("##############")

db = Qdrant(client=client, embeddings=embeddings, collection_name="vector_db")

print(db)
print("######")
query = "What is Metastatic disease?"

docs = db.similarity_search_with_score(query=query, k=3)
for i in docs:
    doc, score = i
    print({"score": score, "content": doc.page_content, "metadata": doc.metadata})


"""







from langchain.vectorstores import Qdrant
from langchain.embeddings import SentenceTransformerEmbeddings
from qdrant_client import QdrantClient
import os  # Added for environment variables

embeddings = SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")

# Use environment variables for cloud configuration
"""client = QdrantClient(
    url=os.getenv("QDRANT_URL", "https://QDRANT_URL.europe-west3-0.gcp.cloud.qdrant.io"),
    api_key=os.getenv("QDRANT_API_KEY"),
    prefer_grpc=False
)"""
client = QdrantClient(
    # url=os.getenv("QDRANT_URL", "https://868005ec-814c-4a06-b5f5-f4051fdf2a5d.europe-west3-0.gcp.cloud.qdrant.io"),
    #api_key=os.getenv("QDRANT_API_KEY"),
    api_key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzQ2MTE5OTc1fQ.MxRF1I8LOx3Oio3ChLmffHsj7lxn1ekl9fuAb-4iSBU",
    url = "https://868005ec-814c-4a06-b5f5-f4051fdf2a5d.europe-west3-0.gcp.cloud.qdrant.io",
    prefer_grpc=False
)

print(client)
print("##############")

db = Qdrant(client=client, embeddings=embeddings, collection_name="vector_db")

print(db)
print("######")

query = "What is Metastatic disease?"

# Updated similarity search (newer LangChain versions)
docs = db.similarity_search_with_relevance_scores(query=query, k=1)
for doc, score in docs:
    print({
        "score": score,
        "content": doc.page_content,
        "metadata": doc.metadata
    })