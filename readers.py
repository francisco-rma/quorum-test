import csv
import os
import string
from typing import Sequence, Tuple


cwd: string = os.getcwd()
os.chdir(cwd)

cwd = os.getcwd()


def read_legislators() -> Sequence:
    """Reads a csv file containing information on legislators and returns a list sorted by their id"""
    sorted_legislators: Sequence = []

    with open(
        f"{cwd}\\inputs\\legislators.csv", newline="", encoding="utf-8"
    ) as legislators:
        reader = csv.reader(legislators)
        _ = next(reader)

        for element in reader:
            sorted_legislators.append(element)

    merge_sort(sorted_legislators, key=0)

    return sorted_legislators


def read_sorted_votes_by_legislator() -> Sequence:
    """Reads a csv file containing vote results and returns a list of sorted by their legislator_id"""
    sorted_votes_by_legislator_id: Sequence = []

    with open(
        f"{cwd}\\inputs\\vote_results.csv", newline="", encoding="utf-8"
    ) as vote_results:
        reader = csv.reader(vote_results)
        _ = next(reader)

        for element in reader:
            sorted_votes_by_legislator_id.append(element)
    merge_sort(sorted_votes_by_legislator_id, key=1)
    return sorted_votes_by_legislator_id


def read_bills() -> Sequence:
    """Reads a csv file containing bills and returns an unsorted list of bills"""
    bills: Sequence = []
    with open(f"{cwd}\\inputs\\bills.csv", newline="", encoding="utf-8") as csv_bills:
        reader = csv.reader(csv_bills)
        _ = next(reader)
        for _, element in enumerate(reader):
            bills.append(element)
    return bills


def read_votes() -> Tuple[Sequence, dict]:
    """Reads a csv file containing votes and returns an unsorted list of votes"""
    votes: Sequence = []
    map_bill_to_vote = {}

    with open(f"{cwd}\\inputs\\votes.csv", newline="", encoding="utf-8") as csv_votes:
        reader = csv.reader(csv_votes)
        _ = next(reader)
        for index, element in enumerate(reader):
            votes.insert(index, element)
            map_bill_to_vote[element[1]] = element[0]
    return votes, map_bill_to_vote


def merge_sort(my_list, key):
    """Merge sort"""

    if len(my_list) > 1:
        midpoint = len(my_list) // 2
        left_array = my_list.copy()[:midpoint]
        right_array = my_list.copy()[midpoint:]

        merge_sort(left_array, key)

        merge_sort(right_array, key)

        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):
            if int(left_array[i][key]) <= int(right_array[j][key]):
                my_list[k] = left_array[i]
                i += 1
            else:
                my_list[k] = right_array[j]
                j += 1

            k += 1

        while i < len(left_array):
            my_list[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            my_list[k] = right_array[j]
            j += 1
            k += 1
