from internship_sites.internshala import internships as list1
from csv import writer

data = list1

with open("scholarships.csv", 'w', newline='') as f:
    the_writer = writer(f)
    header = ['Internship Title', 'Internship Start Date', 'Internnship Duration', "Stipend", 'Link']
    the_writer.writerow(header)
    for item in data:
        print(f'Title : {item[0]}')
        print(f'Start Date : {item[1]}')
        print(f'DUration : {item[2]}')
        print(f'Stipend : {item[3]}')
        print(f'Link : {item[4]}')
        print("---------------------------------------------------------------------------------------------------------------------")
        info = [item[0], item[1], item[2], item[3], item[4]]
        the_writer.writerow(info)