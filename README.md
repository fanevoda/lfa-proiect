# NFA/DFA word acceptor

This is a Python script that implements an Deterministic Finite Automaton (DFA) and Non-Deterministic Finite Automaton (NFA) to check whether a given word is accepted or not.

# Input format

Firstly we'll describe the NFA/DFA by its transition table and its finale states.

```
q0 1 q0
q0 0 q1
q1 1 q0
q1 1 q0
q1 0 q2
q2 2 q3
q1 q3
```
And then give it the words we'd like it to check.
```
110001010
110101002
10101010
```

# Output format

The script outputs as many rows of text as there are words to be checked and they will be as follows.

`A list that showcases the path of the word's acceptance.`: If the given word is accepted by the integrated DFA/NFA.

`Rejected`: If the given word is not accepted by the integrated DFA/NFA.

For the input example shown above, the output would be:

```
Rejected
['q0', 'q0', 'q0', 'q1', 'q0', 'q1', 'q0', 'q1', 'q2', 'q3']
['q0', 'q0', 'q1', 'q0','q1', 'q0', 'q1', 'q0', 'q1']
```
