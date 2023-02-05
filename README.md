<br>

# Context

Custom sprites are created by artists, and they deserve to be credited properly.

<br>

# Issues

## Origin

Some sprites come from Discord, some sprites come from Reddit, some sprites come from unknown sources (*before the creation of the `#sprite-gallery` channel*).

<br>

## Identification

On Reddit, people are identified by their unique username.

On discord, people are identified by a unique user ID and username that can change. 


<br>


## Alternatives

When multiple people create sprites for the same fusion, they create something called "an alt".

This means that there is no longer an obvious connection between "the artist" and "the art".

If the official sprite packs uses an alt, and my calc uses a different calc, and both alts are created by different people. Therefore i'm going to have to manually check each sprite (*annoying and time-consuming*).

<br>

## Collaborations

When multiple people work on a sprite, they create something called "a collab".

This means that there is no longer an obvious connection between "the artist" and "the art".

If a lot of people worked on one sprite, then the text that would appear on the calc would be very long. Therefore i'm going to have to refuse to list the names of all the people who worked on a collab, besides the one who posted the sprite.

<br>

## Errors

Some people posted sprites using the wrong file names in the `#sprite-gallery`.

This means that there is no longer an obvious connection between "the artist" and "the art".

In the calc, i fix the mistakes that people do. So i'm going to have to re-fix their mistakes.

<br>

## Data structures

### Time

My goal is to give the best user experience, my website must be the fastest it can be.

If getting the information "who created that sprite" is slow, it's gonna lower the user experience.

Therefore i must design a system that will provide that information, in the best time possible.

<br>

### Space

I can store all the information in one file, but that file is gonna be massive.

I can store all the information in multiple files, but that would mean a massive amount of files.

<br>

# Solution

1°) Use a discord bot to scrap all the data, into a local file

2°) Sanitize this file, since people have posted sprites with wrong names

3°) Generate folders "per sprite" with names of authors

4°) Manually fix cases where there are alts
