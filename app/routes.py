from flask import Blueprint, jsonify, request
from .storage import read_jobs, write_jobs, generate_id, today
import logging

logger = logging.getLogger(__name__)

jobs_bp = Blueprint('jobs', __name__, url_prefix='/jobs')

# ─── POST /jobs ───────────────────────────────────────────
@jobs_bp.route('', methods=['POST'])
def add_job():
    data = request.get_json()

    # Validate required fields
    required = ['company', 'role', 'status']
    for field in required:
        if not data or field not in data:
            return jsonify({'error': f'Missing field: {field}'}), 400

    job = {
        'id': generate_id(),
        'company': data['company'],
        'role': data['role'],
        'status': data['status'],
        'date_applied': data.get('date_applied', today()),
    }

    jobs = read_jobs()
    jobs.append(job)
    write_jobs(jobs)
    logger.info(f"Job created | id={job['id']} company={job['company']} role={job['role']}")

    return jsonify({'message': 'Job added', 'job': job}), 201


# ─── GET /jobs ────────────────────────────────────────────
@jobs_bp.route('', methods=['GET'])
def get_jobs():
    jobs = read_jobs()

    # Filters
    status = request.args.get('status')
    company = request.args.get('company')

    if status:
        jobs = [
            j for j in jobs
            if j.get('status', '').lower() == status.lower()
        ]

    if company:
        jobs = [
            j for j in jobs
            if company.lower() in j.get('company', '').lower()
        ]

    # Pagination
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)

    total = len(jobs)

    if page and page < 1:
       page = 1
    if limit and limit < 1:
       limit = 5

    if page and limit:
        start = (page - 1) * limit
        end = start + limit
        jobs = jobs[start:end]

    return jsonify({
        'status': 'success',
        'total': total,
        'count': len(jobs),
        'page': page,
        'limit': limit,
        'jobs': jobs
    }), 200

# ── GET /jobs/<id> ────────────────────────────────────────────
@jobs_bp.route('/<job_id>', methods=['GET'])
def get_job(job_id):
    jobs = read_jobs()

    job = next((j for j in jobs if j.get('id') == job_id), None)

    if not job:
        return jsonify({
            'status': 'error',
            'message': f'Job {job_id} not found'
        }), 404

    return jsonify({
        'status': 'success',
        'job': job
    }), 200

# ── PUT /jobs/<id> ────────────────────────────────────────────
@jobs_bp.route('/<job_id>', methods=['PUT'])
def update_job(job_id):
    data = request.get_json()

    if not data:
        return jsonify({
            'status': 'error',
            'message': 'Request body must be JSON'
        }), 400

    jobs = read_jobs()

    job = next((j for j in jobs if j.get('id') == job_id), None)
    if not job:
        return jsonify({
            'status': 'error',
            'message': f'Job {job_id} not found'
        }), 404

    allowed = ['status', 'role', 'company', 'date_applied']

    updated_fields = {}
    for field in allowed:
        if field in data:
            job[field] = data[field]
            updated_fields[field] = data[field]

    write_jobs(jobs)

    logger.info(f"Job updated | id={job_id} changes={updated_fields}")

    return jsonify({
        'status': 'success',
        'message': 'Job updated',
        'job': job
    }), 200

#-- DELETE /jobs/<id> ---------------------------------------------
@jobs_bp.route('/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    jobs = read_jobs()
    original_count = len(jobs)

    jobs = [j for j in jobs if j.get('id') != job_id]

    if len(jobs) == original_count:
        return jsonify({
            'status': 'error',
            'message': f'Job {job_id} not found'
        }), 404

    write_jobs(jobs)

    logger.info(f"Job deleted | id={job_id}")

    return jsonify({
        'status': 'success',
        'message': f'Job {job_id} deleted'
    }), 200

