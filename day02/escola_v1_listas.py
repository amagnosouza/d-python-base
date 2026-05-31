#!/usr/bin/env python3
"""
Display a report of children by activity.

Print the list of children grouped by the classroom they attend
for each of the activities offered by the school.
"""
# Metadata about the script
__version__ = "1.0"
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

# List students in each activity by room
for activity_name, activity in activities:
    room1_students = []
    room2_students = []

    for student in activity:
        if student in room1:
            room1_students.append(student)
        elif student in room2:
            room2_students.append(student)
    print(f"Activity {activity_name} - Room 1:", room1_students)
    print(f"Activity {activity_name} - Room 2:", room2_students)
    print("-"*30)  # Separator for readability