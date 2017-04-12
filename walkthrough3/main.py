#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random
import cgi

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
		 mvList = ["God Father", "Titanic", "Legend", "Avatar", "2012"]		
        # TODO: randomly choose one of the movies, and return it
		 randVal =random.randrange(0,len(mvList))
		 randomMvPick = mvList[randVal]
		 return randomMvPick # "The Big Lebowski"

    def get(self):
        # choose a movie by invoking our new function 
		movie = self.getRandomMovie() 
		tomorrow_movie = self.getRandomMovie() 
		# build the response string 
		content = "<h1>Movie of the Day</h1>" 
		content += "<p>" + movie + "</p>" 
		# TODO: pick a different random movie, and display it under
		content += "<h1>Movie for tomorrow's movie: </h1>"
		content += "<p>" + tomorrow_movie + "</p>"
		self.response.write(content)
        

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
