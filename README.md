# Factory Production Tracker & Data Ecosystem

## 🏭 The Professional Context
As the Head of Production Planning and Inventory Control at a major automotive manufacturing facility, I have consistently faced a common industrial dilemma: **The Gap.** 

Enterprise Resource Planning (ERP) systems are essential for finance and high-level management, but they are often rigid, slow to adapt, and expensive to modify. Shop floor operations—where production pace changes, parts shortages happen, and bottlenecks emerge—require agility that these monolithic systems often lack.

I developed this web-based tracker to bridge the gap between "what the system says" and "what happens on the factory floor." This tool is not just a form-filler; it is the first step in digitizing our production intelligence.

## 🛠 The Journey: From Industrial Engineering to Code
My approach to this project mirrored the methodologies of industrial engineering: Define, Prototype, Optimize, and Deploy.

### 1. Defining the Problem
The core issue was data fragmentation. Crucial metrics—Line Stoppages, Chassis Inventory, and Parts Shortages—were being managed in disparate files or manually tracked. This prevented real-time analytics and data-driven decision-making.

### 2. Prototyping (The Laboratory Phase)
I began by treating the problem as a data analysis exercise. Using **Jupyter Notebooks**, I modeled the logic, tested the data relationships, and validated the flow (historical analysis of these notebooks can be found in the `/notebooks` directory). This phase was my "laboratory," ensuring that the mathematical foundations were sound before writing a single line of production code.

### 3. Architecture & Deployment (The Scalable Phase)
Moving from a notebook to a persistent application required a shift in architecture. I refactored the project into a robust **Flask** web application with a modular structure:
*   **Database Layer (SQLite):** Decoupled storage for persistent, structured historical data.
*   **Backend Logic:** Standardized routing and data handling to ensure scalability.
*   **Frontend (Responsive UI):** Clean, Bootstrap-based RTL interface designed for factory accessibility.

This architecture ensures that the system is not a one-off script, but a **Mini-ERP framework** that can be expanded to cover other factory domains like Quality Control (QC) or Maintenance (PM).

![Demo](production_system.gif)

## 📂 Project Architecture
The project is built with maintainability in mind:
- **`run.py`**: The entry point for the application.
- **`factory_management_new.db`**: The SQLite database engine capturing live operational data.
- **`/notebooks`**: Archival of the initial research and logical proofs.
- **Templates**: HTML structures utilizing Jinja2 for dynamic rendering.

## 🚀 Key Modules
1.  **Production & Delivery:** Real-time synchronization of planned vs. actual production.
2.  **Line Stoppage Monitor:** Root-cause analysis data collection.
3.  **Inventory Management:** Tracking Factory vs. Customs chassis status.
4.  **Parts Shortage:** Identifying supply chain bottlenecks early.

## 💻 Tech Stack
- **Backend:** Python, Flask, SQLite.
- **Frontend:** HTML5/CSS3, Bootstrap 5.
- **Development Environment:** VS Code, Git.

## Getting Started
1. **Clone the repo:**
```bash
   git clone https://github.com/Rezajediyatmonfared/factory-production-tracker.git
   
