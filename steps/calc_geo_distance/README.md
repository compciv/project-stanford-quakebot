# calc_geo_distance

## Summary

In this lesson, we attempt to write a Python function to calculate the distance between two latitude/longitude geo-coordinate points, regardless of our ignorance of geometric principles. This is less a lesson about geospatial analysis and geometry than it is about the fundamental and vital software engineering practice of reusing other programmers' code. 



## Goal

For this lesson, we piggyback off an implementation of the Haversine formula described in this [StackOverflow answer](https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude/19412565#19412565), which is mirrored here:

[so_original_answer.py](so_original_answer.py)

Adapt this code so that it can be used for our general purposes. Specifically, in a function named `calc_geo_distance()` in a file named `foo.py`.

Start with the function skeleton/definition found here:

[foo.skeleton.py](foo.skeleton.py)


See if you can work your way towards the solution (one of an infinite number of variations) that I have posted here:

[foo.py](foo.py)




## Background

### To reuse is divine

As Python programmers, we have been using other people's work  since writing our first "hello world" program -- if  you thought the `print()` function was some kind of fundamental self-evident computational command, take a look at [its source code](https://github.com/python/cpython/blob/master/Python/bltinmodule.c#L1851).

Python isn't one of the world's most dominant programming languages just because of its design and syntax, but because of the vast libraries of functionality that its users have built over the years. The most novice of programmers can bring in this code (after installing the libraries via pip) with a single line:

```py
import requests
resp = requests.get('http://www.example.com')
```

This lesson is a little different in that we are hoping to copy and re-use code that isn't in a pretty self-contained package like the [Requests library](http://docs.python-requests.org/en/master/). This means finding and identifying code that is relevant to our problem, and re-writing it for our purposes.


### About geospatial coordinates


As humans, we think of geographic locations in terms of human-friendly names, e.g. "Stanford University", "my dad's house", "North Hollywood on Radford, near the In-N-Out Burger". But when computers are tasked with calculating locations and distances, such as where exactly your Uber/Lyft driver is, and about how many minutes until they arrive -- they need to work with locations as numbers, specifically **latitude** and **longitude** points.

"San Francisco, CA", for example, has a latitude of `37.773972` and longitude of `-122.431297`, according to [latlong.net](https://www.latlong.net/place/san-francisco-ca-usa-594.html).

And Stanford University has a long/lat pair of `-122.169719`, `37.427475`

### Real-world distance calculation

Longitude and latitude are similar in concept to points on a grid, with longitude being the "x" (i.e. horizontal value) and latitude being the "y". This means calculating the distance between them should be similar to using the good ol Pythagorean Theorem to calculate the distance. 

Unfortunately, the locations and spatial relationships in the real-world are on Earth, and the Earth is commonly theorized to be a sphere rather than something akin to a flat grid. Which means that distances aren't straight lines but curved (i.e. longer) lines.

As much fun as it would be to delve into the advanced geometry of curvatures, it is enough to ponder if calculating distances between two geospatial points is the type of task that people -- perhaps many people and companies -- have had to routinely calculate. If the answer is "yes", then it's almost guaranteed that someone, somewhere has written a function or program that does all the work.

We just have to find it.

### Flaws and limitations

At the end of this section, you'll hopefully be able to produce the `calc_geo_distance()` function as defined in [foo.py](foo.py) with some confidence. However, it's worth pointing out some of the critical designs of the function, namely:

- It requires users to call it and specify 4 different arguments, which gets a little hairy because it's easy to forget things like whether the longitude or latitude value of each pair goes first. Ideally, we want functions to be as pain-free to call as possible.
- It requires users to figure out the latitude/longitude of places that they only know by name. If you tried looking up these coordinates for the examples in this lesson, then you have a taste of how inconvenient that process is.

We don't have to -- nor do we need to -- fix these deficiencies that are inherent to the proposed design of `calc_geo_distance()`. Not because we're lazy, but because that should be *someone else's job* -- or rather, someone else's *function*. But it is good to keep these flaws in mind so that when you see how complicated geocoding can be -- i.e. using a service to convert place names to latitude/longitude coordinates, you'll understand why you're doing it. 


## How-to guide

This next section is an extensive writeup that explains how to frame a problem in a way that you can find other people's solutions to it. However, other people's code -- being written by other people -- is not code that is necessary safe or out-of-the-box ready for *you*. So this section contains some general strategies/patterns for refactoring someone's *specific-purpose* code to make the kind of *general-purpose* code that you need. 


### Googling for answers

This step is a lot more complicated than it may seem, depending on how ignorant you are about the extent that Google "thinks" for us. This situation is relatively simple, though, and it comes down to whether you can abstract this problem, and phrase your needs in the same way that others around the world (preferably expert programmers who speak your native language) have phrased it. 

Searching for *"[What is the Python math algorithmic program for finding how far it is between Stanford and San Francisco](https://www.google.com/search?q=What+is+the+Python+math+algorithmic+program+for+finding+how+far+it+is+between+Stanford+and+San+Francisco)"* probably won't yield useful code.

But something more general, both in concept and in phrasing, is good enough for Google, e.g. "[python calculate distance between latitude longitude points](https://www.google.com/search?q=python+calculate+distance+between+latitude+longitude+points)". 

This StackOverflow question, [Getting distance between two points based on latitude/longitude](https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude), seems to be exactly what we ourselves want to know. And the accepted answer, by user [Michael0x2a](https://stackoverflow.com/users/646543/michael0x2a), seems to be relevant to our use case. You can view Michael0x2a's answer, with context, at this URL:

https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude/19412565#19412565

Or to see just the Python code (with comments), check out my mirror here:

[so_original_answer.py](so_original_answer.py)

And here it is for easy reference:

```py
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

lat1 = radians(52.2296756)
lon1 = radians(21.0122287)
lat2 = radians(52.406374)
lon2 = radians(16.9251681)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)
print("Should be:", 278.546, "km")
```

#### How to avoid destroying yourself with other people's code

The main danger of executing other people's code (especially on your own computer, which you probably are if you are like virtually every programming student in the world) is that you have essentially given a total stranger permission to do whatever they like to your computer, which can be bad if this unknown programmer is malicious or grossly incompetent.

Realistically speaking, the social-feedback-system of Stack Overflow -- in which users openly discuss/criticize and vote on answers -- makes it unlikely that blatantly malicious code is even visible, especially if you take the time to read the comments and narrative. 

#### Slow and steady

In general, if you are trying out someone else's code, you should be doing it line-by-line. If you are a novice, I highly recommend actually typing it out, as this mechanical process is slow enough that your brain gets some exercise in actually thinking about what the code means. If you must copy-and-paste, do it line-by-line.

So while it's possible to take the code in [so_original_answer.py](so_original_answer.py) and copy-paste it into a file that you pass into the Python interpreter, it's inherently risky. More importantly, it's a horrible way to learn programming, especially if the code snippet has bugs. Writing/pasting the lines into Python's interactive mode (i.e. **ipython**) can end up being more efficient sometimes. 

(If a code snippet is too long to work through line-by-line, then that may be a sign that you shouldn't be using this "snippet" at all)


###  Scrubbing someone code of hard-coded values

The first thing to do with the code in [so_original_answer.py](so_original_answer.py) is to just confirm that it runs, bug-free. Again, I recommend doing this line-by-line in interactive Python. When you're reasonably satisfied that the code isn't doing anything strange or harmful, then sure, paste it into a file and run it through the Python interpreter:


```
$ python so_original_answer.py
Result: 278.54558935106695
Should be: 278.546 km
```

What is that output? If you [read the answer on StackOverflow](https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude/19412565#19412565) -- i.e. get the context of the answer -- you'll see that the output comes from `print()` statements meant to debug the questioner's specific problem (lines 24 and 25):

```py
print("Result:", distance)
print("Should be:", 278.546, "km")
```

Code specific to someone else's particular problem is not going to be useful to *our* problems. The last line in the above snippet is clearly a hard-coded (i.e. constant, i.e. never-changing) value of no meaning to us. Let's delete it, and make the last line this:

```py
print("Distance:", distance, "km")
```

To be honest, even if you do go through [so_original_answer.py](so_original_answer.py) very slowly, you may still not *get it*, especially if your memory of geometry class is very hazy. However, what you should strive to do as a programmer is to identify what small parts of someone else's code is worth adjusting (i.e. "hacking") by you, and what code is meant to be a black box.

So first, focus on variable assignments -- which, conveniently, are usually the first lines in a script. 

The snippet below covers lines 3-9 in [so_original_answer.py](so_original_answer.py):


```py
# approximate radius of earth in km
R = 6373.0

lat1 = radians(52.2296756)
lon1 = radians(21.0122287)
lat2 = radians(52.406374)
lon2 = radians(16.9251681)
```

Let's take this line-by-line:

```py
# approximate radius of earth in km
R = 6373.0
```

Thanks to the comment, we can infer that the variable `R` is meant to refer to the *constant* value of the Earth's radius in kilometers. That's probably a variable and value that we want to use ourselves, though we should rename it to our tastes.

####  Don't sweat geometry when you can focus on Python basics


Next:

```py
lat1 = radians(52.2296756)
```

I won't get into the geometry concepts here -- re-read the [StackOverflow question for the context](https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude/19412565) -- other than to say that our calculation involves taking one unit of angular measurement -- degrees -- and converting it to another -- *radians*.

Let's pretend that is mostly over our heads -- what we *can* focus on is what is what is happening in *Python terms*, i.e.

1. The expression `radians(52.2296756)`, in Python terms, involves invoking a function named `radians()` and passing in the literal value of `52.2296756` (a float)
2. The function `radians()` apparently returns something.
3. The return value of `radians(52.2296756)` is being assigned to a variable with the name of `lat1` 

At some point, when you are experienced enough as a programmer, you should be able to infer with confidence that the result of `radians(52.2296756)` will always be the same, which means that the variable `lat1` will always have the same value. You can infer this even with zero awareness of geometry concepts like radians and degrees.

As a novice programmer, you may lack confidence, but you have the tools to make yourself as confident as any pro programmer. You just need to develop the mindset that you can confirm anything in code for yourself:

```py
>>>> from math import radians
>>>> radians(52)
0.9075712110370514
>>>> radians(52)
0.9075712110370514
>>>> radians(52) == radians(52)
True
>>>> lat1 = radians(52)
>>>> type(lat1)
float
>>>> type(radians(52))
float
>>>> lat1
0.9075712110370514
>>>> lat1 == radians(52)
True
```

Again, you can be mostly ignorant of geometry and radians, and the details of the inner workings of the `radians()` function. But you have the complete ability to test inputs and outputs to make some generalizations. The important generalization here is that the variables `lat1`, `lng1`, `lat2`, and `lng2` are hard-coded to values -- e.g. `52.2296756` and `21.0122287` -- that have no relevance to us. Nor are these hard-coded values referred to anywhere else in the rest of the [so_original_answer.py](so_original_answer.py) code, outside of their variable names.

The first step we can take is to rename and refactor these hard-coded variables. Here's one approach:

```py
EARTH_RADIUS_IN_KM = 6373.0

latitude_1 = 52.2296756
longitude_1 = 21.0122287
latitude_2 = 52.406374
longitude_2 = 16.9251681

lat1 = radians(latitude_1)
lon1 = radians(longitude_1)
lat2 = radians(latitude_2)
lon2 = radians(longitude_2)
```

Renaming `R` to `EARTH_RADIUS_IN_KM` means that we have to change all other references to `R`. This is easy, as `R` is only used in line 21:

```py
distance = R * c
```

See the refactored version here: [so_refactored_answer.py](so_refactored_answer.py)


#### Why refactor variable assignments? 

Running [so_refactored_answer.py](so_refactored_answer.py) doesn't get us a substantively different result than running [so_original_answer.py](so_original_answer.py):

```
$ python so_refactored_answer.py 
Distance: 278.54558935106695 km
```

And why should we expect a different result, just because there are new and more variable names? 

This:

```py
latitude_1 = 52.2296756
# ...
lat1 = radians(latitude_1)
```

-- is no different than this, other than being much more verbose:

```py
lat1 = radians(52.2296756)
```

The refactoring wasn't meant to have a computational impact. It was done for *human* reasons -- specifically, separating the hard-coded part of the original script from the part that we intend to re-use. The additional lines devoted to variable assignment makes this separation of concerns much clearer to the reader.

And there is one more benefit -- compare how easy it is to sub in values of our choosing in the refactored version:

```py
latitude_1 = 52.2296756
longitude_1 = 21.0122287
# ...

lat1 = radians(latitude_1)
lon1 = radians(longitude_1)
```

-- versus what you have to do (via point-and-click, probably), to sub in values into the original code:

```py
lat1 = radians(52.2296756)
lon1 = radians(21.0122287)
```

Admittedly, it's not a *major* difference of physical work, but every bit helps...


###  Trust but verify

So far, we've only rearranged Python code. But we haven't done a critical check -- what if the copied code is flawed and does not actually correctly calculate distances? What assurance do we have that the Stack Overflow solution isn't completely off?

The answer is: we have no assurance whatsoever, unless you can do the distance calculation in your head. We don't even know what those hardcoded lat/lng points even refer to in the real world.

For the sake of brevity, let's come up with a rough sanity check for ourselves. It involves a bit of manual work and verification:

1. Think of two places you're familiar with in the real world
2. Figure out the distance between those 2 places, roughly
3. Find the lat/lng coordinates of those 2 places
4. Run those coordinates through our distance calculator

We already have one place in mind: Stanford University. The other place could just be San Francisco.

Use Google, or some other site, to find the as-the-bird-flies distance between those two landmarks:

https://www.distance-cities.com/distance-san-francisco-ca-to-stanford-ca

> There are 27.92 miles from San Francisco to Stanford in southeast direction and 36 miles (57.94 kilometers) by car, following the US-101 route.

Calculate the conversion of 27.92 miles into kilometers:

```py
>>>> 27.92 * 1.60934
44.9327728
```

Look up the coordinates for Stanford and San Francisco:

```
San Francisco: 
  longitude: -122.431297
  latitude: 37.773972

Stanford University:
  longitude: -122.169719
  latitude: 37.427475
```

And insert them into our [so_refactored_answer.py](so_refactored_answer.py) script:


```py
# Stanford
latitude_1 = 37.773972
longitude_1 = -122.431297
# San Francisco
latitude_2 = 37.427475
longitude_2 = -122.169719
```

That's the only adjustment we have to make -- for your convenience, here's the script with the inserted values:

[so_refactored_check.py](so_refactored_check.py)

The result:

```
$ python so_refactored_check.py 
Distance: 44.90843847043176 km
```

That's a bit different than the expected answer of `44.9327728`, but keep in mind that the expected answer is derived from the estimation found at this website:

https://www.distance-cities.com/distance-san-francisco-ca-to-stanford-ca

And we really don't know which lat/lng coordinates they used to represent Stanford and San Francisco. So in actuality, this is a pretty sloppy test, to the degree that I do not recommend you settle for in the real world. But for an example project, we can be satisfied that our algorithm is "in the ballpark".


### Making a function

Being able to convert code from a one-off script into a reusable function is a huge power, and it gets right to the core of why we program in the first place. And like all forms of writing and comprehension, it's a skill that doesn't have a ceiling of perfect mastery, because the solutions are open-ended and unique to programmers/writers and their situation.

That said, this scenario is pretty simple. Take the refactored code we have in [so_refactored_answer.py](so_refactored_answer.py) and abstract it a bit more so that it can fit the `calc_geo_distance()` function defined in [foo.skeleton.py](foo.skeleton.py).



## The solution

You can find one example of a solution in [foo.py](foo.py)

The most direct approach to this is to consider all the ways the syntax of a Python function is different than the kind of code found in [so_refactored_answer.py](so_refactored_answer.py) (here's [a review of some of the basics](http://www.compciv.org/guides/python/fundamentals/function-definitions/))

Here's the key differences I see:

1. A Python function requires a function definition, i.e. `def fooname():`
2. The body (the actual code) of a function is indented, relative to the function definition.
3. Functions can have arguments, which allow users of the functions to assign whatever values to variables as they like. 
4. Functions return a value


Let's implement the function with these differences in mind:


#####  1. Write the function definition

This is easy, it's given to us in [foo.skeleton.py](foo.skeleton.py):

```py
def calc_geo_distance(longitude_1, latitude_1, longitude_2, latitude_2):
```


#####  2. The code for a function is indented relative to its definition

OK, paste all of [so_refactored_answer.py](so_refactored_answer.py) underneat the function definition, and indent the body one level:

```py
from math import sin, cos, sqrt, atan2, radians
EARTH_RADIUS_IN_KM = 6373.0

def calc_geo_distance(longitude_1, latitude_1, longitude_2, latitude_2):
    latitude_1 = 52.2296756
    longitude_1 = 21.0122287
    latitude_2 = 52.406374
    longitude_2 = 16.9251681

    lat1 = radians(latitude_1)
    lon1 = radians(longitude_1)
    lat2 = radians(latitude_2)
    lon2 = radians(longitude_2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = EARTH_RADIUS_IN_KM * c

    print("Distance:", distance, "km")
```

Note that I've made a couple of adjustments as advised by PEP8:

- [`import` statements should be at the top of the line](https://www.python.org/dev/peps/pep-0008/#imports)
- [Constants should be defined and accessible at the module level](https://www.python.org/dev/peps/pep-0008/#constants), i.e. not limited to being inside the scope of the function definition for `calc_geo_distance()`


##### 3. Functions have arguments

When we define arguments for a function, we are giving users a way to define those variables as they need when using our functions. The upshot is: we don't need to write the code that assigns those variables within our function, i.e. 

```py
calc_geo_distance(10, 20, -42, -84)
```

-- automatically assigns `10`, `20`, `-42`, `-84` to `longitude_1`, `latitude_1`, `longitude_2`, and `latitude_2`. 

Our `calc_geo_distance()` now has 4 fewer lines:

```py
from math import sin, cos, sqrt, atan2, radians
EARTH_RADIUS_IN_KM = 6373.0

def calc_geo_distance(longitude_1, latitude_1, longitude_2, latitude_2):
    lat1 = radians(latitude_1)
    lon1 = radians(longitude_1)
    lat2 = radians(latitude_2)
    lon2 = radians(longitude_2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = EARTH_RADIUS_IN_KM * c

    print("Distance:", distance, "km")
```


##### 4. Functions have a return value

A function doesn't necessarily need a `return` statement if we intend it to return a value of `None`. However, this function is expected to return a `float`, i.e. the distance calculation.

Using a `return` statement actually simplifies things. We use it to replace the `print()` statement, which didn't do anything but spit out to screen the result of the calculation. Which is not terribly useful programmatically speaking.

So, here is the final iteration of `calc_geo_distance()`; it could be prettier, but it definitely does what we want it to, for now:

```py
from math import sin, cos, sqrt, atan2, radians
EARTH_RADIUS_IN_KM = 6373.0

def calc_geo_distance(longitude_1, latitude_1, longitude_2, latitude_2):
    lat1 = radians(latitude_1)
    lon1 = radians(longitude_1)
    lat2 = radians(latitude_2)
    lon2 = radians(longitude_2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS_IN_KM * c
```

## Do one thing and do it well

From the [Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)

> Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new "features".

After all this refactoring work, a common question is why remove the `print()` statement? In other words, why not have our function print to screen *and* return a value?

```py
def calc_geo_distance(longitude_1, latitude_1, longitude_2, latitude_2):
    # ...
    # ...

    distance = EARTH_RADIUS_IN_KM * c
    print("Distance:", distance, "km")
    return distance
```

First, there are concrete reasons as to why this "let's just do everything" approach is not practical -- but these reasons aren't evident until we have more experience chaining functions/programs together and seeing how the output of one function is directly consumed by another. In such cases, a function that has 2 different outputs can be a painful problem.

But it's worth considering the *philosophical* (in terms of software design) concepts. More is not always better, and that applies both to output (because extraneous info becomes more noise to filter) and to lines of code (more lines to write, and more to maintain). 

But even more fundamentally, functions (or people, or institutions) that want to have more power (i.e. functionality) often risk overreaching and then being burdened with too much responsibility.

How does that apply to our simple `calc_geo_distance()` and its `print()` statement?

Look at the format of what the `print()` statement outputs:

```py
distance = 42.12345
print("Distance:", distance, "km")
```

```
Distance: 42.12345 km
```

There's nothing inherently wrong about it, but there's nothing inherently right either. What if a user wants a more concise output, like:

```
42.12345 km
```

Or something with more context:

```
The distance between these two points is 42.12345 km
```

Or for the result to be rounded? One user might want it to the nearest tenth of a kilometer; others may not even need that precision if the distance is in the thousands of kilometers.

And what if a user doesn't want the result in kilometers, but in miles? I challenge you to write the code that converts `'Distance: 42.12345 km'` to miles, without being super irritated at the chore.

**However**, if we design `calc_geo_distance()` to be as simple -- some would call it "lazy" -- as possible, so that it exemplified the Unix philosophy of "Do one thing and do it well", then all the stress of trying to satisfy the infinite possible use cases of our function simply disappear, because we defer that thinking and work to the users of our function.

(I sometimes call it the [McNulty Principle](https://www.youtube.com/watch?v=JUKfwQt4yQU))

As it turns out, this simplification/reduction of features ends up being easier on our users. Here's how all the aforementioned usecases are solved:

```py
from foo import calc_geo_distance
lng1, lat1 = (-110, 37)
lng2, lat2 = (-115, 40)
distkm = calc_geo_distance(lng1, lat1, lng2, lat2)

print('Distance:', distkm, 'km')
print('The distance between ({x1},{y1}) and ({x2},{y2}) is {d} km.'.format(
                  x1=lng1, y1=lat1, x2=lng2, y2=lat2, d=distkm))
print('The distance is about', round(distkm), 'km')
distmi = distkm * 0.621371
print('The distance is about', round(distmi, 1), 'miles')
```






