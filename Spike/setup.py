if __name__ == "__main__":

    import sys
    import subprocess
    
    #TODO: Having shell=True in the subprocess call is a known security hazard. Need to research why and if it affects us, and if needed how to get around it
    subprocess.Popen("python -m pip install --upgrade pip", shell=True)
    subprocess.Popen("python -m pip install numpy", shell=True)
    subprocess.Popen("python -m pip install Pillow", shell=True)
    subprocess.Popen("python -m pip install pyqt5", shell=True)
    subprocess.Popen("python -m pip install scipy", shell=True)
    subprocess.Popen("python -m pip install scikit-image", shell=True)
    subprocess.Popen("python -m pip install matplotlib", shell=True)
    subprocess.Popen("python -m pip install opencv-python", shell=True)
    subprocess.Popen("python -m pip install imageio", shell=True)



