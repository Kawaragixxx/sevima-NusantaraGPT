def save_title_and_script(title, script):
  """Saves the title and script to a file."""
  with open("title_and_script.txt", "w") as f:
    f.write(title)
    f.write("n")
    f.write(script)