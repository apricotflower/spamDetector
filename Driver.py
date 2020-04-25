import Read_file
import Generate_model
import Detector
import PARAMETER
import os

if __name__ == '__main__':

    Read_file.allfiles(PARAMETER.PACKAGE_TRAIN)

    Generate_model.create_model()

    Read_file.allfiles(PARAMETER.PACKAGE_TEST)

    Detector.run()
