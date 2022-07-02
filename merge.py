import csv
import pandas as pd
with open('c141.csv') as f :
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]
    headers=data[0]
headers.append('poster_link')

with open("c142.csv","a+")as f:
    csvwriter=csv.write(f)
    csvwriter.writenow(headers)

with open("c142.csv")as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies_links=data[1:]

for movies_item in all_movies:
    poster_found=any(movies_item[8]in movies_link_item for movies_link_item in all_movies_links)
    if poster_found:
        for movies_link_item in all_movies_links:
            if movies_item[8]==movie_link_item[0]:
                movies_item.append(movie_link_item[1])
                if len(movies_item)==28:
                    with open("final.csv","a+") as f:
                        csvwriter=csv.writer(f)
                        csvwriter.writenow(movies_item)

            

            
