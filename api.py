import flask
from flask import request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random, threading, webbrowser
import time
import datetime
from flask import jsonify
import asyncio
# from flask import Flask
# from flask.ext.redis import FlaskRedis
# from core import redis_store
# import redis
# from threading import Thread

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# redis_store = FlaskRedis(app)
# client = redis.Redis(host='172.16.15.68', port='6379')

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get('https://web.whatsapp.com/')
# driver.execute_script("window.open('https://api.whatsapp.com/send?phone=62817466939&text=tes')")

books = [
    {'status': 200,
     'response': 'Pesan Terkirim',
     'terkirim': 'sent',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},

]


@app.route('/api/hello', methods=['GET'])
def api_all():
    test = "hello world"
    # print (now.strftime("%Y-%m-%d %H:%M:%S"))
    respo = [
    {'status': 200,
     'response': 'Pesan Terkirim',
     'terkirim': time.strftime('%x %H:%M:%S')}
        ]
    print (time.strftime('%x %H:%M:%S'))
    return jsonify(respo)


@app.route('/api/v1/resources/otpwa', methods=['GET'])

def api_id():
    # client.set('api')
    driver.implicitly_wait(20)
    time.sleep(20)
    print("enter0")

    nomor  = request.args.get('nomor', None)
    pesan  = request.args.get('pesan', None)

    # tujuan = nomor
    # isi = pesan
    print(nomor)
    print(pesan)

    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
    # driver.get('https://api.whatsapp.com/send?phone={}&text={}'.format(nomor, pesan))
    driver.execute_script("window.open('https://api.whatsapp.com/send?phone={}&text={}'.format('nomor', 'pesan'))")
    # driver.execute_script("window.open('https://api.whatsapp.com/send?phone=62817466939&text=tes')")
    print("enter1")
    tekan = driver.find_element_by_xpath('//a[@id="action-button"]')
    tekan.click()
    driver.implicitly_wait(15)
    time.sleep(10)
    print("enter2")
    button = driver.find_element_by_class_name('_35EW6')
    driver.implicitly_wait(15)
    time.sleep(10)
    print("enter3")
    button.click()
    print("Succesfully sent")
    respo = [
    {'status': 200,
     'response': 'Pesan Terkirim',
     'terkirim': time.strftime('%x %H:%M:%S')}
    ]
    # client.get()
    print (time.strftime('%x %H:%M:%S'))
    return jsonify(respo)


app.run(host="0.0.0.0", threaded=True)
