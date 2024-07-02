class Automata:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def __str__(self):
        return (f"Estados: {self.states}\n"
                f"Estado inicial: {self.initial_state}\n"
                f"Estado(s) final(is): {self.final_states}\n"   
                f"Alfabeto: {self.alphabet}\n"
                f"Transições: {self.transitions}\n")

def get_set(temp):
    return set(input(temp).split())

def get_transitions():
    transitions = {}
    while True:
        entry = input("Insira as transições do automato. Siga o formato ESTADO SÍMBOLO ESTADO (ex.: q0 a q1). Escreva FIM para concluir: ")
        if entry.lower() == 'fim':
            break
        current_state, symbol, next_state = entry.split()
        transitions[(current_state, symbol)] = next_state
    return transitions


