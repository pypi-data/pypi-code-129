r"""
Backend for graph visualization in plotly
"""
from pathlib import Path
import networkx as nx
import numpy as np
import pandas as pd
from typing import List, Any
from spinterface.sps_results.graph_visualization.graph_library.utilities import distribute_around_node
from spinterface.sps_results.evaluation.CMetrics import CGeodesicMetric
from spinterface.inputs.lattice.CLattice import CLattice


class CNetworkXGraph:
    r"""
    Backend class for graph visualization
    """

    def __init__(self, path_sps_calculation: Path = Path.cwd()) -> None:
        r"""
        Initializes Graph Structure based on saddle point search calculation
        """
        self.path_sps_calculation = path_sps_calculation
        self.graph = nx.Graph()
        self.Natom = self._findoutnumberatoms()
        self._add_initial()
        self._add_displaced()
        self._add_escaped(infofilename='info_mf.dat')

    def _findoutnumberatoms(self) -> int:
        r"""
        Calculates the number of atoms from the SpinSTMi file
        """
        return pd.read_csv(self.path_sps_calculation / 'SpinSTMi.dat', sep=r'\s+').shape[0]

    def _add_initial(self) -> None:
        r"""
        Adds center node, which is the initial state
        """
        eval_range = [1, 9]
        try:
            df = pd.read_csv(self.path_sps_calculation / 'info_sps_eigenvalues.dat', sep=r'\s+')
            eigenvalues = np.array(
                [df[f'eig00{eval}'].to_numpy()[0] for eval in range(eval_range[0], eval_range[1] + 1)])
            spinfile = self.path_sps_calculation / (self.path_sps_calculation / df['spin_file'].to_numpy()[0]).stem
            self.graph.add_node("Initial", eigenvalues=eigenvalues, pos=(0, 0), stage="ini", text="Initial State",
                                file=spinfile)
        except FileNotFoundError:
            print('Graph-WARNING: Did not find the eigenvalue file for the initial state. Info will be missing.')
            print('Graph-WARNING: Also initial visualization will be missing.')
            self.graph.add_node("Initial", pos=(0, 0), text="Initial State", stage="ini")

    def _add_displaced(self) -> None:
        r"""
        Adds the displaced nodes
        """
        # draw nodes
        df = pd.read_csv(self.path_sps_calculation / 'info_sps_disp.dat', sep=r'\s+')
        l_folders_sps_attempts = df['folder'].to_numpy()
        l_files_sps_attempts = df['spin_file'].to_numpy()
        # distribute displaced states around a circle
        arc = 2 * np.pi / len(df['DISPKEY'].to_numpy())
        for index, dispkey in enumerate(df['DISPKEY'].to_numpy()):
            df_disp = pd.read_csv(self.path_sps_calculation / l_folders_sps_attempts[index] / 'info_displaced.dat',
                                  sep=r'\s+')
            geo_dist_to_initial = df_disp['geodesic_distance_per_atom'].to_numpy()[0]
            position = (np.cos(index * arc) * geo_dist_to_initial, np.sin(index * arc) * geo_dist_to_initial)

            l_p_evecfile = self.path_sps_calculation / l_folders_sps_attempts[index] / str(
                (self.path_sps_calculation / l_files_sps_attempts[index]).stem).replace('spin', 'evec')
            l_p_spinfile = self.path_sps_calculation / l_folders_sps_attempts[index] / (
                    self.path_sps_calculation / l_files_sps_attempts[index]).stem
            self.graph.add_node(dispkey, eig0=df_disp['eig0'].to_numpy()[0], eig1=df_disp['eig1'].to_numpy()[0],
                                text=dispkey, pos=position, geodist=geo_dist_to_initial, file=l_p_spinfile,
                                evecfile=l_p_evecfile, stage='displace')

    def _add_escaped(self, infofilename: str = 'info_mf.dat', angle_opening: float = 180) -> None:
        r"""
        Adds the escaped nodes
        """
        df = pd.read_csv(self.path_sps_calculation / 'info_sps_esc.dat', sep=r'\s+')
        l_dispkeys_unique = set(df['DISPKEY'].to_numpy())
        # create metric to calculate geodesic distances
        geo_metric = CGeodesicMetric()
        # iterate over displaced nodes:
        for dispkey in l_dispkeys_unique:
            df_filtered = df[df['DISPKEY'] == dispkey]
            dispnode_pos = [dnode for dnode in self.get_displaced() if dnode[0] == dispkey][0][1].get('pos')
            dispnode_file = [dnode for dnode in self.get_displaced() if dnode[0] == dispkey][0][1].get('file')
            latt_disp = CLattice(source='STM',path=Path(str(dispnode_file)+'.dat'))
            esc_folders = df_filtered['folder'].to_numpy()
            nodenames = []
            geodists_total_travelled, geodist_total = [], []
            esckeys = []
            eigenvalues = []
            files = []
            for index, esckey in enumerate(df_filtered['ESCKEY'].to_numpy()):
                nodenames.append(dispkey + esckey)
                esckeys.append(esckey)
                df_esc = pd.read_csv(self.path_sps_calculation / esc_folders[index] / infofilename, sep=r'\s+')
                files.append(self.path_sps_calculation / esc_folders[index] / 'spin_mf_end')
                latt_esc = CLattice(source='STM', path=Path(str(files[index])+'.dat'))
                eigcols = [colheader for colheader in df_esc.columns if colheader.startswith('eig0')]
                last_row = df_esc.iloc[-1]
                geodist_total.append(geo_metric.distance(latt_disp,latt_esc,label1=dispkey,label2=nodenames[index]) / self.Natom)
                geodists_total_travelled.append(float(last_row['distance_total'] / self.Natom))
                eigenvalues.append(
                    np.array([float(last_row[eigcol]) for eigcol in eigcols if not last_row[eigcol] == '-']))
            pos_esc = distribute_around_node(dispnode_pos, opening_angle=180,
                                             distances_child_parent=geodist_total)
            for index, node in enumerate(nodenames):
                self.graph.add_node(node, dispkey=dispkey, esckey=esckeys[index], text=esckeys[index],
                                    pos=pos_esc[index], stage='escape', geodist=geodist_total[index],
                                    geodist_travelled=geodists_total_travelled[index],stagger = geodists_total_travelled[index] / geodist_total[index],
                                    eigenvalues=eigenvalues[index], file=files[index])

    def get_initial(self) -> List[Any]:
        r"""
            :return: The List with the initial state
            """
        return [node for node in self.graph.nodes(data=True) if node[1].get('stage') == "ini"]

    def get_displaced(self) -> List[Any]:
        r"""
            :return: The List with the displaced states
            """
        return [node for node in self.graph.nodes(data=True) if node[1].get('stage') == 'displace']

    def get_escaped(self) -> List[Any]:
        r"""
            :return: The List with the escaped states
            """
        return [node for node in self.graph.nodes(data=True) if node[1].get('stage') == 'escape']
