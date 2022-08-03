import numpy as np

from . import lib
from .decorators import multithreading_enabled, requires_geos
from .enum import ParamEnum

__all__ = [
    "BufferCapStyles",
    "BufferJoinStyles",
    "boundary",
    "buffer",
    "offset_curve",
    "centroid",
    "clip_by_rect",
    "convex_hull",
    "delaunay_triangles",
    "segmentize",
    "envelope",
    "extract_unique_points",
    "build_area",
    "make_valid",
    "normalize",
    "point_on_surface",
    "polygonize",
    "polygonize_full",
    "reverse",
    "simplify",
    "snap",
    "voronoi_polygons",
    "oriented_envelope",
    "minimum_rotated_rectangle",
    "minimum_bounding_circle",
]


class BufferCapStyles(ParamEnum):
    round = 1
    flat = 2
    square = 3


class BufferJoinStyles(ParamEnum):
    round = 1
    mitre = 2
    bevel = 3


@multithreading_enabled
def boundary(geometry, **kwargs):
    """Returns the topological boundary of a geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
        This function will return None for geometrycollections.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import GeometryCollection, LinearRing, LineString, \
MultiLineString, MultiPoint, Point, Polygon
    >>> boundary(Point(0, 0))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(LineString([(0, 0), (1, 1), (1, 2)]))
    <MULTIPOINT (0 0, 1 2)>
    >>> boundary(LinearRing([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT EMPTY>
    >>> boundary(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <LINESTRING (0 0, 1 0, 1 1, 0 1, 0 0)>
    >>> boundary(MultiPoint([(0, 0), (1, 2)]))
    <GEOMETRYCOLLECTION EMPTY>
    >>> boundary(MultiLineString([[(0, 0), (1, 1)], [(0, 1), (1, 0)]]))
    <MULTIPOINT (0 0, 0 1, 1 0, 1 1)>
    >>> boundary(GeometryCollection([Point(0, 0)])) is None
    True
    """
    return lib.boundary(geometry, **kwargs)


