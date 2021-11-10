from bs4 import BeautifulSoup

with open("/Users/marc/Documents/Development/bank_scraping/chequing_html", 'r') as file:
  chequing = file.read()

soup = BeautifulSoup(chequing, 'html.parser')

transactionsList = soup.find_all('tr', class_='rbc-transaction-list-transaction-new')

with open('/Users/marc/Documents/Development/bank_scraping/transactions', 'w') as file:
  for transaction in transactionsList:
    file.write(transaction.text + "\n")