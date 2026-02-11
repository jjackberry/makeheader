#!/usr/bin/env python3
import os
import re
import sys

PACKAGES_H_FILENAME = "packages.h"

PACKAGES_H_CONTENT = """#ifndef PACKAGES_H
#define PACKAGES_H

#include <algorithm>
#include <climits>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#endif
"""

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
    print("Paste the problem description, then press Ctrl+D when done (Mac/Linux) or Ctrl+Z then Enter (Windows).")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip().lower() in ("q", "quit", "exit"):
            bail()
        lines.append(line)
    return "\n".join(lines).strip()

def show_intro():
    print("""
=========================================
 makeheader — Header Generator CLI
=========================================

Paste a problem description (from LeetCode, an assignment, etc.) and it becomes a C++ block comment (/* ... */) at the top of your file.

At any prompt you can type q, quit, or exit to cancel. Runs in the current directory — run it from the folder where the file should live.
""")

def build_header(description):
    # Indent pasted lines so the block comment looks right
    indented = "\n ".join(description.split("\n"))
    return f"""/*
 {indented}
*/

"""

def is_cpp(path):
    return path.lower().endswith(".cpp")

def ensure_packages_h(target_path):
    """Create packages.h in the same directory as target_path if it doesn't exist. Return path to packages.h or None."""
    target_dir = os.path.dirname(target_path) or "."
    packages_h_path = os.path.join(target_dir, PACKAGES_H_FILENAME)
    if not os.path.exists(packages_h_path):
        try:
            os.makedirs(target_dir, exist_ok=True)
            with open(packages_h_path, "w") as f:
                f.write(PACKAGES_H_CONTENT)
            print(f"Created {packages_h_path} with common packages.")
        except OSError as e:
            print(f"Warning: could not create {packages_h_path}: {e}. Continuing without it.")
            return None
    return packages_h_path

def strip_one_include_packages_h(content):
    """Remove the first line that is #include \"packages.h\" or \"leetcode.h\" (with optional whitespace). Returns (stripped_content, was_found)."""
    pattern = re.compile(r'^\s*#\s*include\s*["<](?:packages|leetcode)\.h[">]\s*\n?', re.MULTILINE)
    match = pattern.search(content)
    if match:
        before = content[:match.start()].rstrip()
        after = content[match.end():].lstrip("\n")
        new_content = (before + "\n\n" + after) if after else before
        return new_content, True
    return content, False

def write_header(path, header_text):
    use_include = is_cpp(path)
    include_line = ""
    if use_include:
        ensure_packages_h(path)
        include_line = '\n#include "packages.h"\n\n'

    if not os.path.exists(path):
        target_dir = os.path.dirname(path)
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)
        with open(path, "w") as f:
            f.write(header_text + include_line)
        print(f"Created {path} with header.")
        return

    choice = input("File exists. Overwrite (o) or append (a)? ").strip().lower()
    if choice in ("q", "quit", "exit"):
        bail()

    if choice == "o":
        with open(path, "w") as f:
            f.write(header_text + include_line)
        print(f"Overwrote header in {path}")
    elif choice == "a":
        with open(path, "r") as f:
            existing = f.read()
        if use_include:
            existing_stripped, _ = strip_one_include_packages_h(existing)
            new_content = header_text + include_line + existing_stripped
        else:
            new_content = header_text + existing
        with open(path, "w") as f:
            f.write(new_content)
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