@multithreading_enabled
def buffer(
    geometry,
    radius,
    quadsegs=8,
    cap_style="round",
    join_style="round",
    mitre_limit=5.0,
    single_sided=False,
    **kwargs
):
    """
    Computes the buffer of a geometry for positive and negative buffer radius.

    The buffer of a geometry is defined as the Minkowski sum (or difference,
    for negative width) of the geometry with a circle with radius equal to the
    absolute value of the buffer radius.

    The buffer operation always returns a polygonal result. The negative
    or zero-distance buffer of lines and points is always empty.

    Parameters
    ----------
    geometry : Geometry or array_like
    width : float or array_like
        Specifies the circle radius in the Minkowski sum (or difference).
    quadsegs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    cap_style : {'round', 'square', 'flat'}, default 'round'
        Specifies the shape of buffered line endings. 'round' results in
        circular line endings (see ``quadsegs``). Both 'square' and 'flat'
        result in rectangular line endings, only 'flat' will end at the
        original vertex, while 'square' involves adding the buffer width.
    join_style : {'round', 'bevel', 'mitre'}, default 'round'
        Specifies the shape of buffered line midpoints. 'round' results in
        rounded shapes. 'bevel' results in a beveled edge that touches the
        original vertex. 'mitre' results in a single vertex that is beveled
        depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    single_sided : bool, default False
        Only buffer at one side of the geometry.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon
    >>> buffer(Point(10, 10), 2, quadsegs=1)
    <POLYGON ((12 10, 10 8, 8 10, 10 12, 12 10))>
    >>> buffer(Point(10, 10), 2, quadsegs=2)
    <POLYGON ((12 10, 11.414 8.586, 10 8, 8.586 8.586, 8 10, 8.5...>
    >>> buffer(Point(10, 10), -2, quadsegs=1)
    <POLYGON EMPTY>
    >>> line = LineString([(10, 10), (20, 10)])
    >>> buffer(line, 2, cap_style="square")
    <POLYGON ((20 12, 22 12, 22 8, 10 8, 8 8, 8 12, 20 12))>
    >>> buffer(line, 2, cap_style="flat")
    <POLYGON ((20 12, 20 8, 10 8, 10 12, 20 12))>
    >>> buffer(line, 2, single_sided=True, cap_style="flat")
    <POLYGON ((20 10, 10 10, 10 12, 20 12, 20 10))>
    >>> line2 = LineString([(10, 10), (20, 10), (20, 20)])
    >>> buffer(line2, 2, cap_style="flat", join_style="bevel")
    <POLYGON ((18 12, 18 20, 22 20, 22 10, 20 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre")
    <POLYGON ((18 12, 18 20, 22 20, 22 8, 10 8, 10 12, 18 12))>
    >>> buffer(line2, 2, cap_style="flat", join_style="mitre", mitre_limit=1)
    <POLYGON ((18 12, 18 20, 22 20, 22 9.172, 20.828 8, 10 8, 10 12, 18 12))>
    >>> square = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> buffer(square, 2, join_style="mitre")
    <POLYGON ((-2 -2, -2 12, 12 12, 12 -2, -2 -2))>
    >>> buffer(square, -2, join_style="mitre")
    <POLYGON ((2 2, 2 8, 8 8, 8 2, 2 2))>
    >>> buffer(square, -5, join_style="mitre")
    <POLYGON EMPTY>
    >>> buffer(line, float("nan")) is None
    True
    """
    if isinstance(cap_style, str):
        cap_style = BufferCapStyles.get_value(cap_style)
    if isinstance(join_style, str):
        join_style = BufferJoinStyles.get_value(join_style)
    if not np.isscalar(quadsegs):
        raise TypeError("quadsegs only accepts scalar values")
    if not np.isscalar(cap_style):
        raise TypeError("cap_style only accepts scalar values")
    if not np.isscalar(join_style):
        raise TypeError("join_style only accepts scalar values")
    if not np.isscalar(mitre_limit):
        raise TypeError("mitre_limit only accepts scalar values")
    if not np.isscalar(single_sided):
        raise TypeError("single_sided only accepts scalar values")
    return lib.buffer(
        geometry,
        radius,
        np.intc(quadsegs),
        np.intc(cap_style),
        np.intc(join_style),
        mitre_limit,
        np.bool_(single_sided),
        **kwargs
    )


@multithreading_enabled
def offset_curve(
    geometry, distance, quadsegs=8, join_style="round", mitre_limit=5.0, **kwargs
):
    """
    Returns a (Multi)LineString at a distance from the object
    on its right or its left side.

    For positive distance the offset will be at the left side of
    the input line and retain the same direction. For a negative
    distance it will be at the right side and in the opposite
    direction.

    Parameters
    ----------
    geometry : Geometry or array_like
    distance : float or array_like
        Specifies the offset distance from the input geometry. Negative
        for right side offset, positive for left side offset.
    quadsegs : int, default 8
        Specifies the number of linear segments in a quarter circle in the
        approximation of circular arcs.
    join_style : {'round', 'bevel', 'mitre'}, default 'round'
        Specifies the shape of outside corners. 'round' results in
        rounded shapes. 'bevel' results in a beveled edge that touches the
        original vertex. 'mitre' results in a single vertex that is beveled
        depending on the ``mitre_limit`` parameter.
    mitre_limit : float, default 5.0
        Crops of 'mitre'-style joins if the point is displaced from the
        buffered vertex by more than this limit.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString
    >>> line = LineString([(0, 0), (0, 2)])
    >>> offset_curve(line, 2)
    <LINESTRING (-2 0, -2 2)>
    >>> offset_curve(line, -2)
    <LINESTRING (2 0, 2 2)>
    """
    if isinstance(join_style, str):
        join_style = BufferJoinStyles.get_value(join_style)
    if not np.isscalar(quadsegs):
        raise TypeError("quadsegs only accepts scalar values")
    if not np.isscalar(join_style):
        raise TypeError("join_style only accepts scalar values")
    if not np.isscalar(mitre_limit):
        raise TypeError("mitre_limit only accepts scalar values")
    return lib.offset_curve(
        geometry,
        distance,
        np.intc(quadsegs),
        np.intc(join_style),
        np.double(mitre_limit),
        **kwargs
    )


