# Set the path
from application import create_app
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = create_app()

if __name__ == "__main__":
  debug_mode = os.getenv('WORK_ENV') == 'development'
  app.run(debug=debug_mode)
