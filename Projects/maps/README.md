Maps
=============
CS61A project 2
---------------
![*Let's go out to eat!
Show me places I would like
By learning my tastes.*](http://inst.eecs.berkeley.edu/~cs61a/fa17/proj/maps/visualize/voronoi.png)

# Introduction
In this project, you will create a visualization of restaurant ratings using machine learning and the [Yelp academic dataset](https://www.yelp.com/dataset). In this visualization, Berkeley is segmented into regions, where each region is shaded by the predicted rating of the closest restaurant (yellow is 5 stars, blue is 1 star). Specifically, the visualization you will be constructing is a [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram).

In the map above, each dot represents a restaurant. The color of the dot is determined by the restaurant's location. For example, downtown restaurants are colored green. The user that generated this map has a strong preference for Southside restaurants, and so the southern regions are colored yellow.

This project uses concepts from Sections [2.1](http://composingprograms.com/pages/21-introduction.html), [2.2](http://composingprograms.com/pages/22-data-abstraction.html), [2.3](http://composingprograms.com/pages/23-sequences.html), and [2.4.3](http://composingprograms.com/pages/24-mutable-data.html#dictionaries) of [Composing Programs](http://composingprograms.com). It also introduces techniques and concepts from machine learning, a growing field at the intersection of computer science and statistics that analyzes data to find patterns and make predictions.

