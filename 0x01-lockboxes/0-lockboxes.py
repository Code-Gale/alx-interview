#!/usr/bin/python3
"""
Module for solving the "Unlock All Boxes" problem.

This module contains a function `canUnlockAll` that determines whether all boxes
in a given list of boxes can be opened or not, given that the first box is
initially unlocked, and each box may contain keys to other boxes.
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determine if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists, where each inner list
            represents the keys found in the corresponding box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # Box 0 is initially unlocked
    keys = boxes[0]  # Start with the keys found in box 0

    for key in keys:
        if key < n:
            unlocked[key] = True

    for box_num in range(1, n):
        if not unlocked[box_num]:
            continue

        for key in boxes[box_num]:
            if key < n:
                if not unlocked[key]:
                    unlocked[key] = True
                    keys.extend(boxes[key])

    return all(unlocked)