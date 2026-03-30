from flask import Flask, jsonify
import logging
from datetime import datetime

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

    @app.route("/", methods=["GET"])
    def root():
        """
        Root endpoint - health check
        """
        response = {
           "status": "success",
           "message": "Job Tracker API is running",
           "version": "1.0.0",
           "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        return jsonify(response), 200

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Route not found'}), 404
   
    @app.errorhandler(405)
    def method_not_allowd(e):
        return jsonify({'error': 'Method not allowd'}), 405
   
    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({'error': 'Internal server error'}), 500

    return app
