# Keywords arguments

def vac_feedback(vac="Sinovac", efficacy=20):
    print(f"{vac} Vaccine is having {efficacy} % efficacy.")
    
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effictive. Needs more trial.")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine.")
    elif (efficacy >= 90):
        print("Sure, will take the shot.")
    else:
        print("Needs many more trials.")
        
vac_feedback("Pzizer", 95)
vac_feedback("Unknown", 45)
vac_feedback(efficacy=35, vac="Unknown")
#vac_feedback()
        