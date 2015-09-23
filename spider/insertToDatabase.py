#!/usr/bin/env python
# coding:utf8

'''
	将清洗的数据插入数据库
	author: Honlan
	email: 493722771@qq.com
	date: 2015/09/22
'''
import MySQLdb
import MySQLdb.cursors

inputFile = 'douban_movie_clean.txt'
fr = open(inputFile, 'r')

firstLine = True

db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='douban', port=8889, charset='utf8', cursorclass = MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

count = 0

for line in fr:
	if firstLine:
		firstLine = False
		continue

	line = line.split('^')

	movieId= line[0]
	title = line[1]
	url = line[2]
	cover = line[3]
	rate = line[4]
	director = line[5]
	composer = line[6]
	actor = line[7]
	category = line[8]
	district = line[9]
	language = line[10]
	showtime = line[11]
	length = line[12]
	othername = line[13]
	description = line[14]

	cursor.execute('insert into movie(movieId,title,url,cover,rate,director,composer,actor,category,district,language,showtime,length,othername,description) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[movieId,title,url,cover,rate,director,composer,actor,category,district,language,showtime,length,othername,description])

	count = count + 1
	print count, title

fr.close()
db.close()
cursor.close()