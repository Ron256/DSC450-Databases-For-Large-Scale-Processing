import re
s = '{"created_at":"Thu May 29 00:00:59 +0000 2014","id":471803352850776060,"id_str":"471803352850776064","text":"@taylorcaniff please follow me! @HayesGrier follow @kinslie_alaine she loves you!!!! Follow me please!!! 1","source":"<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":1396698397,"in_reply_to_user_id_str":"1396698397","in_reply_to_screen_name":"taylorcaniff","user":{"id":1170387523,"id_str":"1170387523","name":"CANIFF be my 3/12","screen_name":"kaylabaronofsky","location":" w/ magcon!","url":"http://fgr.am/f/E9gZIJOyrP","description":"I love magcon! (2/12) (GLAMSS 2/6) taylor im beggin you please follow me!!! (Fav youtubers 0/20)","protected":false,"verified":false,"followers_count":866,"friends_count":592,"listed_count":7,"favourites_count":25304,"statuses_count":37092,"created_at":"Tue Feb 12 00:01:44 +0000 2013","utc_offset":-14400,"time_zone":"Eastern Time (US & Canada)","geo_enabled":true,"lang":"en","contributors_enabled":false,"is_translator":false,"profile_background_color":"FFFFFF","profile_background_image_url":"http://pbs.twimg.com/profile_background_images/471712646668894208/WXC86tE3.jpeg","profile_background_image_url_https":"https://pbs.twimg.com/profile_background_images/471712646668894208/WXC86tE3.jpeg","profile_background_tile":true,"profile_link_color":"00B3AA","profile_sidebar_border_color":"FFFFFF","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":"http://pbs.twimg.com/profile_images/471633207667212288/wKDVJSjo_normal.jpeg","profile_image_url_https":"https://pbs.twimg.com/profile_images/471633207667212288/wKDVJSjo_normal.jpeg","profile_banner_url":"https://pbs.twimg.com/profile_banners/1170387523/1401281215""default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":{"type":"Point","coordinates":[40.514557,-75.390121]},"coordinates":{"type":"Point","coordinates":[-75.390121,40.514557]},"place":{"id":"1d86a1f96daf493e","url":"https://api.twitter.com/1.1/geo/id/1d86a1f96daf493e.json","place_type":"city","name":"Coopersburg","full_name":"Coopersburg, PA","country_code":"US","country":"United States","bounding_box":{"type":"Polygon","coordinates":[[[-75.40394,40.500785],[-75.40394,40.518659],[-75.379475,40.518659],[-75.379475,40.500785]]]},"attributes":{}},"contributors":null,"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"trends":[],"urls":[],"user_mentions":[{"screen_name":"taylorcaniff","name":"Taylor Caniff","id":1396698397,"id_str":"1396698397","indices":[0,13]},{"screen_name":"HayesGrier","name":"Hayes Grier","id":330705266,"id_str":"330705266","indices":[32,43]},{"screen_name":"kinslie_alaine","name":"kinslie","id":1056333188,"id_str":"1056333188","indices":[51,66]}],"symbols":[]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"medium","lang":"en"}'
r = re.findall('"user":{"id":1170387523',s) #Manual search by applying the actual value
r2 = re.findall('"user":(.*)',s) #Group the string to get the "user" object

patternid = 'id\":(.*?)\,"' #search for the "id" object in user
userid = re.search(patternid, str(r2)).group(1)

patterngeo = '"geo":\{(.*?)\}\,' #search for the "geo" object in user
usergeo = re.search(patterngeo, str(r2)).group(1)

patterngeotype = 'type\":"(.*?)\","' #search for the "type" object in usergeo
usergeotype = re.search(patterngeotype, str(usergeo)).group(1)

patterngeocoordinates = 'coordinates\":\[(.*?)\]' #search for the "coordinates" object in usergeo
usergeocoordinates = re.search(patterngeocoordinates, str(usergeo)).group(1)


# print(r) #print the manual search
# print(r2) #print the user object
# print(userid) #print the userid object
print(usergeo) #print the usergeo object
# print(usergeotype) #print the usergeotype object
# print(usergeocoordinates) #print the usergeocoordinates object




