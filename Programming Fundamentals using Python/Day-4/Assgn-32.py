#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    speciality_dict = {'P': 0, 'O': 0, 'E' : 0}
    for i in range(1, len(patient_medical_speciality_list), 2):
        speciality_dict[patient_medical_speciality_list[i]] += 1 
    maximum = 0 
    for key in speciality_dict.keys():
        if speciality_dict[key] > maximum:
            maximum = speciality_dict[key]
            speciality = key
    speciality = medical_speciality[speciality]
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
