from scholarships_sites.buddy4study import scholarships as list1
from scholarships_sites.wemakescholars import scholarships as list2
from csv import writer

data = list1+list2

with open("scholarships.csv", 'w', newline='') as f:
    the_writer = writer(f)
    header = ['Scholarship Title', 'Scholarship End Date', 'Scholarshp Applicable For', "Scholarship Rgistration Link", 'Scholarship Image Link']
    the_writer.writerow(header)
    for item in data:
        print(f'Title : {item[0]}')
        print(f'Last Date : {item[1]}')
        print(f'Applicable for : {item[2]}')
        print(f'Link : {item[3]}')
        print(f'Image Link : {item[4]}')
        print("---------------------------------------------------------------------------------------------------------------------")
        info = [item[0], item[1], item[2], item[3], item[4]]
        the_writer.writerow(info)