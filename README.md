## How to use it

Convert & Clean a Netscape file to a Markdown file, and can publish md for example hexo

### Arguments

- -f, --file : the Netscape file path
- -o, --output_file : the output md path,default is 'Bookmarks.md'
- -n, --connection : if you have network connection then will fetch the url such as titles, default is false
- -i, --icon : whether or not you need additional favicons, default is false 

## Console

```shell
md.py -f "Chrome.html" -o "Chrome_Bookmarks.md"
md.py -f "Firefox.html" -o "Firefox_Bookmarks.md"
```

### Basic Bookmarks Structure

**Chrome**

```html
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p> <!------------- START PARSE ----------------->
    <DT><H3 ADD_DATE="1562719012" LAST_MODIFIED="1562725161" PERSONAL_TOOLBAR_FOLDER="true">书签栏</H3>    
    <DL><p> <!------------- BOOKMARKETS START ----------------->
        <DT><H3 ADD_DATE="1562724652" LAST_MODIFIED="1562725029">h1.1</H3>
        <DL><p> 
            <DT><H3 ADD_DATE="1562724661" LAST_MODIFIED="1562724961">h2.1</H3>
            <DL><p> <!------------- FIRST BLOCK ----------------->
                <DT><A HREF="https://www.csswinner.com/" ADD_DATE="1562724823" ICON="">					CSS Winner</A>
				...
            </DL><p> <!------------- FIRST BLOCK END----------------->
            ...
            <DT><H3 ADD_DATE="1562724695" LAST_MODIFIED="1562725246">h2.3</H3>
            <DL><p> <!------------- THIRD BLOCK ----------------->
                <DT><A HREF="https://www.iosicongallery.com/" ADD_DATE="1562724973">iOS Icon Gallery</A>
                <DT><H3 ADD_DATE="1562725235" LAST_MODIFIED="1562725296">H3.1</H3>
                <DL><p>
                    <DT><A HREF="http://www.rgbchallenge.com/" ADD_DATE="1562725271">RGB Challenge</A>
				...
                </DL><p>
                <DT><H3 ADD_DATE="1562725246" LAST_MODIFIED="1562725246">H3.2 EMPTY</H3>
                <DL><p>  <!------------- EMPTY BLOCK----------------->
                </DL><p>
            </DL><p> <!------------- THIRD BLOCK END ----------------->
            <DT><A HREF="https://www.brusheezy.com/" ADD_DATE="1562725029">Free Photoshop Brushes at Brusheezy!</A>  <!------------- EXTRA LINKS---------------->
        </DL><p>
                    
        <DT><H3 ADD_DATE="1562724709" LAST_MODIFIED="1562724908">h1.2</H3>
        <DL><p>
            <DT><H3 ADD_DATE="1562724709" LAST_MODIFIED="1562725037">h2.1</H3>
            <DL><p>
                <DT><A HREF="https://www.behance.net/" ADD_DATE="1562724797">www.behance.net</A>
                <DT><A HREF="http://www.losttype.com/browse/" ADD_DATE="1562724929" ICON="">Lost Type Co-op | Browse</A>
            </DL><p>
            <DT><H3 ADD_DATE="1562724709" LAST_MODIFIED="1562724929">h2.2 EMPTY</H3>
            <DL><p>
            </DL><p>
            <DT><A HREF="https://www.freepik.com/" ADD_DATE="1562724908" ICON="">Free Vectors, Photos and PSD Downloads | Freepik</A>
        </DL><p>
        <DT><H3 ADD_DATE="1562725058" LAST_MODIFIED="1562725058">h1.3 EMPTY</H3>
        <DL><p>
        </DL><p>
            
        <DT><H3 ADD_DATE="1562725159" LAST_MODIFIED="1562725196">h1.4 EMPTY</H3>
        <DL><p>
            <DT><H3 ADD_DATE="1562725181" LAST_MODIFIED="1562725181">h2.1 EMPTY</H3>
            <DL><p>
            </DL><p>
            <DT><H3 ADD_DATE="1562725196" LAST_MODIFIED="1562725213">h2.2 EMPTY</H3>
            <DL><p>
                <DT><H3 ADD_DATE="1562725213" LAST_MODIFIED="1562725213">h3.1 EMPTY</H3>
                <DL><p>
                </DL><p>
            </DL><p>
        </DL><p>
        <DT><A HREF="https://www.google.com/webhp?hl=zh-CN&sa=X&ved=0ahUKEwjP-KDZoqnjAhXsxYsBHQKIAM0QPAgH" ADD_DATE="1562724596" ICON="">Google</A>
    </DL><p> <!------------- BOOKMARKETS CLOSE ----------------->
</DL><p> <!------------- START PARSE CLOSE ----------------->
```

