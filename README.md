# Screenplay Pattern with Cucumber (Behave) Example for Chocair

This project demonstrates web automation using the Screenplay pattern with Cucumber (Behave) in Python.

## Project Structure
```
├── features/
│   ├── login.feature         # Feature files
│   ├── environment.py        # Behave hooks
│   └── steps/
│       └── login_steps.py    # Step definitions
├── screenplay/
│   ├── actor.py             # Actor class
│   ├── tasks/               # Tasks
│   │   ├── navigate.py
│   │   ├── login.py
│   │   ├── click_recruitment.py
│   │   ├── select_position.py
│   │   └── upload_file.py
│   └── questions/           # Questions
│       └── dashboard.py
├── files/                   # Test files directory
│   └── resume.pdf          # PDF file for upload testing
└── requirements.txt         # Dependencies
```

## Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
```bash
behave
```
