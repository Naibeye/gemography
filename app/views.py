from . import  app
from flask import jsonify
from datetime import date
import datetime
import requests
"""
    hello
"""
@app.route('/getlanguage', methods=['GET'])
def getlanguage():
    dateToday=date.today()- datetime.timedelta(days=30)
    stringDateToday=dateToday.strftime("%Y-%m-%d")
    totalRespo=0
    page=1
    listeLanguage=[]
    while(totalRespo<100):
        url="https://api.github.com/search/repositories?q=created:>{0}&sort=stars&order=desc&per_page=100&page={1}".format(stringDateToday, page)
        reqResponse=requests.get(url).json()
        data100=reqResponse['items']
        for item in data100:
            language={}
            if item['language']!=None and item['private']!=True and totalRespo<100:
                itemExistListe=[e for e in listeLanguage if e['name']==item['language']]
                if len(itemExistListe)==0 :
                    language['name']=item['language']
                    data100.remove(item)
                    language['listeRepos']=[item]
                    totalRespo+=1
                    for element in data100:
                        if (item['language']==element['language']) and (totalRespo<100):
                            language['listeRepos'].append(element)
                            data100.remove(element)
                            totalRespo+=1
                    language['numberRepos']=len(language['listeRepos'])
                    listeLanguage.append(language)
                else:
                    elementExist=itemExistListe[0]
                    indexElementExist=listeLanguage.index(elementExist)
                    data100.remove(item)
                    elementExist['listeRepos'].append(item) 
                    totalRespo+=1
                    for element in data100:
                        if (elementExist['name']==element['language']) and (totalRespo<100):
                            elementExist['listeRepos'].append(element)
                            totalRespo+=1
                            data100.remove(element)
                        else:
                            pass
                    elementExist['numberRepos']=len(elementExist['listeRepos'])
                    listeLanguage[indexElementExist]=elementExist
        page+=page
    return jsonify({'message': "succes", 'data': listeLanguage})
@app.route('/ping')
def pingpong():
    return 'pong'