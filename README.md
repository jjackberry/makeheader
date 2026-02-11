# makeheader

Turns a coding problem description into a **C++ block comment** header. Copy the problem text (from LeetCode, an assignment, a PDF, etc.), run makeheader, paste it when prompted, and it gets written as a `/* ... */` comment at the top of your source file. **Output is C++ style only.** No dependencies.

**Requirements.** Python 3. Check with `python3 --version` (Mac/Linux) or `python --version` (Windows). If it’s not installed: [python.org](https://www.python.org/downloads/).

**Install.**

```bash
git clone https://github.com/jjackberry/makeheader.git
cd makeheader
```

**Run it.** From the directory where you want the file created or edited:

```bash
python3 makeheader.py   # Mac / Linux
python makeheader.py    # Windows
```

You’ll be asked for the filename (e.g. `main.cpp`) and then to paste the problem description; when you’re done pasting, press **Ctrl+D** (Mac/Linux) or **Ctrl+Z** then Enter (Windows). If the file exists, choose to overwrite the header or append it above the code. Type `q`, `quit`, or `exit` at any prompt to cancel without writing.

For **.cpp** files, makeheader adds `#include "packages.h"` right after the header. If `packages.h` isn’t in the same directory, it creates one with the necessary packages (vector, string, algorithm, etc.); if it already exists, it’s left unchanged. Your .cpp stays clean with a single include.

---

### Run as a command (alias) — use `makeheader` from any folder

Set up once so you can type `makeheader` from anywhere instead of `python3 makeheader.py`.

**Mac / Linux (Zsh or Bash)**

1. In the makeheader folder, run: `chmod +x makeheader.py`
2. Get the folder path: run `pwd` and copy the path (e.g. `/Users/you/projects/makeheader`).
3. See which shell you use: run `echo $SHELL`. If it prints `/bin/zsh`, you’ll edit `~/.zshrc`; if `/bin/bash`, you’ll edit `~/.bashrc`.
4. Open that file in an editor and add the alias line at the **end** of the file (use your path from step 2 in place of `/path/to/makeheader`):

   ```bash
   alias makeheader='python3 /path/to/makeheader/makeheader.py'
   ```

   **Option A — VS Code:** Run `code ~/.zshrc` (or `code ~/.bashrc`). The file opens in your editor. Scroll to the bottom, add the line above, save (Cmd+S), and close.

   **Option B — Nano (terminal editor):** Run `nano ~/.zshrc` (or `nano ~/.bashrc`). You’ll see the file content. Use the arrow keys to go to the very bottom. Type the alias line (paste your real path). To save: press **Ctrl+O**, then **Enter**. To exit: press **Ctrl+X**.
5. Reload the config: run `source ~/.zshrc` or `source ~/.bashrc`. New terminals will pick it up automatically.

**Windows (PowerShell)**

1. Get the full path to the makeheader folder (e.g. `C:\Users\You\projects\makeheader`). In PowerShell you can `cd` there and run `pwd` to see it.
2. Open your PowerShell profile in an editor. If the file doesn’t exist, create it:

   ```powershell
   notepad $PROFILE
   ```

   If you get an error that the path doesn’t exist, run: `New-Item -Path $PROFILE -ItemType File -Force`, then open it again.
3. Add this line (use your path from step 1; use forward slashes or escaped backslashes):

   ```powershell
   function makeheader { python "$env:USERPROFILE\projects\makeheader\makeheader.py" }
   ```

   Example if your path is `C:\Users\Jane\makeheader`:

   ```powershell
   function makeheader { python "C:/Users/Jane/makeheader/makeheader.py" }
   ```

4. Save and close. Reload the profile: `. $PROFILE` (or open a new PowerShell window).

**Windows (Command Prompt)**

Add the folder that contains `makeheader.py` to your system PATH, then from any directory you can run:

```bat
python makeheader.py
```

To add to PATH: Settings → System → About → Advanced system settings → Environment Variables → under “User variables” select Path → Edit → New → paste the makeheader folder path → OK. You can’t easily get a one-word `makeheader` command in cmd; use PowerShell or Git Bash for that.

---

**Example.** You can just paste like a massive problem description and it will work. but here's easy example:
```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
```

The script writes this C++ block comment at the top of your file:

```cpp
/*
 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
*/
```

Run makeheader from the directory that contains (or will contain) your file. 
License: MIT.