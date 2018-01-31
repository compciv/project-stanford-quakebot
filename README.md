<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Making a Quakebot for Stanford](#making-a-quakebot-for-stanford)
  - [The project](#the-project)
        - [Sample output](#sample-output)
  - [The steps](#the-steps)
  - [And all together](#and-all-together)
  - [And beyond](#and-beyond)
  - [Background](#background)
  - [Command for getting the data](#command-for-getting-the-data)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Making a Quakebot for Stanford

## The project

Write a program that reads from the USGS Earthquakes API and generates automated stories that can be tweeted/texted/published -- a la Ken Schwenke's QuakeBot for the LA Times and [@earthquakebot](https://twitter.com/earthquakeBot/status/956568601850499074).

But let's add some "personalization" for the Stanford community. Instead of generating a story that says an earthquake was detected somewhere, the story should tell us how far an earthquake was from Stanford University. And it should provide a URL that let's us see via Google Maps where a quake is relative to Stanford. 

A few other requirements for our `stanford_quakebot` program:

- The USGS data includes every kind of earthquake event, even ones that have the seismic impact equivalent to when your cat falls off your TV. To keep things simple, `stanford_quakebot` should just tell the user about quakes of magnitude 4.0+
- The time of the earthquake detection should be expressed in California time.
- The story should include a URL to a map visualizing the locations of Stanford and the detected quake.


##### Sample output

> At 8:39 AM on Monday, January 25, 2018, the USGS detected a 5.8-magnitude earthquake about 204 km W of Ferndale, California, i.e. about 517.9 km from Stanford University.

> Map: https://www.google.com/maps/dir/?api=1&origin=37.424107%2C-122.166077&destination=40.4372%2C-126.3397
 
> More info about this quake: https://earthquake.usgs.gov/earthquakes/eventpage/us2000cpba

For this example project, we'll focus on generating the story ("Content is king!"), and worry about how to programmatically tweet/text it laer.


<a name="the-steps-list" id="the-steps-list"></a>

## The steps

1. [calc_geo_distance](steps/calc_geo_distance) - Calculate the distance between two latitude/longitude geo-coordinate points.
2. [get_usgs_event_url](steps/get_usgs_event_url) - Given an ID for a USGS earthquake, generate the URL for that earthquake's official USGS page.
3. [get_gmaps_locator_url](steps/get_gmaps_directions_url) Generate a Google (static) Maps URL that shows where 1 point is compared to another.
4. [make_pretty_pacific_timestamp](steps/make_pretty_timestamp) - Convert a string that contains a timestamp. 
4. [make_quake_story_text](steps/make_quake_story_text) - Given a sample data object, convert it into a "story" (i.e. text).
5. [parse_usgs_quake_csv](steps/parse_usgs_quake_csv) - Given a sample CSV text file of earthquake data, open/read it and convert to Python data objects.
6. [fetch_usgs_quake_csv](steps/fetch_usgs_quake_csv) - Fetch earthquake data from the USGS API.


## And all together

- [all-together/organizing-modules.md]
- [all-together/writing-main-foo.md]


## And beyond

- [Earthquake stories for every zip code](extra-credit/zip-code-quakes)
- [Creating a command-line interface](extra-credit/ui-ux-cli.md)
- [Tweeting about quakes](extra-credit/tweet-quake.md)








If ever you need ideas for programming, just take another idea and personalize it for yourself. Assuming you're a Stanford affiliate, can you think of ways to 
make a bot more relevant to you and your community?

Create the code needed to read from the USGS Earthquake API and to create messages that tell us where earthquakes were in relation to Stanford University. These messages can be tweeted or sent via text message or whatever. 

Sample message:




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



## Command for getting the data

curl 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2018-01-25&endtime=2018-01-25T23:59&minmagnitude=5' > data/sample-quakes.csv
