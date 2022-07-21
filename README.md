# Simple-cellular-automaton

A simple cellular automaton that implements the following rules of life:
* life _begins_ in an empty (or dead) cell next to which there are 3 living cells
* a cell _will be alive_ if it has 2 or 3 live neighboring cells
* a cell _will die_ if it has less than 2 or more than 3 living neighboring cells

> There is also a generation counter and a display of dead cells


#### It all looks something like this:

<img src="https://github.com/Di-peep/Simple-cellular-automaton/blob/master/docs/exmpl.gif" alt="how it works" width="560" height="440" />


##
## Settings

> I was using Google Chrome 103.0.5060.114

> Also you can find requirements.txt

Set up the variable: `set FLASK_APP=app.py`

Just run: `flask run`
