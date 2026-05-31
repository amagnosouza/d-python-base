#!/usr/bin/env python3
"""
Display a report of children by activity.

Print the list of children grouped by the classroom they attend
for each of the activities offered by the school.
"""
# Metadata about the script
__version__ = "1.3"
__author__  = "Alexandre Souza"

# Data
room1 = ["Maria", "João", "Ana", "Pedro", "Lucas", "Sofia"]
room2 = ["Carla", "Rafael", "Beatriz", "Gustavo", "Fernanda", "Bruno"]

english_class = ["Maria", "Carla", "Rafael", "Ana", "Gustavo"]
music_class = ["João", "Beatriz", "Pedro", "Fernanda", "Sofia"]
arts_class = ["Lucas", "Bruno", "Ana", "Gustavo", "Sofia"]

rooms = {
    "Room 1": set(room1),
    "Room 2": set(room2),
}

# Activities and their respective participant sets
activities = {
    "English": set(english_class),
    "Music": set(music_class),
    "Arts": set(arts_class)
}

# List students in each activity by room using sets for efficient lookup
for activity_name, participants in activities.items():
    print(f"Activity {activity_name}")
    for room_name, students in rooms.items():
        enrolled = students & participants
        print(f"{room_name}: {sorted(enrolled)}")
    print("-" * 30)  # Separator for readability