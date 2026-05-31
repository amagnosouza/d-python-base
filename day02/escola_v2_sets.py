#!/usr/bin/env python3
"""
Display a report of children by activity.

Print the list of children grouped by the classroom they attend
for each of the activities offered by the school.
"""
# Metadata about the script
__version__ = "1.1"
__author__  = "Alexandre Souza"

# Data
room1 = ["Maria", "João", "Ana", "Pedro", "Lucas", "Sofia"]
room2 = ["Carla", "Rafael", "Beatriz", "Gustavo", "Fernanda", "Bruno"]

english_class = ["Maria", "Carla", "Rafael", "Ana", "Gustavo"]
music_class = ["João", "Beatriz", "Pedro", "Fernanda", "Sofia"]
arts_class = ["Lucas", "Bruno", "Ana", "Gustavo", "Sofia"]

# Activities and their respective class lists
activities = [
    ("English", english_class),
    ("Music", music_class),
    ("Arts", arts_class)
]

# List students in each activity by room using sets for efficient lookup
for activity_name, activity in activities:
    activity_room1 = set(room1) & set(activity)
    activity_room2 = set(room2) & set(activity)
    print(f"Activity {activity_name} - Room 1:", activity_room1)
    print(f"Activity {activity_name} - Room 2:", activity_room2)
    print("-"*30)  # Separator for readability