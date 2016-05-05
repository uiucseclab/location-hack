import urllib2
import json
from pprint import pprint 


class WhisperPost:
	def __init__(self, wid):
		self.wid = wid
		self.nickname = None
		self.gender = None
		self.text = None
		self.geo_title = None
		self.geo_lat = None
		self.geo_lon = None


if __name__ == "__main__":

	token = "30b79c7dd88a12322265f1336b0345cf36204534"
	query_lat = "31.2304"
	query_lon = "121.4737"
	limit = "100"
	uid = "0530e0488a9963403619fb32b191bf692b99f2"
	nonce = "C32F1EBE-6C09-4510-A5AF-D5CADBD397F3"

	url = """http://prod.eryuapp.com/feeds/whispers?auth_token={token}&feed_id=my_feed_1&lat={query_lat}&limit={limit}&locale=en_us&lon={query_lon}&nonce={nonce}&type=interest&uid={uid}""".format(
		token = token,
		query_lat = query_lat,
		query_lon = query_lon,
		limit = limit,
		uid = uid,
		nonce = nonce
		)

	content = urllib2.urlopen(url).read()
	f = open('output.json', 'w');
	f.write(content)
	f.close()

	data = json.loads(content)
	# pprint(data['whispers'])

	whispers = []
	whispers_json = data['whispers']
	for i in range(0, len(whispers_json)):
		wid = whispers_json[i]['wid']
		text = whispers_json[i]['text']
		gender = int(whispers_json[i]['gender'])
		nickname = whispers_json[i]['nickname']
		geo_title = whispers_json[i]['geo_title']
		meta = whispers_json[i]['meta']
		# pprint(meta)
		geo_lat = meta[0]['lat']
		geo_lon = meta[0]['lon']

		w = WhisperPost(wid)
		w.gender = gender
		w.nickname = nickname
		w.text = text
		w.geo_title = geo_title
		w.geo_lat = geo_lat
		w.geo_lon = geo_lon

		whispers.append(w)

	for i in range(0, len(whispers)):
		w = whispers[i]
		print w.wid + "\t\t" + str(w.geo_lat) + "," + str(w.geo_lon) \
			+ "\t" + w.geo_title + "\t" + w.text 

