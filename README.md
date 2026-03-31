# Job Tracker API

A RESTful API to track and manage job applications — built with Python and Flask, deployed on AWS EC2.

This project demonstrates backend engineering fundamentals:
REST API design, request validation, error handling, filtering, pagination, structured logging, and cloud deployment.

> **Note:** Uses JSON file storage (no database) to keep setup simple and focus on API design and backend fundamentals.

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
│   ├── __init__.py      # App factory, root endpoint, error handlers
│   ├── routes.py        # CRUD endpoints, filtering, pagination, logging
│   └── storage.py       # JSON read/write helpers
├── data/
│   └── jobs.json        # Persistent storage
├── run.py               # Entry point
└── requirements.txt
```

---

## API Endpoints

| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| GET    | /                    | Health check             |
| POST   | /jobs                | Create a new job         |
| GET    | /jobs                | Get all jobs             |
| GET    | /jobs/\<id\>         | Get a job by ID          |
| GET    | /jobs?status=        | Filter by status         |
| GET    | /jobs?company=       | Filter by company        |
| GET    | /jobs?page=&limit=   | Paginate results         |
| PUT    | /jobs/\<id\>         | Update a job             |
| DELETE | /jobs/\<id\>         | Delete a job             |

---

## Sample Requests & Responses

### Health check
```bash
curl http://localhost:5000/
```

**Response:**
```json
{
  "status": "success",
  "message": "Job Tracker API is running",
  "version": "1.0.0",
  "timestamp": "2026-03-30T10:00:00Z"
}
```

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
    "date_applied": "2026-03-30"
  }
}
```

### Get all jobs
```bash
curl http://localhost:5000/jobs
```

### Get job by ID
```bash
curl http://localhost:5000/jobs/a1b2c3d4
```

### Filter by status or company
```bash
curl "http://localhost:5000/jobs?status=applied"
curl "http://localhost:5000/jobs?company=google"
```

### Paginate results
```bash
curl "http://localhost:5000/jobs?page=1&limit=5"
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

## Job Status Flow

```
applied → interviewing → offer
                       → rejected
```

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/ramkumarodc/job-tracker-api.git
cd job-tracker-api

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
```

API will be available at `http://localhost:5000`

---

## Deployment

Deployed on AWS EC2 (Ubuntu 24.04 LTS, t3.micro) using Gunicorn as the production WSGI server.

```bash
gunicorn --bind 0.0.0.0:5000 "run:app"
```

> The instance may not be running continuously to stay within AWS free tier limits.
> Contact me to schedule a live demo.

---

## Author

**Ramkumar Palanichamy**
[GitHub](https://github.com/ramkumarodc) | [LinkedIn](https://linkedin.com/in/ramkumar-palanichamy-21000622)
