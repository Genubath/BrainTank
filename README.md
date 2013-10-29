# Brain Tank
## Summary
This is a little project to teach programming skills as well as basic AI.  It was started by a group associated
with PySgf and rebuilt to use as a programming learning tool for the Lighthouse East Co-op programming class.
To run it just execute main.py with python.

As I am intending to use this as a teaching tool there are bugs to be fixed, one should be somewhat obvious when running
the program, as well as many places where the efficiency of the logic can be greatly improved.  Be sure to submit pull
requests when fixing bugs that everyone can use.

## Simulation Rules
_EDIT: Not all of the simulation rules have been reimplemented yet._

Every time a train becomes "idle" it will run the `think()` function
associated with that brain to queue up more commands.
The tank then executes these, which can take a variable amount of time.
Tanks can also fire shots in the direction they are facing. 
They must turn to aim. 
Turning one facing takes half a second, turning twice takes one second.
The shots move at twice the speed of a tank.

### Tile Rules
_EDIT: Not all of the simulation rules have been reimplemented yet._
  * Crossing __dirt__ will take twice as long as regular tiles.
  * The tank will abort a move if it runs into a blocking tile or other tank.
  * Shots can destroy blocking tiles such as __trees__ or __rocks__.
  * Driving into __water__ will destroy the tank.

## Making a Brain
Copy brains/wander.py to brains/yourname.py.  Rename the class from WanderBrain to whatever name you'd like.

~~There is a small guide that describes what this brain does and what is available for brains to use in wander.py.~~

When creating a tank in the world you then add/fix the import and use your new class instead of WanderBrain()

```python
from brains.doctor import TardisBrain
blue_tank = Tank(self, "Matt Smith", Tank.BLUE, TardisBrain())
self.add_tank(blue_tank)
```

## TODO
  1. Add explosions and other animations.
  2. Make sound effects for actions.
  3. Add GUI elements like victory screen, etc.

## Requirements
  * [Python 3.0+](http://www.python.org/) - have NOT tested it on Python 2.7, but it should work.
  * [Qt 5.1+] (http://qt-project.org/)
    * Windows, OSX and Linux users (until 5.1 is available via standard repos) can install Qt from the downloads page (http://qt-project.org/downloads)
  * [PyQt](http://www.riverbankcomputing.com/software/pyqt/intro) - For Python bindings to the Qt framework

## Licensing
The code is GPLv3, but the art/sound is not.

### Attribution
  * The Planet Cute sprites are from the venerable Danc. Check out his [site](http://www.lostgarden.com).
  * The tank is by Saypen on [Open Game Art](http://opengameart.org/content/american-tank).
  * The Main song is by Mister Electric Demon on [Jamendo](http://www.jamendo.com/en/album/7686).
  * Everything else I've made and is in the public domain.
