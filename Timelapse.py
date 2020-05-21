#Author-Bradley Shrader
#Description-Easily record timelapse footage as you work from a fixed camera angle

import adsk.core, adsk.fusion, adsk.cam, traceback


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        cmdDefs = ui.commandDefinitions

        quickAccessToolbar = ui.toolbars.itemById('QAT')
        
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        # Clean up the UI

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))