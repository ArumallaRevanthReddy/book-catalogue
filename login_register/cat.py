import csv

def writer(header, data, filename):
  with open (filename, "w", encoding="utf8") as csvfile:
    movies = csv.writer(csvfile)
    movies.writerow(header)
    for x in data:
      movies.writerow(x)

def updater():
    filename = "E:\\Mg-alloy(copy).csv"
    data = csv.reader(open(filename), delimiter=',')
    header = next(data)
    updated_data = []
    for row in data:
        if row[0]==0 or row[1]!=0 or row[3]==0 or row[4]==0 or row[9]==0:
            # if row[2]==0 and row[5]==0 and row[6]==0 and row[7]==0 and row[8]==0 and row[10]==0 and row[11]==0 and row[12]==0 and row[13]==0 and row[14]==0 and row[15]==0 and row[16]==0 and row[18]==0 and row[19]==0 and row[20]==0 and row[21]==0 and row[22]==0 and row[23]==0:
            #     row.append(1)
            # else:
            #     row.append(0)
            row.append(0)
        else:
            row.append(1)
        updated_data.append(row)

    writer(header, updated_data, filename)

if __name__=="__main__":
    updater()
