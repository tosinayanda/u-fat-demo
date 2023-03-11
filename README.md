# INTRODUCTION

The Sleuth Kit or TSK is a collection of open source digital forensic tools developed by Brian Carrier and Wieste Venema. TSK can read and parse different types of filesystems, such as FAT, NTFS, and EXT. Each area of the hard drive in the figure in the Hard drive structure section has a set of tools in The Sleuth Kit that parses that area and extracts forensically important information for the investigator. Usually, each step leads to the next while using TSK in analysis.

## DESKTOP APPLICATION

### NOTE
- DD (raw format) is compatible with all the major forensic tools.
- EWF is a propietary format by EnCase

### PYEWF SETUP
https://github.com/libyal/libewf
https://github.com/libyal/libewf/releases 

- ./synclibs.sh
- ./autogen.sh
- sudo python setup.py build
- sudo python setup.py install

### RUN EXAMPLES
- python process_evidence.py ./resources/fat-img-kw.dd raw
- python process_evidence.py ./resources/Mantooth32.E01

### PACKAGING
https://www.pythonguis.com/tutorials/packaging-pyqt5-pyside2-applications-windows-pyinstaller/ 
https://learnpython.com/blog/python-requirements-file/

## TESTING IMAGE SOURCES
https://dftt.sourceforge.net/ 

## WEB APPLICATION

## REF
https://hackernoon.com/getting-started-with-digital-forensics-using-the-sleuth-kit-c34a3wkg
https://github.com/tqdm/tqdm
https://www.varonis.com/blog/how-to-use-volatility 
https://sleuthkit.discourse.group/t/memory-image-file-volatility/433
https://sleuthkit.discourse.group/t/encase-e01-autopsy/3530 
https://sleuthkit.org/autopsy/docs/user-docs/3.1/ds_page.html 