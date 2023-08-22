# Hypixel *Guess the Build* Tool
This tool helps the user collect and identify themes in *Guess the Build*, a subset of Hypixel's *Build Battle* game.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open Terminal in repository folder.
4. Enter ```python main.py```.

# Usage
This program has two functions, *appender* and *solver*.
*appender* appends themes to the text file *list.txt*.
*solver* deduces themes using *list.txt* as a theme database.

### Appender
To use *appender*, run *main.py* via ```python main.py``` in Terminal.
```Option:``` will print.
Enter ```a```.
```Theme:``` will print.
Enter the theme (non-case-sensitive).
If the theme is in *list.txt*, *appender* will not append the theme to *list.txt* and print ```Theme exists.```.
If the theme is not in *list.txt*, *appender* will append the theme to *list.txt* and print ```Theme does not exist; theme appended.```.

If the theme is misspelled, the user will need to manually open *list.txt* and delete the theme.
The most recently appended theme is the last line in *list.txt*.

To quit *appender*, enter ```q``` when ```Theme:``` prints.
To quit the code, enter ```q``` when ```Option:``` prints.

### Solver
To use *solver*, run *main.py* via ```python main.py``` in Terminal.
```Option:``` will print.
Enter ```s```.
```Characters:``` will print.
Enter the number of characters (letters including spaces) in the theme.
The number of characters must be an integer (1, 2, etc.).
A list of all possible themes will print.
This list will subsequently appear for all future interactions with *solver*.

After, ```Spaces:``` will print.
Enter the number of spaces (integer) in the theme.
Usually this value is 0, 1, or 2.
A new list of all possible themes will print.

After, ```Hint:``` will print.
Enter the place of the character followed by the character itself (non-case-sensitive).
The first character is 1, not 0.
A new list of all possible themes will print.

This loop will continue until broken by entering ```q``` when ```Hint:``` prints.
To quit *solver*, enter ```q``` when ```Characters:``` prints.
To quit the code, enter ```q``` when ```Option:``` prints.

# Examples
### Appender
Suppose the theme we want to append is **milky way**.
Run *main.py* via ```python main.py``` in Terminal.
When ```Option:``` prints, enter ```a``` for *appender*.
When ```Theme:``` prints, enter ```milky way```.
The code now loops, allowing the user to append multiple themes.

To return to *menu*, enter ```q``` when ```Theme:``` prints.
To quit the code, enter ```q``` when ```Option:``` prints.

### Solver
Suppose the theme (unbeknownst to the user) is **milky way**.
Run *main.py* via ```python main.py``` in Terminal.
When ```Option:``` prints, enter ```s``` for *solver*.
When ```Characters:``` prints, enter ```9``` as **milky way** has 9 characters.
When ```Spaces:``` prints, enter ```1``` as **milky way** has 1 space.

Since spaces are given, we know the 6th character.
When ```Hint:``` prints, enter ```6``` (6 followed by a space).
The code now loops, allowing the user to enter multiple hints.
Suppose the first hint given is **m** as the 1st character.
When ```Hint:``` prints, enter ```1m```.
Suppose the next hint given is **y** as the 5th character.
When ```Hint:``` prints, enter ```5y```.
This is enough information for the code to identify the theme as **milky way**.

The user need not completely rely on the code.
Cross-referencing builds with the code often enables the user to infer themes.

To return to the beginning of *solver*, enter ```q``` when ```Spaces:``` or ```Hint:``` prints.
To return to *menu*, enter ```q``` when ```Characters:```prints.
To quit the code, enter ```q``` when ```Option:``` prints.

# Errors

1. ```Invalid input. Enter 'a' to append, 's' to solve, or 'q' to quit.```
Solution: Type character (```a```, ```s```, or ```q```) to append, solve, or quit, respectively.
2. ```Invalid input. Enter integer or 'q' to quit.```
Solution: Type an integer (0, 1, 2, etc.) or ```q```.
3. ```Invalid input. Enter place and character or 'q' to quit.```
Solution: Type an integer (0, 1, 2, etc.) followed by a character (a, b, c, etc.) or ```q```.

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.
