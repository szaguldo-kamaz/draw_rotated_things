# Demo_draw_rotated_lines_and_circles v0.1
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

layout = [[sg.Text("Draw rotated lines and circles demo", font="Verdana 20", justification="center", size=(None, 1))],
          [sg.Graph(
              graphsize, (0, graphsize[1]), (graphsize[0], 0),
              background_color=bgcolor,
              change_submits=True,
              drag_submits=True,
              enable_events=True,
              key='-GRAPH-')],
          [sg.Button('Exit', key="-EXIT-", font="Verdana 15")]
         ];

window = sg.Window('Draw rotated lines and circles demo', layout, finalize=True, use_default_focus=False)

graph = window['-GRAPH-']
graph.draw_text("száguldó-kamaz", [graphsize[0]-48, graphsize[1]-22],color='#A0A0A0', font="Verdana 7", angle=14);

# colors of the sticks in the background - bright version
colors_bright=[ '#808080', '#D000D0', '#00D0D0', '#D0D000', '#D00000',
                '#00D000', '#0000D0', '#D00080', '#00D080', '#0080D0',
                '#D08080', '#80D080', '#8080D0', '#D08000', '#80D000',
                '#8000D0', '#D080D0', '#80D0D0', '#D0D080', '#D0D0D0'];
# colors of the sticks in the background - dark version
colors_dark=[ '#804000', '#408000', '#404080', '#808040', '#800080',
              '#008080', '#408040', '#804040', '#800000', '#808000',
              '#008000', '#800040', '#008040', '#000080', '#400080',
              '#404040', '#004080', '#804080', '#408080', '#808080'];

colors=colors_bright;

# colors of the flying circles
rccolors=[ '#202040', '#202060', '#302070', '#382080', '#400090',
           '#500098', '#6000A0', '#7000B0', '#8000C0', '#9000D0',
           '#9800D8', '#A000E0' ];
# colors of the spinning lines in the foreground
rlcolors=[ '#007700', '#008800', '#009900', '#00AA00', '#00BB00',
           '#00CC00', '#00DD00', '#00EE00', '#00FF00' ];

cc=0;
f=0;
fp=5;
fr=0;
crad=20;
drbgl={};
drc={};
drl={};

while True:

    for yy in range(0,graphsize[1],100):
        for xx in range(0,graphsize[0],100):
            drbgl[str(xx)+str(yy)]       =draw_rotated_line( graph, [(xx,yy),       (xx+50 ,yy+50 )], (xx+yy+cc)/200,    colors[int((xx+yy)/100)%20]   , linewidth=4, rotcentdist=50*(f/50), rotcentangle=(xx+yy+cc)/200);
            drbgl[str(xx)+str(yy)+str(2)]=draw_rotated_line( graph, [(xx+50,yy+50), (xx+100,yy+100)], (xx+yy+cc)/200+25, colors[int((xx+yy)/100+10)%20], linewidth=4, rotcentdist=50*(f/50), rotcentangle=(xx+yy+cc)/200+25);

    for rc in range(0,12):
        drc[rc]=draw_rotated_circle( graph, (graphsize[0]/2-150+rc*5, graphsize[1]/2-rc*5), crad-(12-rc), -fr+(rc/10), 150, rccolors[rc], linewidth=5, fillcolor=rccolors[rc]);

    for rl in range(0,9):
        drl[rl]=draw_rotated_line( graph, [(graphsize[0]/2-200+rl*50,graphsize[1]/2),(graphsize[0]/2+250,graphsize[1]/2)], fr-(rl*0.1), rlcolors[rl], linewidth=5, rotcentdist=180-(rl*10), rotcentangle=fr-(rl*0.1));

    event, values = window.read(10);

    cc=cc+10;

    f=f+fp;
    if f >= 200:
        fp=-2;
    if f <= 0:
        fp=2;

    fr=fr-0.05;

    if event in (sg.WIN_CLOSED,"-EXIT-"):
        break

    for yy in range(0,graphsize[1],100):
        for xx in range(0,graphsize[0],100):
            graph.delete_figure(drbgl[str(xx)+str(yy)]);
            graph.delete_figure(drbgl[str(xx)+str(yy)+str(2)]);
    for rc in range(0,12):
        graph.delete_figure(drc[rc]);
    for rl in range(0,9):
        graph.delete_figure(drl[rl]);


window.close();
