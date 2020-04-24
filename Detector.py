import PARAMETER
import Read_file
import math

all_test_document = Read_file.all_test_document
model_lines = dict()


def load_model():
    for line in open(PARAMETER.MODEL):
        if line:
            model_lines[line.split("  ")[1]] = line.split("  ")


def start_detector():
    # print(model_lines)
    output_file = open(PARAMETER.RESULT, "a+", encoding='utf8')
    p_ham = 1000/1997
    p_spam = 997/1997
    error_counter = 0
    i = 1
    for (key, value) in all_test_document.items():
        score_ham = math.log(p_ham,10)
        score_spam = math.log(p_spam,10)
        for term in value:
            if term and term in model_lines:
                score_ham = score_ham + math.log(float(model_lines[term][3]),10)
                score_spam = score_spam + math.log(float(model_lines[term][5]),10)
        if score_ham > score_spam:
            classify_class = PARAMETER.CLASS_HAM
        else:
            classify_class = PARAMETER.CLASS_SPAM
        if classify_class == key.split("-")[0]:
            label = PARAMETER.RIGHT
        else:
            label = PARAMETER.WRONG
            error_counter = error_counter + 1
        output_file.write(str(i) + "  " + PARAMETER.PACKAGE_TEST + "-" + key + ".txt" + "  " + classify_class + "  " + str(score_ham) + "  " + str(score_spam) + "  " + key.split("-")[0] + "  " + label + "\n")
        i = i+1
    print("error: " + str(error_counter))


def run():
    load_model()
    start_detector()