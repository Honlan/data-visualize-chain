#!/usr/bin/env python
# coding:utf8

'''
	对已爬取的4589部电影进行清洗
	author: Honlan
	email: 493722771@qq.com
	date: 2015/09/16
'''

import json
import time
import random

inputFile = 'douban_movie_detail.txt'
fr = open(inputFile, 'r')
outputFile = 'douban_movie_clean.txt'
fw = open(outputFile, 'w')
fw.write('id^title^url^cover^rate^director^composer^actor^category^district^language^showtime^length^othername^description\n')

firstLine = True

count = 1

nameMap = {}
nameMap['阿富汗'] = 'Afghanistan'
nameMap['安哥拉'] = 'Angola'
nameMap['阿尔巴尼亚'] = 'Albania'
nameMap['阿联酋'] = 'United Arab Emirates'
nameMap['阿根廷'] = 'Argentina'
nameMap['亚美尼亚'] = 'Armenia'
nameMap['法属南半球和南极领地'] = 'French Southern and Antarctic Lands'
nameMap['澳大利亚'] = 'Australia'
nameMap['澳大利亚 Australia'] = 'Australia'
nameMap['奥地利'] = 'Austria'
nameMap['阿塞拜疆'] = 'Azerbaijan'
nameMap['布隆迪'] = 'Burundi'
nameMap['比利时'] = 'Belgium'
nameMap['贝宁'] = 'Benin'
nameMap['布基纳法索'] = 'Burkina Faso'
nameMap['孟加拉国'] = 'Bangladesh'
nameMap['保加利亚'] = 'Bulgaria'
nameMap['巴哈马'] = 'The Bahamas'
nameMap['巴哈马 Bahamas'] = 'The Bahamas'
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
nameMap['Canada'] = 'Canada'
nameMap['加拿大 Canada'] = 'Canada'
nameMap['瑞士'] = 'Switzerland'
nameMap['智利'] = 'Chile'
nameMap['中国'] = 'China'
nameMap['香港'] = 'China'
nameMap['台湾'] = 'China'
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
nameMap['捷克 Czech Republic'] = 'Czech Republic'
nameMap['捷克'] = 'Czech Republic'
nameMap['德国'] = 'Germany'
nameMap['西德'] = 'Germany'
nameMap['原西德'] = 'Germany'
nameMap['吉布提'] = 'Djibouti'
nameMap['丹麦'] = 'Denmark'
nameMap['丹麦 Denmark'] = 'Denmark'
nameMap['多明尼加共和国'] = 'Dominican Republic'
nameMap['阿尔及利亚'] = 'Algeria'
nameMap['阿尔及尼亚'] = 'Algeria'
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
nameMap['UK'] = 'United Kingdom'
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
nameMap['印度尼西亚'] = 'Indonesia'
nameMap['印度'] = 'India'
nameMap['爱尔兰'] = 'Ireland'
nameMap['伊朗'] = 'Iran'
nameMap['伊拉克'] = 'Iraq'
nameMap['冰岛'] = 'Iceland'
nameMap['冰島 Iceland'] = 'Iceland'
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
nameMap['苏联'] = 'Russia'
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
nameMap['捷克斯洛伐克'] = 'Slovakia'
nameMap['捷克斯洛伐克 Czechoslovakia'] = 'Slovakia'
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
nameMap['USA'] = 'United States of America'
nameMap['乌兹别克斯坦'] = 'Uzbekistan'
nameMap['委内瑞拉'] = 'Venezuela'
nameMap['越南'] = 'Vietnam'
nameMap['瓦努阿图'] = 'Vanuatu'
nameMap['西岸'] = 'West Bank'
nameMap['也门'] = 'Yemen'
nameMap['南非'] = 'South Africa'
nameMap['赞比亚'] = 'Zambia'
nameMap['津巴布韦'] = 'Zimbabwe'

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

	composer = line[6].split('/')
	temp = ''
	for item in composer:
		temp = temp + item.strip() + '/'
	composer = temp[:-1]

	actor = line[7].split('/')
	temp = ''
	for item in actor:
		temp = temp + item.strip() + '/'
	actor = temp[:-1]

	category = line[8].split('/')
	temp = ''
	for item in category:
		temp = temp + item.strip() + '/'
	category = temp[:-1]

	district = line[9].split('/')
	temp = ''
	for item in district:
		if not nameMap.has_key(item.strip()):
			continue
		temp = temp + nameMap[item.strip()] + '_' + item.strip() + '/'
	district = temp[:-1]
	if len(district) == 0:
		continue

	language = line[10].split('/')
	temp = ''
	for item in language:
		temp = temp + item.strip() + '/'
	language = temp[:-1]

	showtime = line[11].split('/')[0][:4]

	length = line[12].split('/')[0]
	length = length.strip()
	for x in xrange(0, len(length)-1):
		if length[x].isdigit():
			continue
		else:
			length = length[:x]
			break

	othername = line[13].split('/')
	temp = ''
	for item in othername:
		temp = temp + item.strip() + '/'
	othername = temp[:-1]

	description = line[14].split('\t')
	temp = ''
	for item in description:
		item = item.strip().strip('\t')
		if not item == '':
			temp = temp + item + '/'
	description = temp[:-1]

	record = movieId + '^' + title + '^' + url + '^' + cover + '^' + rate + '^' + director + '^' + composer + '^' + actor + '^' + category + '^' + district + '^' + language + '^' + showtime + '^' + length + '^' + othername + '^' + description + '\n'
	fw.write(record)

	print count,title
	count = count + 1

fr.close()
fw.close()