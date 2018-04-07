import scrapy

class QuotesSpider(scrapy.Spider):
	name = "Results"
	start_urls = [
        	'http://results.vtu.ac.in/cbcs_17/result_page.php?usn=1pe15cs{0:0=3d}'.format(usn)
			for usn in range(0,190)]

	def parse(self, response):
		var1 = response.css("div.col-md-12 > div.panel > div.panel-body > div.row > div.col-md-12 > table > tr > td::text").extract()
		var2 = response.css("div.col-md-12 > div.panel > div.panel-body > div.row > div.col-md-12 > table.table > tbody > tr > td::text").extract()

		fi = open('Result1.txt', 'a')
		repe = 0
		n=0
		n1 =0 
		repe1 =0
		for lnk in var1:
			fi.write(lnk)
		fi.write('\n')
		fi.write('--------------------------------------------------------------------------')
		for itm in var2:
			if repe % 6 ==0:
				fi.write('\n')
			if repe == 3:
				repe1 = 0
			if repe1 % 6 ==0:
				if n==1:
					fi.write('+ ')
					n1 = 0
			if n1 == 1:
				if n==1:
					fi.write('----->')
			fi.write(itm+" ")
			n =1
			n1 = n1 + 1
			repe = repe + 1
			repe1 = repe1 + 1
		fi.write('\n')
		#For Printing SGPA
		total = 0
		conv = 0
		index = 0
		i=0
		#fi.write('\n')
		while i < 8:
			#fi.write('\n')
			#fi.write("Adding Numbers:")
			index = index + 4 + conv
			#fi.write(str(index))
			#fi.write(var2[index])
			mark = int(var2[index])
			if(i<6):
				if(mark >=90):
					total = total+40 
				if(80 <= mark < 90):
					total = total+36 
				if(70 <= mark < 80):
					total = total+32 
				if(60 <= mark < 70):
					total = total+28
				if(50 <=mark <60):
					total = total+24 
				if(40 <= mark < 50):
					total = total+20 
			if(i>=6):
				if(mark >=90):
					total = total+20 
				if(80 <= mark < 90):
					total = total+18 
				if(70 <= mark < 80):
					total = total+16 
				if(60 <= mark < 70):
					total = total+14
				if(50 <=mark <60):
					total = total+12 
				if(40 <= mark < 50):
					total = total+10 
	
			conv = 2
			i = i + 1
		fi.write('\n')
		fi.write("SGPA: ")
		total = round(total / 28,2)
		fi.write(str(total))
		fi.write('\n')
		fi.write('--------------------------------------------------------------------------')
		fi.write('\n')
		fi.close()
		#print(k)
