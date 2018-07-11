import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  PIPELINE_LOCATION = os.environ.get('PIPELINE_LOCATION', '')
  return 'hello from %s...5 test-branch-1' % PIPELINE_LOCATION
