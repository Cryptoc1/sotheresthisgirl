#!/usr/bin/env python

# Shitty code, deal with it. (atleast it's better than Instagram.py)

import twitter
from requests_oauthlib import OAuth1Session
import webbrowser, os, sys, time

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'


'''def get_access_token(consumer_key, consumer_secret):
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret)

    print 'Requesting temp token from Twitter'

    try:
        resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)
    except ValueError, e:
        print 'Invalid respond from Twitter requesting temp token: %s' % e
        return
    url = oauth_client.authorization_url(AUTHORIZATION_URL)

    print ''
    print 'I will try to start a browser to visit the following Twitter page'
    print 'if a browser will not start, copy the URL to your browser'
    print 'and retrieve the pincode to be used'
    print 'in the next step to obtaining an Authentication Token:'
    print ''
    print url
    print ''

    webbrowser.open(url)
    print "Enter code prompted after leaving twitter."
    pincode = raw_input("> ")

    print ''
    print 'Generating and signing request for an access token'
    print ''

    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret,
                                 resource_owner_key=resp.get('oauth_token'),
                                 resource_owner_secret=resp.get('oauth_token_secret'),
                                 verifier=pincode
    )
    try:
        resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
    except ValueError, e:
        print 'Invalid respond from Twitter requesting access token: %s' % e
        return

    # print 'Your Twitter Access Token key: %s' % resp.get('oauth_token')
    # print '          Access Token secret: %s' % resp.get('oauth_token_secret')
    print "Authenticated"
    return {'access_token': resp.get('oauth_token'), 'access_secret': resp.get('oauth_token_secret')}'''

def unfav(api, u):
    favs = api.GetFavorites(u.id)
    api.DestroyFavorite(favs[0])
    print "Tweet unfavorited..."
    time.sleep(2)

def main():
    consumer_key = "v8xVBZlXBp2AJoWI3VjDjzDkC"
    consumer_secret = "Wpoom4N6tpTgfywzCt6y83gvZubbYoT0vL0V8FXzhyXA74218D"

    api = twitter.Api(consumer_key=consumer_key, 
            consumer_secret=consumer_secret,
            access_token_key="3200038924-6twEw6XbQ19ibc8Fnt7qI8blFEkSNI5BCqFnPL3",
            access_token_secret="bgqS52Hcg53PXhX5qrk3z5k5oK7F6rRg3yIQKzzZO9iXd")
    
    _skip = "skipping tweet by: @"
    _al_fav = " (most likely already favorited it)"
    _faved = "faved tweet by: @"

    while True:
        search = api.GetSearch("so there's this girl")
        for s in search:
            if api.GetStatus(str(s.id)).favorited:
                print _skip + s.user.screen_name + _al_fav
            else:
                api.CreateFavorite(s)
                print _faved + s.user.screen_name
        search = api.GetSearch("so theres this girl")
        for s in search:
            if api.GetStatus(str(s.id)).favorited:
                print _skip + s.user.screen_name + _al_fav
            else:
                api.CreateFavorite(s)
                print _faved + s.user.screen_name
        search = api.GetSearch("So there's a girl")
        for s in search:
            if api.GetStatus(str(s.id)).favorited:
                print _skip + s.user.screen_name + _al_fav
            else:
                api.CreateFavorite(s)
                print _faved + s.user.screen_name
        search = api.GetSearch("So theres this girl")
        for s in search:
            if api.GetStatus(str(s.id)).favorited:
                print _skip + s.user.screen_name + _al_fav
            else:
                api.CreateFavorite(s)
                print _faved + s.user.screen_name
        search = api.GetSearch("#sotheresthisgirl")
        for s in search:
            if api.GetStatus(str(s.id)).favorited:
                print _skip + s.user.screen_name + _al_fav
            else:
                api.CreateFavorite(s)
                print _faved + s.user.screen_name

        status = api.PostUpdate("so there's this girl")
        status = api.PostUpdate("#sotheresthisgirl")
        
        time.sleep(5)

if __name__ == "__main__":
    main()
