import requests
from bs4 import BeautifulSoup
import random

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

username = input("Enter your username : ")
password = input("Enter your password : ")

url = "https://karsanj.net/login.php"

info = {
    "username": username,
    "password": password,
    "login": "+%D9%88%D8%B1%D9%88%D8%AF+%D8%A8%D9%87+%D8%B3%D8%A7%D9%85%D8%A7%D9%86%D9%87",
}

exam_list = "https://karsanj.net/eTest_exam_list.php"
with requests.Session() as session:
    session.post(url, data=info)
    r = session.get(exam_list)
    soup = BeautifulSoup(r.content, "html.parser")
    exam_pages_urls = soup.find("table", attrs={"id": "old_exams"})

    counter = 1

    for i in exam_pages_urls.find_all("a"):
        print("---------------\n")
        print(f"Downloading {ordinal(counter)} file ...")
        exam_page = session.get("https://karsanj.net/" + i.get("href"))
        p = BeautifulSoup(exam_page.content, "html.parser")
        pdf_url = "https://karsanj.net/" + (
            (p.find_all("a", href=True)[-3]).get("href")
        )
        pdf = session.get(pdf_url)
        with open(f"{random.randint(0,10000)}.pdf", "wb") as file:
            file.write(pdf.content)
        print(f"{ordinal(counter)} file downloaded")
        counter += 1
