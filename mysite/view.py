from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
	return HttpResponse("hello world")

def current_datetime(request):
	now =  datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def book_list(request):
    db = MySQLdb.connect(user='me',db='mydb',passwd='secret',host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html', {'name': names})



