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

        sorted_legislators.append(next(reader))

        for element in reader:
            i = 0

            comparison = int(element[0])

            while (
                i < len(sorted_legislators)
                and int(sorted_legislators[i][0]) <= comparison
            ):
                i += 1

            sorted_legislators.insert(i, element)

        return sorted_legislators


def read_sorted_votes_by_legislator() -> Sequence:
    """Reads a csv file containing vote results and returns a list of sorted by their legislator_id"""
    sorted_votes_by_legislator_id: Sequence = []

    with open(
        f"{cwd}\\inputs\\vote_results.csv", newline="", encoding="utf-8"
    ) as vote_results:
        reader = csv.reader(vote_results)
        _ = next(reader)

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

        return sorted_votes_by_legislator_id


def read_bills() -> Sequence:
    """Reads a csv file containing bills and returns an unsorted list of bills"""
    bills: Sequence = []
    with open(f"{cwd}\\inputs\\bills.csv", newline="", encoding="utf-8") as csv_bills:
        reader = csv.reader(csv_bills)
        _ = next(reader)
        for index, element in enumerate(reader):
            bills.insert(index, element)
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
