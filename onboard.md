##Use case
Suppose you have some text documents (PDF, blog, Notion pages, etc.) and want to ask questions related to the contents of those documents. LLMs, given their proficiency in understanding text, are a great tool for this.

In this walkthrough we'll go over how to build a question-answering over documents application using LLMs. Two very related use cases which we cover elsewhere are:

QA over structured data (e.g., SQL)
QA over code (e.g., Python)
intro.png

## Overview
The pipeline for converting raw unstructured data into a QA chain looks like this:

* [ ] - `Loading:` First we need to load our data. Unstructured data can be loaded from many sources. Use the LangChain integration hub to browse the full set of loaders. Each loader returns data as a LangChain Document. Use Case['https://python.langchain.com/docs/use_cases/code_understanding']

* [ ] - `Splitting:` Text splitters break Documents into splits of specified size

* [ ] - `Storage:` Storage (e.g., often a vectorstore) will house and often embed the splits

* [ ] - `Retrieval:` The app retrieves splits from storage (e.g., often with similar embeddings to the input question)

* [ ] - `Generation:` An LLM produces an answer using a prompt that includes the question and the retrieved data

* [ ] - `Conversation (Extension):` Hold a multi-turn conversation by adding Memory to your QA chain.
flow.jpeg

