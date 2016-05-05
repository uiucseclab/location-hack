#!/usr/bin/env ruby

require 'tinderbot'

# The facebook login creditial of a tinder user
facebook_authentication_token = 'EAAGm0PX4ZCpsBAG7S99nSZCPaS1ZCnQ0yoP6xnogY2U8P3HLROhyB490CRSIThOsDornZCd1C6yCEMGIKhZCZALNRX9Gy8Cw5GXjZCaFZBf3A6MZCAbOcy2RraeLsvcy4nV5RBpkyi30mntJeiYmpfkiuKeBWNMCdFTNMGlJc8rpSYKmX0nJLhcJN'
facebook_user_id = 100011925107325

# Authenticating
tinder_client = Tinderbot::Client.new
tinder_authentication_token = tinder_client.get_authentication_token facebook_authentication_token, facebook_user_id
tinder_client.sign_in tinder_authentication_token

user = tinder_client.profile
puts user.original_tinder_json # all user information, including geo locations

# some information to show
#puts user.id 
#puts user.name
#puts user.bio
#puts user.birth_date
#puts user.photo_urls


# all recommended users
tinder_client.recommended_users.each do |recom|
  puts recom.original_tinder_json # very messy. But we call see exact geo locations
  #puts recom.name # only show the user name
end

