# py-petri
python programs for petri-net
## HOW TO USE THE PACKAGE:
Download or create petri.py in the same directory in your project.
### Import the package
```python
from petri import *
```
### add arguments for terminal cmd:
```python
args = make_parser().parse_args()
```
### Define places:
args.marking will be input from terminal
```python
places = [Place(m) for m in args.marking]
```
### Initializing transitions for your petri-net:
outGoingArc is the description for an outgoing arc attached to a place
<img src="https://i.imgur.com/KSHuUWr.png">

inGoingArc is the description for an ingoing arc attached to a place
<img src="https://i.imgur.com/agMXYSJ.png">
```python
ts = dict(
    t0=Transition(
        [outGoingArc(places[0])],
        [inGoingArc(places[1])],
    ),
    t1=Transition(
        [outGoingArc(places[0])],
        [inGoingArc(places[1])]
    ),
)
```
### Define a firing sequence
```python 
firing_sequence = ["t1", "t1", "t0", "t1"]
```
### Define the petri net:
```python
petri_net = Petri(ts)
```
### Run your petri net:
```python
petri_net.run(firing_sequence, places)
```
### RUN THE COMPUTATION WITH TERMINAL:
Define the inital marking for your places with --markings option.
```python
python main.py --markings 3 0
```
