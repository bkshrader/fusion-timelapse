# Fusion Timelapse

Add-in for Fusion 360 for recording timelapse footage of your design process.

*This software is currently in development and incomplete. Check back for a first release candidate soon.*

# How to Install this Add-in
***This software is not currently in a working state. Check back when an official release is posted***
## Method One (Recommended)
1. Download the project from the [releases page](https://github.com/bkshrader/fusion-timelapse/releases)
1. Extract the add-in and copy the top-level folder into the Fusion 360 Add-ins folder
  - On Windows: %appdata%\Autodesk\Autodesk Fusion 360\API\AddIns
  - On MacOS: ~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns
1. Restart Fusion 360 if it is already open to make the add-in available to the application
1. Open the scripts and add-ins menu in Tools (or Shift+S by default) and make sure the add-in is listed and
check that it's running by looking for a spinner icon next to the add-in name in the list.
  - If the app isn't listed make sure it has been installed in the correct folder, that the folder containing the add-in is named FusionTimelapse and that it contains only the add-in files.
  - If the app is properly installed, you have already restarted your Fusion 360 application, and you have checked you are viewing the add-ins tab and not the scripts tab, attempt method two of installation.
1. (Optional) Select the add-in within the add-ins tab and select or unselect the Run on Startup box at the bottom of the add-ins panel if you'd like the add-in to open as soon as you open Fusion 360
  - **Setting the app to run on startup will *NOT* start the timelapse recording. You *MUST* click on the record button in the Nav Toolbar in the lower center of the screen to start the recording.**

## Method Two
1. Download the project from the [releases page](https://github.com/bkshrader/fusion-timelapse/releases)
1. Extract the add-in to a destination of your choice, though the default location is recommended
  - On Windows: %appdata%\Autodesk\Autodesk Fusion 360\API\AddIns
  - On MacOS: ~/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns
1. Open Fusion 360 and navigate to the scripts and add-ins menu in Tools (or Shift+S by default)
1. Under the add-ins tab click on the green plus sign next to My Add-Ins
1. Select the folder containing this add-in and confirm the selection
1. After the installer completes, if the add-in is not visible in the add-ins panel or if prompted by the application, restart your Fusion 360 application
1. (Optional) Select the add-in within the add-ins tab and select or unselect the Run on Startup box at the bottom of the add-ins panel if you'd like the add-in to open as soon as you open Fusion 360
  - **Setting the app to run on startup will *NOT* start the timelapse recording. You *MUST* click on the record button in the Nav Toolbar in the lower center of the screen to start the recording.**
  
# Using the Add-in
***TODO: The application is still in deveopment and instructions for operation are still not finalized. Check back when a release version is available.***

# What is it
Fusion Timelapse is a solution to the problem that timelapse footage of design processes is often intensely jarring to watch. Since the timelapse is typically recorded by capturing the designer's screen in real-time, the camera is almost never in the same location throughout the whole recording. When sped up, this causes the camera to appear to shake and move wildly and can cause motion sickness for many viewers. Fusion Timelapse aims to make timelapse footage of long design processes much more enjoyable to watch by operating from a stationery or nearly stationery (and configurable) camera location.
