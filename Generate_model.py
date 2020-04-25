import Read_file
import PARAMETER
import math

all_train_document = Read_file.all_train_document


def create_model():
    token_dict = {}
    for (key, value) in all_train_document.items():
        class_type = key.split("-")[0]
        for term in value:
            if term:
                if term not in token_dict:
                    token_dict[term] = [[class_type, 1]]
                else:
                    has_existed_class = False
                    for doc in token_dict[term]:
                        if doc[0] == class_type:
                            doc[1] = doc[1] + 1
                            has_existed_class = True
                    if not has_existed_class:
                        token_dict[term].append([class_type, 1])

    ham_total = 0
    spam_total = 0
    for value in token_dict.values():
        for doc in value:
            if doc[0] == PARAMETER.CLASS_HAM:
                ham_total = ham_total + doc[1]
            if doc[0] == PARAMETER.CLASS_SPAM:
                spam_total = spam_total + doc[1]
                
    vocabulary = len(token_dict)
    smoothing = PARAMETER.SMOOTHING
    
    print("ham total: " + str(ham_total))
    print("spam total: " + str(spam_total))
    print("vocalulary: " + str(vocabulary))

    keys_list = sorted(token_dict.keys())
    output_file = open(PARAMETER.MODEL, "w+", encoding='utf8')
    i = 1
    for key in keys_list:
        line = []
        line.append(str(i))
        line.append(str(key))
        ham = 0
        spam = 0
        for doc in token_dict[key]:
            if doc[0] == PARAMETER.CLASS_HAM:
                ham = doc[1]
            if doc[0] == PARAMETER.CLASS_SPAM:
                spam = doc[1]
        line.append(str(ham))
        line.append(str((ham + smoothing)/(ham_total + 0.5 * vocabulary)))
        line.append(str(spam))
        line.append(str((spam + smoothing) /(spam_total + 0.5 * vocabulary)))
        output_file.write(line[0] + "  " + line[1] + "  " + line[2] + "  " + line[3] + "  " + line[4] + "  " + line[5] + "  " + "\n")
        i = i + 1
