import csv_to_sqlite

# all the usual options are supported
options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250") 
input_files = ["Događanje.csv", "Kategorija.csv", "Lokacije.csv", "Momčadi.csv", "Officials.csv", "Sport.csv", "Statistics.csv", "Tournaments.csv"] # pass in a list of CSV files
csv_to_sqlite.write_csv(input_files, "output.db", options)