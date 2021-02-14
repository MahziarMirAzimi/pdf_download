from os import mkdir
from persiantools.jdatetime import JalaliDate
day = JalaliDate.to_jalali(2021, 2, 14)

mkdir(rf'C:\Users\MAHZIAR\Downloads\{str(day.year)[-2:]} {day.month} {day.day}')

