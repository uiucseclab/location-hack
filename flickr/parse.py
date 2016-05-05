import json_result

photos = json_result.result['photos']['photo']

for photo in photos:
    print 'Owner: ' + photo['owner'] + ', Photo title: ' + photo['title'] + ', latitude: ' + photo['latitude'] + ', longitude: ' + photo['longitude']

