"""
Geometry factories based on the geo interface
"""
import numpy as np

from shapely.errors import GeometryTypeError

from .collection import GeometryCollection
from .linestring import LineString
from .multilinestring import MultiLineString
from .multipoint import MultiPoint
from .multipolygon import MultiPolygon
from .point import Point
from .polygon import LinearRing, Polygon


def _is_coordinates_empty(coordinates):
    """Helper to identify if coordinates or subset of coordinates are empty"""

    if coordinates is None:
        return True

    if isinstance(coordinates, (list, tuple, np.ndarray)):
        if len(coordinates) == 0:
            return True
        return all(map(_is_coordinates_empty, coordinates))
    else:
        return False


def _empty_shape_for_no_coordinates(geom_type):
    """Return empty counterpart for geom_type"""
    if geom_type == "point":
        return Point()
    elif geom_type == "multipoint":
        return MultiPoint()
    elif geom_type == "linestring":
        return LineString()
    elif geom_type == "multilinestring":
        return MultiLineString()
    elif geom_type == "polygon":
        return Polygon()
    elif geom_type == "multipolygon":
        return MultiPolygon()
    else:
        raise GeometryTypeError("Unknown geometry type: %s" % geom_type)


def box(minx, miny, maxx, maxy, ccw=True):
    """Returns a rectangular polygon with configurable normal vector"""
    coords = [(maxx, miny), (maxx, maxy), (minx, maxy), (minx, miny)]
    if not ccw:
        coords = coords[::-1]
    return Polygon(coords)


def shape(context):
    """
    Returns a new, independent geometry with coordinates *copied* from the
    context. Changes to the original context will not be reflected in the
    geometry object.

    Parameters
    ----------
    context :
        a GeoJSON-like dict, which provides a "type" member describing the type
        of the geometry and "coordinates" member providing a list of coordinates,
        or an object which implements __geo_interface__.

    Returns
    -------
    Geometry object

    Examples
    --------
    Create a Point from GeoJSON, and then create a copy using __geo_interface__.

    >>> context = {'type': 'Point', 'coordinates': [0, 1]}
    >>> geom = shape(context)
    >>> geom.type == 'Point'
    True
    >>> geom.wkt
    'POINT (0 1)'
    >>> geom2 = shape(geom)
    >>> geom == geom2
    True
    """
    if hasattr(context, "__geo_interface__"):
        ob = context.__geo_interface__
    else:
        ob = context
    geom_type = ob.get("type").lower()
    if "coordinates" in ob and _is_coordinates_empty(ob["coordinates"]):
        return _empty_shape_for_no_coordinates(geom_type)
    elif geom_type == "point":
        return Point(ob["coordinates"])
    elif geom_type == "linestring":
        return LineString(ob["coordinates"])
    elif geom_type == "linearring":
        return LinearRing(ob["coordinates"])
    elif geom_type == "polygon":
        return Polygon(ob["coordinates"][0], ob["coordinates"][1:])
    elif geom_type == "multipoint":
        return MultiPoint(ob["coordinates"])
    elif geom_type == "multilinestring":
        return MultiLineString(ob["coordinates"])
    elif geom_type == "multipolygon":
        return MultiPolygon([[c[0], c[1:]] for c in ob["coordinates"]])
    elif geom_type == "geometrycollection":
        geoms = [shape(g) for g in ob.get("geometries", [])]
        return GeometryCollection(geoms)
    else:
        raise GeometryTypeError("Unknown geometry type: %s" % geom_type)


def mapping(ob):
    """
    Returns a GeoJSON-like mapping from a Geometry or any
    object which implements __geo_interface__

    Parameters
    ----------
    ob :
        An object which implements __geo_interface__.

    Returns
    -------
    dict

    Examples
    --------
    >>> pt = Point(0, 0)
    >>> mapping(pt)
    {'type': 'Point', 'coordinates': (0.0, 0.0)}
    """
    return ob.__geo_interface__
