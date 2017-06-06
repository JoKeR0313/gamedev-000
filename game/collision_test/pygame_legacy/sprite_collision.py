def collide_rect(left, right):
    """collision detection between two sprites, using rects.

    pygame.sprite.collide_rect(left, right): return bool

    Tests for collision between two sprites. Uses the pygame.Rect colliderect
    function to calculate the collision. It is intended to be passed as a
    collided callback function to the *collide functions. Sprites must have
    "rect" attributes.

    New in pygame 1.8.0

    """
    return left.rect.colliderect(right.rect)


class collide_rect_ratio:
    """A callable class that checks for collisions using scaled rects

    The class checks for collisions between two sprites using a scaled version
    of the sprites' rects. Is created with a ratio; the instance is then
    intended to be passed as a collided callback function to the *collide
    functions.

    New in pygame 1.8.1

    """

    def __init__(self, ratio):
        """create a new collide_rect_ratio callable

        Ratio is expected to be a floating point value used to scale
        the underlying sprite rect before checking for collisions.

        """
        self.ratio = ratio

    def __call__(self, left, right):
        """detect collision between two sprites using scaled rects

        pygame.sprite.collide_rect_ratio(ratio)(left, right): return bool

        Tests for collision between two sprites. Uses the pygame.Rect
        colliderect function to calculate the collision after scaling the rects
        by the stored ratio. Sprites must have "rect" attributes.

        """

        ratio = self.ratio

        leftrect = left.rect
        width = leftrect.width
        height = leftrect.height
        leftrect = leftrect.inflate(width * ratio - width,
                                    height * ratio - height)

        rightrect = right.rect
        width = rightrect.width
        height = rightrect.height
        rightrect = rightrect.inflate(width * ratio - width,
                                      height * ratio - height)

        return leftrect.colliderect(rightrect)


def collide_circle(left, right):
    """detect collision between two sprites using circles

    pygame.sprite.collide_circle(left, right): return bool

    Tests for collision between two sprites by testing whether two circles
    centered on the sprites overlap. If the sprites have a "radius" attribute,
    then that radius is used to create the circle; otherwise, a circle is
    created that is big enough to completely enclose the sprite's rect as
    given by the "rect" attribute. This function is intended to be passed as
    a collided callback function to the *collide functions. Sprites must have a
    "rect" and an optional "radius" attribute.

    New in pygame 1.8.0

    """

    xdistance = left.rect.centerx - right.rect.centerx
    ydistance = left.rect.centery - right.rect.centery
    distancesquared = xdistance ** 2 + ydistance ** 2

    if hasattr(left, 'radius'):
        leftradius = left.radius
    else:
        leftrect = left.rect
        # approximating the radius of a square by using half of the diagonal,
        # might give false positives (especially if its a long small rect)
        leftradius = 0.5 * \
            ((leftrect.width ** 2 + leftrect.height ** 2) ** 0.5)
        # store the radius on the sprite for next time
        setattr(left, 'radius', leftradius)

    if hasattr(right, 'radius'):
        rightradius = right.radius
    else:
        rightrect = right.rect
        # approximating the radius of a square by using half of the diagonal
        # might give false positives (especially if its a long small rect)
        rightradius = 0.5 * \
            ((rightrect.width ** 2 + rightrect.height ** 2) ** 0.5)
        # store the radius on the sprite for next time
        setattr(right, 'radius', rightradius)
    return distancesquared <= (leftradius + rightradius) ** 2


class collide_circle_ratio(object):
    """detect collision between two sprites using scaled circles

    This callable class checks for collisions between two sprites using a
    scaled version of a sprite's radius. It is created with a ratio as the
    argument to the constructor. The instance is then intended to be passed as
    a collided callback function to the *collide functions.

    New in pygame 1.8.1

    """

    def __init__(self, ratio):
        """creates a new collide_circle_ratio callable instance

        The given ratio is expected to be a floating point value used to scale
        the underlying sprite radius before checking for collisions.

        When the ratio is ratio=1.0, then it behaves exactly like the 
        collide_circle method.

        """
        self.ratio = ratio

    def __call__(self, left, right):
        """detect collision between two sprites using scaled circles

        pygame.sprite.collide_circle_radio(ratio)(left, right): return bool

        Tests for collision between two sprites by testing whether two circles
        centered on the sprites overlap after scaling the circle's radius by
        the stored ratio. If the sprites have a "radius" attribute, that is
        used to create the circle; otherwise, a circle is created that is big
        enough to completely enclose the sprite's rect as given by the "rect"
        attribute. Intended to be passed as a collided callback function to the
        *collide functions. Sprites must have a "rect" and an optional "radius"
        attribute.

        """

        ratio = self.ratio
        xdistance = left.rect.centerx - right.rect.centerx
        ydistance = left.rect.centery - right.rect.centery
        distancesquared = xdistance ** 2 + ydistance ** 2

        if hasattr(left, "radius"):
            leftradius = left.radius * ratio
        else:
            leftrect = left.rect
            leftradius = ratio * 0.5 * \
                ((leftrect.width ** 2 + leftrect.height ** 2) ** 0.5)
            # store the radius on the sprite for next time
            setattr(left, 'radius', leftradius)

        if hasattr(right, "radius"):
            rightradius = right.radius * ratio
        else:
            rightrect = right.rect
            rightradius = ratio * 0.5 * \
                ((rightrect.width ** 2 + rightrect.height ** 2) ** 0.5)
            # store the radius on the sprite for next time
            setattr(right, 'radius', rightradius)

        return distancesquared <= (leftradius + rightradius) ** 2


