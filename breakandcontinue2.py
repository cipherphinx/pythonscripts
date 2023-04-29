import random
"""
VACCINES = ["Moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca", "CoronaVac"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"*******TESTING VACCINE {vac}***********")
    
    if vac == LUCKY:
        print("#######################################")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("#######################################")
        print()
        break
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print()
"""

VACCINES = ["Moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca", "CoronaVac"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"*******TESTING VACCINE {vac}***********")
    
    if vac == LUCKY:
        print("#######################################")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("#######################################")
        print()
        continue
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print()

