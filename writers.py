import csv
import os
import string
from typing import Sequence


cwd: string = os.getcwd()
os.chdir(cwd)

cwd = os.getcwd()


def write_legislator_support_ooppose_count(
    sorted_legislators: Sequence, sorted_votes_by_legislator_id: Sequence
):
    with open(
        cwd + "\\legislator_support_oppose_count.csv", "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        fields = ["id", "name", "num_supported_bills", "num_opposed_bills"]

        writer.writerow(fields)
        i = 0
        for _, legislator in enumerate(sorted_legislators):
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


def write_bill_support(
    sorted_legislators: Sequence,
    sorted_votes_by_legislator_id: Sequence,
    bills: Sequence,
    map_bill_to_vote: Sequence,
):
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
