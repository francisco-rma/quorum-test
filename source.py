"""csv reading and writing tools"""
import csv
import math

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


def search_legislator_by_id(input_array: Sequence, target: int) -> int:
    """Find legislator by id, assuming a sorted input sequence"""
    start = 0
    end = len(input_array) - 1
    while start <= end:
        target_index = (start + end) // 2

        if input_array[target_index][0] == target:
            return target_index

        elif input_array[target_index][0] > target:
            end = target_index - 1
        else:
            start = target_index + 1

    return -1


sorted_legislators: Sequence = []
sorted_votes_by_legislator_id: Sequence = []
bills: Sequence = []
votes: Sequence = []
map_bill_to_vote = {}

cwd: string = os.getcwd()
os.chdir(cwd)

cwd = os.getcwd()

# reading

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


with open(f"{cwd}/source" + "\\bills.csv", newline="", encoding="utf-8") as csv_bills:
    reader = csv.reader(csv_bills)
    headers = next(reader)
    for index, element in enumerate(reader):
        bills.insert(i, element)

with open(f"{cwd}/source" + "\\votes.csv", newline="", encoding="utf-8") as csv_votes:
    reader = csv.reader(csv_votes)
    headers = next(reader)
    for index, element in enumerate(reader):
        votes.insert(i, element)
        map_bill_to_vote[element[1]] = element[0]

# writing

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

with open(cwd + "\\bill_support.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    fields = ["id", "title", "supporter_count", "opposer_count", "primary_sponsor"]

    writer.writerow(fields)
    i = 0
    vote_count = {}
    for index, vote_result in enumerate(sorted_votes_by_legislator_id):
        key = vote_result[2]
        if key not in vote_count:
            vote_count[key] = [0, 0]

        if int(vote_result[3]) == 1:
            vote_count[key][0] += 1
        else:
            vote_count[key][1] += 1

    for index, bill in enumerate(bills):
        sponsor_index = search_legislator_by_id(sorted_legislators, bill[2])
        sponsor = ""
        if sponsor_index != -1:
            sponsor = sorted_legislators[sponsor_index][1]
        else:
            sponsor = "Unkown"

        vote_id = map_bill_to_vote[bill[0]]
        row = [
            bill[0],
            bill[1],
            vote_count[vote_id][0],
            vote_count[vote_id][1],
            sponsor,
        ]
        writer.writerow(row)

# print([a for a in sorted_legislators])
# print([a for a in sorted_votes_by_legislator_id])
