#!/usr/bin/python3
"""  module for lockboxes coding task"""


def canUnlockAll(boxes):
    """function that checks if all boxes can be unlocked"""
    box = boxes[0]
    unlocked_boxes = {0}
    for key in box:
        if key not in unlocked_boxes:
            try:
                unlocked_box = boxes[key]
                unlocked_boxes.add(key)
                box += unlocked_box
            except Exception as e:
                continue
        if len(unlocked_boxes) == len(boxes):
            return True
    return False