def collide_mask(left, right):
    """collision detection between two sprites, using masks.

    pygame.sprite.collide_mask(SpriteLeft, SpriteRight): bool

    Tests for collision between two sprites by testing if their bitmasks
    overlap. If the sprites have a "mask" attribute, that is used as the mask;
    otherwise, a mask is created from the sprite image. Intended to be passed
    as a collided callback function to the *collide functions. Sprites must
    have a "rect" and an optional "mask" attribute.

    New in pygame 1.8.0

    """
    xoffset = right.rect[0] - left.rect[0]
    yoffset = right.rect[1] - left.rect[1]
    try:
        leftmask = left.mask
    except AttributeError:
        leftmask = from_surface(left.image)
    try:
        rightmask = right.mask
    except AttributeError:
        rightmask = from_surface(right.image)
    return leftmask.overlap(rightmask, (xoffset, yoffset))


def spritecollide(sprite, group, dokill, collided=None):
    """find Sprites in a Group that intersect another Sprite

    pygame.sprite.spritecollide(sprite, group, dokill, collided=None):
        return Sprite_list

    Return a list containing all Sprites in a Group that intersect with another
    Sprite. Intersection is determined by comparing the Sprite.rect attribute
    of each Sprite.

    The dokill argument is a bool. If set to True, all Sprites that collide
    will be removed from the Group.

    The collided argument is a callback function used to calculate if two
    sprites are colliding. it should take two sprites as values, and return a
    bool value indicating if they are colliding. If collided is not passed, all
    sprites must have a "rect" value, which is a rectangle of the sprite area,
    which will be used to calculate the collision.

    """
    if dokill:

        crashed = []
        append = crashed.append

        if collided:
            for s in group.sprites():
                if collided(sprite, s):
                    s.kill()
                    append(s)
        else:
            spritecollide = sprite.rect.colliderect
            for s in group.sprites():
                if spritecollide(s.rect):
                    s.kill()
                    append(s)

        return crashed

    elif collided:
        return [s for s in group if collided(sprite, s)]
    else:
        spritecollide = sprite.rect.colliderect
        return [s for s in group if spritecollide(s.rect)]


def groupcollide(groupa, groupb, dokilla, dokillb, collided=None):
    """detect collision between a group and another group

    pygame.sprite.groupcollide(groupa, groupb, dokilla, dokillb):
        return dict

    Given two groups, this will find the intersections between all sprites in
    each group. It returns a dictionary of all sprites in the first group that
    collide. The value for each item in the dictionary is a list of the sprites
    in the second group it collides with. The two dokill arguments control if
    the sprites from either group will be automatically removed from all
    groups. Collided is a callback function used to calculate if two sprites
    are colliding. it should take two sprites as values, and return a bool
    value indicating if they are colliding. If collided is not passed, all
    sprites must have a "rect" value, which is a rectangle of the sprite area
    that will be used to calculate the collision.

    """
    crashed = {}
    SC = spritecollide
    if dokilla:
        for s in groupa.sprites():
            c = SC(s, groupb, dokillb, collided)
            if c:
                crashed[s] = c
                s.kill()
    else:
        for s in groupa:
            c = SC(s, groupb, dokillb, collided)
            if c:
                crashed[s] = c
    return crashed


def spritecollideany(sprite, group, collided=None):
    """finds any sprites in a group that collide with the given sprite

    pygame.sprite.spritecollideany(sprite, group): return sprite

    Given a sprite and a group of sprites, this will return return any single
    sprite that collides with with the given sprite. If there are no
    collisions, then this returns None.

    If you don't need all the features of the spritecollide function, this
    function will be a bit quicker.

    Collided is a callback function used to calculate if two sprites are
    colliding. It should take two sprites as values and return a bool value
    indicating if they are colliding. If collided is not passed, then all
    sprites must have a "rect" value, which is a rectangle of the sprite area,
    which will be used to calculate the collision.

    """
    if collided:
        for s in group:
            if collided(sprite, s):
                return s
    else:
        # Special case old behaviour for speed.
        spritecollide = sprite.rect.colliderect
        for s in group:
            if spritecollide(s.rect):
                return s
    return None
