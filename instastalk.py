import requests
import json
import csv
import os.path
import pandas as pd
from os import path
from bs4 import BeautifulSoup


def get_info(username):
    url = 'https://www.instagram.com/' + str(username) +'/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    profile_info = json.loads(soup.find('script', type='application/ld+json').text)
    
    name = json.loads(soup.find('script', type='application/ld+json').text)['name'].strip('\n')
    bio = json.loads(soup.find('script', type='application/ld+json').text)['description'].strip('\n')

    return bio

def create_csv():
    if not path.exists('profiles.csv'):
        file = open('profiles.csv', 'w', newline='') 
            
        file.close()

def add_user(username):
    info = list(get_info(username))
    for i in range(len(info)):
        if info[i] == '\n':
            info[i] = ' *** '
    info = ''.join(info)
    
    
    with open('profiles.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        
        writer.writerow([str(username)] + [str(info)])
        
    return(True,"Profile has been added to watchlist")

def remove_user(username):
    return(True,"Feature has not been implemented")
    
        
def check_list():
    with open('profiles.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            new = list(get_info(row[0]))
            for i in range(len(new)):
                if new[i] == '\n':
                    new[i] = ' *** '
            new = ''.join(new)
            
            if str(row[1]) != str(new):
                print("{}'s bio has changed".format(row[0]))
                print("Old bio:", row[1])
                print("New bio:", new + "\n")
                
    return(True, "No bio has changed since last check")
        
def view_watchlist():
    with open('profiles.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        index = 1
        for row in readCSV:
            print(index, row[0])
            index += 1
    
    return(False,'')

def main():
    print("What would you like to do?")
    
    while True:        
        print("\n1. add")
        print("2. remove")
        print("3. check")
        print("4. view watchlist")
        choice = input()
        
        create_csv()
        
        if choice == '1':
            username = input("Username please: ")
            re = add_user(username)
        elif choice == '2':
            username = input("Username please: ")
            re = remove_user(username)     
        elif choice == '3':
            re = check_list()
        elif choice == '4':
            re = view_watchlist()    
        else:
            break
            
        if re[0]:
            print(re[1])        



main()