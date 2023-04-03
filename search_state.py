import pandas


class SearchState:
    def __init__(self):
        self.data = pandas.read_csv("50_states.csv")
        self.states = self.data.state.tolist()
        self.state = []

    def check_state(self, answer_state):
        if answer_state in self.states:
            return True
        else:
            return False

    def get_state_cor(self, answer_state):
        self.state = self.data[self.data.state == answer_state]
        self.state = self.state.values.tolist()
        self.state = self.state[0]
        return self.state

    def not_guessed_states(self, guessed_states):
        for state in self.states:
            if state in guessed_states:
                self.states.remove(state)
        return self.states
