import os
import sys

# get_resource_path & is_running_as_executable are required when builds are compiled to an executable
def get_resource_path(relative_path, file=__file__):
    """Get the absolute path to the resource, works for development and PyInstaller."""
    # Define the name of the project root directory
    project_root_name = "Application"

    if getattr(sys, 'frozen', False):
        print(sys._MEIPASS)
        # If the application is frozen, use the _MEIPASS folder
        base_path = sys._MEIPASS
    
    else:
        # If the application is not frozen, navigate up to the project root
        current_path = os.path.abspath(file)
        
        # Pop directories until we find the project root
        while current_path and project_root_name not in os.path.basename(current_path):
            current_path = os.path.dirname(current_path)
        
        # If we exited the loop and found the project root
        if project_root_name in os.path.basename(current_path):
            base_path = current_path  # Set base path to the project root
        else:
            raise FileNotFoundError(f"Could not find project root '{project_root_name}' in the path.")

    return os.path.join(base_path, relative_path)

def is_running_as_executable():
    """Check if the application is running as a bundled executable."""
    return getattr(sys, 'frozen', False)