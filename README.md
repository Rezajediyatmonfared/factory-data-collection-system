# Factory Production Tracker & Inventory Manager

A lightweight, modular, and web-based solution for real-time factory data management, designed to bridge the gap between enterprise ERP limitations and operational efficiency needs.

![Demo](production_system.gif)

## The Story Behind This Project
As the Head of Production Planning and Inventory Control in an automotive factory, I frequently encountered constraints within our enterprise software. Enterprise systems are often rigid, high-cost to modify, and lack the agility required for rapid operational changes. 

I initiated this project to solve specific data-gap problems:
1. **Data Integrity**: Ensuring daily production and stoppage data is structured and stored for future analysis.
2. **Operational Agility**: Creating a rapid-deployment tool to capture data that the main ERP system fails to track efficiently.
3. **Engineering Approach**: Moving from quick-and-dirty data analysis to a scalable, production-ready environment.

## Project Evolution
### Phase 1: Problem Definition & Prototyping
The project began as an exploratory research phase within **Jupyter Notebooks** (archived in `/notebooks`). The goal was to prove the data logic and ensure the metrics we needed—such as line stoppages and chassis inventory levels—could be accurately calculated and stored.

### Phase 2: Architectural Transition
As the complexity grew, keeping logic within notebooks became unsustainable. I refactored the entire system into a modular **Flask** web application. This transition focused on:
- **Clean Architecture**: Separating concerns to ensure the codebase remains maintainable and scalable.
- **Persistent Data**: Implementing **SQLite** to replace volatile memory, allowing for long-term historical analysis.
- **Frontend Optimization**: Using Bootstrap for a responsive UI, ensuring accessibility on the factory floor.

## Core Modules
- **Production & Delivery**: Tracking real-time production counts versus targets (Plan vs. Actual).
- **Line Stoppage Monitoring**: Capturing downtime details, stations, and root causes for continuous improvement.
- **Chassis Inventory**: Real-time visibility into factory and customs chassis.
- **Parts Shortage**: Proactive management of supply chain bottlenecks.

## Technology Stack
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Frontend**: HTML5, Bootstrap 5 (RTL-optimized for Persian context)
- **Environment**: VS Code, Git

## How to Run
1. Clone the repository:
```bash
   git clone https://github.com/Rezajediyatmonfared/factory-production-tracker.git
   cd factory-production-tracker
   
