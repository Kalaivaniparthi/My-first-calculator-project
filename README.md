# proj-1 calculator

A small Python calculator project with both a **CLI** (terminal) version and a **GUI** (Tkinter) version.

## Features
- Basic arithmetic: addition, subtraction, multiplication, division (CLI)
- Simple calculator GUI with buttons (GUI)

## CLI (terminal) calculator
Uses `calc/basic_calculator.py`.

Run:
```bash
python calc/basic_calculator.py
```

Then choose an operation from the menu (1-5).

## GUI calculator (Tkinter)
Uses `calc/gui_calculator.py`.

Run:
```bash
python calc/gui_calculator.py
```

A window will open with calculator buttons.

## Project structure
- `calc/basic_calculator.py` — CLI calculator
- `calc/gui_calculator.py` — GUI calculator

## Notes
The GUI implementation uses `eval()` to evaluate the entered expression.

