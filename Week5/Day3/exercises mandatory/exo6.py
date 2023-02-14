import datetime

today = datetime.date.today()
birthday = datetime.date(2002, 7, 22)
nombres_jour = today - birthday
nombres_jour_oflife = nombres_jour.days
print(f' Mister patate are living from {nombres_jour_oflife} day on her life ')