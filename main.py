import os
import sys

# Add the src directory to Python's module search path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from terabox_gateway.api import app  # noqa: E402


def main():
    """Run the Flask application on Railway or locally."""
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"

    app.run(
        host=host,
        port=port,
        debug=debug,
        use_reloader=False,
    )


if __name__ == "__main__":
    main()
