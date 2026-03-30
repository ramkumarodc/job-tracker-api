# Job Tracker API

A RESTful API built with Flask to track and manage job applications.

##i Purpose
This project helps users manage their job search by allowing them to:
- Add job applications
- Update application status (applied, interview, offer, rejected)
- Track companies and roles in one place
Note: This project uses JSON file storage to keep the setup simple and focus on API design and deployment fundamentals.


## Tech Stack
- Python 3 
- Flask
- JSON file storage (no database)
- AWS EC2 (deployment)
- Gunicorn 


##Step
```bash
git clone https://github.com/ramkumarodc/job-tracker-api.git
cd job-tracker-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

## API Endpoints

| Method | Endpoint |Description |
|--------|----------|------------|
| POST | `/jobs` | Add a new job application |
| GET | `/jobs` | Get all job applications |
| PUT | `/jobs/<id>` | Update a job's status |
| DELETE | `/jobs/<id>` | Delete a job |

## Example Requests

**Add a job:**
```bash
curl -X post http://localhost:5000/jobs \
  -H "Content-Type: application/json" \
  -d '{"company": "Google", "role": "SWE", "status": "applied"}'
```

**Update status:**
```bash
curl -X PUT http://localhost:5000/jobs/ \
  -H "Content-Type: application/json" \
  -d '{"status": "interviewing"}'
```

## Job Status Flow
`applied` → `interviewing` → `offer` / `rejected`

## Author
Ramkumar Palanichamy — [https://github.com/ramkumarodc/job-tracker-api.git]
