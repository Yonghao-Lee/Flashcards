# Python Flashcard Application

A command-line flashcard application developed in Python, based on the JetBrains Academy "Flashcards (Python)" project. This application allows users to create, manage, test, and refine their knowledge using custom flashcards. It's a practical tool for memorizing vocabulary, concepts, or any paired data.

## Features

* **Create & Add:** Add new flashcards with unique terms and definitions.
* **Test Knowledge:** Quiz yourself on the flashcards; the application prompts with a term and checks your definition input.
* **Remove Cards:** Delete flashcards you no longer need.
* **Import/Export:**
    * Save your current flashcard deck to a file.
    * Load flashcards from a previously saved file.
    * Import/Export can also be managed via command-line arguments upon starting/exiting the application.
* **Statistics:** Tracks incorrect answers to identify the "hardest" cards (those answered incorrectly most often).
* **Error Handling:** Prevents duplicate terms and handles potential file I/O issues.
* **Menu Driven:** Simple text-based menu for easy navigation and operation.

## How to Run

1.  Ensure you have Python 3.x installed.
2.  Navigate to the project directory in your terminal.
3.  Run the main script (assuming it's named `flashcards.py` or similar):
    ```bash
    python flashcards.py
    ```
4.  Follow the on-screen menu prompts.

### Command-Line Arguments

You can optionally import a card set file when starting the application or export the current set when exiting using command-line arguments:

* **Import:** Load cards from `input.txt` at the start:
    ```bash
    python flashcards.py --import input.txt
    ```
* **Export:** Save cards to `output.txt` upon exiting:
    ```bash
    python flashcards.py --export output.txt
    ```
* **Both:** Import from `input.txt` and export to `output.txt`:
    ```bash
    python flashcards.py --import input.txt --export output.txt
    ```

## Project Context

This project was developed as part of the JetBrains Academy Python Developer track, covering fundamental concepts like:

* Basic I/O and data types
* Conditional logic and loops
* Data structures (specifically Dictionaries/Hashtables for card storage)
* File handling (reading and writing)
* Exception handling
* Command-line arguments (`argparse`)
* Code style (PEP 8)

It serves as a practical application demonstrating core Python skills and is suitable for inclusion in a developer portfolio.

## Acknowledgements

Based on the "Flashcards (Python)" project provided by JetBrains Academy.

---

*(Optional: Add a License section here if you choose to include one, e.g., MIT License)*
