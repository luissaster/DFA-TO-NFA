import automata as au

# Receber como entrada um AFD ou um AFN
# Converter AFN em AFD
# Simular aceitação de palavras no AFD e no AFN
# Demonstrar equivalência entre AFN e AFD
# Minimizar AFDs
# Front End

def main():
    print("------Inserção do AFD------")
    states = au.get_set("Insira os estados (separados por um espaço): ")
    initial_state = input("Insira o estado inicial: ")
    final_states = au.get_set("Insira o(s) estado(s) final(is) (separados por um espaço): ")
    alphabet = au.get_set("Insira o alfabeto (separados por um espaço): ")
    transitions = au.get_transitions()

    newAutomata = au.Automata(states, alphabet, transitions, initial_state, final_states)
    print("Automato criado")
    print(newAutomata)

    au.convert_to_dfa(newAutomata)

if __name__ == "__main__":
    main()