@multithreading_enabled
def centroid(geometry, **kwargs):
    """Computes the geometric center (center-of-mass) of a geometry.

    For multipoints this is computed as the mean of the input coordinates.
    For multilinestrings the centroid is weighted by the length of each
    line segment. For multipolygons the centroid is weighted by the area of
    each polygon.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> centroid(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> centroid(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(MultiPoint([(0, 0), (10, 10)]))
    <POINT (5 5)>
    >>> centroid(Polygon())
    <POINT EMPTY>
    """
    return lib.centroid(geometry, **kwargs)


@multithreading_enabled
def clip_by_rect(geometry, xmin, ymin, xmax, ymax, **kwargs):
    """
    Returns the portion of a geometry within a rectangle.

    The geometry is clipped in a fast but possibly dirty way. The output is
    not guaranteed to be valid. No exceptions will be raised for topological
    errors.

    Note: empty geometries or geometries that do not overlap with the
    specified bounds will result in GEOMETRYCOLLECTION EMPTY.

    Parameters
    ----------
    geometry : Geometry or array_like
        The geometry to be clipped
    xmin : float
        Minimum x value of the rectangle
    ymin : float
        Minimum y value of the rectangle
    xmax : float
        Maximum x value of the rectangle
    ymax : float
        Maximum y value of the rectangle
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (10, 10)])
    >>> clip_by_rect(line, 0., 0., 1., 1.)
    <LINESTRING (0 0, 1 1)>
    >>> polygon = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> clip_by_rect(polygon, 0., 0., 1., 1.)
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    """
    if not all(np.isscalar(val) for val in [xmin, ymin, xmax, ymax]):
        raise TypeError("xmin/ymin/xmax/ymax only accepts scalar values")
    return lib.clip_by_rect(
        geometry,
        np.double(xmin),
        np.double(ymin),
        np.double(xmax),
        np.double(ymax),
        **kwargs
    )


@multithreading_enabled
def convex_hull(geometry, **kwargs):
    """Computes the minimum convex geometry that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import MultiPoint, Polygon
    >>> convex_hull(MultiPoint([(0, 0), (10, 0), (10, 10)]))
    <POLYGON ((0 0, 10 10, 10 0, 0 0))>
    >>> convex_hull(Polygon())
    <GEOMETRYCOLLECTION EMPTY>
    """
    return lib.convex_hull(geometry, **kwargs)


@multithreading_enabled
def delaunay_triangles(geometry, tolerance=0.0, only_edges=False, **kwargs):
    """Computes a Delaunay triangulation around the vertices of an input
    geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns an None if an input geometry
    contains less than 3 vertices.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Polygon
    >>> points = MultiPoint([(50, 30), (60, 30), (100, 100)])
    >>> delaunay_triangles(points)
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 60 30, 100 100, 50 30)))>
    >>> delaunay_triangles(points, only_edges=True)
    <MULTILINESTRING ((50 30, 100 100), (50 30, 60 30), ...>
    >>> delaunay_triangles(MultiPoint([(50, 30), (51, 30), (60, 30), (100, 100)]), \
tolerance=2)
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 60 30, 100 100, 50 30)))>
    >>> delaunay_triangles(Polygon([(50, 30), (60, 30), (100, 100), (50, 30)]))
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 60 30, 100 100, 50 30)))>
    >>> delaunay_triangles(LineString([(50, 30), (60, 30), (100, 100)]))
    <GEOMETRYCOLLECTION (POLYGON ((50 30, 60 30, 100 100, 50 30)))>
    >>> delaunay_triangles(GeometryCollection([]))
    <GEOMETRYCOLLECTION EMPTY>
    """
    return lib.delaunay_triangles(geometry, tolerance, only_edges, **kwargs)


