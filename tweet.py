#!/usr/bin/env python

# Shitty code, deal with it.

import twitter
import time, sys

def main():
    consumer_key = "v8xVBZlXBp2AJoWI3VjDjzDkC"
    consumer_secret = "Wpoom4N6tpTgfywzCt6y83gvZubbYoT0vL0V8FXzhyXA74218D"

    api = twitter.Api(consumer_key=consumer_key, 
            consumer_secret=consumer_secret,
            access_token_key="3200038924-6twEw6XbQ19ibc8Fnt7qI8blFEkSNI5BCqFnPL3",
            access_token_secret="bgqS52Hcg53PXhX5qrk3z5k5oK7F6rRg3yIQKzzZO9iXd")
    
    _skip = " [sotheresthisgirl] skipping tweet by: @"
    _al_fav = " (most likely already favorited it)"
    _faved = " [sotheresthisgirl] faved tweet by: @"
    _post = " [sotheresthisgirl] posted update"
    
    # i = 1
    # j = 1
    k = int(sys.argv[1])
    l = int(sys.argv[2])
    while True:
        # we already finished this off, so don't need it anymore
        '''# should post updates with spaces from 0 to 123 spaces
        if i < 123:
            tmp = "." * i
            api.PostUpdate(tmp + "#sotheresthisgirl")
            api.PostUpdate("#sotheresthisgirl" + tmp)
            print _post
        # should post updates with spaces from 0 to 120 spaces
        if j < 120:
            tmp = "." * j
            api.PostUpdate(tmp + "so there's this girl")
            api.PostUpdate("so there's this girl" + tmp)
            print _post'''
        # should print numbers until the number is 122 (becuase there's a space between the number and the hashtag) digits long
        if len(str(k)) < 122:
           api.PostUpdate("#sotheresthisgirl " + str(k))
           print _post
        # should post update until the number is 119 (because the space between, yada, yada..) digits long, yada, yada..."
        if len(str(l)) < 119:
            api.PostUpdate("so there's this girl " + str(l))
            print _post

        # Waits ~10mins (if my math is correct)
        time.sleep(200)
        # i += 1
        # j += 1
        k += 1
        l += 1

if __name__ == "__main__":
    main()
