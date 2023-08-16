from __future__ import print_function
from game import sd_peers, sd_spots, sd_domain_num, init_domains, \
    restrict_domain, SD_DIM, SD_SIZE
import random, copy

class AI:
    def __init__(self):
        pass

    def solve(self, problem):
        domains = init_domains()
        restrict_domain(domains, problem) 

        decision_stack = []
        assignment = {}

        # TODO: implement backtracking search. 

        while True:
            assignment["conflict"] = 0 # Conflict indicator
            assignment, domains = self.propagate(assignment, domains)
            if assignment["conflict"] != 1:
                if len(assignment) >= SD_SIZE*SD_SIZE:
                    return domains
                else:
                    assignment, spot = self.make_decision(assignment, domains)
                    decision_stack.append([copy.deepcopy(assignment), spot, copy.deepcopy(domains)])    
            else:
                if len(decision_stack) == 0:
                    return None
                else:
                    assignment, domains = self.backtrack(decision_stack)
                

    # TODO: add any supporting function you need
    def propagate(self, assignment, domains):
        while True:

            for spot in sd_spots:
                if len(domains[spot]) == 1:
                    assignment[spot] = domains[spot][0]
            
            for spot in assignment.keys():
                if spot != "conflict":
                    domains[spot] = [assignment[spot]]
            
            for spot in sd_spots:
                if domains[spot] == []:
                    assignment["conflict"] = 1
                    return assignment, domains
                
            conflict = False
            for spot in sd_spots:
                for peer in sd_peers[spot]:
                    if len(domains[peer]) == 1:
                        if domains[peer][0] in domains[spot]:
                            conflict = True
                            domains[spot].remove(domains[peer][0])
            
            if not conflict:
                return assignment, domains
            
    
    def make_decision(self, assignment, domains):
        for spot in sd_spots:
            if len(domains[spot]) > 1:
                assignment[spot] = domains[spot][0]
                return assignment, spot


    def backtrack(self, decision_stack):
        assignment, spot, domains = decision_stack.pop()
        num = assignment[spot]
        assignment.pop(spot, None)
        if num in domains[spot]:
            domains[spot].remove(num)
        return assignment, domains
    

    #### The following templates are only useful for the EC part #####

    # EC: parses "problem" into a SAT problem
    # of input form to the program 'picoSAT';
    # returns a string usable as input to picoSAT
    # (do not write to file)
    def sat_encode(self, problem):
        text = ""

        
        # TODO: write CNF specifications to 'text'

        return text

    # EC: takes as input the dictionary mapping 
    # from variables to T/F assignments solved for by picoSAT;
    # returns a domain dictionary of the same form 
    # as returned by solve()
    def sat_decode(self, assignments):
        # TODO: decode 'assignments' into domains
        
        # TODO: delete this ->
        domains = {}
        for spot in sd_spots:
            domains[spot] = [1]
        return domains
        # <- TODO: delete this