@multithreading_enabled
def envelope(geometry, **kwargs):
    """Computes the minimum bounding box that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point
    >>> envelope(LineString([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(MultiPoint([(0, 0), (10, 10)]))
    <POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))>
    >>> envelope(Point(0, 0))
    <POINT (0 0)>
    >>> envelope(GeometryCollection([]))
    <POINT EMPTY>
    """
    return lib.envelope(geometry, **kwargs)


@multithreading_enabled
def extract_unique_points(geometry, **kwargs):
    """Returns all distinct vertices of an input geometry as a multipoint.

    Note that only 2 dimensions of the vertices are considered when testing
    for equality.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Point, Polygon
    >>> extract_unique_points(Point(0, 0))
    <MULTIPOINT (0 0)>
    >>> extract_unique_points(LineString([(0, 0), (1, 1), (1, 1)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 0, 1 1, 0 1)>
    >>> extract_unique_points(MultiPoint([(0, 0), (1, 1), (0, 0)]))
    <MULTIPOINT (0 0, 1 1)>
    >>> extract_unique_points(LineString())
    <MULTIPOINT EMPTY>
    """
    return lib.extract_unique_points(geometry, **kwargs)


@requires_geos("3.8.0")
@multithreading_enabled
def build_area(geometry, **kwargs):
    """Creates an areal geometry formed by the constituent linework of given geometry.

    Equivalent of the PostGIS ST_BuildArea() function.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import GeometryCollection, Polygon
    >>> polygon1 = Polygon([(0, 0), (3, 0), (3, 3), (0, 3), (0, 0)])
    >>> polygon2 = Polygon([(1, 1), (1, 2), (2, 2), (1, 1)])
    >>> build_area(GeometryCollection([polygon1, polygon2]))
    <POLYGON ((0 0, 0 3, 3 3, 3 0, 0 0), (1 1, 2 2, 1 2, 1 1))>
    """
    return lib.build_area(geometry, **kwargs)


@requires_geos("3.8.0")
@multithreading_enabled
def make_valid(geometry, **kwargs):
    """Repairs invalid geometries.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import is_valid, Polygon
    >>> polygon = Polygon([(0, 0), (1, 1), (1, 2), (1, 1), (0, 0)])
    >>> is_valid(polygon)
    False
    >>> make_valid(polygon)
    <MULTILINESTRING ((0 0, 1 1), (1 1, 1 2))>
    """
    return lib.make_valid(geometry, **kwargs)


@multithreading_enabled
def normalize(geometry, **kwargs):
    """Converts Geometry to normal form (or canonical form).

    This method orders the coordinates, rings of a polygon and parts of
    multi geometries consistently. Typically useful for testing purposes
    (for example in combination with ``equals_exact``).

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import MultiLineString
    >>> line = MultiLineString([[(0, 0), (1, 1)], [(2, 2), (3, 3)]])
    >>> normalize(line)
    <MULTILINESTRING ((2 2, 3 3), (0 0, 1 1))>
    """
    return lib.normalize(geometry, **kwargs)


@multithreading_enabled
def point_on_surface(geometry, **kwargs):
    """Returns a point that intersects an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, Polygon
    >>> point_on_surface(Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)]))
    <POINT (5 5)>
    >>> point_on_surface(LineString([(0, 0), (2, 2), (10, 10)]))
    <POINT (2 2)>
    >>> point_on_surface(MultiPoint([(0, 0), (10, 10)]))
    <POINT (0 0)>
    >>> point_on_surface(Polygon())
    <POINT EMPTY>
    """
    return lib.point_on_surface(geometry, **kwargs)


