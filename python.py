import random
class Die:
    die = []
    def __init__(self):
        self.die = [1,2,3,4,6]
        
    def nextRoll(self):
        r = random.randrange(1, len(self.die)+1)
        return r
    
class UserPigPlayer:

    def __init__(self):
        print("Enter nothing to roll; enter anything to hold.")

    def isRolling(self, myScore, otherScore, turnTotal):
        ans = input("Turn total: " + str(turnTotal) + "    Roll/Hold? ")
        if len(ans) == 0:
            return True
        else:
            return False

class KPERPigPlayer:

    def __init__(self):
        None

    def isRolling(self, myScore, otherScore, turnTotal):
        if myScore >= 71 or otherScore >= 71:
            return True
        elif turnTotal >= 21 + round((otherScore - myScore)/8):
            return False
        else:
            return True

class PigGame:
    GOAL_SCORE = 100
    player1 = None 
    player2 = None

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    def play(self):
        p1s = 0
        p2s = 0
        end = 0
        player = self.player1
        other = self.player2
        die =  Die()
        while (end != 1):
            if (player == self.player1):
                p = "player1"
            else:
                p = "player2"
            print("Player1 score: " + str(p1s))
            print("Player2 score: " + str(p2s))
            print("It is " + p + "'s turn")
            turn = 0
            tt = 0
            while turn != 1:
                if (player == self.player1):
                    ps = p1s
                    os = p2s
                else:
                    ps = p2s
                    os = p1s
                if player.isRolling(ps,os,tt) == False:
                    if player == self.player1:
                        p1s = p1s+tt
                        turn = 1
                        print ("Turn total: " + str(tt))
                        player, other = other, player
                    else:
                        p2s = p2s+tt
                        turn = 1
                        print ("Turn total: " + str(tt))
                        player, other = other, player
                else:
                    dt = die.nextRoll()
                    print("Roll: " + str(dt))
                    if dt == 1:
                        tt = 0
                        turn = 1
                        print ("Turn total: " + str(tt))
                        player, other = other, player
                    else:
                        tt = tt+dt
            if p1s >= self.GOAL_SCORE or p2s >= self.GOAL_SCORE:
                end = 1

                
r = random.randrange(1, 3)
user =  UserPigPlayer()
comp =  KPERPigPlayer()
if (r == 1):
    game =  PigGame (user, comp)
    game.play()
else:
    game =  PigGame (comp, user)
    game.play()
        
            
    
