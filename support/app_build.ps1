# change directory two levels up to project folder
$scriptpath = $MyInvocation.MyCommand.Path
$dir1 = Split-Path $scriptpath   # parent folder
$dir2 = Split-Path $dir1         # up second level
Set-Location $dir2


# Activate the virtual environment
$venvPath = ".\env"
& $venvPath\Scripts\activate

# update version info file
$versionScript = ".\support\create_version_file.py"
& $venvPath\Scripts\python.exe $versionScript

# Run the pyinstaller command
$launcherFile = ".\src\dpg_demo.py"
$pyInstallerExecutable = "pyinstaller"
$appName = "template_app"
$versionFile = ".\support\app_version_info.txt"
$iconFile = ".\src\data\app_icon.ico"
# $addIcon = ".\src\data\icon.ico;.\data" # use this to add specific file
$addDataFolder = ".\src\data;.\data" # use this to add entire folder

# build command with settings args
& $pyInstallerExecutable $launcherFile --add-data $addDataFolder --version-file $versionFile -w -n $appName -i $iconFile --noconfirm --onefile

# deactivate environment
& deactivate