if __name__ == "__main__":

    import sys
    import subprocess
    subprocess.Popen("python -m pip install --upgrade pip", shell=True)
    subprocess.Popen("python -m pip install numpy", shell=True)
    subprocess.Popen("python -m pip install Pillow", shell=True)
    subprocess.Popen("python -m pip install pyqt5", shell=True)
    subprocess.Popen("python -m pip install scipy", shell=True)
    subprocess.Popen("python -m pip install scikit-image", shell=True)
    subprocess.Popen("python -m pip install matplotlib", shell=True)
