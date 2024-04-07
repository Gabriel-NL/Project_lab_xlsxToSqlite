import sqlite3
import openpyxl
 # Connect to SQLite database
database = sqlite3.connect('data.sqlite')
excel_file = "Producao por municipio (Formatada).xlsx"
sheet_name = "Produção_aquícola"

wb = openpyxl.load_workbook(excel_file)
sheet = wb[sheet_name]



