#PF-Assgn-22
def find_leap_years(given_year):
    list_of_leap_years = list()
    # Write your logic here
    while True:
        if given_year%4==0 and given_year%100!=0 or given_year%400==0:
            given_year += 4 
            break
        given_year += 1 
    for _ in range(15):
        list_of_leap_years.append(given_year)
        given_year += 4 
    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
