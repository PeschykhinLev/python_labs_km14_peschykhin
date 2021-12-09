import csv
with open("Kanye_West.csv", "w", newline='') as file:
    song_info = ["Song", "Year"]
    writer = csv.DictWriter(file, fieldnames=song_info,)
    writer.writeheader()
    writer.writerow({"Song": "Mercy", 
                     "Year": "2012"})
    writer.writerow({"Song": "Black Skinhead", 
                     "Year": "2013"})
    writer.writerow({"Song": "Ni**as in Paris", 
                     "Year": "2011"})
    writer.writerow({"Song": "Run This Town", 
                     "Year": "2009"})
    writer.writerow({"Song": "Gold Digger", 
                     "Year": "2005"})
    writer.writerow({"Song": "All Mine", 
                     "Year": "2018"}) 



print('Starting to read CSV with songs\n')
with open('Kanye_West.csv', newline='') as file:
    reader = csv.DictReader(file)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n--------------------')
    for row in reader:
        print(row['Song'], row['Year'])
print('\nDone')                