def polygonize(geometries, **kwargs):
    """Creates polygons formed from the linework of a set of Geometries.

    Polygonizes an array of Geometries that contain linework which
    represents the edges of a planar graph. Any type of Geometry may be
    provided as input; only the constituent lines and rings will be used to
    create the output polygons.

    Lines or rings that when combined do not completely close a polygon
    will result in an empty GeometryCollection.  Duplicate segments are
    ignored.

    This function returns the polygons within a GeometryCollection.
    Individual Polygons can be obtained using ``get_geometry`` to get
    a single polygon or ``get_parts`` to get an array of polygons.
    MultiPolygons can be constructed from the output using
    ``shapely.multipolygons(shapely.get_parts(shapely.polygonize(geometries)))``.

    Parameters
    ----------
    geometries : array_like
        An array of geometries.
    axis : int
        Axis along which the geometries are polygonized.
        The default is to perform a reduction over the last dimension
        of the input array. A 1D array results in a scalar geometry.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Returns
    -------
    GeometryCollection or array of GeometryCollections

    See Also
    --------
    get_parts, get_geometry
    polygonize_full

    Examples
    --------
    >>> from shapely import LineString
    >>> lines = [
    ...     LineString([(0, 0), (1, 1)]),
    ...     LineString([(0, 0), (0, 1)]),
    ...     LineString([(0, 1), (1, 1)])
    ... ]
    >>> polygonize(lines)
    <GEOMETRYCOLLECTION (POLYGON ((1 1, 0 0, 0 1, 1 1)))>
    """
    return lib.polygonize(geometries, **kwargs)


def polygonize_full(geometries, **kwargs):
    """Creates polygons formed from the linework of a set of Geometries and
    return all extra outputs as well.

    Polygonizes an array of Geometries that contain linework which
    represents the edges of a planar graph. Any type of Geometry may be
    provided as input; only the constituent lines and rings will be used to
    create the output polygons.

    This function performs the same polygonization as ``polygonize`` but does
    not only return the polygonal result but all extra outputs as well. The
    return value consists of 4 elements:

    * The polygonal valid output
    * **Cut edges**: edges connected on both ends but not part of polygonal output
    * **dangles**: edges connected on one end but not part of polygonal output
    * **invalid rings**: polygons formed but which are not valid

    This function returns the geometries within GeometryCollections.
    Individual geometries can be obtained using ``get_geometry`` to get
    a single geometry or ``get_parts`` to get an array of geometries.

    Parameters
    ----------
    geometries : array_like
        An array of geometries.
    axis : int
        Axis along which the geometries are polygonized.
        The default is to perform a reduction over the last dimension
        of the input array. A 1D array results in a scalar geometry.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Returns
    -------
    (polgyons, cuts, dangles, invalid)
        tuple of 4 GeometryCollections or arrays of GeometryCollections

    See Also
    --------
    polygonize

    Examples
    --------
    >>> from shapely import LineString
    >>> lines = [
    ...     LineString([(0, 0), (1, 1)]),
    ...     LineString([(0, 0), (0, 1), (1, 1)]),
    ...     LineString([(0, 1), (1, 1)])
    ... ]
    >>> polygonize_full(lines)  # doctest: +NORMALIZE_WHITESPACE
    (<GEOMETRYCOLLECTION (POLYGON ((1 1, 0 0, 0 1, 1 1)))>,
     <GEOMETRYCOLLECTION EMPTY>,
     <GEOMETRYCOLLECTION (LINESTRING (0 1, 1 1))>,
     <GEOMETRYCOLLECTION EMPTY>)
    """
    return lib.polygonize_full(geometries, **kwargs)


@requires_geos("3.7.0")
@multithreading_enabled
def reverse(geometry, **kwargs):
    """Returns a copy of a Geometry with the order of coordinates reversed.

    If a Geometry is a polygon with interior rings, the interior rings are also
    reversed.

    Points are unchanged. None is returned where Geometry is None.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    See also
    --------
    is_ccw : Checks if a Geometry is clockwise.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> reverse(LineString([(0, 0), (1, 2)]))
    <LINESTRING (1 2, 0 0)>
    >>> reverse(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
    <POLYGON ((0 0, 0 1, 1 1, 1 0, 0 0))>
    >>> reverse(None) is None
    True
    """

    return lib.reverse(geometry, **kwargs)


