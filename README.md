# fuzzy-set-django

I implemented the core logic of fuzzy sets in a very practical way. The system takes input in the form of (element : membership value) pairs and processes it to compute two important concepts. First, the Support Set, which includes all elements whose membership value is greater than 0 , meaning they have some presence in the set. Second, the Alpha where we filter elements whose membership value is greater than or equal to a chosen threshold value. This helped me clearly understand how fuzzy logic transitions into crisp decision-making based on conditions. 
