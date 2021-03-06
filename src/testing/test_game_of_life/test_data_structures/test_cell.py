'''
Created on 20 Oct 2013

@author: Michael and Richard
'''

from game_of_life.data_structures.cell import GolCell
from game_of_life.data_structures.states import Alive, Dead


def initialise_cell():
    '''
    Abstracted initialisation as it was being repeated
    '''
    return GolCell()


class TestCell(object):
    '''
    Tests the functionality of the cell module
    '''

    def test_cell_init(self):
        '''
        Test initialisation of Cell object
        '''
        assert initialise_cell()

    def test_get_state(self):
        '''
        Test correct functionality of Cell's accessor method
        '''
        c = initialise_cell()
        s = c.get_state()
        # Make sure it returned a state
        assert s
        # Make sure the state was Dead
        assert isinstance(s, Dead)

    def test_is_alive(self):
        '''
        Test whether the cell knows it is alive.
        '''
        c = GolCell(Alive())
        assert c.is_alive()

        c = initialise_cell()
        assert not c.is_alive()

    def test_set_state(self):
        '''
        Test correct functionality of Cell's mutator method
        '''
        c = initialise_cell()
        c.set_state(Alive())
        s = c.get_state()
        # Ensure that a state was set correct
        assert s
        # Ensure that state was set as alive
        assert isinstance(s, Alive)
