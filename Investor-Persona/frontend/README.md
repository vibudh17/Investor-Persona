# Stock Investor Frontend

## Overview

The Investor AI Frontend is a React-based user interface that allows investors to interact with the AI recommendation system.

Users can:

* Select investor profile
* Submit financial news
* View AI-generated recommendations
* Read simplified explanations


The frontend communicates with the **FastAPI backend** via REST APIs.

---

# Tech Stack

| Technology | Purpose            |
| ---------- | ------------------ |
| React      | Frontend framework |
| fetchAPI      | API communication  |

---

# Application Flow

```
User
  │
  ▼
React Dashboard
  │
  ▼
Submit News
  │
  ▼
Backend API
  │
  ▼
AI Agents + LLM
  │
  ▼
Recommendation + Explanation
  │
  ▼
Display Result
```

---

# Project Structure

```
frontend
│
├── src
│   ├── components
│   │   ├── InvestorSelector.js
│   │   ├── NewsInput.js
│   │   └── ResultCard.js
│   │
│   ├── App.js
│   ├── api.js
│   └── index.js
│
├── public
└── README.md
```

---

# Installation

Navigate to the frontend folder:

```
cd investor-ai-app/frontend
```

Install dependencies:

```
npm install
```

---

# Running the Frontend

Start the React development server:

```
npm start
```

Application will run at:

```
http://localhost:3000
```

# Example UI Workflow

1. User selects investor profile
2. User enters financial news
3. Click **Analyze**
4. AI processes request
5. UI displays:

* Investor persona
* Investment recommendation
* AI explanation

---

