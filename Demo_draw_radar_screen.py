# Demo_draw_radar_screen v0.1
# using draw_rotated_things and PySimpleGUI
#
# author: David Vincze
# github.com/szaguldo-kamaz/
#

import PySimpleGUI as sg
from draw_rotated_things import *


graphsize=(800,600);
#graphsize=(1400,800);
bgcolor='#003000';

layout = [[sg.Text("Radar screen demo", font="Verdana 20", justification="center", size=(None, 1))],
          [sg.Graph(
              graphsize, (0, graphsize[1]), (graphsize[0], 0),
              background_color=bgcolor,
              change_submits=True,
              drag_submits=True,
              enable_events=True,
              key='-GRAPH-')],
          [sg.Button('Exit', key="-EXIT-", font="Verdana 15")]
         ];

window = sg.Window('Draw radar screen demo', layout, finalize=True, use_default_focus=False)

graph = window['-GRAPH-']
graph.draw_text("száguldó", [graphsize[0]-40, graphsize[1]-22],color='#00A000', font="Verdana 7", angle=14);
graph.draw_text("kamaz", [graphsize[0]-22, graphsize[1]-16],color='#00A000', font="Verdana 7", angle=14);

# to make a smoother transition from the background color to the color of the circles there will be three layers
# first layer of circles
for rcn in range(50,300,50):
    graph.draw_circle( [graphsize[0]/2,graphsize[1]/2], rcn, line_color='#005000', line_width=6);
# first layer of the cross
graph.draw_line( [graphsize[0]/2,graphsize[1]-20],  [graphsize[0]/2,20],  color='#005000', width=6);
graph.draw_line( [graphsize[0]-120,graphsize[1]/2], [120,graphsize[1]/2], color='#005000', width=6);

# second layer of circles
for rcn in range(50,300,50):
    graph.draw_circle( [graphsize[0]/2,graphsize[1]/2], rcn, line_color='#007000', line_width=4);
# second layer of the cross
graph.draw_line( [graphsize[0]/2,graphsize[1]-22],  [graphsize[0]/2,22],  color='#007000', width=4);
graph.draw_line( [graphsize[0]-122,graphsize[1]/2], [122,graphsize[1]/2], color='#007000', width=4);

# third layer of circles
topcircles={};
for rcn in range(50,300,50):
    topcircles[rcn]=graph.draw_circle( [graphsize[0]/2,graphsize[1]/2], rcn, line_color='#009000', line_width=2);
# third layer of the cross
topcross=[ graph.draw_line( [graphsize[0]/2,graphsize[1]-24],  [graphsize[0]/2,24],  color='#009000', width=2),
           graph.draw_line( [graphsize[0]-124,graphsize[1]/2], [124,graphsize[1]/2], color='#009000', width=2) ];

drl={}; # for storing the line objects
ran=0; # angle of the current line
# colors of the "fading" lines
rlcolors=[ '#004000', '#004800', '#005000', '#005800', '#006000', '#006800', '#006B00', '#007000', '#007400',
           '#007800', '#007B00', '#008000', '#008400', '#008800', '#008B00', '#009000', '#00A000', '#00FF00' ];

while True:

    for rl in range(0,17):
        drl[rl]=draw_rotated_line( graph, [(graphsize[0]/2,graphsize[1]/2-125),(graphsize[0]/2,graphsize[1]/2+125)], 0, rlcolors[rl], linewidth=7, rotcentdist=125, rotcentangle=ran+(rl*0.025));
    rl=17;
    drl[rl]=draw_rotated_line( graph, [(graphsize[0]/2,graphsize[1]/2-125),(graphsize[0]/2,graphsize[1]/2+125)], 0, rlcolors[rl], linewidth=3, rotcentdist=125, rotcentangle=ran+(rl*0.025));

    ran=ran+0.05;

    # bring forward the third layer, so the newly drawn lines will be under it
    for rcn in range(50,300,50):
        graph.bring_figure_to_front(topcircles[rcn]);
    graph.bring_figure_to_front(topcross[0]);
    graph.bring_figure_to_front(topcross[1]);

    event, values = window.read(5);

    if event in (sg.WIN_CLOSED,"-EXIT-"):
        break

    for rl in range(0,18):
        graph.delete_figure(drl[rl]);


window.close();
