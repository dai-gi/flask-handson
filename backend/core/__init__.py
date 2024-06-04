from flask import Flask

app = Flask(__name__)
app.config.from_object('core.config')

import core.views