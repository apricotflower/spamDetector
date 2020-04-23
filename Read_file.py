import re
import PARAMETER

all_train_document = dict()
all_test_document = dict()


def tokenize(class_type, file_id):

    if cur_packet == PARAMETER.PACKET_TRAIN:
        cur_document = all_train_document
        path = PARAMETER.TRAIN_PATH
    elif cur_packet == PARAMETER.PACKET_TEST:
        cur_document = all_test_document
        path = PARAMETER.TEST_PATH
    else:
        print("Error packet !")

    f = None
    if class_type == PARAMETER.CLASS_HAM:
        f = open(path + "-" + PARAMETER.CLASS_HAM + "-" + file_id + ".txt", 'r', encoding='latin-1')
    elif class_type == PARAMETER.CLASS_SPAM:
        f = open(path + "-" + PARAMETER.CLASS_SPAM + "-" + file_id + ".txt", 'r', encoding='latin-1')

    if f:
        cur_document[class_type + "-" + file_id] = re.split('[^a-zA-Z]', f.read().lower())

        # empty_token_list = []
        # for token in all_train_document[class_type + "_" + file_id]:
        #     if token == '':
        #         empty_token_list.append(token)
        # for e in empty_token_list:
        #     all_train_document[class_type + "_" + file_id].remove(e)

    else:
        print("Read file error!")


def allfiles(package):
    global cur_packet
    cur_packet = package

    if package == PARAMETER.PACKET_TRAIN:
        for num in range(1, 1001): # 1-1000
            tokenize(PARAMETER.CLASS_HAM, str(num).zfill(5))

        for num in range(1, 998): # 1-997
            tokenize(PARAMETER.CLASS_SPAM, str(num).zfill(5))

    elif package == PARAMETER.PACKET_TEST:
        for num in range(1, 401):  # 1-400
            tokenize(PARAMETER.CLASS_HAM, str(num).zfill(5))

        for num in range(1, 401):  # 1-400
            tokenize(PARAMETER.CLASS_SPAM, str(num).zfill(5))

# allfiles(PARAMETER.TEST_PATH)
# allfiles(PARAMETER.PACKET_TEST)