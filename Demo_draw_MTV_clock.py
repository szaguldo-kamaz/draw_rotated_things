# Demo_draw_MTV_clock v0.1
# using draw_rotated_things and PySimpleGUI
#
# author: David Vincze
# github.com/szaguldo-kamaz/
#

import PySimpleGUI as sg
from draw_rotated_things import *
import datetime


debug=False;

graphsize=(800,600);
#graphsize=(1400,800);
bgcolor='#344DE9';
color1='#D0E8FF';
color2='#98AFFF';

layout = [[sg.Text("Magyar TeleVízió 1 wallclock - cca. 1987", font="Verdana 20", justification="center", size=(None, 1))],
          [sg.Graph(
              graphsize, (0, graphsize[1]), (graphsize[0], 0),
              background_color=bgcolor,
              change_submits=True,
              drag_submits=True,
              enable_events=True,
              key='-GRAPH-')],
          [sg.Button('Exit', key="-EXIT-", font="Verdana 15")]
         ];

window = sg.Window('Magyar TeleVízió 1 wallclock - cca. 1987', layout, finalize=True, use_default_focus=False)

if debug:
    window.bind('<Button-4>', '+SCRUP+');
    window.bind('<Button-5>', '+SCRDN+');

graph = window['-GRAPH-']
graph.draw_text("száguldó", [graphsize[0]-40, graphsize[1]-22],color=color1, font="Verdana 7", angle=14);
graph.draw_text("kamaz", [graphsize[0]-22, graphsize[1]-16],color=color1, font="Verdana 7", angle=14);

topmark_start=0.55*(graphsize[1]/2);
topmark_end=0.20*(graphsize[1]/2);
bottommark_start=1.45*(graphsize[1]/2);
bottommark_end=1.80*(graphsize[1]/2);
leftmark_start=0.66*(graphsize[0]/2);
leftmark_end=0.4*(graphsize[0]/2);
rightmark_start=1.34*(graphsize[0]/2);
rightmark_end=1.6*(graphsize[0]/2);

graph.draw_line( [graphsize[0]/2-8,topmark_start+2], [graphsize[0]/2-8,topmark_end-2], color=color2, width=10);
graph.draw_line( [graphsize[0]/2+8,topmark_start+2], [graphsize[0]/2+8,topmark_end-2], color=color2, width=10);
graph.draw_line( [graphsize[0]/2-8,topmark_start],   [graphsize[0]/2-8,topmark_end],   color=color1, width=6);
graph.draw_line( [graphsize[0]/2+8,topmark_start],   [graphsize[0]/2+8,topmark_end],   color=color1, width=6);

graph.draw_line( [graphsize[0]/2,bottommark_start-2], [graphsize[0]/2,bottommark_end+2], color=color2, width=10);
graph.draw_line( [graphsize[0]/2,bottommark_start],   [graphsize[0]/2,bottommark_end],   color=color1, width=6);

graph.draw_line( [leftmark_start+2, graphsize[1]/2], [leftmark_end-2, graphsize[1]/2], color=color2, width=10);
graph.draw_line( [leftmark_start,   graphsize[1]/2], [leftmark_end,   graphsize[1]/2], color=color1, width=6);

graph.draw_line( [rightmark_start-2, graphsize[1]/2], [rightmark_end+2, graphsize[1]/2], color=color2, width=10);
graph.draw_line( [rightmark_start,   graphsize[1]/2], [rightmark_end,   graphsize[1]/2], color=color1, width=6);

for strot in range(0,4):
    draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2+((topmark_end-topmark_start)/4)-2], [graphsize[0]/2,graphsize[1]/2-((topmark_end-topmark_start)/4)+2]], 0, color2, rotcentangle=math.pi/6+strot*math.pi/2, rotcentdist=topmark_start-graphsize[1]/2+((topmark_end-topmark_start)/4), linewidth=10);
    draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2+((topmark_end-topmark_start)/4)],   [graphsize[0]/2,graphsize[1]/2-((topmark_end-topmark_start)/4)]],   0, color1, rotcentangle=math.pi/6+strot*math.pi/2, rotcentdist=topmark_start-graphsize[1]/2+((topmark_end-topmark_start)/4), linewidth=6);
    draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2+((topmark_end-topmark_start)/4)-2], [graphsize[0]/2,graphsize[1]/2-((topmark_end-topmark_start)/4)+2]], 0, color2, rotcentangle=math.pi/3+strot*math.pi/2, rotcentdist=topmark_start-graphsize[1]/2+((topmark_end-topmark_start)/4), linewidth=10);
    draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2+((topmark_end-topmark_start)/4)],   [graphsize[0]/2,graphsize[1]/2-((topmark_end-topmark_start)/4)]],   0, color1, rotcentangle=math.pi/3+strot*math.pi/2, rotcentdist=topmark_start-graphsize[1]/2+((topmark_end-topmark_start)/4), linewidth=6);

graph.draw_circle( [graphsize[0]/2,graphsize[1]/2], 11, line_color=color2, line_width=12);

covercirc1=graph.draw_circle( [graphsize[0]/2,graphsize[1]/2], 10, line_color=color1, line_width=11);
covercirc2=graph.draw_circle( [graphsize[0]/2,graphsize[1]/2], 4, line_color=color2, fill_color=color2);

