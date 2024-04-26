#Creating Dataframe out of a Dictionary
import pandas as pd
song={'Album':['Thriller','Back in Black','The Dark side of The Moon','The Bodygurd','Bat out of Hell'],'Released':['1982','1980','1973','1992','1977'],'Length':['00:42:11','00:42:19','00:42:49','00:57:44','00:46:33']}
song_frame=pd.DataFrame(song)
print(song_frame)

#Creating csv File & Delete The Index
song_frame.to_csv('New_Song_csv_File_Without_Index.csv',index=False)