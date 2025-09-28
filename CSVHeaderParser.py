
#09/28/2025

'''
Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

The first line of a CSV file contains headings separated by commas.
Remove any leading or trailing whitespace from each heading.
'''

#-------------------------------------------------------------------------------

def get_headings(csv):
    parts = csv.split(",")
    headings = []

    for part in parts:
        cleaned = part.strip()
        headings.append(cleaned)
        
    return headings


'''
1. get_headings("name,age,city") should return ["name", "age", "city"].
2. get_headings("first name,last name,phone") should return ["first name", "last name", "phone"].
3. get_headings("username , email , signup date ") should return ["username", "email", "signup date"].
'''