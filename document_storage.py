from typing import Dict, List

import lancedb
from langchain_community.document_loaders import DirectoryLoader, Docx2txtLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import LanceDB
from pdf_md_reader import PDFMarkdownReader
from utils import config_loader

config = config_loader("conf/conf.yaml")


def get_sources_for_user_roles(user_roles: List[str]) -> Dict[str, str]:
    sources = {}
    role_config = {
        "Sozialhilfe": config["DOC_SOURCES"]["SH"],
        "Ergänzungsleistungen": config["DOC_SOURCES"]["EL"],
    }
    for role, folder in role_config.items():
        if role in user_roles:
            sources[role] = folder
    return sources


def create_lancedb_document_store(user_roles: List[str]):
    sources = get_sources_for_user_roles(user_roles)
    documents = []

    for role, folder in sources.items():
        pdf_loader = DirectoryLoader(
            folder, glob="**/*.pdf", loader_cls=PDFMarkdownReader, show_progress=True
        )
        docx_loader = DirectoryLoader(
            folder, glob="**/*.docx", loader_cls=Docx2txtLoader, show_progress=True
        )

        pdf_docs = pdf_loader.load()
        docx_docs = docx_loader.load()

        for doc in pdf_docs + docx_docs:
            doc.metadata["organization"] = role

        documents.extend(pdf_docs + docx_docs)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config["DOC_STORE"]["SPLIT_SIZE"],
        chunk_overlap=config["DOC_STORE"]["SPLIT_OVERLAP"],
    )
    split_docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name=config["EMBEDDINGS"]["MODEL"],
        model_kwargs={"device": "cuda", "trust_remote_code": True},
    )

    db = lancedb.connect(config["DOC_STORE"]["PATH"])
    table = config["DOC_STORE"]["TABLE_NAME"]

    vector_store = LanceDB.from_documents(
        split_docs,
        embeddings,
        connection=db,
        table_name=table,
    )

    return vector_store


def get_lancedb_doc_store():
    db = lancedb.connect(config["DOC_STORE"]["PATH"])
    table = config["DOC_STORE"]["TABLE_NAME"]
    embeddings = HuggingFaceEmbeddings(
        model_name=config["EMBEDDINGS"]["MODEL"],
        model_kwargs={"device": "cuda", "trust_remote_code": True},
    )

    return LanceDB(connection=db, table_name=table, embedding=embeddings)


if __name__ == "__main__":
    create_lancedb_document_store(["Sozialhilfe", "Ergänzungsleistungen"])