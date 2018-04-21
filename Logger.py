#coding=utf-8  
import logging
import logging.handlers
import os
#logDir=r"E:\taskTrain\taskTrainLog"  
class Logger():  
	def __init__(self, logName, modelName, logLevel, logger):  
		# 创建一个logger  
		self.logger = logging.getLogger(logger)
		self.logger.setLevel(logging.DEBUG)  

		# 创建一个handler，用于写入日志文件
		fh = logging.FileHandler(logName)  
		fh.setLevel(logLevel)  

		# 再创建一个handler，用于输出到控制台  
		ch = logging.StreamHandler()  
		ch.setLevel(logLevel)  

		# 定义handler的输出格式      
		log_format = logging.Formatter('%(message)s - %(asctime)s - %(name)s - %(levelname)s -[%(filename)s:%(lineno)d]')  
		fh.setFormatter(log_format)  
		ch.setFormatter(log_format)  

		# 给logger添加handler  
		self.logger.addHandler(fh)  
		self.logger.addHandler(ch)  
		with open(logName,'r') as fp:
			lines = fp.readlines()
		count = 0
		for index,line in enumerate(lines): #遍历所有行
			pass
			count+=1
		self.logger.info((count+1))
		count+=1
		self.logger.warning((count+1))
		count+=1
		self.logger.error((count+1))     
		count+=1
		self.logger.critical((count+1))
		for i in range(30): #30000000
			print (i)
		with open(modelName,"a+") as fw:
			for i in range(10): #100000000
				fw.write("txt message"+'\n')
				fw.write("txt message01"+'\n')
			fw.close()
		