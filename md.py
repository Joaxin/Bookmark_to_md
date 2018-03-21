from bs4 import BeautifulSoup
import requests
import re
import argparse
from requests import RequestException


parser = argparse.ArgumentParser(description="Convert & Clean Netscape file to Markdown, and can publish md for example hexo")
parser.add_argument("-i", "--input",help="the Netscape file path ")
parser.add_argument("-o", "--output", default= "Bookmarks.md",help="the outpur md path,default is 'Bookmarks.md'")
parser.add_argument("-n", "--connection", default="false",help="if you have network connection then will fetch the url such as titles,default is false")
args = parser.parse_args()
conn = "True" == str(args.connection.capitalize())

links = {}


def Fetching(url):
    s = requests.Session()
    try:
        r = s.get(url, allow_redirects=True)
        title = BeautifulSoup(r.text, "lxml").title
        if r.status_code == 200 and title:
            return title.string
        elif title is None:
            print('Request to ', url, "failed!!!", 'No title found!')
        elif response.history:
            print("Request was redirected to ", r.url)
            rr = s.get(r.url)
            if rr.status_code == 200:
                return BeautifulSoup(rr.text, "lxml").title.string
    except RequestException:
        print('Request to ', url, "failed!!!")


def bookmarks_to_md(Netscape_file, connection=False):
    for element in Netscape_file:
        if element.name == 'dt':
            folder_title = element.find('h3', recursive=False)
            if folder_title:
                if folder_title.parent.a is None:  # empty folders
                    print(folder_title.string, 'is empty, has been removed.')
                else:
                    f.write('\n###  ' + folder_title.string + "\n")
                    folder = element.dt.find('a', recursive=False)
                    if folder:
                        for a in element.find_all('a'):
                            if a['href'] in links:
                                links[a['href']].append(
                                    str(folder_title.string))
                                print("the %s has found in %s , its a duplicated link, it's been removed" % (
                                    a['href'], links[a['href']]))
                            else:
                                links[a['href']] = [folder_title.string]
                                if re.match("http://|https://", a.string):  # blank titles
                                    title = re.sub(".*://.*?\.(.*?)\..*", '\\1', a['href'])
                                    if connection:
                                        print('Fetching For', a['href'],)
                                        temp_title = Fetching(a['href'])
                                        if temp_title is None:
                                            print('Rename the ',
                                                  a.string, ' to ', title)
                                        else:
                                            print('Rename the ', a.string,
                                                  ' to ', temp_title)
                                            title = temp_title
                                    else:
                                        print('Rename the ',
                                              a.string, ' to ', title)
                                    f.write("\n[{0}]({1})\n".format(
                                        title, a['href']))
                                else:
                                    #                                 print(a.string)
                                    #                                 print(a['href'])
                                    if re.search("icon", str(a), re.S):
                                        try:
                                            f.write("\n[{0}]:{1}\n".format(
                                                a.string, a['icon']))
                                            f.write("![icon][{0}][{1}]({2})\n" .format(
                                                a.string, a.string, a['href']))
                                        except KeyError:
                                            print(
                                                a.string, " loaded icon but encoutered a key error")
                                            f.write("[{0}]({1})\n".format(
                                                a.string, a['href']))
                                    else:
                                        f.write("\n[{0}]({1})\n".format(
                                            a.string, a['href']))
                    else:
                        return bookmarks_to_md(element, connection=connection)
            elif element.find('a', recursive=False):  # isolate links under the folders
                s = element.find('a', recursive=False).string
                url = element.find('a', recursive=False)['href']
                f.write("\n[{0}]({1})\n".format(s, url))
#                 print(element.find('a', recursive=False).string)
#                 print(element.find('a', recursive=False)['href'])
        elif element.name == 'a':  # links outside the folders
            #             print(element.string)
            #             print(element['href'])
            f.write("\n[{0}]({1})\n".format(element.string, element['href']))


def write_to_md(file, connection=False):
    with open(file, encoding='utf-8') as fl:
        soup = BeautifulSoup(fl, "html5lib").body.dt
        for p in soup.find_all('p'):
            p.unwrap()
        for dl in soup.find_all('dl'):
            dl.unwrap()
        # print(soup.prettify())
        fl.close()
        for title in soup.find_all('dt', recursive=False):
            if title.find("h3"):
                if title.a is None:  # empty folders
                    print(title.h3.string, 'is empty,  has been removed')
                else:
                    f.write("\n##  " + title.find("h3").string)
                    f.write('\n---\n')
                    bookmarks_to_md(title, connection=connection)

def main():
    write_to_md(args.input, connection = conn)
    print("Total Links: ",len(links))



if __name__ == '__main__':
    with open(args.output, "w", encoding='utf-8') as f:
        main()
        f.close()