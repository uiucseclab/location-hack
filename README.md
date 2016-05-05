===Flickr Hack===

One can easily obtain a Flickr API_KEY once it has a Flickr account. 

API_KEY = 686a04cc684a9b86ac053496b73c01c0
Secret = 44aeb63b5c759c19

This api allows us to get all photos, including its detailed information, 
of a specific user. As long as the attacker learns the user_id of the victim, 
it can easily execute the attack to learn the vicim's locations. 
Further, the URL has a parameter 'page' to determine which page of 
photos it will retrieve. To obtain all photos, one can increase this 
parameter until no results are returned. The 'flickr_result.json' contains 
the returned results using the following URL

https://api.flickr.com/services/rest/?user_id=48247111@N07&format=json&nojsoncallback=1&extras=original_format,tags,description,geo,date_upload,owner_name&page=1&method=flickr.photos.search&format=json&nojsoncallback=1&api_key=686a04cc684a9b86ac053496b73c01c0


Just for fun, the Following API allows us to obtain the top places with most posted photos.

https://api.flickr.com/services/rest/?method=flickr.places.getTopPlacesList&place_type_id=7&format=json&nojsoncallback=1&api_key=686a04cc684a9b86ac053496b73c01c0

===Tinder Hack===

The hack is based on the tool 'tinderbot'

With tinderbot, we can get the full information the tinder user, such as its name, locations and photos

We can get the all recommended users of a given user. The returned information 
includes the geo locations of each user. In our report, we introduce an 
attack strategy to disclose one victim's locations. 

NOTE: Bundle is reqired for running the ruby code. We have provide the gem files. 
Once you have bundle installed, run 'bundle install' to install all required 
module in the gem files. After that, run 'bundle exec ruby bot.py' to execute 
the code. Also, the Facebook creditial may be outdated. If so, you will need to 
provide a valid Facebook creditial that has been used for Tinder login. 


===Whisper Hack===

The script whisper_parser.py will call the query API of Whisper China, and fetch posts around a specified location. The script will further parse the JSON result of the query and display the result in the terminal.
