#!/usr/bin/env python
# coding:utf8

'''
	对清洗后的电影数据进行基本统计
	author: Honlan
	email: 493722771@qq.com
	date: 2015/09/20
'''

import json
import time
import random
import pprint
import MySQLdb
import MySQLdb.cursors

inputFile = 'douban_movie_clean.txt'
fr = open(inputFile, 'r')

db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='douban', port=8889, charset='utf8', cursorclass = MySQLdb.cursors.DictCursor)
db.autocommit(True)
cursor = db.cursor()

firstLine = True

nameMap = {}
nameMap['阿富汗'] = 'Afghanistan'
nameMap['安哥拉'] = 'Angola'
nameMap['阿尔巴尼亚'] = 'Albania'
nameMap['阿联酋'] = 'United Arab Emirates'
nameMap['阿根廷'] = 'Argentina'
nameMap['亚美尼亚'] = 'Armenia'
nameMap['法属南半球和南极领地'] = 'French Southern and Antarctic Lands'
nameMap['澳大利亚'] = 'Australia'
nameMap['奥地利'] = 'Austria'
nameMap['阿塞拜疆'] = 'Azerbaijan'
nameMap['布隆迪'] = 'Burundi'
nameMap['比利时'] = 'Belgium'
nameMap['贝宁'] = 'Benin'
nameMap['布基纳法索'] = 'Burkina Faso'
nameMap['孟加拉国'] = 'Bangladesh'
nameMap['保加利亚'] = 'Bulgaria'
nameMap['巴哈马'] = 'The Bahamas'
nameMap['波斯尼亚和黑塞哥维那'] = 'Bosnia and Herzegovina'
nameMap['白俄罗斯'] = 'Belarus'
nameMap['伯利兹'] = 'Belize'
nameMap['百慕大'] = 'Bermuda'
nameMap['玻利维亚'] = 'Bolivia'
nameMap['巴西'] = 'Brazil'
nameMap['文莱'] = 'Brunei'
nameMap['不丹'] = 'Bhutan'
nameMap['博茨瓦纳'] = 'Botswana'
nameMap['中非共和国'] = 'Central African Republic'
nameMap['加拿大'] = 'Canada'
nameMap['瑞士'] = 'Switzerland'
nameMap['智利'] = 'Chile'
nameMap['中国'] = 'China'
nameMap['中国大陆'] = 'China'
nameMap['象牙海岸'] = 'Ivory Coast'
nameMap['喀麦隆'] = 'Cameroon'
nameMap['刚果民主共和国'] = 'Democratic Republic of the Congo'
nameMap['刚果共和国'] = 'Republic of the Congo'
nameMap['哥伦比亚'] = 'Colombia'
nameMap['哥斯达黎加'] = 'Costa Rica'
nameMap['古巴'] = 'Cuba'
nameMap['北塞浦路斯'] = 'Northern Cyprus'
nameMap['塞浦路斯'] = 'Cyprus'
nameMap['捷克共和国'] = 'Czech Republic'
nameMap['德国'] = 'Germany'
nameMap['吉布提'] = 'Djibouti'
nameMap['丹麦'] = 'Denmark'
nameMap['多明尼加共和国'] = 'Dominican Republic'
nameMap['阿尔及利亚'] = 'Algeria'
nameMap['厄瓜多尔'] = 'Ecuador'
nameMap['埃及'] = 'Egypt'
nameMap['厄立特里亚'] = 'Eritrea'
nameMap['西班牙'] = 'Spain'
nameMap['爱沙尼亚'] = 'Estonia'
nameMap['埃塞俄比亚'] = 'Ethiopia'
nameMap['芬兰'] = 'Finland'
nameMap['斐济'] = 'Fiji'
nameMap['福克兰群岛'] = 'Falkland Islands'
nameMap['法国'] = 'France'
nameMap['加蓬'] = 'Gabon'
nameMap['英国'] = 'United Kingdom'
nameMap['格鲁吉亚'] = 'Georgia'
nameMap['加纳'] = 'Ghana'
nameMap['几内亚'] = 'Guinea'
nameMap['冈比亚'] = 'Gambia'
nameMap['几内亚比绍'] = 'Guinea Bissau'
nameMap['赤道几内亚'] = 'Equatorial Guinea'
nameMap['希腊'] = 'Greece'
nameMap['格陵兰'] = 'Greenland'
nameMap['危地马拉'] = 'Guatemala'
nameMap['法属圭亚那'] = 'French Guiana'
nameMap['圭亚那'] = 'Guyana'
nameMap['洪都拉斯'] = 'Honduras'
nameMap['克罗地亚'] = 'Croatia'
nameMap['海地'] = 'Haiti'
nameMap['匈牙利'] = 'Hungary'
nameMap['印尼'] = 'Indonesia'
nameMap['印度'] = 'India'
nameMap['爱尔兰'] = 'Ireland'
nameMap['伊朗'] = 'Iran'
nameMap['伊拉克'] = 'Iraq'
nameMap['冰岛'] = 'Iceland'
nameMap['以色列'] = 'Israel'
nameMap['意大利'] = 'Italy'
nameMap['牙买加'] = 'Jamaica'
nameMap['约旦'] = 'Jordan'
nameMap['日本'] = 'Japan'
nameMap['哈萨克斯坦'] = 'Kazakhstan'
nameMap['肯尼亚'] = 'Kenya'
nameMap['吉尔吉斯斯坦'] = 'Kyrgyzstan'
nameMap['柬埔寨'] = 'Cambodia'
nameMap['韩国'] = 'South Korea'
nameMap['科索沃'] = 'Kosovo'
nameMap['科威特'] = 'Kuwait'
nameMap['老挝'] = 'Laos'
nameMap['黎巴嫩'] = 'Lebanon'
nameMap['利比里亚'] = 'Liberia'
nameMap['利比亚'] = 'Libya'
nameMap['斯里兰卡'] = 'Sri Lanka'
nameMap['莱索托'] = 'Lesotho'
nameMap['立陶宛'] = 'Lithuania'
nameMap['卢森堡'] = 'Luxembourg'
nameMap['拉脱维亚'] = 'Latvia'
nameMap['摩洛哥'] = 'Morocco'
nameMap['摩尔多瓦'] = 'Moldova'
nameMap['马达加斯加'] = 'Madagascar'
nameMap['墨西哥'] = 'Mexico'
nameMap['马其顿'] = 'Macedonia'
nameMap['马里'] = 'Mali'
nameMap['缅甸'] = 'Myanmar'
nameMap['黑山'] = 'Montenegro'
nameMap['蒙古'] = 'Mongolia'
nameMap['莫桑比克'] = 'Mozambique'
nameMap['毛里塔尼亚'] = 'Mauritania'
nameMap['马拉维'] = 'Malawi'
nameMap['马来西亚'] = 'Malaysia'
nameMap['纳米比亚'] = 'Namibia'
nameMap['新喀里多尼亚'] = 'New Caledonia'
nameMap['尼日尔'] = 'Niger'
nameMap['尼日利亚'] = 'Nigeria'
nameMap['尼加拉瓜'] = 'Nicaragua'
nameMap['荷兰'] = 'Netherlands'
nameMap['挪威'] = 'Norway'
nameMap['尼泊尔'] = 'Nepal'
nameMap['新西兰'] = 'New Zealand'
nameMap['阿曼'] = 'Oman'
nameMap['巴基斯坦'] = 'Pakistan'
nameMap['巴拿马'] = 'Panama'
nameMap['秘鲁'] = 'Peru'
nameMap['菲律宾'] = 'Philippines'
nameMap['巴布亚新几内亚'] = 'Papua New Guinea'
nameMap['波兰'] = 'Poland'
nameMap['波多黎各'] = 'Puerto Rico'
nameMap['北朝鲜'] = 'North Korea'
nameMap['葡萄牙'] = 'Portugal'
nameMap['巴拉圭'] = 'Paraguay'
nameMap['卡塔尔'] = 'Qatar'
nameMap['罗马尼亚'] = 'Romania'
nameMap['俄罗斯'] = 'Russia'
nameMap['卢旺达'] = 'Rwanda'
nameMap['西撒哈拉'] = 'Western Sahara'
nameMap['沙特阿拉伯'] = 'Saudi Arabia'
nameMap['苏丹'] = 'Sudan'
nameMap['南苏丹'] = 'South Sudan'
nameMap['塞内加尔'] = 'Senegal'
nameMap['所罗门群岛'] = 'Solomon Islands'
nameMap['塞拉利昂'] = 'Sierra Leone'
nameMap['萨尔瓦多'] = 'El Salvador'
nameMap['索马里兰'] = 'Somaliland'
nameMap['索马里'] = 'Somalia'
nameMap['塞尔维亚共和国'] = 'Republic of Serbia'
nameMap['苏里南'] = 'Suriname'
nameMap['斯洛伐克'] = 'Slovakia'
nameMap['斯洛文尼亚'] = 'Slovenia'
nameMap['瑞典'] = 'Sweden'
nameMap['斯威士兰'] = 'Swaziland'
nameMap['叙利亚'] = 'Syria'
nameMap['乍得'] = 'Chad'
nameMap['多哥'] = 'Togo'
nameMap['泰国'] = 'Thailand'
nameMap['塔吉克斯坦'] = 'Tajikistan'
nameMap['土库曼斯坦'] = 'Turkmenistan'
nameMap['东帝汶'] = 'East Timor'
nameMap['特里尼达和多巴哥'] = 'Trinidad and Tobago'
nameMap['突尼斯'] = 'Tunisia'
nameMap['土耳其'] = 'Turkey'
nameMap['坦桑尼亚联合共和国'] = 'United Republic of Tanzania'
nameMap['乌干达'] = 'Uganda'
nameMap['乌克兰'] = 'Ukraine'
nameMap['乌拉圭'] = 'Uruguay'
nameMap['美国'] = 'United States of America'
nameMap['乌兹别克斯坦'] = 'Uzbekistan'
nameMap['委内瑞拉'] = 'Venezuela'
nameMap['越南'] = 'Vietnam'
nameMap['瓦努阿图'] = 'Vanuatu'
nameMap['西岸'] = 'West Bank'
nameMap['也门'] = 'Yemen'
nameMap['南非'] = 'South Africa'
nameMap['赞比亚'] = 'Zambia'
nameMap['津巴布韦'] = 'Zimbabwe'

