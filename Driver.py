import Read_file
import Generate_model
import Detector
import PARAMETER
import os

if __name__ == '__main__':
    if os.path.exists(PARAMETER.MODEL):
        os.remove(PARAMETER.MODEL)
    if os.path.exists(PARAMETER.RESULT):
        os.remove(PARAMETER.RESULT)

    Read_file.allfiles(PARAMETER.PACKAGE_TRAIN)

    Generate_model.create_model()

    Read_file.allfiles(PARAMETER.PACKAGE_TEST)

    Detector.run()
