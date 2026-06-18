# Python Mini Projects 🐍

A collection of beginner-friendly Python mini projects to practice core programming concepts and build practical applications.

## 📋 Projects

### 1. **Calculator** 🧮
A simple command-line calculator that performs basic arithmetic operations.

**Features:**
- Addition, Subtraction, Multiplication, and Division
- Input validation to prevent division by zero

**How to Run:**
```bash
python calculator.py
```

**Usage:**
```
Enter 1st number: 10
Enter 2nd number: 5
Enter what you do: +
Output: 15
```

---

### 2. **Guess the Number** 🎯
A fun guessing game where the computer picks a random number and you try to guess it.

**Features:**
- Random number generation between 0-100
- Feedback on whether your guess is too high or too low
- Attempt counter to track how many tries it took

**How to Run:**
```bash
python GuessNumber.py
```

**Game Play:**
```
Enter number between 0 to 100: 50
Your guessing number is too high
Enter number between 0 to 100: 25
Your guessing number is too low
Enter number between 0 to 100: 37
You are win right num are: 37
Attempts: 3
```

---

### 3. **Student Grade Management** 📊
A data management system to add, update, delete, and view student grades.

**Features:**
- Add new student records with grades
- Update existing student grades
- Delete student records
- View all student data
- Uses dictionary for data storage

**How to Run:**
```bash
python Grade.py
```

**Menu Options:**
```
------ STUDENT GRADE MANAGEMENT ------
1. Add Student Data
2. Update Student Grade
3. Delete Student Data
4. View Student Data
5. Exit
```

---

### 4. **Password Manager** 🔐
A secure password manager that saves and retrieves passwords for different websites.

**Features:**
- Save passwords for websites
- View saved passwords
- Generate random strong passwords (12 characters with letters, numbers, and special characters)
- Persistent storage in `password.txt`

**How to Run:**
```bash
python Password_Gent.py
```

**Menu Options:**
```
---Password Manager---
1. Save Password
2. View Password
3. Generate Password
4. Exit
```

**Generated Password Example:**
```
Generated Password: aB3!@#xYz9-+
```

---

### 5. **Rock Paper Scissors** ✂️
A classic game where you compete against the computer.

**Features:**
- Play against the computer
- Computer makes random choices
- Determines winner for each round

**How to Run:**
```bash
python RockPaper.py
```

---

### 6. **Tic Tac Toe** ⭕❌
A two-player Tic Tac Toe game playable in the terminal.

**Features:**
- Interactive game board
- Turn-based gameplay
- Win detection
- Draw detection

**How to Run:**
```bash
python TicTac.py
```

---

### 7. **QR Code Generator** 📲
Generates QR codes for text or URLs.

**How to Run:**
```bash
python QR.py
```

---

### 8. **To-Do List** ✅
A simple task management application to add, view, and manage your to-do items.

**Features:**
- Add new tasks
- View all tasks
- Mark tasks as complete
- Delete tasks

**How to Run:**
```bash
python To-Do.py
```

---

### 9. **EMI Calculator** 💸
A small script to calculate the Equated Monthly Installment (EMI) for a loan given the principal, annual interest rate, and tenure.

**Features:**
- Calculates EMI using principal, annual interest rate, and tenure in years
- Displays monthly EMI and total payment

**How to Run:**
```bash
python emi_calculator.py
```

Added: 2026-06-18

---

## 🚀 Requirements

- Python 3.6 or higher
- No external dependencies for most projects (all use Python standard library)

For the QR Code generator, you may need to install:
```bash
pip install qrcode[pil]
```

## 📁 Project Structure

```
python-mini-projects/
├── calculator.py
├── emi_calculator.py
├── GuessNumber.py
├── Grade.py
├── Password_Gent.py
│   └── password.txt (generated after use)
├── RockPaper.py
├── TicTac.py
├── QR.py
├── To-Do.py
└── README.md
```

## 💡 Learning Outcomes

These projects help you practice:
- **Basic Python Syntax** - variables, data types, operators
- **Control Flow** - if/else statements, loops
- **Data Structures** - dictionaries, lists
- **Functions** - defining and calling functions
- **File Handling** - reading and writing files
- **Built-in Modules** - random, string, etc.
- **User Input/Output** - interactive console applications

## 🛠️ How to Use

1. **Clone or Download** this repository
2. **Navigate** to the project directory
3. **Run** any project using: `python filename.py`
4. **Follow** the on-screen prompts

## 📝 Notes

- All projects use the Python standard library for maximum compatibility
- Projects are designed for beginners and include comments for understanding
- Feel free to modify and extend these projects for learning purposes

## 👨‍💻 Author

[Shivam Singh](https://github.com/ShivamSingh1660)

## 📄 License

This project is open source and available for educational purposes.

---

**Happy Coding! 🎉**

Feel free to fork, contribute, or use these projects as learning material.
