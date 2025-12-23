"""
This script runs the FlaskWebProject application using a development server.
"""

from dotenv import load_dotenv
load_dotenv()  # MUST be before importing the app

from os import environ
from FlaskWebProject import app

if __name__ == "__main__":
    HOST = environ.get("SERVER_HOST", "localhost")

    try:
        PORT = int(environ.get("SERVER_PORT", "5555"))
    except ValueError:
        PORT = 5555

    app.run(
        host=HOST,
        port=PORT,
        debug=True,
        ssl_context="adhoc"
    )
