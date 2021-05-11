from Settings import *
from scene_pics import *
import re
import glob
import os
import pyautogui as gui
import time
from time import sleep


screen_center = (gui.size()[0] / 2, (gui.size()[1] / 2) - 50)

def start():
    os.startfile(scene_path)
    time.sleep(3)

def close_pop_ups():
    gui.press('tab' presses = 2)
    gui.press('space')
    #check_for_image(close_png)
    #gui.click()

def new_project(job):
    check_for_image(create_png)
    gui.click()
    time.sleep(1)
    gui.press('tab', presses=2)
    time.sleep(1)
    gui.write(job[0] + '_' + job[2])
    time.sleep(1)
    gui.press('tab', presses=3)
    time.sleep(1)
    gui.press('enter')
    time.sleep(3)

def load_scans(job):
    check_for_image(import_png)
    gui.click()
    check_for_image(importscans_png)
    gui.click()
    check_for_image(folder_explorer_png)
    gui.mouseDown()
    gui.moveTo(screen_center)
    gui.mouseUp()
    check_for_image(file_explore_path_png)
    gui.click()
    gui.write(new_job_folder + '\\' + job[0] + scan_folder + r'\filtered')
    gui.press('enter')
    check_for_image(folders_png)
    gui.click()
    gui.hotkey('ctrl', 'a')
        #drag selected folders to side panel
    check_for_image(selected_png)
    gui.mouseDown()
    check_for_image(side_panel_png)
    gui.mouseUp()
    check_for_image(cancel_png)
    gui.click()
    check_for_image(ok_png)
    gui.click()

def process_scans():
    check_for_image(process_png)
    gui.click()
    check_for_image(process_scan_png)
    gui.click()
    check_for_image(big_scan_png)
    gui.click()
    check_for_image(configure_png)
    gui.click()
    time.sleep(2)
    gui.click()

def check_processing(job):
    handle_errors(job)

def create_point_cloud():
    check_for_image(explore_png)
    gui.click()
    time.sleep(5)
    check_for_image(pointCloud_png)
    gui.click()
    time.sleep(1)
    gui.move(0, 55)
    gui.click()
    time.sleep(1)
    gui.press('enter')
    time.sleep(1)
    #check_for_image(successfulSave_png)
    gui.press('enter')
    #time.sleep(1)
    #gui.press('enter')
    check_for_image(cloudDone_png)
    gui.press('enter')

def export_xyz_e57(job):
    check_for_image(exportTab_png)
    gui.click()
    time.sleep(2)
    check_for_image(exportPointCloud_png)
    gui.click()
    check_for_image(exportDropBox_png)
    gui.click()
    time.sleep(1)
    gui.press('e')
    gui.press('enter')
    gui.press('tab')
    gui.write(new_job_folder + '\\' + job[0] + processed_folder + scene_folder + '\\' + job[0] + '_' + job[2] +'.e57')
    gui.press('enter')
    check_for_image(exportPointCloud_png)
    gui.click()
    check_for_image(exportDropBox_png)
    gui.click()
    time.sleep(1)
    gui.press('x')
    gui.press('enter')
    gui.press('tab')
    gui.write(new_job_folder + '\\' + job[0] + processed_folder + scene_folder + '\\' + job[0] + '_' + job[2] +'.xyz')
    gui.press('enter')
    check_for_image(exportFlag_png)
    wait_for_load(exportFlag_png)

def export_project(job):
    check_for_image(exportProj_png)
    gui.click()
    time.sleep(1)
    #save before export
    gui.press('enter')
    time.sleep(1)
    gui.press('enter')
    time.sleep(2)
    gui.press('tab', presses=3)
    time.sleep(1)
    gui.write(new_job_folder + '\\' + job[0] + processed_folder + scene_folder)
    time.sleep(1)
    gui.press('enter')
    check_for_image(exportSuccess_png)
    gui.press('enter')

def close_scene():
    check_for_image(closeScene_png)
    gui.move(30, -20)
    gui.click()
    return True

##### USED IN OTHER FUNCS########

def check_for_image(image):
    checking = True
    while checking:
        image_location = gui.locateCenterOnScreen(image)
        gui.moveTo(image_location)
        if gui.position() == image_location:
            checking = False

def wait_for_load(image):
    waiting = True
    while waiting:
        image_location = gui.locateCenterOnScreen(image)
        if gui.position() != image_location:
            waiting = False

def delete_imports():
    check_for_image(import_png)
    gui.click()
    check_for_image(scansMini_png)
    gui.click()
    gui.press('delete')
    time.sleep(1)
    gui.press('enter')

def reprocess(job):
    delete_imports()
    check_for_image(process_png)
    gui.click()
    check_for_image(import_png)
    gui.click()
    check_for_image(importscans_png)
    gui.click()
    check_for_image(folder_explorer_png)
    gui.mouseDown()
    gui.moveTo(screen_center)
    gui.mouseUp()
    check_for_image(file_explore_path_png)
    gui.click()
    gui.write(new_job_folder + '\\' + job[0] + scan_folder + r'\filtered')
    gui.press('enter')
    check_for_image(folders_png)
    gui.click()
    gui.hotkey('ctrl', 'a')
        #drag selected folders to side panel
    check_for_image(selected_png)
    gui.mouseDown()
    check_for_image(side_panel2_png)
    gui.mouseUp()
    check_for_image(cancel_png)
    gui.click()
    check_for_image(ok_png)
    gui.click()
    check_for_image(process_png)
    gui.click()
    check_for_image(process_scan_png)
    gui.click()
    check_for_image(big_scan_png)
    gui.click()
    check_for_image(configure_png)
    gui.click()
    check_for_image(scrollBar_png)
    gui.mouseDown()
    gui.move(0,300)
    gui.mouseUp()
    check_for_image(regMethod_png)
    gui.click()
    time.sleep(1)
    check_for_image(targetBased_png)
    gui.click()
    check_for_image(startProcessing_png)
    gui.click()

def handle_errors(job):
    error_check = False
    checking = True
    while checking:
        time_loop = time.time() + 30
        while time.time() < time_loop:
            success = gui.locateCenterOnScreen(process_success_png)
            if success != None:
                gui.moveTo(success)
            if gui.position() == success:
                error_check = False
                checking = False
        next_loop = time.time() + 30
        while time.time() < next_loop:
            failure = gui.locateCenterOnScreen(errorAutoReg_png)
            if failure != None:
                gui.moveTo(failure)
            if gui.position() == failure:
                error_check = True
                checking = False
    check_for_image(ok_png)
    gui.click()
    if error_check == True:
        reprocess(job)
        error_check2 = False
        checking2 = True
        while checking2:
            time_loop = time.time() + 30
            while time.time() < time_loop:
                success = gui.locateCenterOnScreen(process_success_png)
                if success != None:
                    gui.moveTo(success)
                if gui.position() == success:
                    error_check2 = False
                    checking2 = False
            next_loop = time.time() + 30
            while time.time() < next_loop:
                failure = gui.locateCenterOnScreen(errorAutoReg_png)
                if failure != None:
                    gui.moveTo(failure)
                if gui.position() == failure:
                    error_check2 = True
                    checking2 = False
        if error_check2 == True:
            return True
