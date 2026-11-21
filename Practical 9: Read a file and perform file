# Practical 9: Read a file and perform file operations
from pathlib import Path
from collections import Counter

input_file = Path("input.txt")

if not input_file.exists():
    input_file.write_text(
        "Python is easy to learn.\n"
        "File handling is useful.\n"
        "This is the third line.\n",
        encoding="utf-8"
    )
    print("Sample input.txt created.")

content = input_file.read_text(encoding="utf-8")
lines = content.splitlines()
words = content.split()

print("Total characters:", len(content))
print("Total words:", len(words))
print("Total lines:", len(lines))

# Count every character, including spaces and newline characters.
frequency = dict(Counter(content))
print("Character frequency:")
for character, count in frequency.items():
    display_character = repr(character)
    print(display_character, ":", count)

print("Words in reverse order:")
print(" ".join(reversed(words)))

# Copy even-numbered lines to File1.txt and odd-numbered lines to File2.txt.
# Line numbering starts from 1.
even_lines = [line for line_number, line in enumerate(lines, start=1)
              if line_number % 2 == 0]
odd_lines = [line for line_number, line in enumerate(lines, start=1)
             if line_number % 2 != 0]

Path("File1.txt").write_text(
    "\\n".join(even_lines) + ("\\n" if even_lines else ""),
    encoding="utf-8"
)
Path("File2.txt").write_text(
    "\\n".join(odd_lines) + ("\\n" if odd_lines else ""),
    encoding="utf-8"
)

print("Even-numbered lines copied to File1.txt.")
print("Odd-numbered lines copied to File2.txt.")
