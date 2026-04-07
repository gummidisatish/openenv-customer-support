def grade_extraction(predicted, actual):
    correct = 0
    total = len(actual)

    for key in actual:
        if predicted.get(key) == actual.get(key):
            correct += 1

    return correct / total