from Settings import *
from scene_pics import *
import re
import glob
import os
import pyautogui as gui
import scene_funcs as scene
import time
from time import sleep


kill_job = False
while not kill_job:
    scene.start()
    scene.close_pop_ups()
    if scene.close_scene() == True:
        kill_job = True
