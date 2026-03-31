import json
import os
import uuid
from datetime import date

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'jobs.json')

def read_jobs():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def write_jobs(jobs):
    with open(DATA_FILE, 'w') as f:
        json.dump(jobs, f, indent=2)


def generate_id():
    return str(uuid.uuid4())[:8]

def today():
    return str(date.today())

