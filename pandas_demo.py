import pandas as pd 
  
dict = { "Name":["Pankaj", "Aparna", "Sudhir", "Geeku"], 
        "Degree": ["MBA", "BCA", "M.Tech", "MBA"], 
        "Score":[90, 40, 80, 98] } 
  
df = pd.DataFrame(dict) 
  
print(df)
