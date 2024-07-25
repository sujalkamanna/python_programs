#Number Plate Genetator 
import random

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
letters = "abcdefghijklmnopqrstuvwxyz"

print('''List of Districts and their RTO Codes:
Mumbai (City): MH-01
Mumbai (Western Suburbs): MH-02
Mumbai (Eastern Suburbs): MH-03
Thane: MH-04
Kalyan: MH-05
Raigad: MH-06
Sindhudurg: MH-07
Ratnagiri: MH-08
Kolhapur: MH-09
Sangli: MH-10
Satara: MH-11
Pune: MH-12
Solapur: MH-13
Pimpri-Chinchwad: MH-14
Nashik: MH-15
Ahmednagar: MH-16
Shrirampur: MH-17
Dhule: MH-18
Jalgaon: MH-19
Aurangabad: MH-20
Jalna: MH-21
Parbhani: MH-22
Beed: MH-23
Latur: MH-24
Osmanabad: MH-25
Nanded: MH-26
Amravati: MH-27
Buldhana: MH-28
Yavatmal: MH-29
Akola: MH-30
Nagpur: MH-31
Wardha: MH-32
Gadchiroli: MH-33
Chandrapur: MH-34
Gondia: MH-35
Bhandara: MH-36
Washim: MH-37
Hingoli: MH-38
Nandurbar: MH-39
Wadi: MH-40
Malegaon: MH-41
Baramati: MH-42
Navi Mumbai: MH-43
Panvel: MH-46
Nagpur East: MH-49
Karad: MH-50
''')

districts = input("Enter district number (e.g., 12 for Pune): ").strip()

# Mapping of districts to their corresponding RTO codes
rto_codes = {
    "Mumbai (City)": "MH-01",
    "Mumbai (Western Suburbs)": "MH-02",
    "Mumbai (Eastern Suburbs)": "MH-03",
    "Thane": "MH-04",
    "Kalyan": "MH-05",
    "Raigad": "MH-06",
    "Sindhudurg": "MH-07",
    "Ratnagiri": "MH-08",
    "Kolhapur": "MH-09",
    "Sangli": "MH-10",
    "Satara": "MH-11",
    "Pune": "MH-12",
    "Solapur": "MH-13",
    "Pimpri-Chinchwad": "MH-14",
    "Nashik": "MH-15",
    "Ahmednagar": "MH-16",
    "Shrirampur": "MH-17",
    "Dhule": "MH-18",
    "Jalgaon": "MH-19",
    "Aurangabad": "MH-20",
    "Jalna": "MH-21",
    "Parbhani": "MH-22",
    "Beed": "MH-23",
    "Latur": "MH-24",
    "Osmanabad": "MH-25",
    "Nanded": "MH-26",
    "Amravati": "MH-27",
    "Buldhana": "MH-28",
    "Yavatmal": "MH-29",
    "Akola": "MH-30",
    "Nagpur": "MH-31",
    "Wardha": "MH-32",
    "Gadchiroli": "MH-33",
    "Chandrapur": "MH-34",
    "Gondia": "MH-35",
    "Bhandara": "MH-36",
    "Washim": "MH-37",
    "Hingoli": "MH-38",
    "Nandurbar": "MH-39",
    "Wadi": "MH-40",
    "Malegaon": "MH-41",
    "Baramati": "MH-42",
    "Navi Mumbai": "MH-43",
    "Panvel": "MH-46",
    "Nagpur East": "MH-49",
    "Karad": "MH-50"
}

# Create a reverse mapping from RTO code numbers to district names
reverse_rto_codes = {code.split('-')[1]: district for district, code in rto_codes.items()}

if districts in reverse_rto_codes:
    district_name = reverse_rto_codes[districts]
    district_code = rto_codes[district_name]
    
    letters1 = random.choice(letters).upper()
    letters2 = random.choice(letters).upper()

    numbers1 = random.choice(numbers)
    numbers2 = random.choice(numbers)
    numbers3 = random.choice(numbers)
    numbers4 = random.choice(numbers)

    format_code = f"{district_code}-{letters1}{letters2}-{numbers1}{numbers2}{numbers3}{numbers4}"
    print("Generated Number:", format_code)
else:
    print("District number not found in the list.")
    