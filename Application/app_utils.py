import os
import sys

# get_resource_path & is_running_as_executable are required when builds are compiled to an executable
def get_resource_path(relative_path, file=__file__):
    """Get the absolute path to the resource, works for development and PyInstaller."""
    # Define the name of the project root directory
    if getattr(sys, 'frozen', False):
        print(f"MEIPass: {sys._MEIPASS} Relative Path: {relative_path}")
        # If the application is frozen, use the _MEIPASS folder
        base_path = sys._MEIPASS
        
        print(f"Get Resource Path returns: {os.path.join(base_path, relative_path)}")
        return os.path.join(base_path, relative_path)
    return None

def is_running_as_executable():
    """Check if the application is running as a bundled executable."""
    # if getattr(sys, 'frozen', False):
    #     print("We are running as executable")
    # else:
    #     print("We are not running as executable")
    return getattr(sys, 'frozen', False)