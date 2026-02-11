# makeheader

Turns a coding problem description into a file header. Copy the problem text (from LeetCode, an assignment, a PDF, etc.), run makeheader, paste it when prompted, and it gets written as a comment block at the top of your source file. No dependencies.

**Requirements.** Python 3. Use `python3 --version` (Mac/Linux) or `python --version` (Windows) to check. If it’s not installed, get it from [python.org](https://www.python.org/downloads/).

**Install.**

```bash
git clone https://github.com/jjackberry/makeheader.git
cd makeheader
```

**Run it.** Execute the script from the directory where you want the target file to be created or edited.

```bash
python3 makeheader.py   # Mac/Linux
python makeheader.py    # Windows
```

**Run it as a command (alias).** So you can type `makeheader` from any folder instead of `python3 makeheader.py`:

1. **Make the script executable.** In the terminal, go to the makeheader folder and run:
   ```bash
   chmod +x makeheader.py
   ```

2. **Find the path to that folder.** While you're still in the makeheader folder, run:
   ```bash
   pwd
   ```
   Copy the path it prints (e.g. `/Users/you/makeheader` or `/Users/you/projects/makeheader`). You'll use it in the next step.

3. **Choose the right config file.** Your shell reads one of these when the terminal starts:
   - **`.zshrc`** — used by Zsh (default on macOS and some Linux setups). Check with: `echo $SHELL` — if it prints `/bin/zsh`, use `.zshrc`.
   - **`.bashrc`** — used by Bash (common on Linux, older Macs). If `echo $SHELL` prints `/bin/bash`, use `.bashrc`.

   Open that file in any editor (e.g. `nano ~/.zshrc` or `code ~/.zshrc` if you use VS Code).

4. **Add one line** at the end of the file. Replace `YOUR_PATH_FROM_STEP_2` with the path you copied (include the full path to the folder that contains `makeheader.py`):
   ```bash
   alias makeheader='python3 YOUR_PATH_FROM_STEP_2/makeheader.py'
   ```
   Example, if `pwd` was `/Users/jane/projects/makeheader`:
   ```bash
   alias makeheader='python3 /Users/jane/projects/makeheader/makeheader.py'
   ```
   Save and close the file.

5. **Load the change.** Run one of these so the alias works in this terminal session (use the same file you edited):
   ```bash
   source ~/.zshrc
   ```
   or
   ```bash
   source ~/.bashrc
   ```
   New terminal windows will pick it up automatically.

After that, you can `cd` to any project folder and run `makeheader`; no need to type `python3` or the path to the script.

From whatever folder or location you want, run the script, then enter the filename (e.g. `main.cpp` or `script.py`) then paste the problem description (blank line when done). If the file already exists, you can overwrite the header or append it above the existing code.

**Quit.** At any prompt, type `q`, `quit`, or `exit` to exit without writing anything.

**Example.** You paste a problem description like:

```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
```

The script writes it as the file header:

```cpp
/*
 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
*/
```

Run it from the directory that contains (or should contain) the file so paths stay simple.

Possible later additions: comment style by language, problem title extraction, CLI packaging For now it’s single-file, interactive only.

License: MIT.
