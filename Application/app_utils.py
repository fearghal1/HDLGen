import os
import sys

####################################################
# This file contains functions required to support #
# compilation into a single executable (.exe) file #
####################################################

# get_resouce_path(relative_path)
#   - This API is used to find the path of application (non-py) resources
#   - For example, the processDiagram.png shown on the splash page 
#   - Normally located at os.getcwd() + /Resources/processDiagram.png
#   - When running as an executable, Windows unpacks all project resources into a temporary location
#   - This location is accessed using sys._MEIPASS.
#   - Example MEIPASS directory for processDiagram.png
#      - C:\Users\lcann\AppData\Local\Temp\_MEI154562\Resources/processdiagram.png
#   - If you use os.getcwd() + "/Resources/processDiagram.png" as normal, os.getcwd() will return
#     the location of the **executable file**, eg: C:\Users\lcann\Downloads\HDLGen-ChatGPT.exe
# Please Note: This flow of using _MEIPASS is specific to PyInstaller, it may not work for other compiler packages.

# get_resource_path & is_running_as_executable are required when builds are compiled to an executable
def get_resource_path(relative_path):
    """Get the absolute path to the resource, works for development and PyInstaller."""
    # Define the name of the project root directory
    if getattr(sys, 'frozen', False):
        print(f"MEIPass: {sys._MEIPASS} Relative Path: {relative_path}")
        # If the application is frozen, use the _MEIPASS folder
        base_path = sys._MEIPASS
        
        print(f"Get Resource Path returns: {os.path.join(base_path, relative_path)}")
        return os.path.join(base_path, relative_path)
    return None

# is_running_as_executble()
#   - This API is used to check if the application is running as an executable
#   - This is required to know whether or not the get_resource_path API should be used instead 
#     of the standard os.getcwd() (or whatever other) method for getting filepaths.
def is_running_as_executable():
    """Check if the application is running as a bundled executable."""
    # if getattr(sys, 'frozen', False):
    #     print("We are running as executable")
    # else:
    #     print("We are not running as executable")
    return getattr(sys, 'frozen', False)