@requires_geos("3.10.0")
@multithreading_enabled
def segmentize(geometry, tolerance, **kwargs):
    """Adds vertices to line segments based on tolerance.

    Additional vertices will be added to every line segment in an input geometry
    so that segments are no greater than tolerance.  New vertices will evenly
    subdivide each segment.

    Only linear components of input geometries are densified; other geometries
    are returned unmodified.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like
        Additional vertices will be added so that all line segments are no
        greater than this value.  Must be greater than 0.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (0, 10)])
    >>> segmentize(line, tolerance=5)
    <LINESTRING (0 0, 0 5, 0 10)>
    >>> polygon = Polygon([(0, 0), (10, 0), (10, 10), (0, 10), (0, 0)])
    >>> segmentize(polygon, tolerance=5)
    <POLYGON ((0 0, 5 0, 10 0, 10 5, 10 10, 5 10, 0 10, 0 5, 0 0))>
    >>> segmentize(None, tolerance=5) is None
    True
    """
    return lib.segmentize(geometry, tolerance, **kwargs)


@multithreading_enabled
def simplify(geometry, tolerance, preserve_topology=True, **kwargs):
    """Returns a simplified version of an input geometry using the
    Douglas-Peucker algorithm.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like
        The maximum allowed geometry displacement. The higher this value, the
        smaller the number of vertices in the resulting geometry.
    preserve_topology : bool, default False
        By default (True), the operation will avoid creating invalid
        geometries (checking for collapses, ring-intersections, etc), but
        this is computationally more expensive.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString, Polygon
    >>> line = LineString([(0, 0), (1, 10), (0, 20)])
    >>> simplify(line, tolerance=0.9)
    <LINESTRING (0 0, 1 10, 0 20)>
    >>> simplify(line, tolerance=1)
    <LINESTRING (0 0, 0 20)>
    >>> polygon_with_hole = Polygon(
    ...     [(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)],
    ...     holes=[[(2, 2), (2, 4), (4, 4), (4, 2), (2, 2)]]
    ... )
    >>> simplify(polygon_with_hole, tolerance=4, preserve_topology=True)
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0), (2 2, 2 4, 4 4, 4 2...>
    >>> simplify(polygon_with_hole, tolerance=4, preserve_topology=False)
    <POLYGON ((0 0, 0 10, 10 10, 10 0, 0 0))>
    """
    if preserve_topology:
        return lib.simplify_preserve_topology(geometry, tolerance, **kwargs)
    else:
        return lib.simplify(geometry, tolerance, **kwargs)


@multithreading_enabled
def snap(geometry, reference, tolerance, **kwargs):
    """Snaps an input geometry to reference geometry's vertices.

    The tolerance is used to control where snapping is performed.
    The result geometry is the input geometry with the vertices snapped.
    If no snapping occurs then the input geometry is returned unchanged.

    Parameters
    ----------
    geometry : Geometry or array_like
    reference : Geometry or array_like
    tolerance : float or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString, Point, Polygon
    >>> point = Point(0.5, 2.5)
    >>> target_point = Point(0, 2)
    >>> snap(point, target_point, tolerance=1)
    <POINT (0 2)>
    >>> snap(point, target_point, tolerance=0.49)
    <POINT (0.5 2.5)>
    >>> polygon = Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)])
    >>> snap(polygon, Point(8, 10), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 10 0, 0 0))>
    >>> snap(polygon, LineString([(8, 10), (8, 0)]), tolerance=5)
    <POLYGON ((0 0, 0 10, 8 10, 8 0, 0 0))>
    """
    return lib.snap(geometry, reference, tolerance, **kwargs)


