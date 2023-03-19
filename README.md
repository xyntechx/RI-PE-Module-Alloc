# Auto Module Allocator
The script to automate PE module allocations

## Usage
- Clone this repository
```bash
https://github.com/xyntechx/RI-PE-Module-Alloc.git
```

- CD into your local copy of this repository

- Create a Python virtual environment
```bash
python3 -m venv .venv
```

- Activate the virtual environment
```bash
source .venv/bin/activate
```

- Install the required packages
```bash
pip install -r requirements.txt
```

- Place the input excel sheets for each timeslot into `/inputs` (name each file \<timeslot>.xlsx; refer to the [list of timeslots](#list-of-timeslots))

- Run `main.py` for each timeslot (refer to the [list of timeslots](#list-of-timeslots))
```bash
python3 main.py <timeslot>
```

- View the generated module allocations in `/outputs`

## List of Timeslots
Choose one of the following to replace \<timeslot> (e.g. `mon0825.xlsx`, `python3 main.py mon0825`):

- mon0825
- mon0920
- mon1015
- tues0825
- tues0920
- tues1015
- thurs0825
- thurs0920
- fri0825
- fri0920
- fri1015
