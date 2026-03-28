from flask import Blueprint, jsonify, request
from .storage import read_jobs, write_jobs, generate_id, today

jobs_bp = Blueprint('jobs', __name__, url_prefix='/jobs')


@jobs_bp.app_errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Route not found'}), 404



@jobs_bp.app_errorhandler(405)
def method_not_allowd(e):
    return jsonify({'error': 'Method not allowd'}), 405

@jobs_bp.app_errorhandler(500)
def internal_error(e):
    return jsonify({'error': 'Internal server error'}), 500

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

    return jsonify({'message': 'Job added', 'job': job}), 201


# ── GET /jobs ────────────────────────────────────────────
@jobs_bp.route('', methods=['GET'])
def get_jobs():
    jobs = read_jobs()
    return jsonify({'count': len(jobs), 'jobs': jobs}), 200

# ── PUT /jobs/<id> ────────────────────────────────────────────
@jobs_bp.route('/<job_id>', methods=['PUT'])
def update_job(job_id):
    data = request.get_json()
    jobs = read_jobs()

    job = next((j for j in jobs if j['id'] == job_id), None)
    if not job:
        return jsonify({'error': f'job {job_id} not found'}),  404

    # Only allow updating these fields
    allowed = ['status', 'role', 'company', 'date_applied']
    for field in allowed:
        if field in data:
            job[field] = data[field]

    write_jobs(jobs)
    return jsonify({'message': 'Job updated', 'job':job}), 200


#-- DELETE /jobs/<id> ---------------------------------------------
@jobs_bp.route('/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    jobs = read_jobs()
    original_count  = len(jobs)
    
    jobs = [j for j in jobs if j['id'] != job_id]

    if len(jobs) == original_count:
        return jsonify({'error': f'Job {job_id} not found'}), 404

    write_jobs(jobs)
    return jsonify({'message': f'Job {job_id} deleted'}), 200

