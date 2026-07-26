# Industrial Intelligence Platform: Factory Production & Inventory Control
### *A Multidisciplinary Approach to Manufacturing Excellence*

## 🏭 The Philosophy of Synthesis: The Trifecta of Engineering
This platform is the result of a complex problem-solving journey. It represents a rare intersection of three distinct domains, proving that modern industrial problems cannot be solved by a single discipline alone.

1.  **Industrial Engineering (The Process Strategy):** 
    Leveraging my background as Head of Production Planning, I designed the system to address **Operational Bottlenecks**, **Lean Manufacturing** principles, and **OEE (Overall Equipment Effectiveness)**. The system doesn't just store data; it maps the physical flow of the factory.

2.  **Data Science (The Analytical Engine):** 
    Every feature was first prototyped in **Jupyter Notebooks**. I applied exploratory data analysis (EDA) to production logs to ensure the logic reflects the reality of the shop floor. This phase validated how stoppage durations correlate with daily targets—turning raw numbers into predictive insights.

3.  **Software Engineering (The Scalable Infrastructure):** 
    To make these insights accessible, I architected a full-stack **Flask** application. By using a modular design and an optimized **SQLite** database, I ensured that the tool is responsive, reliable, and ready for deployment in a high-pressure industrial environment.

---

## 📸 System Preview (Dynamic Demo)
Below is a visual overview of the platform in action, showcasing the seamless integration of production tracking and inventory control:

![Factory Production Tracker Demo](production_system.gif)

---

## 🛠 Strategic Operational Modules: Deep Dive

### 1. Production Throughput & Capacity Planning
*   **IE Logic:** Managing the "Takt Time" and ensuring daily output matches the assembly line's theoretical capacity.
*   **The Bridge:** This module acts as a real-time **Plan vs. Actual** dashboard. It identifies "Under-Capacity" events instantly, allowing for immediate corrective actions in the next shift.

### 2. Line Stoppage & Root Cause Analysis (RCA)
*   **IE Logic:** Following the **DMAIC (Define, Measure, Analyze, Improve, Control)** methodology to reduce downtime.
*   **The Bridge:** By categorizing stoppages (Technical, Human, Material), we create a high-fidelity data set. This data is the foundation for future Machine Learning models to predict and prevent machine failures before they occur.

### 3. Smart Inventory & Chassis Management
*   **IE Logic:** Solving the **Just-in-Time (JIT)** puzzle.
*   **The Bridge:** This module tracks the lifecycle of a chassis—from the Customs warehouse to the Factory floor. It prevents the "Bullwhip Effect" in the supply chain by providing a single source of truth for inventory levels.

### 4. Parts Shortage & Supply Chain Early-Warning
*   **IE Logic:** Minimizing the "Work-in-Process" (WIP) bottlenecks caused by missing components.
*   **The Bridge:** A proactive monitoring tool that logs missing parts. It serves as a direct communication bridge between the Production floor and the Procurement department.

---

## 🚀 The Engineering Lifecycle: From Lab to Floor

### Phase 1: The Laboratory (Validation)
The development started in `/notebooks`. Here, I treated the factory data as a scientific subject. I used **Pandas** and **Matplotlib** to visualize production trends and validate that the proposed database schema would support complex industrial queries.

### Phase 2: The Architecture (Deployment)
Moving to a **Flask-based** architecture, I focused on:
*   **Relational Integrity:** Ensuring that every production log is linked to a specific chassis and stoppage reason.
*   **User Experience (UX):** Designing an RTL-optimized (Persian) interface with **Bootstrap 5** to ensure that operators, regardless of their tech proficiency, can input data accurately.

---

## 💻 Tech Stack & Deployment
*   **Core:** Python 3.x, Flask (Web Backend).
*   **Persistence:** SQLite3 (Industrial-grade relational storage).
*   **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsive & RTL).
*   **Environment:** Virtualenv for dependency isolation.

### ⚙️ Quick Start
1.  **Clone:** `git clone https://github.com/Rezajediyatmonfared/factory-production-tracker.git`
2.  **Activate Environment:** `.venv\Scripts\activate`
3.  **Run:** `python run.py`
4.  **Explore:** Navigate to `http://127.0.0.1:5000`

---
*Developed by **Reza Jeddi***
*Industrial Intelligence Architect | Production Planning Expert | Python Developer*
