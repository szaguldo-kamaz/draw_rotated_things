# draw_rotated_things v0.1
# for use with PySimpleGUI
# see examples (Demo_draw_rotated_*)
#
# author: David Vincze
# github.com/szaguldo-kamaz/
#

import math

# TODO: integrate with draw_rectangle, etc. as parameters like angle/rotcentangle/rotcentdist

# TODO: could be easily extended to support polygons...
def draw_rotated_rectangle(graph, rectcoord, angle, outlinecolor, rotcentangle=0, rotcentdist=0, fill=True, fillcolor=None, linewidth=1):

    coord=( rectcoord[0], (rectcoord[1][0],rectcoord[0][1]), rectcoord[1], (rectcoord[0][0],rectcoord[1][1]) );
    coord_center=( int((rectcoord[0][0]+rectcoord[1][0])/2), int((rectcoord[0][1]+rectcoord[1][1])/2) );
    cosangle=math.cos(angle);
    sinangle=math.sin(angle);

    cosangle_cd=math.cos(rotcentangle);
    sinangle_cd=math.sin(rotcentangle);
    coord_cd=(coord_center[0],coord_center[1]-rotcentdist);

    coord_rot=[];
    for c in range(0,4):
        temp=[ (coord[c][0]-coord_center[0])*cosangle - (coord[c][1]-coord_center[1])*sinangle + coord_center[0],
               (coord[c][0]-coord_center[0])*sinangle + (coord[c][1]-coord_center[1])*cosangle + coord_center[1] ];
        coord_rot.append(
              [ (temp[0]-coord_cd[0])*cosangle_cd - (temp[1]-coord_cd[1])*sinangle_cd + coord_center[0],
                (temp[0]-coord_cd[0])*sinangle_cd + (temp[1]-coord_cd[1])*cosangle_cd + coord_center[1] ] );

    if fill:
        if fillcolor==None:
            fillcolor=outlinecolor;
        return graph.draw_polygon(coord_rot, line_color=outlinecolor, fill_color=fillcolor);
    else:
        coord_rot.append(coord_rot[0]);
        return graph.draw_lines(coord_rot, width=linewidth, color=outlinecolor);


def draw_rotated_line(graph, coord, angle, color, rotcentangle=0, rotcentdist=0, linewidth=1):
    coord_center=( int((coord[0][0]+coord[1][0])/2), int((coord[0][1]+coord[1][1])/2) );
    cosangle=math.cos(angle);
    sinangle=math.sin(angle);

    coord_rot=( ((coord[0][0]-coord_center[0])*cosangle - (coord[0][1]-coord_center[1])*sinangle + coord_center[0],
                 (coord[0][0]-coord_center[0])*sinangle + (coord[0][1]-coord_center[1])*cosangle + coord_center[1]),
                ((coord[1][0]-coord_center[0])*cosangle - (coord[1][1]-coord_center[1])*sinangle + coord_center[0],
                 (coord[1][0]-coord_center[0])*sinangle + (coord[1][1]-coord_center[1])*cosangle + coord_center[1]) );

    if rotcentangle != 0 or rotcentdist != 0:
        cosangle_cd=math.cos(rotcentangle);
        sinangle_cd=math.sin(rotcentangle);
        coord_cd=(coord_center[0],coord_center[1]-rotcentdist);
        coord_rot=( ((coord_rot[0][0]-coord_cd[0])*cosangle_cd - (coord_rot[0][1]-coord_cd[1])*sinangle_cd + coord_center[0],
                     (coord_rot[0][0]-coord_cd[0])*sinangle_cd + (coord_rot[0][1]-coord_cd[1])*cosangle_cd + coord_center[1]),
                    ((coord_rot[1][0]-coord_cd[0])*cosangle_cd - (coord_rot[1][1]-coord_cd[1])*sinangle_cd + coord_center[0],
                     (coord_rot[1][0]-coord_cd[0])*sinangle_cd + (coord_rot[1][1]-coord_cd[1])*cosangle_cd + coord_center[1]) );

    return graph.draw_line(coord_rot[0], coord_rot[1], color=color, width=linewidth);


def draw_rotated_circle(graph, coord_center, radius, angle, rotcentdist, linecolor, linewidth=1, fillcolor=None):
    coord=(coord_center[0],coord_center[1]-rotcentdist);
    cosangle=math.cos(angle);
    sinangle=math.sin(angle);

    coord_rot=((coord[0]-coord_center[0])*cosangle - (coord[1]-coord_center[1])*sinangle + coord_center[0],
               (coord[0]-coord_center[0])*sinangle + (coord[1]-coord_center[1])*cosangle + coord_center[1]);

    return graph.draw_circle(coord_rot, radius, line_width=linewidth, line_color=linecolor, fill_color=fillcolor);