@multithreading_enabled
def voronoi_polygons(
    geometry, tolerance=0.0, extend_to=None, only_edges=False, **kwargs
):
    """Computes a Voronoi diagram from the vertices of an input geometry.

    The output is a geometrycollection containing polygons (default)
    or linestrings (see only_edges). Returns empty if an input geometry
    contains less than 2 vertices or if the provided extent has zero area.

    Parameters
    ----------
    geometry : Geometry or array_like
    tolerance : float or array_like, default 0.0
        Snap input vertices together if their distance is less than this value.
    extend_to : Geometry or array_like, optional
        If provided, the diagram will be extended to cover the envelope of this
        geometry (unless this envelope is smaller than the input geometry).
    only_edges : bool or array_like, default False
        If set to True, the triangulation will return a collection of
        linestrings instead of polygons.
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import LineString, MultiPoint, normalize, Point
    >>> points = MultiPoint([(2, 2), (4, 2)])
    >>> normalize(voronoi_polygons(points))
    <GEOMETRYCOLLECTION (POLYGON ((3 0, 3 4, 6 4, 6 0, 3 0)), POLYGON ((0 0, 0 4...>
    >>> voronoi_polygons(points, only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(MultiPoint([(2, 2), (4, 2), (4.2, 2)]), 0.5, only_edges=True)
    <LINESTRING (3 4.2, 3 -0.2)>
    >>> voronoi_polygons(points, extend_to=LineString([(0, 0), (10, 10)]), only_edges=True)
    <LINESTRING (3 10, 3 0)>
    >>> voronoi_polygons(LineString([(2, 2), (4, 2)]), only_edges=True)
    <LINESTRING (3 4, 3 0)>
    >>> voronoi_polygons(Point(2, 2))
    <GEOMETRYCOLLECTION EMPTY>
    """
    return lib.voronoi_polygons(geometry, tolerance, extend_to, only_edges, **kwargs)


@requires_geos("3.6.0")
@multithreading_enabled
def oriented_envelope(geometry, **kwargs):
    """
    Computes the oriented envelope (minimum rotated rectangle)
    that encloses an input geometry.

    Unlike envelope this rectangle is not constrained to be parallel to the
    coordinate axes. If the convex hull of the object is a degenerate (line
    or point) this degenerate is returned.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> oriented_envelope(MultiPoint([(0, 0), (10, 0), (10, 10)]))
    <POLYGON ((0 0, 5 -5, 15 5, 10 10, 0 0))>
    >>> oriented_envelope(LineString([(1, 1), (5, 1), (10, 10)]))
    <POLYGON ((1 1, 3 -1, 12 8, 10 10, 1 1))>
    >>> oriented_envelope(Polygon([(1, 1), (15, 1), (5, 10), (1, 1)]))
    <POLYGON ((15 1, 15 10, 1 10, 1 1, 15 1))>
    >>> oriented_envelope(LineString([(1, 1), (10, 1)]))
    <LINESTRING (1 1, 10 1)>
    >>> oriented_envelope(Point(2, 2))
    <POINT (2 2)>
    >>> oriented_envelope(GeometryCollection([]))
    <POLYGON EMPTY>
    """
    return lib.oriented_envelope(geometry, **kwargs)


minimum_rotated_rectangle = oriented_envelope


@requires_geos("3.8.0")
@multithreading_enabled
def minimum_bounding_circle(geometry, **kwargs):
    """Computes the minimum bounding circle that encloses an input geometry.

    Parameters
    ----------
    geometry : Geometry or array_like
    **kwargs
        For other keyword-only arguments, see the
        `NumPy ufunc docs <https://numpy.org/doc/stable/reference/ufuncs.html#ufuncs-kwargs>`_.

    Examples
    --------
    >>> from shapely import GeometryCollection, LineString, MultiPoint, Point, Polygon
    >>> minimum_bounding_circle(Polygon([(0, 0), (0, 10), (10, 10), (10, 0), (0, 0)]))
    <POLYGON ((12.071 5, 11.935 3.621, 11.533 2.294, 10.879 1.07...>
    >>> minimum_bounding_circle(LineString([(1, 1), (10, 10)]))
    <POLYGON ((11.864 5.5, 11.742 4.258, 11.38 3.065, 10.791 1.9...>
    >>> minimum_bounding_circle(MultiPoint([(2, 2), (4, 2)]))
    <POLYGON ((4 2, 3.981 1.805, 3.924 1.617, 3.831 1.444, 3.707...>
    >>> minimum_bounding_circle(Point(0, 1))
    <POINT (0 1)>
    >>> minimum_bounding_circle(GeometryCollection([]))
    <POLYGON EMPTY>

    See also
    --------
    minimum_bounding_radius
    """
    return lib.minimum_bounding_circle(geometry, **kwargs)
