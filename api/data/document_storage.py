from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import LanceDB

import lancedb
from core.bento_embeddings import BentoEmbeddings
from data.docling_loader import DoclingLoader
from utils.config import load_config

config = load_config()


def create_lancedb_document_store():
    import os

    os.chdir("..")
    print(os.getcwd())
    sources = config.DOC_SOURCES

    documents = []
    extensions = ["pdf", "docx", "pptx", "html"]  # , "xlsx"]

    for role, folder in sources.items():
        for extension in extensions:
            doc_loader = DirectoryLoader(
                folder,
                glob=f"**/*.{extension}",
                loader_cls=DoclingLoader,
                show_progress=True,
                loader_kwargs={"organization": role},
            )

            docs = doc_loader.load()
            documents.extend(docs)

    embeddings = BentoEmbeddings(api_url=config.EMBEDDINGS.API_URL)

    db = lancedb.connect(config.DOC_STORE.PATH)
    table = config.DOC_STORE.TABLE_NAME

    vector_store = LanceDB.from_documents(
        documents,
        embeddings,
        connection=db,
        table_name=table,
    )

    vector_store.get_table().create_fts_index(
        "text", use_tantivy=True, language="German", stem=True, remove_stop_words=True
    )

    return vector_store


def get_lancedb_doc_store():
    db = lancedb.connect(config.DOC_STORE.PATH)
    table = config.DOC_STORE.TABLE_NAME

    embeddings = BentoEmbeddings(api_url=config.EMBEDDINGS.API_URL)

    return LanceDB(connection=db, table_name=table, embedding=embeddings)
