from flask import Flask, jsonify


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
