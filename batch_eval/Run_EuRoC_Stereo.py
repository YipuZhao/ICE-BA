# This script is to run all the experiments in one program

import os
import subprocess
import time
import signal


# SeqNameList = ['MH_01_easy', 'MH_03_medium', 'MH_05_difficult', 'V2_02_medium'];
SeqNameList = ['MH_01_easy', 'V2_02_medium', 'MH_05_difficult'];
# SeqNameList = ['MH_01_easy', 'MH_02_easy', 'MH_03_medium', 'MH_04_difficult', 'MH_05_difficult', 'V1_01_easy', 'V1_02_medium', 'V1_03_difficult', 'V2_01_easy', 'V2_02_medium', 'V2_03_difficult'];

# Result_root = '/mnt/DATA/tmp/EuRoC/iceBA_Stereo_Speedx1/'
# Result_root = '/mnt/DATA/tmp/EuRoC/iceBA_Stereo_Speedx2/'
# Result_root = '/mnt/DATA/tmp/EuRoC/iceBA_Stereo_Speedx4/'
#
Result_root = '/mnt/DATA/tmp/EuRoC/iceBA_Stereo_Extra_Speedx1/'
# Result_root = '/mnt/DATA/tmp/EuRoC/iceBA_Stereo_Extra_Speedx2/'
# Result_root = '/mnt/DATA/tmp/EuRoC/iceBA_Stereo_Extra_Speedx4/'

# Number_GF_List = [70, 150, 200, 400, 600, 800]; 
Number_GF_List = [70, 150, 200, 400]; 

rate = 1.0 # 2.0 # 4.0 # 

Num_Repeating = 10 # 1 # 

SleepTime = 2 # 10 # 25

#----------------------------------------------------------------------------------------------------------------------
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ALERT = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

File_Config = '../config/config_of_stereo_v2.txt'

for ri, num_gf in enumerate(Number_GF_List):
    
    Experiment_prefix = 'ObsNumber_' + str(int(num_gf))

    for iteration in range(0, Num_Repeating):

        Experiment_dir = Result_root + Experiment_prefix + '_Round' + str(iteration + 1)
        cmd_mkdir = 'mkdir -p ' + Experiment_dir
        subprocess.call(cmd_mkdir, shell=True)

        for sn, sname in enumerate(SeqNameList):
            
            print bcolors.ALERT + "====================================================================" + bcolors.ENDC

            SeqName = SeqNameList[sn]
            print bcolors.ALERT + "Round: " + str(iteration + 1) + "; Seq: " + SeqName

            Path_Image   = '/mnt/DATA/Datasets/EuRoC_dataset/' + SeqName + '/'
            File_traj = Experiment_dir + '/' + SeqName

            # cmd="../bin/ice_ba --imgs_folder $EuRoC_PATH/$Sequence 
            # --start_idx 0 --end_idx -1 --iba_param_path ../config/config_of_stereo_v2.txt 
            # --stereo"
            cmd_slam   = str('../bin/ice_ba --stereo --imgs_folder ' + Path_Image + ' ' \
                + '--start_idx 0 --end_idx -1 --iba_param_path ' + File_Config + ' --budget_per_frame ' + str(int(50/rate + 0.5)) + ' ' \
                + '--max_num_per_grid '  + str(int(num_gf/24.0 + 0.5)) + ' --grid_row_num 4 --grid_col_num 6' )
            cmd_timelog = str('cp /mnt/DATA/iceBA_tmpLog.txt ' + Experiment_dir + '/' + SeqName + '_Log.txt')
            cmd_GBA_log = str('cp /mnt/DATA/iceBA_tmpGBA.txt ' + Experiment_dir + '/' + SeqName + '_KeyFrameTrajectory.txt')
            cmd_LBA_log = str('cp /mnt/DATA/iceBA_tmpLBA.txt ' + Experiment_dir + '/' + SeqName + '_AllFrameTrajectory.txt')

            print bcolors.WARNING + "cmd_slam: \n"   + cmd_slam   + bcolors.ENDC
            print bcolors.WARNING + "cmd_timelog: \n" + cmd_timelog + bcolors.ENDC
            print bcolors.WARNING + "cmd_GBA_log: \n" + cmd_GBA_log + bcolors.ENDC
            print bcolors.WARNING + "cmd_LBA_log: \n" + cmd_LBA_log + bcolors.ENDC

            print bcolors.OKGREEN + "Launching SLAM" + bcolors.ENDC
            # proc_slam = subprocess.Popen(cmd_slam, shell=True)
            proc_slam = subprocess.call(cmd_slam, shell=True)

            # print bcolors.OKGREEN + "Sleeping for a few secs to wait for voc loading" + bcolors.ENDC
            # time.sleep(SleepTime)

            print bcolors.OKGREEN + "Sleeping for a few secs to wait for ice_ba quit" + bcolors.ENDC
            time.sleep(SleepTime)
            # print bcolors.OKGREEN + "Copy the lmk log to result folder" + bcolors.ENDC
            # subprocess.call(cmd_lmklog, shell=True)
            print bcolors.OKGREEN + "Copy the time log to result folder" + bcolors.ENDC
            subprocess.call(cmd_timelog, shell=True)
            print bcolors.OKGREEN + "Copy the track to result folder" + bcolors.ENDC
            subprocess.call(cmd_LBA_log, shell=True)
            subprocess.call(cmd_GBA_log, shell=True)
            # print bcolors.OKGREEN + "Finished playback, kill the process" + bcolors.ENDC
            # subprocess.call('pkill Mono', shell=True)

