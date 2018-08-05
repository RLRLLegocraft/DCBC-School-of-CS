"""
There are a lot of trainy things going on, so a StationMaster is in need. She
will keep a list of available carriages that can be altered and chosen from when
creating a train. There will be more attributes - but for now the focus is on
distributing customers and volunteers among
"""
################################################################################

class Carriage(object):

    #create a carriage, lets just use 'cruise' max as max capacity
    def __init__(self, name, max):
        self.name = name
        self.max = max

################################################################################
class StationMaster:
    #Cruise carriages
    t = Carriage("T", 44)
    x = Carriage("X", 32)
    h = Carriage("H", 38)
    n = Carriage("N", 42)
    y = Carriage("Y", 44)
    w = Carriage("W", 0)
    u = Carriage("U", 26)
    m = Carriage("M", 30)
    q = Carriage("Q", 20)
    s = Carriage("S", 40)
    p = Carriage("P", 32)

    #Public carriages
    g = Carriage("G", 22)
    j = Carriage("J", 24)
    c = Carriage("C", 26)
    a = Carriage("A", 26)
    v = Carriage("V", 17)
    e = Carriage("E", 24)
    d = Carriage("D", 24)
    r = Carriage("R", 44)

    #possible trains
    W = [t, x, h, n, y, w, u, m, q, s, p]
    Q = [t, h, n, w, u, m, q, s, p]
    V = [g, j, c, a, v, e, d, r]

    def __init__(self):
        pass
    def newTrain(lst):
        pass
    def removeCarriage(car):
        pass
    def addCarriage(name, max):
        pass
#########################################################################
class Train(object):

    #lets define a train with a list of carriage objects
    #but the train may have different carriages so lets build from scratch
    def __init__(self, customers):
        self.carriages = []
        if customers < 272:
            self.carriages = StationMaster.Q
        else:
            self.carriages = StationMaster.W
