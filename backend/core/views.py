from core import app

@app.route('/')
def show_entries():
  return "hello hello hello"