from petri import *
args = make_parser().parse_args()
places = [Place(m) for m in args.marking]
ts = dict(
    start=Transition(
        [outGoingArc(places[0]),outGoingArc(places[1])],
        [inGoingArc(places[2])]
    ),
    change=Transition(
        [outGoingArc(places[2])],
        [inGoingArc(places[3]),inGoingArc(places[4])]
    ),
    end=Transition(
        [outGoingArc(places[3])],
        [inGoingArc(places[0])]
    ),
)
# from random import choice
# firing_sequence = [choice(list(ts.keys())) for _ in range(args.firings)]  # random

firing_sequence = ["start",
                   "change",
                   "end",
                   "start",
                   "change",
                   "end",
                   "start",
                   "change",
                   "end"]

petri_net = Petri(ts)
petri_net.run(firing_sequence, places)