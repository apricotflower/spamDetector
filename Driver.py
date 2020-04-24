import Read_file
import Generate_model
import Detector
import PARAMETER
import os

if __name__ == '__main__':

    os.remove(PARAMETER.MODEL)
    os.remove(PARAMETER.RESULT)

    Read_file.allfiles(PARAMETER.PACKET_TRAIN)

    Generate_model.create_model()

    Read_file.allfiles(PARAMETER.PACKET_TEST)
    Detector.run()