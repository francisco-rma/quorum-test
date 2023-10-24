"""csv reading and writing tools"""
import csv

import os
import string
from typing import Sequence


def sort(input_array: Sequence, key: string = "") -> Sequence:
    """sort"""

    index = 1
    while index < input_array.line_num:
        key = input_array[index]
        j = index - 1

        while j >= 0 and input_array[j] > key:
            input_array[j + 1] = input_array[j]
            j -= 1

        input_array[j + 1] = key
        index += 1
    return


sorted_legislators: Sequence = []
sorted_votes_by_legislator_id: Sequence = []

cwd: string = os.getcwd()
os.chdir(cwd)

cwd = os.getcwd()

with open(
    f"{cwd}/source" + "\\legislators.csv", newline="", encoding="utf-8"
) as vote_results:
    reader = csv.reader(vote_results)
    headers = next(reader)

    sorted_legislators.append(next(reader))

    for element in reader:
        i = 0

        comparison = int(element[0])

        while (
            i < len(sorted_legislators) and int(sorted_legislators[i][0]) <= comparison
        ):
            i += 1

        sorted_legislators.insert(i, element)

with open(
    f"{cwd}/source" + "\\vote_results.csv", newline="", encoding="utf-8"
) as vote_results:
    reader = csv.reader(vote_results)
    headers = next(reader)

    sorted_votes_by_legislator_id.append(next(reader))

    for element in reader:
        i = 0

        comparison = int(element[1])

        while (
            i < len(sorted_votes_by_legislator_id)
            and int(sorted_votes_by_legislator_id[i][1]) <= comparison
        ):
            i += 1

        sorted_votes_by_legislator_id.insert(i, element)


with open(
    cwd + "\\legislator_support_oppose_count.csv", "w", newline="", encoding="utf-8"
) as file:
    writer = csv.writer(file)
    fields = ["id", "name", "num_supported_bills", "num_opposed_bills"]

    writer.writerow(fields)
    i = 0
    for index, legislator in enumerate(sorted_legislators):
        oppose_count = 0
        support_count = 0

        while (
            i < len(sorted_votes_by_legislator_id)
            and sorted_votes_by_legislator_id[i][1] == legislator[0]
        ):
            if int(sorted_votes_by_legislator_id[i][3]) == 1:
                support_count += 1
            else:
                oppose_count += 1

            i += 1

        row = [
            legislator[0],
            legislator[1],
            support_count,
            oppose_count,
        ]
        writer.writerow(row)

# print([a for a in sorted_legislators])
# print([a for a in sorted_votes_by_legislator_id])
