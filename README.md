## How to use it

Convert & Clean a Netscape file to a Markdown file, and can publish md for example hexo

### Arguments

- -f, --file : the Netscape file path
- -o, --output_file : the output md path,default is 'Bookmarks.md'
- -n, --connection : if you have network connection then will fetch the url such as titles,default is false
- -i, --icon : whether or not you need additional favicons, default is false 

## Console

```shell
md.py -f "Chrome.html" -o "Chrome_Bookmarks.md"
md.py -f "Firefox.html" -o "Firefox_Bookmarks.md"
```

