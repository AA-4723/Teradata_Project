import pandas as pd
import random
from datetime import datetime
from babel.dates import format_date


num_rows_to_generate = 1000000
output_filename = "date_data.csv"

def convert_to_eastern_arabic_numerals(text):
    western_to_eastern = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
    return text.translate(western_to_eastern)


def random_date(start_year=1970, end_year=2030):
    y = random.randint(start_year, end_year)
    m = random.randint(1, 12)
    d = random.randint(1, 28)
    return datetime(y, m, d)



english_formats = [
    "%d/%m/%y", "%m/%d/%y", "%y/%m/%d",
    "%d-%m-%y", "%m-%d-%y", "%y-%m-%d",
    "%d.%m.%y", "%m.%d.%y", "%d %m %y",
    "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d",
    "%d-%m-%Y", "%m-%d-%Y", "%Y-%m-%d",
    "%B %d, %Y", "%d %B %Y", "%b %d, %Y", "%d %b %Y",
    "%A, %B %d, %Y", "%a, %b %d, %Y", "%Y %B %d",
    "%Y", "%d/%b", "%b/%Y", "%d/%m", "%m/%Y"
]#all english formats available on Excel

#different arabic formats provided by
arabic_babel_formats = ["short", "medium", "long", "full"]


rows = []
all_formats = english_formats + arabic_babel_formats
for _ in range(num_rows_to_generate):

    dt = random_date()


    selected_format = random.choice(all_formats)

    if selected_format in english_formats:
        sample = dt.strftime(selected_format)
    else:
        sample = format_date(dt, format=selected_format, locale="ar_EG")
        sample = convert_to_eastern_arabic_numerals(sample)

    rows.append({"date": sample})


df = pd.DataFrame(rows)
df.to_csv(output_filename, index=False)
