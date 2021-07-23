# Demo_draw_rotated_rectangles v0.1
# using draw_rotated_things and PySimpleGUI
#
# author: David Vincze
# github.com/szaguldo-kamaz/
#

import PySimpleGUI as sg
from draw_rotated_things import *


graphsize=(800,600);
#graphsize=(1400,800);

bgcolor='#202020';
# bright
#colors=[ '#808080','#D000D0', '#00D0D0', '#D0D000', '#D00000', '#00D000', '#0000D0', '#D00080', '#00D080', '#0080D0', '#D08080', '#80D080', '#8080D0','#D08000', '#80D000', '#8000D0', '#D080D0', '#80D0D0', '#D0D080', '#D0D0D0'] ;
# dark
colors=[ '#804000', '#408000',  '#404080', '#808040', '#800080', '#008080', '#408040','#804040','#800000','#808000', '#008000', '#800040', '#008040', '#000080', '#400080', '#404040', '#004080', '#804080', '#408080', '#808080'] ;

layout = [[sg.Text("Draw rotated rectangles demo", font="Verdana 20", justification="center", size=(None, 1))],
          [sg.Graph(
              graphsize, (0, graphsize[1]), (graphsize[0], 0),
              background_color=bgcolor,
              change_submits=True,
              drag_submits=True,
              enable_events=True,
              key='-GRAPH-')],
          [sg.Button('Exit', key="-EXIT-", font="Verdana 14")]
         ];

window = sg.Window('Draw rotated rectangles demo', layout, finalize=True, use_default_focus=False)

graph = window['-GRAPH-']
graph.draw_text("száguldó-kamaz", [graphsize[0]-48, graphsize[1]-22],color='#808080', font="Verdana 7", angle=14);

cc=0;
drc={};
f=0;
fp=1;
fr=0;

while True:

    for yy in range(0,graphsize[1],100):
        for xx in range(0,graphsize[0],100):
            drc[str(xx)+str(yy)]       =draw_rotated_rectangle( graph, [(xx,yy),       (xx+50 ,yy+50 )], (xx+yy+cc)/200   , colors[int((xx+yy)/100)%20], fillcolor=colors[int((xx+yy)/100)%20], rotcentdist=100, rotcentangle=(xx+yy+cc)/200);
            drc[str(xx)+str(yy)+str(2)]=draw_rotated_rectangle( graph, [(xx+50,yy+50), (xx+100,yy+100)], (xx+yy+cc)/200+25, colors[int((xx+yy)/100+10)%20], fillcolor=colors[int((xx+yy)/100+10)%20], rotcentdist=50, rotcentangle=(xx+yy+cc)/200+25);

    nofill1=draw_rotated_rectangle( graph, [(graphsize[0]/2-f,graphsize[1]/2-f),(graphsize[0]/2+f,graphsize[1]/2+f)], fr/2, 'red', fill=False, linewidth=8, rotcentdist=-f, rotcentangle=fr/2);
    nofill2=draw_rotated_rectangle( graph, [(graphsize[0]/2-(f/2),graphsize[1]/2-(f/2)),(graphsize[0]/2+(f/2),graphsize[1]/2+(f/2))], -fr, 'orange', fill=False, linewidth=8, rotcentdist=f, rotcentangle=fr/2);

    event, values = window.read(10);

    cc=cc+10;

    f=f+fp;
    if f > 200:
        fp=-2;
    if f < 0:
        fp=2;
    fr=fr-0.1;

    if event in (sg.WIN_CLOSED,"-EXIT-"):
        break

    graph.delete_figure(nofill1);
    graph.delete_figure(nofill2);
    for yy in range(0,graphsize[1],100):
        for xx in range(0,graphsize[0],100):
            graph.delete_figure(drc[str(xx)+str(yy)]);
            graph.delete_figure(drc[str(xx)+str(yy)+str(2)]);


window.close();
