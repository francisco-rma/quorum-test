"""Typing"""
from typing import Sequence
import readers
import writers

sorted_legislators = readers.read_legislators()
sorted_votes_by_legislator_id: Sequence = readers.read_sorted_votes_by_legislator()
bills: Sequence = readers.read_bills()
votes, map_bill_to_vote = readers.read_votes()

writers.write_legislator_support_ooppose_count(
    sorted_legislators=sorted_legislators,
    sorted_votes_by_legislator_id=sorted_votes_by_legislator_id,
)

writers.write_bill_support(
    sorted_legislators=sorted_legislators,
    sorted_votes_by_legislator_id=sorted_votes_by_legislator_id,
    bills=bills,
    map_bill_to_vote=map_bill_to_vote,
)