main_angle=0;

hourhandlen=-(graphsize[1]/2-topmark_start-5);
hourhandwidth=12;
hourrot=0;

minutehandlen=-(graphsize[1]/2-(topmark_start-((topmark_start-topmark_end)/2))-5);
minutehandwidth=10;
minuterot=0;

secondhandlen=-(graphsize[1]/2-(topmark_start-((topmark_start-topmark_end)/2))+10);
secondhandwidth=4;
secondrot=0;

backhandlen=hourhandlen/6;


while True:

    if not debug:
        curtime=datetime.datetime.now().timetuple()[3:6];

        #time rotcalc
        hour=curtime[0];
        if hour>11:
            hour=hour-12;
        minute=curtime[1];
        second=curtime[2];

        hourrot=2*math.pi*((hour+minute/60)/12);
        minuterot=2*math.pi*((minute+second/60)/60);
        secondrot=2*math.pi*second/60;

    hourhand1  =draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-hourhandlen/2-1],   [graphsize[0]/2,graphsize[1]/2+hourhandlen/2+1]],   0, color2, rotcentangle=hourrot,   rotcentdist= hourhandlen/2-3,   linewidth=hourhandwidth+4);
    hourhand2  =draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-backhandlen-1],     [graphsize[0]/2,graphsize[1]/2+backhandlen+1]],     0, color2, rotcentangle=hourrot,   rotcentdist=-backhandlen+3,     linewidth=hourhandwidth+4);
    hourhand3  =draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-hourhandlen/2],     [graphsize[0]/2,graphsize[1]/2+hourhandlen/2]],     0, color1, rotcentangle=hourrot,   rotcentdist= hourhandlen/2,     linewidth=hourhandwidth);
    hourhand4  =draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-backhandlen],       [graphsize[0]/2,graphsize[1]/2+backhandlen]],       0, color1, rotcentangle=hourrot,   rotcentdist=-backhandlen,       linewidth=hourhandwidth);
    minutehand1=draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-minutehandlen/2-1], [graphsize[0]/2,graphsize[1]/2+minutehandlen/2+1]], 0, color2, rotcentangle=minuterot, rotcentdist= minutehandlen/2-3, linewidth=minutehandwidth+3);
    minutehand2=draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-backhandlen-1],     [graphsize[0]/2,graphsize[1]/2+backhandlen+1]],     0, color2, rotcentangle=minuterot, rotcentdist=-backhandlen+3,     linewidth=minutehandwidth+3);
    minutehand3=draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-minutehandlen/2],   [graphsize[0]/2,graphsize[1]/2+minutehandlen/2]],   0, color1, rotcentangle=minuterot, rotcentdist= minutehandlen/2,   linewidth=minutehandwidth);
    minutehand4=draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-backhandlen],       [graphsize[0]/2,graphsize[1]/2+backhandlen]],       0, color1, rotcentangle=minuterot, rotcentdist=-backhandlen,       linewidth=minutehandwidth);
    secondhand1=draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-secondhandlen/2-1], [graphsize[0]/2,graphsize[1]/2+secondhandlen/2+1]], 0, color2, rotcentangle=secondrot, rotcentdist= secondhandlen/2-3, linewidth=secondhandwidth+3);
    secondhand2=draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-backhandlen-1],     [graphsize[0]/2,graphsize[1]/2+backhandlen+1]],     0, color2, rotcentangle=secondrot, rotcentdist=-backhandlen+3,     linewidth=secondhandwidth+3);
    secondhand3=draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-secondhandlen/2],   [graphsize[0]/2,graphsize[1]/2+secondhandlen/2]],   0, color1, rotcentangle=secondrot, rotcentdist= secondhandlen/2,   linewidth=secondhandwidth);
    secondhand4=draw_rotated_line(graph, [ [graphsize[0]/2,graphsize[1]/2-backhandlen],       [graphsize[0]/2,graphsize[1]/2+backhandlen]],       0, color1, rotcentangle=secondrot, rotcentdist=-backhandlen,       linewidth=secondhandwidth);
    graph.bring_figure_to_front(covercirc1);
    graph.bring_figure_to_front(covercirc2);

    event, values = window.read(100);

    if event in (sg.WIN_CLOSED,"-EXIT-"):
        break

    if debug:
        if event == '+SCRDN+':
            main_angle=main_angle-(math.pi/32);
            if main_angle < 0:
                main_angle=(31/16)*math.pi;

        if event == '+SCRUP+':
            main_angle=main_angle+(math.pi/32);
            if main_angle >= (2*math.pi):
                main_angle=0;

        hourrot=main_angle;
        minuterot=main_angle+0.7;
        secondrot=main_angle+1.4;

    graph.delete_figure(hourhand1);
    graph.delete_figure(hourhand2);
    graph.delete_figure(hourhand3);
    graph.delete_figure(hourhand4);
    graph.delete_figure(minutehand1);
    graph.delete_figure(minutehand2);
    graph.delete_figure(minutehand3);
    graph.delete_figure(minutehand4);
    graph.delete_figure(secondhand1);
    graph.delete_figure(secondhand2);
    graph.delete_figure(secondhand3);
    graph.delete_figure(secondhand4);


window.close();
