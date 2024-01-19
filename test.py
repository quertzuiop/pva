import os

def test(directory, results):
    i=0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and "out" in filename:
            correct = open(f, "r").read().split("\n")
            if results[i] in correct:
                print("Correct")

            