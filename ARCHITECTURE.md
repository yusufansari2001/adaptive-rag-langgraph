# ARCHITECTURE.md

# Adaptive RAG LangGraph

## Repository

adaptive-rag-langgraph

---

# Project Objective

Build a production-grade Adaptive Retrieval Augmented Generation (Adaptive RAG) system from scratch while learning every component of modern AI application architecture.

The system should not blindly perform retrieval for every question.

Instead, it should intelligently determine:

* Whether retrieval is needed
* Which retrieval strategy should be used
* Whether web search is required
* Whether the retrieved context is relevant
* Whether the generated answer is grounded in evidence
* Whether the final answer actually answers the user's question

The final system should be capable of handling:

* General knowledge questions
* Document-based questions
* Real-time questions
* Multi-hop reasoning questions
* Hybrid retrieval scenarios

---

# What Is Adaptive RAG?

Traditional RAG:

Question
↓
Retrieve
↓
Generate

Adaptive RAG:

Question
↓
Analyze
↓
Choose Strategy
↓
Retrieve (if needed)
↓
Generate
↓
Verify

The retrieval strategy adapts based on the question.

---

# Example Scenarios

## Example 1

Question:

What is Java?

Decision:

Direct LLM Answer

Reason:

No retrieval required.

---

## Example 2

Question:

What does the uploaded employee handbook say about leave policy?

Decision:

Vector Retrieval

Reason:

Answer exists inside uploaded documents.

---

## Example 3

Question:

Who won yesterday's IPL match?

Decision:

Web Search

Reason:

Requires real-time information.

---

## Example 4

Question:

Compare our leave policy with Infosys leave policy.

Decision:

Vector Retrieval
+
Web Search

Reason:

Need both internal and external sources.

---

## Example 5

Question:

Compare Spring Boot, Quarkus and Micronaut based on startup time, memory usage and ecosystem maturity.

Decision:

Multi-Hop Retrieval

Reason:

Complex comparison requiring multiple information sources.

---

# Final Architecture

User Question

↓

Complexity Analyzer

↓

Adaptive Router

↓

┌─────────────────────────────────────────────┐
│                                             │
│ Direct LLM                                  │
│ Vector Retrieval                            │
│ Web Search                                  │
│ Hybrid Retrieval                            │
│ Multi-Hop Retrieval                         │
│                                             │
└─────────────────────────────────────────────┘

↓

Document Grader

↓

Query Rewriter

↓

Generator

↓

Hallucination Checker

↓

Answer Verifier

↓

Final Response

---

# Development Phases

The project will be built incrementally.

Every phase introduces one major concept.

---

# Phase 1

## Basic RAG

Architecture

Question

↓

Retriever

↓

Vector Database

↓

LLM

↓

Answer

Goals

* Understand embeddings
* Understand chunking
* Understand vector search
* Understand retrieval

Technologies

* LangChain
* OpenAI Embeddings
* FAISS

Deliverable

Ask questions against uploaded PDFs.

---

# Phase 2

## LangGraph Foundation

Architecture

Question

↓

Retrieve Node

↓

Generate Node

↓

Answer

Goals

Learn:

* StateGraph
* Nodes
* Edges
* START
* END

Deliverable

RAG implemented using LangGraph.

---

# Phase 3

## Query Routing

Architecture

Question

↓

Classifier

↓

General

Retrieval

Search

Goals

Learn:

* Structured Output
* Conditional Edges
* Routing Logic

Deliverable

System automatically selects route.

---

# Phase 4

## Document Grading

Architecture

Retriever

↓

Document Grader

↓

Relevant?

├── Yes

└── No

Goals

Learn:

* LLM-as-a-Judge
* Relevance Evaluation

Deliverable

Reject irrelevant retrievals.

---

# Phase 5

## Query Rewriting

Architecture

Question

↓

Retrieve

↓

Poor Results

↓

Rewrite Query

↓

Retrieve Again

Goals

Learn:

* Query Expansion
* Query Optimization

Deliverable

Improved retrieval quality.

---

# Phase 6

## Hallucination Detection

Architecture

Context

*

Generated Answer

↓

Hallucination Grader

↓

Grounded?

↓

Accept or Retry

Goals

Learn:

* Grounding
* Verification

Deliverable

Reduced hallucinations.

---

# Phase 7

## Answer Verification

Architecture

Question

*

Answer

↓

Answer Grader

↓

