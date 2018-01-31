# Making a Quakebot for Stanford

## Contents

- [00-calc_point_distances](00-calc_point_distances)
- [01-create_google_maps_url](01-create_google_maps_url)
- [02-parse_quakes](02-parse_quakes)
- [03-fetch_quakes](03-fetch_quakes)


## Proposal


If ever you need ideas for programming, just take another idea and personalize it for yourself. Assuming you're a Stanford affiliate, can you think of ways to 
make a bot more relevant to you and your community?

Create the code needed to read from the USGS Earthquake API and to create messages that tell us where earthquakes were in relation to Stanford University. These messages can be tweeted or sent via text message or whatever. 

Sample message:

    On Janary 25, 2018, 8:39 AM (PST), the USGS detected a 
    5.8-magnitude earthquake about 204 km W of Ferndale, California,
    -- which puts it 519.7 km from Stanford University. 

    Here is the USGS official page:
    https://earthquake.usgs.gov/earthquakes/eventpage/us2000cpba

    Here is a map:
    https://www.google.com/maps/dir/?api=1&origin=37.424107%2C-122.166077&destination=40.4372%2C-126.3397
    



Some previous, and convoluted assignments on this topic (using different APIs):

- http://www.compciv.org/practicum/projects/showme_examples/nearest-earthquakes/show-me-nearest-earthquakes-landing-page/
- http://2017.compciv.org/syllabus/assignments/homework/earthquake-mapper.html
- http://2017.compciv.org/syllabus/assignments/homework/local-quake-bot.html


## Background

Bots are all the rage these day, from LATimes QuakeBot to the fake-follower-bots in the NYT's excellent, [The Follower Factory](https://www.nytimes.com/interactive/2018/01/27/technology/social-media-bots.html). Bots are just a fancy word for any other kind of automated program, which means it can be broken down to even more basic processes and logics (all 1s and 0s in the end).

For this assignment, we'll create all of the components needed for an automated story-writing bot. And we'll base it off of the LATimes Quakebot:

http://www.slate.com/blogs/future_tense/2014/03/17/quakebot_los_angeles_times_robot_journalist_writes_article_on_la_earthquake.html

> Here’s Monday morning’s initial Quakebot report:

    > A shallow magnitude 4.7 earthquake was reported Monday morning five miles from Westwood, California, according to the U.S. Geological Survey. The temblor occurred at 6:25 a.m. Pacific time at a depth of 5.0 miles.
    
    > According to the USGS, the epicenter was six miles from Beverly Hills, California, seven miles from Universal City, California, seven miles from Santa Monica, California and 348 miles from Sacramento, California. In the past ten days, there have been no earthquakes magnitude 3.0 and greater centered nearby.
    
    > This information comes from the USGS Earthquake Notification Service and this post was created by an algorithm written by the author.
    
    Read more about [Southern California earthquakes](http://www.latimes.com/news/local/earthquakes/).



The LAT still has Quakebot run its feed: http://www.latimes.com/local/earthquakes/

But note the difference between formulaic stories, such as this one:

http://www.latimes.com/local/lanow/la-me-earthquakesa-earthquake-35-quake-strikes-near-san-benito-calif-ottc-story.html


And human-written stories, such as this one:

http://www.latimes.com/local/lanow/la-me-earthquakesa-earthquake-50-quake-strikes-near-capetown-calif-lh5t-story.html

(What's the difference in the story presentation? Why does one earthquake get special treatment and the others don't?)

And there are many copycats:

- https://twitter.com/earthquakessf
- https://twitter.com/earthquakeBot/status/956568601850499074


And with all bots, GIGO

- [Breaking news, literally: Newspaper's quakebot rumbled for fake story](https://www.theregister.co.uk/2017/06/22/la_times_bot_spreads_fake_news/)
- [A massive earthquake was reported in California Wednesday — by mistake](https://www.washingtonpost.com/news/morning-mix/wp/2017/06/22/a-massive-earthquake-was-just-reported-in-california-turns-out-it-happened-in-1925/?utm_term=.9cbb37b8965d)
hi
