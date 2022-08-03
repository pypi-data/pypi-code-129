import numpy as np

from . import lib
from .decorators import requires_geos
from .enum import ParamEnum

__all__ = [
    "from_geojson",
    "from_wkb",
    "from_wkt",
    "to_geojson",
    "to_wkb",
    "to_wkt",
]


# Allowed options for handling WKB/WKT decoding errors
# Note: cannot use standard constructor since "raise" is a keyword
DecodingErrorOptions = ParamEnum(
    "DecodingErrorOptions", {"ignore": 0, "warn": 1, "raise": 2}
)


def to_wkt(
    geometry,
    rounding_precision=6,
    trim=True,
    output_dimension=3,
    old_3d=False,
    **kwargs,
):
    """
    Converts to the Well-Known Text (WKT) representation of a Geometry.

    The Well-known Text format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKT serialization:

    - for GEOS <= 3.8 a multipoint with an empty sub-geometry will raise an exception
    - for GEOS <= 3.8 empty geometries are always serialized to 2D
    - for GEOS >= 3.9 only simple empty geometries can be 3D, collections are still
      always 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    rounding_precision : int, default 6
        The rounding precision when writing the WKT string. Set to a value of
        -1 to indicate the full precision.
    trim : bool, default True
        If True, trim unnecessary decimals (trailing zeros).
    output_dimension : int, default 3
        The output dimension for the WKT string. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKT string.
    old_3d : bool, default False
        Enable old style 3D/4D WKT generation. By default, new style 3D/4D WKT
        (ie. "POINT Z (10 20 30)") is returned, but with ``old_3d=True``
        the WKT will be formatted in the style "POINT (10 20 30)".
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import Point
    >>> to_wkt(Point(0, 0))
    'POINT (0 0)'
    >>> to_wkt(Point(0, 0), rounding_precision=3, trim=False)
    'POINT (0.000 0.000)'
    >>> to_wkt(Point(0, 0), rounding_precision=-1, trim=False)
    'POINT (0.0000000000000000 0.0000000000000000)'
    >>> to_wkt(Point(1, 2, 3), trim=True)
    'POINT Z (1 2 3)'
    >>> to_wkt(Point(1, 2, 3), trim=True, output_dimension=2)
    'POINT (1 2)'
    >>> to_wkt(Point(1, 2, 3), trim=True, old_3d=True)
    'POINT (1 2 3)'

    Notes
    -----
    The defaults differ from the default of the GEOS library. To mimic this,
    use::

        to_wkt(geometry, rounding_precision=-1, trim=False, output_dimension=2)

    """
    if not np.isscalar(rounding_precision):
        raise TypeError("rounding_precision only accepts scalar values")
    if not np.isscalar(trim):
        raise TypeError("trim only accepts scalar values")
    if not np.isscalar(output_dimension):
        raise TypeError("output_dimension only accepts scalar values")
    if not np.isscalar(old_3d):
        raise TypeError("old_3d only accepts scalar values")

    return lib.to_wkt(
        geometry,
        np.intc(rounding_precision),
        np.bool_(trim),
        np.intc(output_dimension),
        np.bool_(old_3d),
        **kwargs,
    )


def to_wkb(
    geometry, hex=False, output_dimension=3, byte_order=-1, include_srid=False, **kwargs
):
    r"""
    Converts to the Well-Known Binary (WKB) representation of a Geometry.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    The following limitations apply to WKB serialization:

    - linearrings will be converted to linestrings
    - a point with only NaN coordinates is converted to an empty point
    - for GEOS <= 3.7, empty points are always serialized to 3D if
      output_dimension=3, and to 2D if output_dimension=2
    - for GEOS == 3.8, empty points are always serialized to 2D

    Parameters
    ----------
    geometry : Geometry or array_like
    hex : bool, default False
        If true, export the WKB as a hexidecimal string. The default is to
        return a binary bytes object.
    output_dimension : int, default 3
        The output dimension for the WKB. Supported values are 2 and 3.
        Specifying 3 means that up to 3 dimensions will be written but 2D
        geometries will still be represented as 2D in the WKB represenation.
    byte_order : int, default -1
        Defaults to native machine byte order (-1). Use 0 to force big endian
        and 1 for little endian.
    include_srid : bool, default False
        If True, the SRID is be included in WKB (this is an extension
        to the OGC WKB specification).
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_wkb(point, byte_order=1)
    b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?'
    >>> to_wkb(point, hex=True, byte_order=1)
    '0101000000000000000000F03F000000000000F03F'
    """
    if not np.isscalar(hex):
        raise TypeError("hex only accepts scalar values")
    if not np.isscalar(output_dimension):
        raise TypeError("output_dimension only accepts scalar values")
    if not np.isscalar(byte_order):
        raise TypeError("byte_order only accepts scalar values")
    if not np.isscalar(include_srid):
        raise TypeError("include_srid only accepts scalar values")

    return lib.to_wkb(
        geometry,
        np.bool_(hex),
        np.intc(output_dimension),
        np.intc(byte_order),
        np.bool_(include_srid),
        **kwargs,
    )


