Protocol for using venvs:
1. Create a repo and add code like normal
2. Once packages are installed, use "pip freeze > requirements.txt" to create and update a requirements.txt file
   that contains all of the information about the packages you're using.
3. Once all of your code is in the repo (INCLUDING requirements.txt) you can clone the repo.
4. After it is cloned, you can enter the terminal through PyCharm (you can do it through the regular terminal,
   but Pycharm removes a few steps) and use "pip install -r requirements.txt" to auto install all of the packages
   that the venv needs.
5. Congratulations! You now have a cloned venv!

A few extra tid bits:
  Update your requirements.txt with every new package installed to avoid issues down the line.
    (Remember the command is "pip freeze > requirements.txt")
  The original venv may have a "bin" or "lib" folder with packages/other code that isn't for you to access, so
    don't be alarmed if you can't add them to the git repo.
