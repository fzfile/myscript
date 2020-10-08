import os
import subprocess

def main():
    file_list = os.listdir()
    for file_name in file_list:
        if file_name.endswith('flv'):
            do = subprocess.Popen('ffmpeg -i "%s" -c copy "./temp/%s"' %(file_name, file_name[:-3] + 'mp4'), shell=True)
            do.wait()
            de = subprocess.Popen('rm "%s"' % file_name, shell=True)
            de.wait()
        elif file_name.endswith('mp4'):
            do = subprocess.Popen('ffmpeg -i "%s" -i "%s" -c copy "./temp/%s"' % (file_name, file_name.replace('mp4', 'm4a'), file_name), shell=True)
            do.wait()
            de = subprocess.Popen('rm "%s"' % file_name, shell=True)
            de.wait()
            de = subprocess.Popen('rm "%s"' % file_name.replace('mp4', 'm4a'), shell=True)
            de.wait()

if __name__ == "__main__":
    main()
