import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

client = gspread.authorize(creds)

sheet = client.open('Altombo').sheet1

#  Access data
#print(sheet.get_all_records())

#sheet.insert_row(["matheus", "timppa", "allu"],4)