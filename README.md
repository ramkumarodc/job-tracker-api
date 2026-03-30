# Job Tracker API

A RESTful API to track job applications — built with Python and Flask, deployed on AWS EC2.

Built as a portfolio project to demonstrate backend engineering skills:
clean code structure, REST design, error handling, logging, and cloud deployment.

---

## Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Language   | Python 3          |
| Framework  | Flask             |
| Storage    | JSON file         |
| Server     | Gunicorn          |
| Deployment | AWS EC2 (Ubuntu)  |

---

## Project Structure
```
job-tracker-api/
├── app/
│   ├── __init__.py      # App factory, root endpoint
│   ├── routes.py        # All CRUD endpoints + logging
│   └── storage.py       # JSON read/write helpers
├── data/
│   └── jobs.json        # Persistent storage
├── run.py               # Entry point
└── requirements.txt
```

---

## API Endpoints

| Method | Endpoint        | Description            |
|--------|-----------------|------------------------|
| GET    | /               | Health check           |
| POST   | /jobs           | Add a job application  |
| GET    | /jobs           | Get all jobs           |
| GET    | /jobs?status=   | Filter by status       |
| GET    | /jobs?company=  | Filter by company      |
| PUT    | /jobs/\<id\>    | Update a job           |
| DELETE | /jobs/\<id\>    | Delete a job           |

---

## Sample Requests & Responses

### Add a job
```bash
curl -X POST http://localhost:5000/jobs \
  -H "Content-Type: application/json" \
  -d '{"company": "Google", "role": "Backend Engineer", "status": "applied"}'
```

**Response:**
```json
{
  "message": "Job added",
  "job": {
    "id": "a1b2c3d4",
    "company": "Google",
    "role": "Backend Engineer",
    "status": "applied",
    "date_applied": "2026-03-29"
  }
}
```

### Get all jobs
```bash
curl http://localhost:5000/jobs
```

### Filter by status
```bash
curl "http://localhost:5000/jobs?status=applied"
```

### Update a job
```bash
curl -X PUT http://localhost:5000/jobs/a1b2c3d4 \
  -H "Content-Type: application/json" \
  -d '{"status": "interviewing"}'
```

### Delete a job
```bash
curl -X DELETE http://localhost:5000/jobs/a1b2c3d4
```

---

## Run Locally
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/job-tracker-api.git
cd job-tracker-api

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
```

API will be available at `http://localhost:5000`

---

## Job Status Flow
```
applied → interviewing → offer
                       → rejected
```

---

## Author

Ramkumar Palanichamy
[GitHub](https://github.com/ramkumarodc) 
