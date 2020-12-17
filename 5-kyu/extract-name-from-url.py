"""
Extract the domain name from a URL

The link: https://www.codewars.com/kata/514a024011ea4fb54200004b

Problem Description:
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
  
Examples:
      domain_name("http://github.com/carbonfive/raygun") == "github" 
      domain_name("http://www.zombie-bites.com") == "zombie-bites"
      domain_name("https://www.cnet.com") == "cnet"
"""

HTTP = "http://"
HTTPS = "https://"
WWW = "www"
HTTPSWWW = "http://www"

def domain_name(url):
    print(url)
    if HTTPSWWW in url:
        url = url[11:]
    elif HTTP in url:
        url = url[7:]
    elif HTTPS in url:
        url = url[8:]
    elif WWW in url:
        url = url[4:]
    url = url[0:url.find('.')]
    return url
