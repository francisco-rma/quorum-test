import csv
from typing import Sequence

with open("legislators.csv", newline="") as legislators:
    spamreader = csv.reader(legislators)
    for element in spamreader:
        print(element)


def sort(input: Sequence):
    sorted_array = []
    return
