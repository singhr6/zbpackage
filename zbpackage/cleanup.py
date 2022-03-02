'''
This module contain following functions

'''

import time
import os
import shutil

# This function delete directory and sub directory of directory timestamp is older than retention period
def dir_cleanup(cleanup_dir,retention):
    try:
        # initializing some variables
        current_time = time.time()

        # Checking directory timestamp and deciding to delete
        past_days_time = current_time - int(retention) * 86400
        for name in os.listdir(cleanup_dir):
            path = os.path.join(cleanup_dir, name)
            if os.path.isdir(path):
                modified_time = os.path.getmtime(path)
                if modified_time > past_days_time:
                    continue
                else:
                    shutil.rmtree(path)
            else:
                continue

        return 'success'

    except Exception as e:
        return str(e)



def file_cleanup(cleanup_dir,retention):
    try:
        # initializing some variables
        files = ''
        current_time = time.time()

        # Checking directory timestamp and deciding to delete
        past_days_time = current_time - int(retention) * 86400
        for file_name in os.listdir(cleanup_dir.rstrip()):
            file_path = os.path.join(cleanup_dir.rstrip(), file_name)
            if os.stat(file_path).st_mtime < past_days_time:
                files = files + file_path + '\n'
                os.remove(file_path)

        return 'success'

    except Exception as e:
        return str(e)


# This is for unit test of this module
if __name__ == "__main__":
    print(file_cleanup("C:\\temp\\out",0))

if __name__== "__main__":
    print(dir_cleanup("C:\\temp\\out",0))