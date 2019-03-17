

Welcome to the first MMO-API-based game ever. The goal of the game is to manage a fleet of bots on a unexplored mysterious land. Program and optimize your own client that will control your army of bots and make them Mine, collect, build, farm resources and survive the hostile environment as well as the other players.

# API requests


post request = Action

get request = get current bot state


## POST requests

POST requests are used to make your bot execute an action. A POST action returns information about action success (or fail) and some basic data about bot's surrounding by default.
**No more than 1 post request per bot per second.**
Every action uses 1 action point (AP). If the bot doesn't have anymore AP, it won't do anything

POST requests look like this:

```json
{
    "credentials": {
      "account": "Albatroz",
      "key": "sdfjozjek293J"
    },
    "bots": [ "1234", "5678", "9543" ],
    "action": {
      ## see sections below
    },
    "return":["map", "inventory", "weather"]
}
```
``action`` element should contains all the actions you want your bot to do
### move the character
```json
"action": {
      "go": {
          "direction": "up",
          "collect": true
      }
    }
```

* ``direction``
>can be ``up``,``right-up``,``right``,``right-down``,``down``,``left-down``,``left`` and ``left-up``
* ``collect``
> set if you want your bot to automatically collect things on the floor of the next tile you walk on (true by default)

### mine
```json
"action": {
      "mine": {
          "direction": "up"
      }
    }
```
* ``direction``
>where you want to mine.
>can be ``up``,``right-up``,``right``,``right-down``,``down``,``left-down``,``left`` and ``left-up``,

### build
```json
"action": {
      "build": {
          "direction": "up",
          "material": "stone"
      }
    }
```
* ``direction``
>where you want to build
>can be ``up``,``right-up``,``right``,``right-down``,``down``,``left-down``,``left`` and ``left-up``,

* ``material``

>building material such as ``stone``





## GET requests

GET requests give you all the information about the surrounding area.

### Get your environment's information

```json
{
    "information": [
        "map",
        "inventory",
        "others_players",
        "thermic_map",
        "weather",
        ""
    ]
}
```

You should always specify the information that you want to acquire.

To do so, use the ``information`` property as a list that might contain the following elements:
* ``map``
>The map is a representation of the world that will help you find your way in this magnificent world. This property returns the surrounding area that the player can see, depending on how high he is, his sight accuracy, and so on.
>- - -
> Example: Let's imagine the total sight of your player is 1, the API will return a 3x3 area starting from the top-left (-1, -1) to the bottom-right (1, 1):
```json
{
    "distance": "2",
    "mapArrayArray": {
      "level" : [
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
        ],
      "weather" : [
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
        ],
      "temperature" : [
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
        ]
    }
}
```
* ``inventory``
* ``others_players``
* ``thermic_map``
* ``weather``


## Response

the API will return a json with this format:
```json
{
    "action": 0,
    "information": see GET request section above,
    "next": 1552845369

}
```
* ``action``
 > It is only for POST requests and consists of the code response for the action. These are the different codes that can be returned:

| 0 | SUCCESS |
|---|---------|
|   |         |
|   |         |
|   |         |
|   |         |
|   |         |
* ``information``
> information about your surrounding or your bot
* ``next``:
> next timestamp at which it will be possible to exexute an action from a bot again





## World Organization

### Height levels

| Height Levels | Value |
|---------------|-------|
| Bedrock       | -5    |
| Underground 4 | -4    |
| Underground 3 | -3    |
| Underground 2 | -2    |
| Underground 1 | -1    |
| Sea Level     | 0     |
| Beach         | 1     |
| Ground        | 2     |
| Hill          | 3     |
| Mountain      | 4     |
| Top           | 5     |
| Sky           | 6     |
| Heaven & Hell | 7     |

### Existing Materials

* Sand
* Water
* Coal
* Silver
* Gold
* Diamond





## Things you can build
(maybe this should remain secret)

### Training units

* City Hall
* Military Base
* Witch

### Resources

* Mine
* Sawmill (scierie en français)

### Research

* Workshop (crafting box?) (atelier en français)
* Laboratory

### Food

* Farm

### Transportation (each has a different speed)

* Boats
* Teleportation Portal (convenient but very expensive - can be found at some places)

### Ancient buildings

* Dungeons
* Hell & Heaven portal





## Units you can face

### Casual units

* Humans like you
* Vagabonds you can encounter

### Jobs (when you find a non-violent vagabond, you can ask him to work for you)

* Scientist
* Soldier
* Witch
* Worker

### Animals

* Pokemons

### Sci-fi creatures

* Skeletons
* Zombies

### Mechanical

* Machines (like the bots you can create)

### Ancient creatures

* Dragons
