from Settings import *
from deltav_functions import *

scene_list = []
pix4d_list = []
job_list = []
job = [['J8632', DEN, 'tractor']]
########GET LIST OF JOBS TO PROCESS############
job_list, scene_list, pix4d_list = find_jobs()
#print(scene_list)
############ COPY FILES FROM SERVER ############
create_local_files(job_list)

################# RUN JOBS #####################

for job in scene_list:
    run_scene(job)

#run_scene(job[0])
