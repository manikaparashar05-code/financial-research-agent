# System Architecture

User Query
│
▼
Planner Agent
│
▼
ReAct Reasoning Loop
│
┌────┼────┬──────┬──────┐
▼    ▼    ▼      ▼
Financial News SEC Earnings
Tool    Tool Tool   Tool
└────┬────┴──────┬──────┘
▼
Conflict Resolution
▼
Memory (ChromaDB)
▼
Report Generator
▼
Research Report
