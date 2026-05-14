# 🤖 Insurance Chatbot RAG - Complete Application Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Core Components](#core-components)
6. [Installation & Setup](#installation--setup)
7. [Usage Guide](#usage-guide)
8. [API Documentation](#api-documentation)
9. [Configuration](#configuration)
10. [Troubleshooting](#troubleshooting)
11. [Future Enhancements](#future-enhancements)

---

## Project Overview

### What is This Application?

The **Insurance Chatbot RAG** is an intelligent conversational AI system designed to answer insurance-related queries with precision and context awareness. It implements a **Retrieval-Augmented Generation (RAG)** pipeline that combines:

- **Document Retrieval**: Uses FAISS (Facebook AI Similarity Search) for fast semantic search
- **Text Generation**: Leverages transformer models for coherent, context-aware responses
- **Multiple Interfaces**: Supports both web-based (Flask) and interactive (Gradio) chat interfaces

### Key Features

✅ **Retrieval-Augmented Generation (RAG)**: Combines retrieval and generation for accurate, grounded responses  
✅ **Vector Search**: FAISS-based semantic similarity search for optimal document retrieval  
✅ **Pre-trained Models**: Sentence Transformers for embeddings + FLAN-T5/Mistral for text generation  
✅ **Dual Interfaces**: Flask web app + Gradio chat interface for flexibility  
✅ **JSON Knowledge Base**: Easy-to-maintain document storage  
✅ **Fast & Efficient**: Runs on CPU with minimal memory footprint  
✅ **Production-Ready**: Scalable backend architecture  

### Use Cases

- 🏥 Insurance policy inquiries
- 📋 Coverage information lookup
- ❓ FAQ automation
- 📞 Customer support automation
- 🔍 Insurance knowledge base search

---

## System Architecture

### High-Level Flow Diagram
