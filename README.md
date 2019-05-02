# PolyWind
Demonstrates and computes winding number for a point in a non-simple polygon.
Contributors: Radu Visina, Taylore Westbrook, and Keyur Shah.
References consulted:
Eric Haines, "Point in Polygon Strategies" chapter of Graphics Gems IV (1994)
Dan Sunday, "Inclusion of a Point in a Polygon" webpage at GeomAlgorithms.com

HOW TO USE THE PYTHON SCRIPT
Note: Numpy is required

The Polygon Winding program is run from PolyWind.py

A window spawns. There are two buttons in this window: [Clear] and [Toggle Ray]. The [Clear] button resets the window blank, and the [Toggle Ray] button
toggles the display of the ray used in the computation of the winding number and other tutorial displays.
The first click into the window lays down the winding point, which is the point around which the polygon winds.
Subsequent clicks lay down the points of the polygon. Note that the polygon can be non-simple, meaning that its edges are allowed to intersect.
If the polygon winds around the point in clockwise ordering of the points, then the winding number increases.
Since the polygon can be non-simple, it may continue winding around the point more than once.
The winding number reflects the number of winds of the polygon around that point.
The number may be negative if the polygon points are layed down in counter-clockwise order.

When toggling the tutorial display using [Toggle Ray], a red "ray" appears that extends from the winding point.
The ray is actually a line segment that extends to an arbitrary point on the edge of the display window.
The winding number is computed using an algorithm similar to polygon membership testing in a non-convex polygon.
Each edge of the polygon is tested for intersection with the ray segment. Counter-clockwise derivative sign tests are used for this.
Depending on the orientation of a particular polygon edge, the intersection may be valued at:
+1 (clockwise orientation of the ray and polygon edge), -1 (counter-clockwise orientation of the ray and polygon edge), or 0 for no intersection.
The intersections valued at +1 and -1 are displayed in the window at the points where the intersections happen.
Note: The algorithm that finds the intersection points is not part of the winding number algorithm. Intersection points are only found for tutorial display purposes.
The sum of the intersection values is the winding number, which is displayed near the winding point.
Close the window by pressing c on the keyboard, or just by clicking the close button of the window.