from flask import Flask, jsonify
import logging

# ── Logging setup ────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s  %(levelname)s  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)

    from .routes import jobs_bp
    app.register_blueprint(jobs_bp)

    @app.route('/')
    def root():
        return jsonify({
            'status':  'ok',
            'message': 'Job Tracker API is running',
            'version': '1.0.0',
            'endpoints': {
                'add_job':    'POST   /jobs',
                'get_jobs':   'GET    /jobs',
                'update_job': 'PUT    /jobs/<id>',
                'delete_job': 'DELETE /jobs/<id>',
            }
        }), 200

    return app