categories = {}

districts = {}

languages = {}

showtimes = {}

lengths = {}

rates = {} 

combined = {}

for line in fr:
	if firstLine:
		firstLine = False
		continue

	line = line.split('^')

	# 统计各个区域各个分类的平均评分
	category = line[8].split('/')
	district = line[9].split('/')
	rate = float(line[4])
	for d in district:
		d = d.split('_')[0]
		if not combined.has_key(d):
			combined[d] = {}
		for c in category:
			if c == '':
				continue
			if not combined[d].has_key(c):
				combined[d][c] = {"average": 0.0, "count": 0.0}
			combined[d][c]["average"] = (combined[d][c]["average"] * combined[d][c]["count"] + rate) / (combined[d][c]["count"] + 1)
			combined[d][c]["count"] = combined[d][c]["count"] + 1

	if line[11] == '' or line[12] == '':
		continue

	# 分类统计
	category = line[8].split('/')
	for item in category:
		if item == '':
			continue
		if not categories.has_key(item):
			categories[item] = 1
		else:
			categories[item] = categories[item] + 1

	# 区域统计
	district = line[9].split('/')
	for item in district:
		item = item.split('_')[0]
		# for key in nameMap.keys():
			# if nameMap[key] == item:
				# item = key
				# break
		if item == '':
			continue
		if not districts.has_key(item):
			districts[item] = 1
		else:
			districts[item] = districts[item] + 1

	# 语言统计
	language = line[10].split('/')
	for item in language:
		if item == '':
			continue
		if not languages.has_key(item):
			languages[item] = 1
		else:
			languages[item] = languages[item] + 1

	# 上映时间统计
	showtime = line[11]
	if not showtime == '':
		if not showtimes.has_key(showtime):
			showtimes[showtime] = 1
		else:
			showtimes[showtime] = showtimes[showtime] + 1

	# 片长统计
	length = line[12]
	if not length == '':
		if not lengths.has_key(length):
			lengths[length] = 1
		else:
			lengths[length] = lengths[length] + 1

	# 评分统计
	rate = line[4]
	if not rate == '':
		if not rates.has_key(rate):
			rates[rate] = 1
		else:
			rates[rate] = rates[rate] + 1

# temp = ''
# categories = sorted(categories.items(), key=lambda x:x[1], reverse=True)
# for item in categories:
# 	temp = temp + "'" + item[0] + "',"
# print temp[:-1]


temp = {}
for key,value in combined.items():
	temp[key] = {}
	temp1 = ''
	temp2 = ''
	for k,v in value.items():
		temp1 = temp1 + k + ','
		temp2 = temp2 + '%.1f' % v['average'] + ','
	temp[key]['categories'] = temp1[:-1]
	temp[key]['rates'] = temp2[:-1]
	cursor.execute("insert into rate(name,categories,rates) values(%s,%s,%s)",[key,temp1[:-1],temp2[:-1]])
combined = temp

# pprint.pprint(combined)

fr.close()
db.close()
cursor.close()