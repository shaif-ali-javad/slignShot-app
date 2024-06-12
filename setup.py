import sys
from cx_Freeze import setup, Executable

# Define the executables
executables = [
    Executable(script='main.py', base=None)  # Replace 'your_app_script.py' with your script name
]

# Define additional options
options = {
    'build_exe': {
        'includes': ['socket', 'PyQt5'],  # Include necessary modules
        'packages': [],  # Include any packages here if necessary
        'include_files': [],  # Add any additional files or dependencies here
        'excludes': [],  # Exclude any modules or packages if necessary
        'optimize': 2,  # Optimization level (0 or 1 for debugging, 2 for release)
    },
    'bdist_msi': {
        'initial_target_dir': r'[ProgramFilesFolder]\YourApp',  # Installation directory
        'data': {
            'Shortcut': [
                ("DesktopShortcut",  # Shortcut name
                 "DesktopFolder",   # Directory (Desktop)
                 "YourApp",         # Shortcut description
                 "TARGETDIR",       # Directory of the executable
                 "[TARGETDIR]\YourApp.exe",  # Path to the executable
                 None,              # Arguments
                 None,              # Description
                 None,              # Hotkey
                 None,              # Icon
                 None,              # Icon index
                 None,              # Working directory
                 None,              # Component
                )
            ]
        }
    }
}

# Setup configuration
setup(
    name='YourApp',  # Replace 'YourApp' with your app name
    version='1.0',  # Set the version of your app
    description='Description of Your App',  # Add a description for your app
    options=options,
    executables=executables
)
