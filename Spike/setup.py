if __name__ == "__main__":

    import sys
    import subprocess
    subprocess.Popen("pip install --upgrade pip", shell=True)
    subprocess.Popen("pip install numpy", shell=True)
    subprocess.Popen("pip install Pillow", shell=True)
    subprocess.Popen("pip install pyqt5", shell=True)
    subprocess.Popen("pip install scipy", shell=True)
    subprocess.Popen("pip install scikit-image", shell=True)

    sys.exit(app.exec_())

