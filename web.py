import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  PIPELINE_LOCATION = os.environ.get('PIPELINE_LOCATION', '')
  TESTVAR = os.environ.get('TESTVAR', '')
  return 'hello from %s...10 .... TESTVAR=%s' % (PIPELINE_LOCATION, TESTVAR)
