from flask import Flask

from gaokao_profile_flask import blueprint as gaokao_profile

if __name__ == "__main__":
    app = Flask(__name__)
    app.register_blueprint(gaokao_profile)
    app.run("0.0.0.0", 8000)