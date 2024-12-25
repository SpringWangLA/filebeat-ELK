from flask import Flask
import logging
import os

# Initialize the Flask app
app = Flask(__name__)

# Configure logging
log_folder = 'logs'
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, 'app.log')

logger = logging.getLogger('FlaskApp')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

@app.route('/')
def index():
  logger.info('Index page accessed')
  return 'Hello, this is Flask!'

@app.route('/log/<message>')
def log_message(message):
  logger.info(f"Log message: {message}")
  return f"Logged message: {message}"

if __name__ == '__main__':
  app.run(debug=True)