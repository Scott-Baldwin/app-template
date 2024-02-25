# dont use this for a while until stable versions are established


# # change directory two levels up
# $scriptpath = $MyInvocation.MyCommand.Path
# $dir1 = Split-Path $scriptpath   # parent folder
# $dir2 = Split-Path $dir1         # up second level
# Set-Location $dir2

# # Create the Python virtual environment
# $pythonExecutable = "py"
# $venvPath = ".\env"
# & $pythonExecutable -m venv $venvPath

# # Activate the virtual environment
# & $venvPath\Scripts\activate

# # update pip
# & $venvPath\Scripts\python.exe -m pip install --upgrade pip

# # reset environment
# & pip freeze > freeze.txt
# pip uninstall -r freeze.txt -y
# Remove-Item freeze.txt

# # install & update dependencies with pip
# # & pip install --upgrade pysimplegui
# & pip install --upgrade pyinstaller
# & pip install --upgrade pyinstaller_versionfile
# & pip install --upgrade dearpygui

# # update requirements file
# & pip freeze > requirements.txt

# # deactivate environment
# & deactivate