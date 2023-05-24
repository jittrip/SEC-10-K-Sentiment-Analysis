def clean_html_text(html_text: str) -> str:

    ''' html_text : str
        Raw html text read from a .html file
    html_string : str
        Contents pf html_text cleaned and stripped to leave just useful text 
        content
    ''' 
    from bs4 import BeautifulSoup
    import requests

    sec = BeautifulSoup(html_text,'html.parser') ## This is parsing the html text 
    html_string = sec.get_text(separator=' ')           # Returns all text elements of the html file.
    return html_string

def write_clean_html_text_files(input_folder, dest_folder):

    ''' assign directory
        iterate over files in
        that directory
    '''

    from pathlib import Path
    import os.path
    

    for file in os.listdir(input_folder):

        html_page = open(input_folder + '\\'+ file, "r")
        clean_text = clean_html_text(html_page)

        splitter = str(file).split('.')
        filename = splitter[0]+'.txt'

        completeName = os.path.join(dest_folder, filename)

        filehandle = open(completeName, 'w', encoding='utf-8')
        filehandle.write(clean_text)
        filehandle.close()

    return


