# Factory Production Tracker

A lightweight, web-based production management tool designed to track daily factory performance, including production metrics, line stoppages, inventory status, and parts shortages.

![Demo](production_system.gif)

## Project Evolution
### Phase 1: The Notebook Approach
This project began as a **Jupyter Notebook** to quickly prototype logic for production tracking. While it successfully handled calculations, it lacked a structured database and a user-friendly interface for operators. 
*You can find this initial research phase in the `/notebooks` directory.*

### Phase 2: Building the Flask Web App
To make the tool production-ready and scalable, the logic was migrated to a full **Flask** web application. This version features:
- **Responsive UI**: A modern interface styled with Bootstrap for ease of use in factory environments.
- **Structured Data**: Transitioned to an SQLite database for persistent and organized record-keeping.
- **Localized Features**: Integrated Jalali (Persian) date support to match factory reporting standards.

## Key Features
- **Production & Delivery Tracking**: Log real-time production counts vs. daily plans.
- **Line Stoppage Monitoring**: Track machine downtime, reasons, and responsible units.
- **Chassis Inventory**: Manage stock levels for factory and customs chassis.
- **Parts Shortage Management**: Keep track of missing items for supply chain efficiency.

## Tech Stack
- **Backend**: Python, Flask, SQLite
- **Frontend**: Bootstrap 5, HTML5/CSS3
- **Tools**: VS Code, Git

## How to Run
1. Clone this repository:
```bash
   git clone https://github.com/Rezajediyatmonfared/factory-production-tracker.git
   cd factory-production-tracker
   
