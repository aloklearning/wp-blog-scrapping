'''
All the commented code is for XLWT which is again a module
to write the data into the excel sheet, however, there is 
and advanced module that is XLXSWRITER which lets us write the 
URL, String in a more professional manner
'''
import json
import requests
import xlsxwriter

# workbook is created
workbook = xlsxwriter.Workbook('blog_final_data.xlsx')
worksheet = workbook.add_worksheet('CL Blogs')

# add_sheet is used to create
#data_sheet = wb.add_sheet("CL Blog Post Data")

# style = xlwt.easyxf('font: bold 1') 
# data_sheet.write(0, 0, 'BLOG TITLE', style) 
# data_sheet.write(0, 1, 'BLOG URL', style) 

# Bol format styling
bold_format = workbook.add_format({
    'font_color': 'blue',
    'bold':       1,
    'font_size':  15,
})

# Write the headers
worksheet.write_string('A1', 'BLOG TITLE', bold_format)
worksheet.write_string('B1', 'BLOG URL', bold_format)

def get_blog_data(page_count):
    api_url = 'http://thecareerlabs.com/wp-json/wp/v2/posts?_embed&per_page=10&page=' + str(page_count) 
    response = requests.get(api_url)

    if response.status_code == 200:
        json_data = json.loads(response.content.decode('utf-8'))
        return json_data # this returns json array
    else:
        return 'Problem Fetching url'

arr_final_data = []

for i in range(1,84):
    new_arr = get_blog_data(i) # we get the arr here, now we will add the dict
    for value in new_arr: 
        arr_final_data.append(value)

# this arr_final_data is used to print our data to the text file
# text_file = open("Output.txt", "a")
# for item in arr_final_data:
#     text_file.write(item["title"]["rendered"].encode("utf-8") + "   " + item["link"].encode("utf-8") + "\n")
# text_file.close()

for i in range(len(arr_final_data)):
    # data_sheet.write(i+1, 0, arr_final_data[i]["title"]["rendered"])
    # data_sheet.write(i+1, 1, arr_final_data[i]["link"]) 
    worksheet.write_string('A'+str(i+2), arr_final_data[i]["title"]["rendered"])
    worksheet.write_url('B'+str(i+2), arr_final_data[i]["link"])

#wb.save('xlwt blog_final_data.xls')
workbook.close()