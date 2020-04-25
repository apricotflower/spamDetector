import PARAMETER
import Read_file
import math
import matplotlib.pyplot as plt
import numpy as np

all_test_document = Read_file.all_test_document
model_lines = dict()


def load_model():
    for line in open(PARAMETER.MODEL):
        if line:
            model_lines[line.split("  ")[1]] = line.split("  ")


def start_detector():
    # print(model_lines)
    tp_ham, fp_ham, fn_ham, tn_ham, = 0, 0, 0, 0 # real:ham predict:ham,real:spam predict:ham,real:ham predict:spam,real:spam predict:spam
    tp_spam, fp_spam, fn_spam, tn_spam, = 0, 0, 0, 0
    output_file = open(PARAMETER.RESULT, "w+", encoding='utf8')
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
            if classify_class == PARAMETER.CLASS_HAM:
                tp_ham = tp_ham + 1
                tn_spam = tn_spam + 1
            if classify_class == PARAMETER.CLASS_SPAM:
                tn_ham = tn_ham + 1
                tp_spam = tp_spam + 1
        else:
            label = PARAMETER.WRONG
            error_counter = error_counter + 1
            if classify_class == PARAMETER.CLASS_HAM:
                fp_ham = fp_ham + 1
                fn_spam = fn_spam + 1
            if classify_class == PARAMETER.CLASS_SPAM:
                fn_ham = fn_ham + 1
                fp_spam = fp_spam + 1
        output_file.write(str(i) + "  " + PARAMETER.PACKAGE_TEST + "-" + key + ".txt" + "  " + classify_class + "  " + str(score_ham) + "  " + str(score_spam) + "  " + key.split("-")[0] + "  " + label + "\n")
        i = i+1
    print("error: " + str(error_counter))

    ham_arr = [[tp_ham, fp_ham], [fn_ham, tn_ham]]
    show_confusion_matrix(ham_arr, title='ham confusion matrix')
    print("ham: ")
    calculation(tp_ham, fp_ham, fn_ham, tn_ham)
    spam_arr = [[tp_spam, fp_spam], [fn_spam, tn_spam]]
    show_confusion_matrix(spam_arr, title='spam confusion matrix')
    print("spam: ")
    calculation(tp_spam, fp_spam, fn_spam, tn_spam)


def show_confusion_matrix(cm, title):
    # print(cm)
    cm = np.array(cm)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.matshow(cm, cmap=plt.cm.binary)

    # ax.imshow(np.array(cm), cmap=plt.cm.jet,
    #           interpolation='nearest')

    width, height = cm.shape

    for x in range(width):
        for y in range(height):
            ax.annotate(str(cm[x][y]), xy=(y, x),color = "red",
                        horizontalalignment='center',
                        verticalalignment='center')

    ax.set_xticklabels([''] + ["in real it is", "in real not"])
    ax.set_yticklabels([''] + ["in predict it is", "in predict not"])
    ax.set_xlabel('Real')
    ax.set_ylabel('Predicted')
    plt.title(title)
    plt.show()


def calculation(tp, fp, fn, tn):
    accuracy = round((tp + tn)/(tp+fp+fn+tn),3)
    print("accuracy: " + str(accuracy))
    precision = round(tp/(tp + fp),3)
    print("precision: " + str(precision))
    recall = round(tp/(tp + fn),3)
    print("recall: " + str(recall))
    f1_measure = round(2 * precision * recall/(precision + recall),3)
    print("f1_measure: " + str(f1_measure))





def run():
    load_model()
    start_detector()