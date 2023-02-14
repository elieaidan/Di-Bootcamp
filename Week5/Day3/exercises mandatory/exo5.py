import datetime


today = datetime.date.today()
someday = datetime.date(2024, 1, 1)
diff = someday - today
jour = diff.days
print(jour)
