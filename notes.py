#!/usr/bin/env python3

import yaml;
import os;
import datetime;
from settings import Settings;

def clear() -> None:
	os.system('clear')

def open_file() -> dict:
	with open(Settings.storage_file, 'r') as file:
		notes = yaml.safe_load(file)
	return notes

def create_new_group(notes: dict) -> dict:
	clear()
	group_name = input("Enter the new group name: ")
	notes[group_name] = {}
	clear()
	return notes

def delete_group(notes: dict) -> dict:
	i = 0
	clear()
	print("Choose a note group to delete:")
	for key in notes.keys():
		print(f"{i}) {key}")
		i += 1
	choice = input("Enter the number of the note group to delete: ")
	note_group = list(notes.keys())[int(choice)]
	clear()
	choice = input(f"Really delete group: {note_group} (y/n): ")
	if choice.lower() == 'y':
		notes.pop(note_group)
	return notes

def get_dates(the_list: str, notes: dict) -> list:
	dates = []
	for date in notes[the_list]:
		dates.append(date)
	return dates

def print_notes(the_list: str, date: str, notes: dict) -> list:
	print(f"\033[1mNotes for: {the_list} on {date}\033[0m")
	for note in notes[the_list][date]:
		print('-', note)

def create_new_note(notes: dict) -> None:
	clear()
	i = 0
	for key in notes.keys():
		print(f"{i}) {key}")
		i += 1
	group = int(input("What group does this note belong to?"))
	try:
		'' in notes[list(notes.keys())[group]][str(datetime.date.today())]
	except (NameError, KeyError) :
		notes[list(notes.keys())[group]][str(datetime.date.today())] = []
	clear()
	print("Type your notes. Enter DONE when finished. Each line will be one note")
	while True:
		note = input("> ")
		if note == "DONE":
			break;
		else:
			notes[list(notes.keys())[group]][str(datetime.date.today())].append(note)
	return notes

def write_notes(notes: dict) -> None:
	with open(Settings.storage_file, 'w') as file:
		file.write(yaml.dump(notes))

def main():
	clear()
	while True:
		print("\n\033[1mWelcome to the note-inator. Please choose a function\033[0m")
		print("0) Read notes")
		print("1) Write notes")
		print("2) Add Group")
		print("3) Delete Group")
		choice = int(input(">: "))
		notes = open_file()
		if choice == 0:
			i = 0
			print("\033[1mAvailable groups:\033[0m")
			for key in notes.keys():
				print(f"{i}) {key}")
				i += 1
			the_group = int(input("\033[1mChoose a group: \033[0m"))
			dates = get_dates(list(notes.keys())[the_group], notes)
			print("\033[1mDates in the note\033[0m")
			i = 0
			for date in dates:
				print(f"{i}) {date}")
				i += 1
			j = int(input("\033[1mChoose a date: \033[0m"))
			clear()
			print_notes(list(notes.keys())[the_group], dates[j], notes)
		elif choice == 1:
			notes = create_new_note(notes)
			write_notes(notes)
		elif choice == 2:
			notes = create_new_group(notes)
			write_notes(notes)
		elif choice == 3:
			notes = delete_group(notes)
			write_notes(notes)
		else:
			break
main()
