import datetime
import pandas as pd
import os

class Record :
    def __init__(self):
        self.database = None
        self.check_file()
        self.append_files()

    def check_file(self):
        if not os.path.exists('./files'):
            os.makedirs('./files')
        return
        
    def append_files(self):
        files = []
        if len (os.listdir('./files')) < 1 :
            return files
        for filename in os.listdir('./files'):
            print(filename)
            f = os.path.join('./files', filename)
            print(f)
            if f.endswith('.csv') and os.path.isfile(f) and os.stat(f).st_size != 0:        
                try :
                    df = pd.read_csv(f,skiprows=1,header=None)
                    df['Date']=filename.split(".")[0]
                    files.append(df)
                except:
                    continue
        if len(files) > 0 :        
            df = pd.concat(files,ignore_index=True)
            df.columns = ['Name', 'Email', 'Mobile number', 'Address', 'Time','Date']
            self.database = df
            print(self.database)
        else:
            print("No Data stored !")
            self.database = None
            
    def add(self, name, email, phone, address):
        data = {
            "Name" : name,
            "Email" : email,
            "Mobile number" : phone,
            "Address" : address,
            "Time" : datetime.datetime.now().strftime("%X"),
        }
        today = str(datetime.date.today()).replace("-", "_")
        try:
            self.database[self.database["Name"]==data['Name']]
            print("Duplicated Name")
            input("Press Enter to continue...")
        except:
            file_path=f"./files/{today}.csv"
            df = pd.DataFrame(data, index=[0])
            if os.path.isfile(file_path):
                df.to_csv(file_path, mode='a', header=False, index=False)
            else:
                df.to_csv(file_path, mode='a', header=True, index=False)
            self.append_files()
        
    def get_file(self, name):
        try:
            file_date = self.database[self.database.Name == name].Date.to_string(index=False)
            file_path = f"./files/{file_date}.csv"
            df_search = pd.read_csv(file_path)
            return df_search,file_path
        except:
            print("Name not found!")
            return 1,1
    
    def update(self, name, phone):
        df_search,file_path = self.get_file(name)
        if type(df_search) != int :
            df_search.loc[df_search['Name'] == name, 'Mobile number'] = str(phone)
            df_search.to_csv(file_path, mode='w+', header=True, index=False)
            self.append_files()
    
    def delete(self,name):
        df_search,file_path = self.get_file(name)
        if type(df_search) != int :
            df_search = df_search.drop(df_search[df_search['Name'] == name].index)
            df_search.to_csv(file_path, mode='w+', header=True, index=False)
            self.append_files()
        
    def list(self):
        print(self.database)
        input("Press Enter to continue...")

        
        

