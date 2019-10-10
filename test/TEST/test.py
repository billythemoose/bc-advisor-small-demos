#coding:UTF-8
import requests
import csv
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup
import json  

def get_Content(url,data=None):
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    
    timeout = random.choice(range(80, 180))
    while True:
        
        try:
            rep = requests.get(url,headers = header,timeout = timeout)
            rep.encoding = 'utf-8'
            # req = urllib.request.Request(url, data, header)
            # response = urllib.request.urlopen(req, timeout=timeout)
            # html1 = response.read().decode('UTF-8', errors='ignore')
            # response.close()
            break
        # except urllib.request.HTTPError as e:
        #         print( '1:', e)
        #         time.sleep(random.choice(range(5, 10)))
        #
        # except urllib.request.URLError as e:
        #     print( '2:', e)
        #     time.sleep(random.choice(range(5, 10)))
        except socket.timeout as e:
            print( '3:', e)
            time.sleep(random.choice(range(8,15)))

        except socket.error as e:
            print( '4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print( '5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print( '6:', e)
            time.sleep(random.choice(range(5, 15)))

    return rep.text

def get_data(html_text):
    final = [];
    bs = BeautifulSoup(html_text,"html.parser");
    body = bs.find(id='content').select('ul li')
    allC = {};
    i=1;
    for piece in body:
        pieceString = piece.get_text();
        pieceString = pieceString.replace('\r','').replace('\n','').replace('\t','');
        #allC.append(pieceString); for list allC
        allC[i] = pieceString;
        i = i+1;
    return allC;


def write_data(data,name):
    file_name = name
    with open(file_name,'a',errors='ignore',newline='') as f:
        f_csv = csv.writer(f);
        f_csv.writerow(data);

def write_data_json(data,name):
    file_name = name;
    with open(file_name, 'w') as f:
        json.dump(data,f);
        #print(data);



if __name__ == '__main__':
    url = "https://www2.bellevuecollege.edu/classes/Fall2019"
    html = get_Content(url);
    result = get_data(html);
    #write_data(result,'classes.csv');
    write_data_json(result,'classes.json')