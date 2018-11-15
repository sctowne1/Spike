# Spike Image Processing

 **When you run this program, it will automatically update your pip command and install the following packages:**
   - PIL,
   - scikit-image,
   - scipy,
   - numpy,
   - pyqt5,
   - matplotlib
   - opencv-python
   - imageio

_This program has only been tested on Windows machines uing Python 3.7._

This is an image editing program that implements image editing functions from the following packages:
   - PIL
   - skikit-image
   - scipy
   - numpy

 It also utilizes **pyqt5** for creation of the GUI.

 The following functions have been implemented:
   Load Image, Save Image, Mirror Image, Invert Image, Rotate Image, Grayscale Image, Compare and Undo.
   
 ### Known Issues:

- The  _Feature Extraction_ portion of the program is used to extract key points from an image and provide comparisons to images in a
 given directory, then displaying the query image and the most similar image. This feature of the program functions properly with images
 that are of smaller size (around 80Kb), but only returns approximately a 67% match for an image with a singular pixel modification. We
 are currently using a combination of **scipy** and **opencv** for this portion of the program, however, due to limitations concerning
 file size and accuracy we are researching other resources and methods.

- This program supports **.jpg** and **.png** files; HOWEVER, when editing a **.png** file the image that appears in the Spike display
 _appears to lose quality_, though if you open the edited image outside of the program after saving it, _no quality has 
 actually been lost._