@requires_geos("3.10.0")
def to_geojson(geometry, indent=None, **kwargs):
    """Converts to the GeoJSON representation of a Geometry.

    The GeoJSON format is defined in the `RFC 7946 <https://geojson.org/>`__.
    NaN (not-a-number) coordinates will be written as 'null'.

    The following are currently unsupported:

    - Geometries of type LINEARRING: these are output as 'null'.
    - Three-dimensional geometries: the third dimension is ignored.

    Parameters
    ----------
    geometry : str, bytes or array_like
    indent : int, optional
        If indent is a non-negative integer, then GeoJSON will be formatted.
        An indent level of 0 will only insert newlines. None (the default)
        selects the most compact representation.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import Point
    >>> point = Point(1, 1)
    >>> to_geojson(point)
    '{"type":"Point","coordinates":[1.0,1.0]}'
    >>> print(to_geojson(point, indent=2))
    {
      "type": "Point",
      "coordinates": [
          1.0,
          1.0
      ]
    }
    """
    # GEOS Tickets:
    # - handle linearrings: https://trac.osgeo.org/geos/ticket/1140
    # - support 3D: https://trac.osgeo.org/geos/ticket/1141
    if indent is None:
        indent = -1
    elif not np.isscalar(indent):
        raise TypeError("indent only accepts scalar values")
    elif indent < 0:
        raise ValueError("indent cannot be negative")

    return lib.to_geojson(geometry, np.intc(indent), **kwargs)


def from_wkt(geometry, on_invalid="raise", **kwargs):
    """
    Creates geometries from the Well-Known Text (WKT) representation.

    The Well-known Text format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.

    Parameters
    ----------
    geometry : str or array_like
        The WKT string(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if WKT input geometries are invalid.
        - warn: a warning will be raised and invalid WKT geometries will be
          returned as ``None``.
        - ignore: invalid WKT geometries will be returned as ``None`` without a warning.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from_wkt('POINT (0 0)')
    <POINT (0 0)>
    """
    if not np.isscalar(on_invalid):
        raise TypeError("on_invalid only accepts scalar values")

    invalid_handler = np.uint8(DecodingErrorOptions.get_value(on_invalid))

    return lib.from_wkt(geometry, invalid_handler, **kwargs)


def from_wkb(geometry, on_invalid="raise", **kwargs):
    r"""
    Creates geometries from the Well-Known Binary (WKB) representation.

    The Well-Known Binary format is defined in the `OGC Simple Features
    Specification for SQL <https://www.opengeospatial.org/standards/sfs>`__.


    Parameters
    ----------
    geometry : str or array_like
        The WKB byte object(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if a WKB input geometry is invalid.
        - warn: a warning will be raised and invalid WKB geometries will be
          returned as ``None``.
        - ignore: invalid WKB geometries will be returned as ``None`` without a warning.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from_wkb(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\xf0?')
    <POINT (1 1)>
    """

    if not np.isscalar(on_invalid):
        raise TypeError("on_invalid only accepts scalar values")

    invalid_handler = np.uint8(DecodingErrorOptions.get_value(on_invalid))

    # ensure the input has object dtype, to avoid numpy inferring it as a
    # fixed-length string dtype (which removes trailing null bytes upon access
    # of array elements)
    geometry = np.asarray(geometry, dtype=object)
    return lib.from_wkb(geometry, invalid_handler, **kwargs)


@requires_geos("3.10.1")
def from_geojson(geometry, on_invalid="raise", **kwargs):
    """Creates geometries from GeoJSON representations (strings).

    If a GeoJSON is a FeatureCollection, it is read as a single geometry
    (with type GEOMETRYCOLLECTION). This may be unpacked using the ``pygeos.get_parts``.
    Properties are not read.

    The GeoJSON format is defined in `RFC 7946 <https://geojson.org/>`__.

    The following are currently unsupported:

    - Three-dimensional geometries: the third dimension is ignored.
    - Geometries having 'null' in the coordinates.

    Parameters
    ----------
    geometry : str, bytes or array_like
        The GeoJSON string or byte object(s) to convert.
    on_invalid : {"raise", "warn", "ignore"}, default "raise"
        - raise: an exception will be raised if an input GeoJSON is invalid.
        - warn: a warning will be raised and invalid input geometries will be
          returned as ``None``.
        - ignore: invalid input geometries will be returned as ``None`` without a warning.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    See also
    --------
    get_parts

    Examples
    --------
    >>> from_geojson('{"type": "Point","coordinates": [1, 2]}')
    <POINT (1 2)>
    """
    # GEOS Tickets:
    # - support 3D: https://trac.osgeo.org/geos/ticket/1141
    # - handle null coordinates: https://trac.osgeo.org/geos/ticket/1142
    if not np.isscalar(on_invalid):
        raise TypeError("on_invalid only accepts scalar values")

    invalid_handler = np.uint8(DecodingErrorOptions.get_value(on_invalid))

    # ensure the input has object dtype, to avoid numpy inferring it as a
    # fixed-length string dtype (which removes trailing null bytes upon access
    # of array elements)
    geometry = np.asarray(geometry, dtype=object)

    return lib.from_geojson(geometry, invalid_handler, **kwargs)
