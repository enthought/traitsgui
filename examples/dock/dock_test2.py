#-------------------------------------------------------------------------------
#
#  Test the DockWindow.
#
#  Written by: David C. Morrill
#
#  Date: 10/20/2005
#
#  (c) Copyright 2005 by Enthought, Inc.
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

import sys

from enthought.traits.api \
    import *

from enthought.traits.ui.api \
    import *

from enthought.traits.ui.menu \
    import *

#-------------------------------------------------------------------------------
#  'TestDock' class:
#-------------------------------------------------------------------------------

class TestDock ( HasPrivateTraits ):

    #---------------------------------------------------------------------------
    #  Trait definitions:
    #---------------------------------------------------------------------------

    button1 = Button
    button2 = Button
    button3 = Button
    button4 = Button
    button5 = Button
    button6 = Button

    #---------------------------------------------------------------------------
    #  Traits view definitions:
    #---------------------------------------------------------------------------

    view = View( [ 'button1' ],
                 [ 'button2' ],
                 [ 'button3' ],
                 [ 'button4' ],
                 [ 'button5' ],
                 [ 'button6' ],
                 title     = 'DockWindow Test',
                 resizable = True,
                 width     = 0.5,
                 height    = 0.5,
                 buttons   = NoButtons )

#-------------------------------------------------------------------------------
#  Run the test program:
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    TestDock().configure_traits()