Correct?

↓

Accept or Retry

Goals

Learn:

* Answer Validation
* LLM Evaluation

Deliverable

Ensure answer addresses the question.

---

# Phase 8

## Adaptive Retrieval Strategy

Architecture

Question

↓

Complexity Classifier

↓

Simple

Medium

Complex

Simple

↓

Direct LLM

Medium

↓

Single Retrieval

Complex

↓

Multi-Step Retrieval

Goals

Learn:

* Adaptive Retrieval
* Dynamic Workflows

Deliverable

Different retrieval strategies per question.

---

# Phase 9

## Multi-Hop Retrieval

Architecture

Question

↓

Question Decomposition

↓

Sub Question 1

Sub Question 2

Sub Question 3

↓

Retrieve

Retrieve

Retrieve

↓

Merge Context

↓

Generate

Goals

Learn:

* Multi-Hop Reasoning
* Query Decomposition

Deliverable

Handle complex questions.

---

# Phase 10

## Hybrid Retrieval

Architecture

Question

↓

Vector Search

*

Keyword Search

↓

Merge Results

↓

Generate

Goals

Learn:

* Hybrid Search
* Dense Retrieval
* Sparse Retrieval

Deliverable

Improved recall.

---

# Phase 11

## Web Search Integration

Architecture

Question

↓

Need Current Information?

↓

Tavily Search

↓

Generate

Goals

Learn:

* Tool Calling
* External Knowledge Sources

Deliverable

Real-time answers.

---

# Phase 12

## Memory

Architecture

Conversation

↓

Memory Store

↓

Context Builder

↓

Generate

Goals

Learn:

* Conversation Memory
* Session Management

Deliverable

Multi-turn conversations.

---

# Phase 13

## FastAPI Backend

Endpoints

POST /query

POST /upload

POST /health

Goals

Learn:

* API Design
* Backend Architecture

Deliverable

Production-ready API.

---

# Phase 14

## Streamlit Frontend

Features

* Chat Interface
* File Upload
* Session History

Goals

Learn:

* Frontend Integration

Deliverable

Interactive application.

---

# Planned Folder Structure

adaptive-rag-langgraph/

app/

├── graph/

│ ├── state.py

│ ├── graph_builder.py

│ └── routing.py

│

├── nodes/

│ ├── classify.py

│ ├── retrieve.py

│ ├── grade_documents.py

│ ├── rewrite_query.py

│ ├── generate.py

│ ├── hallucination.py

│ ├── answer_verifier.py

│ ├── web_search.py

│ └── multi_hop.py

│

├── prompts/

│ ├── classifier.py

│ ├── grading.py

│ ├── rewriting.py

│ ├── generation.py

│ └── verification.py

│

├── vectorstore/

│ ├── embeddings.py

│ ├── ingest.py

│ ├── retriever.py

│ └── qdrant_setup.py

│

├── memory/

│ └── chat_history.py

│

├── api/

│ └── routes.py

│

├── config/

│ └── settings.py

│

└── main.py

data/

documents/

tests/

requirements.txt

.env

README.md

ARCHITECTURE.md

.gitignore

---

# Git Commit Strategy

Commit 1

Project Setup

Commit 2

Basic RAG

Commit 3

FAISS Integration

Commit 4

LangGraph Foundation

Commit 5

Query Router

Commit 6

Document Grader

Commit 7

Query Rewriter

Commit 8

Hallucination Detection

Commit 9

Answer Verification

Commit 10

Adaptive Retrieval Strategy

Commit 11

Multi-Hop Retrieval

Commit 12

Hybrid Retrieval

Commit 13

Web Search

Commit 14

Memory

Commit 15

FastAPI

Commit 16

Streamlit

Commit 17

Documentation

Commit 18

Production Cleanup

---

# Success Criteria

The final system must:

✓ Answer general knowledge questions

✓ Answer questions from uploaded documents

✓ Search the web when required

✓ Rewrite poor queries

✓ Grade retrieved documents

✓ Detect hallucinations

✓ Verify answers

✓ Support multi-hop retrieval

✓ Support adaptive routing

✓ Maintain conversation memory

✓ Expose APIs

✓ Provide a web interface

✓ Be deployable

✓ Be portfolio-ready

✓ Demonstrate LangGraph expertise

---

# Current Status

Phase: 0

Next Step:

Repository Creation

Repository Name:

adaptive-rag-langgraph
