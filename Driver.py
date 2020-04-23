import Read_file
import Generate_model
import Detector
import PARAMETER

if __name__ == '__main__':

    # Read_file.allfiles(PARAMETER.PACKET_TRAIN)
    #
    # Generate_model.create_model()

    Read_file.allfiles(PARAMETER.PACKET_TEST)
    Detector.run()