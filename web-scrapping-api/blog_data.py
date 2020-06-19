'''
All the commented code is for XLWT which is again a module
to write the data into the excel sheet, however, there is 
and advanced module that is XLXSWRITER which lets us write the 
URL, String in a more professional manner
'''
import os
import json
import urllib
import requests
import xlsxwriter
from flask import Flask, request

# Creating flask app
app = Flask(__name__)
app.secret_key = 'alok'

# for fetching the data per page wise from wordpress
def get_blog_data(domain, per_page, page):
    api_url = 'http://{}/wp-json/wp/v2/posts?_embed&per_page={}&page={}'.format(domain, per_page, page) 
    response = requests.get(api_url)

    if response.status_code == 200:
        json_data = json.loads(response.content.decode('utf-8'))
        return json_data # this returns json array
    else:
        return "Failure"


# Initializing Workbook for excel
def workbook(domain, per_page_count, total_pages):
    # workbook is created
    workbook = xlsxwriter.Workbook('blog_final_data.xlsx')
    worksheet = workbook.add_worksheet('WP Blogs Data')

    # add_sheet is used to create
    #data_sheet = wb.add_sheet("CL Blog Post Data")

    # style = xlwt.easyxf('font: bold 1') 
    # data_sheet.write(0, 0, 'BLOG TITLE', style) 
    # data_sheet.write(0, 1, 'BLOG URL', style) 

    # Bold format styling
    bold_format = workbook.add_format({
        'font_color': 'blue',
        'bold':       1,
        'font_size':  15,
    })

    # Write the headers
    worksheet.write_string('A1', 'BLOG TITLE', bold_format)
    worksheet.write_string('B1', 'BLOG URL', bold_format)

    arr_final_data = []

    for i in range(1, total_pages+1):
        new_arr = get_blog_data(domain, per_page_count, i) # we get the arr here, now we will add the dict
        if new_arr == "Failure":
            return "Failed"
        else:
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

    # after successful operation download the file
    download_file()

def download_file():
    url = "http://127.0.0.1:4000/Users/alok/MyProjects/BlogFetchExcel/"
    urllib.request.urlretrieve(url, "blog_final_data.xlsx")

    # deleting the file which got saved in our file
    os.remove("blog_final_data.xlsx")
    print("File Removed!")


@app.route('/blog-scrap', methods=['POST'])
def web_scrapping():
    # Getting data from the requests
    request_data = request.get_json()

    # calling workbook for initialization
    response = workbook(**request_data)
    if response == "Failed":
        return {"message": "No wordpress domain found with the provided domain data"}
    else:
        return {"message": "Successfull Operation"}
    

if __name__ == "__main__":
    app.run(port=4000, debug=True)
    