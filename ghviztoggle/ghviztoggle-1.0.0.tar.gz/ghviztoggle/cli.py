import typer
from ghviztoggle import utils

# set typer app
app = typer.Typer()

# define command start
@app.command()
def run():
  """Begin changing repo visibility"""
  utils.run()

@app.command()
def set():
  """Set owner and token"""
  utils.set_config()
