#Job Tracker API

A REst API to track job application, built with python and Flask. Deployed on AWS EC2.


## Tech Stack
- Python 3 +  Flask
- JSON file storage
- Deployed on AWS EC2 with Gunicorn + Nginx


##Step
```bash
git clone https://github.com/YOUR_USERNAME/job-tracker-api
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
Ramkumar Palanichamy — [github.com/YOUR_USERNAME](https://github.com)