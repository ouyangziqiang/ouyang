#@Time   : 
#@Author :Tester_ouyang
# coding:utf-8
import allure
import pytest
import os
class TestClass:

	def func(self, x):
		return x + 3

	@allure.feature('test_02')
	def test_func_0(self):
		src = 0
		expect = 3
		assert self.func(src) == expect

	@allure.feature('test_03')
	def test_func_1(self):
		src = 0.1
		expect = 3.1
		assert self.func(src) == expect

	@allure.feature('test_04')
	def test_one(self):
		x = "hello"
		assert 'x' in x

	@allure.story('一个功能点')
	def test_func(self):
		src = -1
		expect = 2
		assert self.func(src) == expect

if __name__ =="__main__":
# 	pytest.main(['-s', 'pytest_01.py'])
	#pytest.main(['-r','-q','--alluredir','./report'])
	#os.system('allure generate ./report -o ./report/allure_report -c')
	pytest.main(['--alluredir=report'])
	os.system('allure generate report -o ../../allure-report --clean')