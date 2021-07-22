# Demo_draw_rotated_things v0.1
# using draw_rotated_things
#
# author: David Vincze
# github.com/szaguldo-kamaz/
#

import PySimpleGUI as sg
import math
from draw_rotated_things import *


graphsize=(800,600);

bgcolor='#202020';
# bright
#colors=[ '#808080','#D000D0', '#00D0D0', '#D0D000', '#D00000', '#00D000', '#0000D0', '#D00080', '#00D080', '#0080D0', '#D08080', '#80D080', '#8080D0','#D08000', '#80D000', '#8000D0', '#D080D0', '#80D0D0', '#D0D080', '#D0D0D0'] ;
# dark
colors=[ '#804000', '#408000',  '#404080', '#808040', '#800080', '#008080', '#408040','#804040','#800000','#808000', '#008000', '#800040', '#008040', '#000080', '#400080', '#404040', '#004080', '#804080', '#408080', '#808080'] ;

layout = [[sg.Text('Draw rotated things demo', font='Verdana 20', justification='center', size=(None, 1))],
          [sg.Graph(
              graphsize, (0, graphsize[1]), (graphsize[0], 0),
              background_color=bgcolor,
              change_submits=True,
              drag_submits=True,
              enable_events=True,
              key='-GRAPH-')],
          [sg.Button('Exit', key='-EXIT-', font='Verdanar 14'),
          sg.Text('Use the mouse scroll wheel to rotate objects', font='Verdana 12')]
         ];

window = sg.Window('Draw rotated things demo', layout, finalize=True, use_default_focus=False);
window.bind('<Button-4>', '+SCRUP+');
window.bind('<Button-5>', '+SCRDN+');

graph = window['-GRAPH-'];
graph.draw_circle( [graphsize[0]/2,graphsize[1]/2], 250, line_color='#808080', line_width=3);
graph.draw_text("száguldó", [graphsize[0]-40, graphsize[1]-22],color='#A0A0A0', font="Verdana 7", angle=14);
graph.draw_text("kamaz", [graphsize[0]-22, graphsize[1]-16],color='#A0A0A0', font="Verdana 7", angle=14);

main_angle=0;
changed=True;

while True:

    if changed:
        changed=False;
        # rectangles in the middle
        rect_fill  =draw_rotated_rectangle( graph, [(graphsize[0]/2+75,graphsize[1]/2-50),(graphsize[0]/2+175,graphsize[1]/2+50)], main_angle, '#00DC80', fill=True, linewidth=5, fillcolor='#00BB40');
        rect_nofill=draw_rotated_rectangle( graph, [(graphsize[0]/2-150,graphsize[1]/2-50),(graphsize[0]/2-100 ,graphsize[1]/2+50)], main_angle, '#80DC00', fill=False, linewidth=5);
        # rectangles on the circle - rotating around their centers
        rect_fill_dr  =draw_rotated_rectangle( graph, [(graphsize[0]/2-25,graphsize[1]/2-25),(graphsize[0]/2+25,graphsize[1]/2+25)], 0, '#0080DC', fill=True, linewidth=5, fillcolor='#0080DC', rotcentdist=250, rotcentangle=main_angle-math.pi/4);
        rect_nofill_dr=draw_rotated_rectangle( graph, [(graphsize[0]/2-25,graphsize[1]/2-25),(graphsize[0]/2+25,graphsize[1]/2+25)], 0, '#8000DC', fill=False, linewidth=5, rotcentdist=250, rotcentangle=main_angle+math.pi/4);
        # rectangles on the circle - not rotating around their centers
        rect_fill_dr_st  =draw_rotated_rectangle( graph, [(graphsize[0]/2-25,graphsize[1]/2-25),(graphsize[0]/2+25,graphsize[1]/2+25)], -main_angle, '#00DCDC', fill=True, linewidth=5, fillcolor='#00DCDC', rotcentdist=250, rotcentangle=main_angle-math.pi/2);
        rect_nofill_dr_st=draw_rotated_rectangle( graph, [(graphsize[0]/2-25,graphsize[1]/2-25),(graphsize[0]/2+25,graphsize[1]/2+25)], -main_angle, '#DC00DC', fill=False, linewidth=5, rotcentdist=250, rotcentangle=main_angle+math.pi/2);
        # circles on the circle
        circ_fill  =draw_rotated_circle( graph, [graphsize[0]/2,graphsize[1]/2], 25, main_angle, 250, '#8000D0', fillcolor='#8000D0');
        circ_nofill=draw_rotated_circle( graph, [graphsize[0]/2,graphsize[1]/2], 35, main_angle+math.pi, 250, '#F06040', linewidth=5, fillcolor=None);
        # cross in the middle
        cross_vert =draw_rotated_line( graph, [[graphsize[0]/2,graphsize[1]/2-30], [graphsize[0]/2,graphsize[1]/2+30]], main_angle, 'orange', linewidth=5);
        cross_horiz=draw_rotated_line( graph, [[graphsize[0]/2-30,graphsize[1]/2], [graphsize[0]/2+30,graphsize[1]/2]], main_angle, 'orange', linewidth=5);
        # lines on the circle
        line_dr   =draw_rotated_line( graph, [[graphsize[0]/2,graphsize[1]/2-30], [graphsize[0]/2,graphsize[1]/2+30]], 0, 'yellow', linewidth=5, rotcentdist=250, rotcentangle=main_angle-math.pi/4*3);
        line_dr_st=draw_rotated_line( graph, [[graphsize[0]/2,graphsize[1]/2-30], [graphsize[0]/2,graphsize[1]/2+30]], -main_angle+math.pi/4, 'brown', linewidth=5, rotcentdist=250, rotcentangle=main_angle+math.pi/4*3);

    event, values = window.read();

    if event in (sg.WIN_CLOSED,'-EXIT-'):
        break

    if event == '+SCRUP+':
        main_angle=main_angle-(math.pi/16);
        if main_angle < 0:
            main_angle=(31/16)*math.pi;
        changed=True

    if event == '+SCRDN+':
        main_angle=main_angle+(math.pi/16);
        if main_angle >= (2*math.pi):
            main_angle=0;
        changed=True

    if changed:
        graph.delete_figure(rect_fill);
        graph.delete_figure(rect_nofill);
        graph.delete_figure(rect_fill_dr);
        graph.delete_figure(rect_nofill_dr);
        graph.delete_figure(rect_fill_dr_st);
        graph.delete_figure(rect_nofill_dr_st);
        graph.delete_figure(circ_fill);
        graph.delete_figure(circ_nofill);
        graph.delete_figure(cross_vert);
        graph.delete_figure(cross_horiz);
        graph.delete_figure(line_dr);
        graph.delete_figure(line_dr_st);


window.close();
