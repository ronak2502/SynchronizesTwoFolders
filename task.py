import os
import shutil
import time


# if folder is not exits then create a new folder
if not os.path.exists('source_folder'):
        source_folder =   os.makedirs('source_folder')

if not os.path.exists('replica_folder'):
        replica_folder = os.makedirs('replica_folder')

current_directory = os.getcwd()
source_folder = current_directory + "/source_folder/"     #Path/Location of the source directory
replica_folder = current_directory + "/replica_folder/"   #Path/Location of the replica folder

print("script is running...")


def source_copy_to_replica():
    '''
        This function has used to create and copy the sources into the replica
    '''
    for source_path, source_dirs, source_files in os.walk(source_folder):
        replica_path = source_path.replace(source_folder, replica_folder)
        if not os.path.exists(replica_path):
            os.makedirs(replica_path)
            print("Directory created....", replica_path)
        for file_ in source_files:
            source_file = os.path.join(source_path, file_)
            replica_file = os.path.join(replica_path, file_)
            if os.path.exists(replica_file):
                os.remove(replica_file)
            shutil.copy(source_file, replica_path)
                    
def source_removal_to_replica():
    '''
        This function has used to remove directory and file the source into the replica folder
    '''
    for source_path, source_dirs, source_files in os.walk(replica_folder):
        replica_path = source_path.replace(replica_folder, source_folder)
        if not os.path.exists(replica_path):
            shutil.rmtree(source_path)   
            print("Directory deleted....",source_path)
        for file_ in source_files:
            source_file = os.path.join(source_path, file_)
            replica_file = os.path.join(replica_path, file_)
            try:
                if not os.path.exists(replica_file):
                    os.remove(source_file)
                    print("File deleted....", source_file)
            except:
                pass
                                
starttime = time.time()
while True:
    source_copy_to_replica()
    source_removal_to_replica()
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))