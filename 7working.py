import bs4 as bs
import urllib.request
import sys
import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

sauce= urllib.request.urlopen('http://timesofindia.indiatimes.com/entertainment/hindi/movie-reviews').read()
soup=bs.BeautifulSoup(sauce,'lxml')



'''for div in soup.findAll('div',attrs={'class':'mr_listing_right'}):
        print (div.find('a').text)
        print (div.find('p').text)
        print('\n')'''

##for div in soup.findAll('div',attrs={'class':'mr_listing_right'}):
#    print (div.find('a').text)
#    for para in div.find('p',attrs={'class':'mrB10'}):
##      print (para.text)

j=0
i=0
for div in soup.findAll('div',attrs={'class':'mr_listing_right'}):
                print (div.find('a').text)
                ws.write(i, 0, div.find('a').text)
                #print (div.find('p').text)
                attrib_value = []
                attrib_value += [a['href'] for a in div.findAll('a',{'href':True})]
                #print(attrib_value)
                i = i + 1
                for l in attrib_value:
                    link='http://timesofindia.indiatimes.com'+l
                    #print(link)
                    sauce1= urllib.request.urlopen(link).read()
                    soup1=bs.BeautifulSoup(sauce1,'lxml')                              
                    #for div in soup1.findAll('div',attrs={'class':'Normal'})[0]:
                    div2=soup1.findAll('div',attrs={'class':'Normal'})[0]
                    for linebreak in div2.find_all('br'):
                        linebreak.extract()
                    print(div2.text.translate(non_bmp_map))
                    ws.write(j, 1, div2.text.translate(non_bmp_map))
                    j= j + 1
                            

wb.save('example.xls')
                            

