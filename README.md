# Industrial Intelligence Platform: Factory Production & Inventory Control

A web-based production data collection and inventory management system designed for real manufacturing operations.  
This project integrates **industrial engineering logic**, **data analysis workflows**, and **software engineering architecture** to support production tracking, stoppage analysis, and inventory visibility in a factory environment.

---

## Overview

This platform was developed to address practical challenges in production planning and shop-floor monitoring, where operational data is often fragmented, manually recorded, and difficult to analyze consistently.

The system provides a structured way to collect, manage, and review production and inventory-related information, with a strong focus on:

- daily production tracking
- capacity monitoring
- line stoppage logging
- root-cause-oriented categorization
- inventory and chassis flow control
- shortage reporting and operational visibility

The project reflects a multidisciplinary approach at the intersection of:

- **Industrial Engineering** — process design, production planning, bottleneck awareness, and operational control  
- **Data Science** — exploratory analysis, KPI thinking, structured data modeling, and insight generation  
- **Software Engineering** — modular application design, persistent storage, and scalable deployment through a web-based interface

---

## System Preview

### 1) Operational Web Application (Persian UI)

> The deployed interface is in Persian because the system was designed for real operational use in an Iranian manufacturing context.

![Operational Web Application](./production_system.gif)

### 2) Early Analytical / Prototype Version (Jupyter-Based)

> Before the web architecture was developed, the problem was first modeled and validated in Jupyter Notebook.  
> This prototype phase helped test the logic, workflows, and data structure before implementation as a full web application.

![Jupyter Prototype](./notebooks/your-second-gif-name.gif)

---

## Project Evolution

This project was not built as a web application from the start.

It began as a **Jupyter Notebook-based prototype**, where the core workflow, data structure, and operational logic were first explored and validated using Python. That early version made it possible to:

- test data organization logic
- simulate production and inventory workflows
- evaluate the feasibility of the solution
- identify what information operators and planners actually needed
- examine whether the analytical outputs matched real production requirements

After validating the concept, the solution was redesigned as a **Flask-based web application** because the notebook format was not suitable for long-term operational use.

The web version was necessary to support:

- structured and repeatable daily data entry
- multi-page workflow organization
- persistent relational storage
- improved usability for non-technical users
- easier operational deployment in a real factory setting

In short, the development path was:
```text
Problem in Production Environment
→ Jupyter-Based Prototype
→ Workflow Validation
→ Flask Web Architecture
→ Operational Factory Tool
