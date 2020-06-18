import pandas as pd

def csvtojson():
<<<<<<< HEAD
    csv_file = pd.DataFrame(pd.read_csv("tmdb_movies_data.csv", sep = ",", header = 0, index_col = False))
    csv_file.to_json("movie.json", indent=2 ,orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
=======
    csv_file = pd.DataFrame(pd.read_csv("tmdb_movies_data.csv", sep=",", header=0, index_col=False))
    csv_file.to_json("tmdb_movie.json", indent=2, orient="records", date_format="epoch", double_precision=10,force_ascii=True, date_unit="ms", default_handler=None)



>>>>>>> origin
