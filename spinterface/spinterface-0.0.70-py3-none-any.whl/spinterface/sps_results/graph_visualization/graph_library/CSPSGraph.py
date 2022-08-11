r"""
Class for graph visualization of saddle point searches as graph.
"""
from pathlib import Path
import plotly.graph_objects as go
from spinterface.sps_results.graph_visualization.graph_library.CNetworkXGraph import CNetworkXGraph
from typing import Tuple, List, Union
from PIL import Image
from spinterface.sps_results.graph_visualization.graph_library.utilities import make_multiline_text


class CSPSGraph:
    r"""
    Class for graph visualization of saddle point searches
    """

    def __init__(self, path_sps_calculation: Path = Path.cwd(),
                 title_graph: str = 'Graph: Saddle point search') -> None:
        r"""
        Initialize the graph visualization
        """
        self._path_sps_calc = path_sps_calculation
        self.title_graph = title_graph
        self.graph = CNetworkXGraph(path_sps_calculation=path_sps_calculation)
        self.fig = None
        self.edge_traces = []
        self.node_trace = go.Scatter(x=[], y=[], text=[], textposition="top center",
                                     textfont=dict(family=[],size=[],color=[]),hovertext=[],
                                     mode='markers',
                                     hoverinfo='text', marker=dict(color=[], size=[], line=None))
        self.fig = go.Figure(layout=self.graph_layout())
        self._reset_xy_limits(xrange=[-2, 2], yrange=[-2, 2])

    def load_initial(self, marker_color: str = 'black', text_color: str ='white', text_size: int = 18) -> None:
        r"""
        Adds the initial state node to the node traces
        """
        for node in self.graph.get_initial():
            self.node_trace['x'] += tuple([node[1]['pos'][0]])
            self.node_trace['y'] += tuple([node[1]['pos'][1]])
            hoverlines = [node[1]['text']]
            hoverlines.extend([f'e{i}={round(n*1e3,4)}meV' for i,n in enumerate(node[1]['eigenvalues'])])
            self.node_trace['text'] += tuple([make_multiline_text(lines=hoverlines)])
            self.node_trace['marker']['color'] += tuple([marker_color])
            self.node_trace['marker']['size'] += tuple([15])
            self.node_trace['textfont']['color'] += tuple([text_color])
            self.node_trace['textfont']['size'] += tuple([text_size])
            self.node_trace['textfont']['family'] += tuple(["sans serif"])

    def load_images_initial(self, size: Union[float, str] = 'auto') -> None:
        r"""
        Adds the initial image to the graph
        """
        # Calculate image size
        xsize = self.fig.layout.xaxis['range'][0]
        if size == 'auto':
            size = 0.3 * xsize
        for node in self.graph.get_initial():
            with Image.open(str(node[1]['file']) + '.png') as im:
                self.fig.add_layout_image(
                    dict(source=im, xref="x", yref="y", x=0, y=0, sizex=size, sizey=size, xanchor='center',
                         yanchor='middle', sizing="stretch", opacity=1.0, layer="below"))

    def load_images_displaced(self, size: Union[float, str] = 'auto', size_evec: Union[float, str] = 'auto', i_load_eigenvectors: bool = True) -> None:
        r"""
        Adds the displaced images to the graph
        """
        # Calculate image size
        xsize = self.fig.layout.xaxis['range'][0]
        if size == 'auto':
            size = 0.3 * xsize
        if size_evec == 'auto':
            size_evec = 0.15 * xsize
        for node in self.graph.get_displaced():
            with Image.open(str(node[1]['file']) + '.png') as im:
                self.fig.add_layout_image(
                    dict(source=im, xref="x", yref="y", x=node[1]['pos'][0], y=node[1]['pos'][1], sizex=size, sizey=size, xanchor='center',
                         yanchor='middle', sizing="stretch", opacity=1.0, layer="below"))
            if i_load_eigenvectors:
                with Image.open(str(node[1]['evecfile']) + '.png') as im:
                    self.fig.add_layout_image(
                        dict(source=im, xref="x", yref="y", x=node[1]['pos'][0]/2, y=node[1]['pos'][1]/2, sizex=size_evec, sizey=size_evec, xanchor='center',
                             yanchor='middle', sizing="stretch", opacity=1.0, layer="below"))

    def load_images_escaped(self, size: Union[float, str] = 'auto', size_evec: Union[float, str] = 'auto', i_load_eigenvectors: bool = False) -> None:
        r"""
        Adds the escaped images to the graph
        """
        # Calculate image size
        xsize = self.fig.layout.xaxis['range'][0]
        if size == 'auto':
            size = 0.3 * xsize
        if size_evec == 'auto':
            size_evec = 0.15 * xsize
        for node in self.graph.get_escaped():
            with Image.open(str(node[1]['file']) + '.png') as im:
                self.fig.add_layout_image(
                    dict(source=im, xref="x", yref="y", x=node[1]['pos'][0], y=node[1]['pos'][1], sizex=size, sizey=size, xanchor='center',
                         yanchor='middle', sizing="stretch", opacity=1.0, layer="above"))
            if i_load_eigenvectors:
                with Image.open(str(node[1]['evecfile']) + '.png') as im:
                    self.fig.add_layout_image(
                        dict(source=im, xref="x", yref="y", x=node[1]['pos'][0]/2, y=node[1]['pos'][1]/2, sizex=size_evec, sizey=size_evec, xanchor='center',
                             yanchor='middle', sizing="stretch", opacity=1.0, layer="below"))

    def load_displaced(self, marker_color: str = 'black', i_set_scale: bool = True) -> None:
        r"""
        Adds the displaced state nodes to the node traces
        :param i_set_scale: If the scale of the graph x,y limits shall be defined by the displaced stage
        """
        geo_dist_max = max([node[1]['geodist'] for node in self.graph.get_displaced()])
        geo_dist_max = geo_dist_max + 0.1 * geo_dist_max
        for node in self.graph.get_displaced():
            self.node_trace['x'] += tuple([node[1]['pos'][0]])
            self.node_trace['y'] += tuple([node[1]['pos'][1]])
            self.node_trace['text'] += tuple([make_multiline_text(lines=[node[1]['text'],
                                                                         'e0='+str(round(node[1]['eig0']*1e3,4))+'meV',
                                                                         'e1='+str(round(node[1]['eig1']*1e3,4))+'meV',
                                                                         'distance='+str(node[1]['geodist'])])])
            self.node_trace['marker']['color'] += tuple([marker_color])
            self.node_trace['marker']['size'] += tuple([15])
        if i_set_scale:
            self._reset_xy_limits(xrange=[-geo_dist_max, geo_dist_max], yrange=[-geo_dist_max, geo_dist_max])

    def load_escaped(self, marker_color: str = 'black', i_set_scale: bool = True) -> None:
        r"""
        Adds the escaped state nodes to the node traces
        :param i_set_scale: If the scale of the graph x,y limits shall be defined by the escaped stage
        """
        geo_dist_max_escaped = max([node[1]['geodist'] for node in self.graph.get_escaped()])
        geo_dist_max_displaced = max([node[1]['geodist'] for node in self.graph.get_displaced()])
        geo_dist_max = geo_dist_max_escaped + geo_dist_max_displaced
        geo_dist_max = geo_dist_max + 0.1 * geo_dist_max
        for node in self.graph.get_escaped():
            self.node_trace['x'] += tuple([node[1]['pos'][0]])
            self.node_trace['y'] += tuple([node[1]['pos'][1]])
            hoverlines = [node[1]['text'],'distance='+str(round(node[1]['geodist'],4)),'stagger='+str(round(node[1]['stagger'],4))]
            hoverlines.extend([f'e{i}={round(n*1e3,4)}meV' for i,n in enumerate(node[1]['eigenvalues'])])
            self.node_trace['text'] += tuple([make_multiline_text(lines=hoverlines)])
            self.node_trace['marker']['color'] += tuple([marker_color])
            self.node_trace['marker']['size'] += tuple([15])
        if i_set_scale:
            self._reset_xy_limits(xrange=[-geo_dist_max, geo_dist_max], yrange=[-geo_dist_max, geo_dist_max])

    def load_edge_initial_displaced(self, color:str ='red') -> None:
        r"""
        Draws the connection between the initial and the displaced states
        """
        initial_node = self.graph.get_initial()[0]
        for node in self.graph.get_displaced():
            self.edge_traces.append(
                self._make_edge(pos1=initial_node[1]['pos'], pos2=node[1]['pos'], text=node[1]['text'],color=color))

    def load_edge_displaced_escaped(self, color:str='blue') -> None:
        r"""
        Draws the connections between the displaced states and the escaped nodes
        """
        for disp_node in self.graph.get_displaced():
            esc_nodes = [esc_node for esc_node in self.graph.get_escaped() if esc_node[1].get('dispkey') == disp_node[0]]
            for esc_node in esc_nodes:
                self.edge_traces.append(
                    self._make_edge(pos1=disp_node[1].get('pos'), pos2=esc_node[1].get('pos'),text=str(esc_node[1].get('geodist')),color=color)
                )

    def _reset_xy_limits(self, xrange: List[float], yrange: List[float]) -> None:
        r"""
        Updates the xy-limits
        :param xrange: lower and upper x limit
        :param yrange: lower and upper y limit
        """
        self._checkforfig()
        xax = self.fig.layout.xaxis
        yax = self.fig.layout.yaxis
        xax['range'] = xrange
        yax['range'] = yrange
        self.fig.update_layout(xaxis=xax, yaxis=yax)

    def _make_edge(self, pos1: Tuple[float, float], pos2: Tuple[float, float], text: str, width: float = 2.0,
                   color: str = 'black') -> go.Scatter:
        r"""
        Creates a scatter object for a pair of nodes representing an edge
        :param pos1: position of node 1
        :param pos2: position of node 2
        :param text: text information for the edge
        :param width: line width
        :return: graph_objects scatter object representing the edge
        """
        return go.Scatter(x=[pos1[0], pos2[0], None], y=[pos1[1], pos2[1], None],
                          line=dict(width=width, color=color), hoverinfo='text', text=([text]), mode='lines')

    def graph_layout(self) -> go.Layout:
        r"""
        Defines the layout of the graph.
        :return: the plotly.graph_objects.layout instance
        """
        return go.Layout(title=self.title_graph, font=None, showlegend=True, hovermode='closest',
                         xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': True},
                         yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': True}
                         )

    def force_quadratic_layout(self, size: int = 500) -> None:
        r"""
        Forces quadratic layout
        :param size: x- and y-size in px
        """
        self._checkforfig()
        self.fig.update_layout(autosize=False, width=size, height=size, margin=dict(b=20, l=5, r=5, t=40))

    def _checkforfig(self) -> None:
        r"""
        Checks if figure was already created. Otherwise raise Exception
        """
        if self.fig is None:
            raise ValueError("Please create figure first (call create_graph_visualization)")

    def create_graph_visualization(self, i_transparent_background: False, paper_bgcolor: str = "LightSteelBlue",
                                   plot_bgcolor: str = "beige") -> None:
        r"""
        Visualizes the graph with plotly-api.
        """
        if i_transparent_background:
            self.fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        else:
            self.fig.update_layout(paper_bgcolor=paper_bgcolor, plot_bgcolor=plot_bgcolor)
        # Add nodes
        self.fig.add_trace(self.node_trace)
        for edge_trace in self.edge_traces:
            self.fig.add_trace(edge_trace)
        self.fig.update_layout(showlegend=False)

    def show(self) -> None:
        r"""
        Shows the visualization of the graph.
        """
        self.fig.show()
