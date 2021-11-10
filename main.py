from petri import *
args = make_parser().parse_args()
places = [Place(m) for m in args.marking]
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
# from random import choice
# firing_sequence = [choice(list(ts.keys())) for _ in range(args.firings)]  # random

firing_sequence = ["t1", "t1", "t0", "t1"]

petri_net = Petri(ts)
petri_net.run(firing_sequence, places)