import json
import urllib2

def searchTwitter(searchTerm):
    twitterRequest = urllib2.urlopen("http://search.twitter.com/search.json?q="+searchTerm+"&rpp=10")
    jsonResponse = twitterRequest.read()
    items = json.loads(jsonResponse)["results"]

    for item in items:
        print item["from_user"]+": \n"+ item["text"] +"\n"
    print "\n"
    enterSearchTerm()

def enterSearchTerm():
    searchTerm = raw_input("Enter a term to search for:")
    searchTwitter(searchTerm.replace(" ","%20")) #replace spaces with http standard

enterSearchTerm()
