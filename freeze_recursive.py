from frozen_dict import FrozenDict

def freeze(obj):
    ''' Recursive function which turns dictionaries into 
        FrozenDict objects, lists into tuples, and sets
        into frozensets.

        THIS FUNCTION IS IN BETA AND HAS NOT BEEN
        EXTENSIVELY TESTED.
    '''

    try:
        #See if the object is hashable
        hash(obj)
        return obj
    except TypeError:
        pass

    # See if the object is iterable.  If not, raise an error
    try:
        itr = iter(obj)
        is_iterable = True
    except TypeError:
        is_iterable = False
        
    if not is_iterable:
        msg = 'Unsupported type: %r' % type(obj).__name__
        raise TypeError(msg)

    try:
        #Try to see if this is a mapping
        try:
            obj[tuple(obj)]
        except KeyError:
            pass
        is_mapping = True
    except TypeError:
        is_mapping = False
        
    if is_mapping:
        frz = {k: freeze(obj[k]) for k in obj}
        return FrozenDict(frz)

    # See if the object is a set like
    # or sequence like object
    try:
        obj[0]
        cls = tuple
    except TypeError:
        cls = frozenset
    except IndexError:
        cls = tuple

    return cls(freeze(i) for i in obj)
