from Settings import *
from scene_pics import *
import scene_funcs as scene
import pyautogui as gui
import os
from datetime import date as dt
import time
from time import sleep


######### COPY JOB DATA FROM SERVER TO LOCAL FOLDER ###############
def create_local_files(job_list):
    for job in job_list:
        #Create Local Folder
        shutil.copytree(new_job_template, new_job_folder + '\\' + job[0])
        #Copy Drone Data
        shutil.copytree(job[1] + '\\' + job[0] + drone_folder, new_job_folder + '\\' + job[0] + drone_folder)
        #Copy Scan Data
        shutil.copytree(job[1] + '\\' + job[0] + scan_folder, new_job_folder + '\\' + job[0] + scan_folder)
        i = 0
        for file in glob.glob(job[1] + '/*/Scans/*'):
            ind = str(i)
            os.rename(file, file.lower())
            if job[2] in file:
                shutil.copytree(file, new_job_folder + '\\' + job[0] + scan_folder + r'\filtered\\' + ind + job[2])
                i += 1

def find_jobs():
    today = dt.today()
    date = today.strftime("%m-%d-%y")
    text_file = open(text_path + '\\' + date + '.txt', 'r')
    list = text_file.read().split()

    list_o_jobs = []
    scene_jobs = []
    pix4d_jobs = []
    i = 0
    for job in list:
        job2 = job.split(',')
        list_o_jobs.append(job2)
        i += 1


    for job in list_o_jobs:
        if job[1] == 'CLT':
            job[1] = CLT
        elif job[1] == 'DEN':
            job[1] = DEN
        elif job[1] == 'ATL':
            job[1] = ATL
        elif job[1] == 'NAS':
            job[1] = NAS
    for job in list_o_jobs:
        if job[3] == 'Scene':
            scene_jobs.append(job)
        if job[3] == 'Pix4D':
            pix4d_jobs.append(job)
        if job[3] == 'Both':
            scene_jobs.append(job)
            pix4d_jobs.append(job)

    return list_o_jobs, scene_jobs, pix4d_jobs


def run_scene(job):
    kill_job = False
    while not kill_job:
        #open FARO
        scene.start()
        #Close license warning and pop up
        scene.close_pop_ups()
        #Open New Project
        scene.new_project(job)
        #Load in scans
        scene.load_scans(job)
        #Processing The Scans
        scene.process_scans()
        if scene.check_processing(job) == True:
            scene.close_scene()
            kill_job = True
        #Export after Successful Processing
        scene.create_point_cloud()
        scene.export_xyz_e57(job)
        scene.export_project(job)
        if scene.close_scene() == True:
            kill_job = True
