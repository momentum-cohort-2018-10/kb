class Vote:
    def __init__(self, voter_id, candidate):
        self.voter_id = voter_id
        self.candidate = candidate


class BallotBox:
    def __init__(self):
        self.votes = []

    def add_vote(self, new_vote):
        if new_vote.voter_id in [v.voter_id for v in self.votes]:
            raise RuntimeError("You can't vote twice!")
        else:
            self.votes.append(new_vote)

    def tally_votes(self):
        tally = {}
        for v in self.votes:
            if v.candidate in tally:
                tally[v.candidate] += 1
            else:
                tally[v.candidate] = 1

        return tally
