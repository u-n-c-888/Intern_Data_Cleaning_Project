import pandas as pd

data = {
    "Customer_ID":[1,2,3,4,4,5],
    "Name":["John","Alice","Bob","Sara","Sara","David"],
    "Gender":["M","Female","male","F","F","Male"],
    "Date_of_Birth":["1998-05-12","1995-08-20","2000-03-11","1997-07-25","1997-07-25","1993-01-18"],
    "City":["New York","Chicago",None,"Los Angeles","Los Angeles","Houston"],
    "Join_Date":["2022-01-10","2021-06-15","2023-02-01","2020-09-12","2020-09-12","2021-12-01"],
    "Purchase_Amount":[2500,5000,1200,7000,7000,15000],
    "Email":["john@gmail.com","alice@gmail.com",None,"sara@gmail.com","sara@gmail.com","david@gmail.com"]
}

df = pd.DataFrame(data)

df.to_csv("customer_data.csv", index=False)

print("Dataset created successfully!")
