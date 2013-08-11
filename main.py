import webapp2

from pagehandler import PageHandler

application = webapp2.WSGIApplication([(r'/(.*)', PageHandler)], debug=False)