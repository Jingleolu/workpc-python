# -*- coding: utf-8 -*-

height = float(input('身高为:  '))
weight = float(input('体重为: '))
bmi=weight/(height*height)
if bmi>32:
	print('过于肥胖')
elif bmi>28:
	print('肥胖')
elif bmi>25:
	print('过重')
elif bmi>18.5:
	print('正常')
else:
	print('过轻')
