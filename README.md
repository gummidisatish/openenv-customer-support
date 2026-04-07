# Customer Support OpenEnv

## Overview

This project is a simple simulation of a real-world customer support system. The goal is to create an environment where an AI agent can read emails, understand them, and take appropriate actions like classifying the issue, extracting details, and generating a response.

---

## What this project does

The environment provides three main tasks:

1. **Classification**
   The agent identifies the category of the email (for example: Billing).

2. **Extraction**
   The agent extracts important details such as order ID, date, and issue.

3. **Response Generation**
   The agent generates a proper reply to the customer.

---

## How it works

* The environment starts with an email using the `/reset` endpoint
* The agent performs actions using `/step`
* Each action gives a reward based on correctness
* Final performance can be checked using `/grader` or `/baseline`

---

## API Endpoints

* `/reset` → Load a new email
* `/step` → Perform an action
* `/state` → View current state
* `/tasks` → View available tasks
* `/baseline` → Run a sample agent

---

## Running the project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python -m uvicorn app.main:app --reload
```

Open in browser:

```text
http://127.0.0.1:8000/docs
```

---

## Baseline

You can test the system by running:

```text
http://127.0.0.1:8000/baseline
```

This runs a simple agent and shows scores for all tasks.

---

## Notes

* This is a basic version meant for demonstration
* More tasks and data can be added later
* The reward system is simple and can be improved

---

## Summary

This project shows how an AI agent can interact with a structured environment to solve real-world tasks like customer support.
