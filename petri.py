class Place:
    def __init__(self, nTokens):
        self.nTokens = nTokens

class Arc:
    def __init__(self,place,amt=1):
        """
        ## an arc in petri_net, could be out going or in going.
        ## place: a place attached to it.
        ## amt  : amount of tokens required for a transaction.
        """
        self.place =  place
        self.amt   =  amt

class outGoingArc(Arc):
    """
    ##  when fired, take_action
    ##
    """
    def take_action(self):
        self.place.nTokens -= self.amt
    def isValid(self):
        """
        ##  check if there is enough tokens for the transaction
        ## to take place
        """
        return self.place.nTokens >= self.amt

class inGoingArc(Arc):
    """
    ##  similar to out going arcs
    """
    def take_action(self):
        self.place.nTokens += self.amt

class Transition:
    """
    ## oarcs: in-going arc of a transition is the outgoing arc of a place.
    ## iarcs: similar.
    """
    def __init__(self, oarcs, iarcs):
        self.oarcs = set(oarcs)
        self.arcs  = self.oarcs.union(iarcs)
    def fire(self):
        not_blocked = all(arc.isValid() for arc in self.oarcs)
        if not_blocked:
            for arc in self.arcs:
                arc.take_action()
        return not_blocked
class Petri:
    def __init__(self, transitions):
        self.transitions = transitions
    def run(self, fire_seq, places):
        print('\nFiring sequence: {}'.format([f for f in fire_seq]))
        print('Initial markings {}'.format([p.nTokens for p in places]))

        for f in fire_seq:
            t = self.transitions[f]
            if t.fire():
                print("{} fired".format(f))
                print(" => {}".format([p.nTokens for p in places]))
            else:
                print("{} failed".format(f))
        print("final: {}".format([p.nTokens for p in places]))

###args passing in cmd with python
def make_parser():
    """
    :return: A parser reading in some of our simulation paramaters.
    """
    from argparse import ArgumentParser
    parser = ArgumentParser()
    #parser.add_argument('--firings', type=int)
    parser.add_argument('--marking', type=int, nargs='+')
    return parser


