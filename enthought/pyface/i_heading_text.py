#------------------------------------------------------------------------------
# Copyright (c) 2005, Enthought, Inc.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Enthought, Inc.
# Description: <Enthought pyface package component>
#------------------------------------------------------------------------------
""" Heading text. """


# Enthought library imports.
from enthought.traits.api import Instance, Int, Interface, Unicode

# Local imports.
from image_resource import ImageResource


class IHeadingText(Interface):
    """ Heading text. """

    #### 'IHeadingText' interface #############################################

    # Heading level.
    #
    # fixme: Currently we ignore anything but one, but in future we could
    # have different visualizations based on the level.
    level = Int(1)

    # The heading text.
    text = Unicode('Default')

    # The background image.
    image = Instance(ImageResource)


class MHeadingText(object):
    """ The mixin class that contains common code for toolkit specific
    implementations of the IHeadingText interface.
    """

#### EOF ######################################################################
