# lexcel-global-explainability

Once in the lexcel-explainability2/ folder, launch command is 

python3 main.py

(NB: an interactive menu allows for manual input setting)



lexcel contains pre-processing + evaluation functions: 
  - given a list of coalitions associated with an evaluation (generated at random for now), ordered_coals returns the induced preorder over coalitions
  - given a preorder over coalitions, ordered_ind returns the preorder over individuals obtained using lex-cel


voting_rules contains aggregation functions. Given a list of votes (preorder over individuals), each method returns the preorder resulting for aggregation
