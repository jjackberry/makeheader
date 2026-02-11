#!/usr/bin/env python3
import os
import sys

def bail(msg="\nExiting makeheader. No files were modified."):
    print(msg)
    sys.exit(0)

def prompt(field_name, required=True):
    while True:
        val = input(f"{field_name}: ").strip()
        if val.lower() in ("q", "quit", "exit"):
            bail()
        if val or not required:
            return val
        print("Can't be empty. Enter something or type q to quit.")


def prompt_multiline():
    print("Paste the problem description (blank line when done):")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip().lower() in ("q", "quit", "exit"):
            bail()
        if line == "":
            break
        lines.append(line)
    return "\n".join(lines).strip()

def show_intro():
    print("""
=========================================
 makeheader — Header Generator CLI
=========================================

Paste a problem description (from LeetCode, an assignment, etc.) and it becomes the header comment in your source file.

At any prompt you can type q, quit, or exit to cancel. Runs in the current directory — run it from the folder where the file should live.
""")

def build_header(description):
    # Indent pasted lines so the block comment looks right
    indented = "\n ".join(description.split("\n"))
    return f"""/*
 {indented}
*/

"""

def write_header(path, header_text):
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write(header_text)
        print(f"Created {path} with header.")
        return

    choice = input("File exists. Overwrite (o) or append (a)? ").strip().lower()
    if choice in ("q", "quit", "exit"):
        bail()

    if choice == "o":
        with open(path, "w") as f:
            f.write(header_text)
        print(f"Overwrote header in {path}")
    elif choice == "a":
        with open(path, "r+") as f:
            existing = f.read()
            f.seek(0)
            f.write(header_text + existing)
        print(f"Prepended header to {path}")
    else:
        print("Didn't recognize that. No changes made.")

def main():
    show_intro()

    file_name = prompt("Target file (e.g. main.cpp, script.py)")
    description = prompt_multiline()
    if not description:
        print("No description entered. Exiting.")
        sys.exit(0)

    header = build_header(description)
    write_header(file_name, header)

    print("\nDone.")

if __name__ == "__main__":
    main()
