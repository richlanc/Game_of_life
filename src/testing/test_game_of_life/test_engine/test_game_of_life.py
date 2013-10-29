'''
Created on 28.10.2013

@author: Michael and Geoff

This module contains and runs all the tests for the game_of_life module.
'''

from game_of_life.data_structures import grid, cell, state
from game_of_life.engine import game_of_life, rule_sets


class TestGameOfLife(object):
    '''
    This class contains and runs the tests for the GameOfLife class in the
    game_of_life module.
    '''
    
    def set_inital_input(self):
        '''
        Returns a pattern of cells to use as the 'initial input'
        in testing.
        '''
        cells = [[cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell(),
                  cell.Cell(state.Alive())],
                 [cell.Cell(),
                  cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell()],
                 [cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell(),
                  cell.Cell()],
                 [cell.Cell(),
                  cell.Cell(),
                  cell.Cell(),
                  cell.Cell()]]
        
        return cells
    
    def set_current_state(self):
        '''
        Returns a pattern of cells to use as the 'current generation'
        in testing.
        '''
        cells = [[cell.Cell(),
                  cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell()],
                 [cell.Cell(state.Alive()),
                  cell.Cell(state.Alive()),
                  cell.Cell(state.Alive()),
                  cell.Cell()],
                 [cell.Cell(),
                  cell.Cell(),
                  cell.Cell(),
                  cell.Cell()],
                 [cell.Cell(state.Alive()),
                  cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell()]]
        
        return cells
    
    def set_next_state(self):
        '''
        Returns a pattern of cells to use as the 'next generation'
        in testing.
        '''
        
        cells = [[cell.Cell(state.Alive()),
                  cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell()],
                 [cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell(state.Alive()),
                  cell.Cell(state.Alive())],
                 [cell.Cell(state.Alive()),
                  cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell()],
                 [cell.Cell(),
                  cell.Cell(state.Alive()),
                  cell.Cell(),
                  cell.Cell(state.Alive())]]
        
        return cells
    
    def test_init(self):
        '''
        Tests initialisation of a GameOfLife object. Also tests that
        the GameOfLife object initialises with the correct rule set.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        assert gol
        
        rs = gol._rule_set
        assert isinstance(rs, rule_sets.RuleSetStandard)
    
    def test_set_initial_input(self):
        '''
        Tests that the initial input can be successfully set. Also
        correct object has been set to initial input.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        
        # Create a grid and give it a pattern of cells:
        # dada
        # ddad
        # dadd
        # dddd
        gr = grid.Grid(4, 4)
        gr.set_cells(self.set_initial_input())
        
        # Give the Game of Life this grid as the initial input
        gol.set_initial_input(gr)
        
        # Test the initial input is now not none
        assert gol._initial_input
        
        # Test the initial input has been given the correct pattern
        test_pattern = self.set_initial_input()
        for x, row in enumerate(gol._initial_input):
            for y, c in enumerate(row):
                assert c.get_state() == test_pattern[x][y].get_state()        
    
    def test_get_initial_input(self):
        '''
        Tests that the initial input can be retrieved from storage
        and that the correct configuration has been retrieved.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        
        # Create a grid and give it a pattern of cells:
        # dada
        # ddad
        # dadd
        # dddd
        gr = grid.Grid(4, 4)
        gr.set_cells(self.set_initial_input())
        
        # Give the Game of Life this grid as the initial input
        gol.set_initial_input(gr)
        
        # Test the initial input can be retrieved
        retrieved_pattern = gol.get_initial_input()
        assert retrieved_pattern
        
        # Test the intial input has been given the correct pattern
        test_pattern = self.set_initial_input()
        for x, row in enumerate(retrieved_pattern):
            for y, c in enumerate(row):
                assert c.get_state() == test_pattern[x][y].get_state()
    
    def test_set_current_generation(self):
        '''
        Tests that the current generation can be stored and tests
        that the correct configuration has been stored.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        
        # Create a grid and give it a pattern of cells:
        # ddad
        # aaad
        # dddd
        # adad
        gr = grid.Grid(4, 4)
        gr.set_cells(self.set_current_state())
        
        # Give the Game of Life this grid as the current generation
        gol._set_current_generation(gr)
        
        # Test the current generation is not none
        assert gol._current_generation
        
        #Test the current generation has been given the correct pattern
        test_pattern = self.set_current_state()
        for x, row in enumerate(gol._current_generation):
            for y, c in enumerate(row):
                assert c.get_state() == test_pattern[x][y].get_state()
    
    def test_get_current_generation(self):
        '''
        Tests that the current generation can be retrieved from
        storage and that the correct configuration has been
        retrieved.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        
        # Create a grid and give it a pattern of cells:
        # ddad
        # aaad
        # dddd
        # adad
        gr = grid.Grid(4, 4)
        gr.set_cells(self.set_current_state())
        
        # Give the Game of Life this grid as the current generation
        gol._set_current_generation(gr)
        
        # Test the current generation can be retrieved
        retrieved_pattern = gol.get_current_generation()
        assert retrieved_pattern
        
        # Test that the correct pattern has been retrieved.
        test_pattern = self.set_current_state()
        for x, row in enumerate(retrieved_pattern):
            for y, c in enumerate(row):
                assert c.get_state() == test_pattern[x][y].get_state()
    
    def test_set_next_generation(self):
        '''
        Tests that the next generation can be stored and tests
        that the correct configuration has been stored.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        
        # Create a grid and give it a pattern of cells:
        # adad
        # daaa
        # adad
        # dada
        gr = grid.Grid(4, 4)
        gr.set_cells(self.set_next_state())
        
        # Give the Game of Life this grid as the next generation
        gol._set_next_generation(gr)
        
        # Test that the next generation is now not none
        assert gol._next_generation()
        
        # Test that the next generation has been set to the correct pattern
        test_pattern = self.set_next_state()
        for x, row in enumerate(gol._next_generation):
            for y, c in enumerate(row):
                assert c.get_state == test_pattern[x][y].get_state()
    
    def test_get_next_generation(self):
        '''
        Tests that the next generation can be retrieved from
        storage and tests that the correct configuration
        has been retrieved.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        
        # Create a grid and give it a pattern of cells:
        # adad
        # daaa
        # adad
        # dada
        gr = grid.Grid(4, 4)
        gr.set_cells(self.set_next_state())
        
        # Give the Game of Life this grid as the next generation
        gol._set_next_generation(gr)
        
        # Test that the next generation can be retrieved
        retrieved_pattern = gol.get_next_generation()
        assert retrieved_pattern
        
        # Test that the correct pattern has been retrieved.
        test_pattern = self.set_next_state()
        for x, row in enumerate(retrieved_pattern):
            for y, c in enumerate(row):
                assert c.get_state == test_pattern[x][y].get_state()
    
    def test_calculate_next_generation(self):
        '''
        Tests that the next generation of cells has been
        correctly calculated.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        # Create a grid and give it a pattern of cells:
        # ddad
        # aaad
        # dddd
        # adad
        # Represents the 'current generation'
        cur_gen = grid.Grid(4, 4)
        cur_gen.set_cells(self.set_current_state())
        
        #Create a grid and give it a pattern of cells:
        # adad
        # daaa
        # adad
        # dada
        # Represents the correct 'next generation'
        nex_gen = grid.Grid(4, 4)
        nex_gen.set_cells(self.set_next_state())
        
        # Give the Game of Life the first grid as the current generation
        gol._set_current_generation(cur_gen)
        
        # Let the Game of Life calculate the next generation.
        res = gol.calculate_next_generation(cur_gen)
        
        # Test the result against the correct result - if match, test passed
        for x, row in enumerate(res):
            for y, c in enumerate(row):
                assert c.get_state() == nex_gen[x][y].get_state()
    
    def test_first_turn(self):
        '''
        Tests that the first turn of the game retrieves
        the correct information from storage and calculates
        the first generation of cells in the correct way.
        '''
        gol = game_of_life.GameOfLife(rule_sets.RuleSetStandard())
        
        # Create a grid and give it a pattern of cells:
        # dada
        # ddad
        # dadd
        # dddd
        # Represents the initial input
        ini_inp = grid.Grid(4, 4)
        ini_inp.set_cells(self.set_inital_input())
        
        # Create a grid and give it a pattern of cells:
        # ddad
        # aaad
        # dddd
        # adad
        # Represents the correct first generation
        cur_gen = grid.Grid(4, 4)
        cur_gen.set_cells(self.set_current_state())
        
        # Give the Game of Life the first grid as the initial input
        gol.set_initial_input(ini_inp)
        
        # Run the first turn of the game.
        gol.first_turn()
        
        # Test that the initial input has been correctly stored
        retrieved_input = gol.get_initial_input()
        assert retrieved_input
        
        for x, row in enumerate(retrieved_input):
            for y, c in enumerate(row):
                assert c.get_state() == ini_inp.get_cells()[x][y].get_state()
                
        # Test that the current generation has been correctly stored
        
    def test_next_turn(self):
        '''
        Tests that the next turn of the game retrieves
        the correct information from storage and calculates
        the next generation of cells in the next way.
        '''
        # Create a grid and give it a pattern of cells:
        # ddad
        # aaad
        # dddd
        # adad
        # Represents the 'current generation'
        
        # Create a grid and give it a pattern of cells:
        # adad
        # daaa
        # adad
        # dada
        # Represents the correct 'next' generation
        
        # Give the Game of life the first table as the current generation
        # Run the next turn of the game.
        # Test that current generation has been correctly stored.
        pass
