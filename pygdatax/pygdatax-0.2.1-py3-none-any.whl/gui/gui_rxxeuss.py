import h5py
from silx.gui import qt, hdf5, colors
from silx.math.fit import fittheories
from silx.math.fit import FitManager, FitTheory
from silx.gui.plot.items.roi import RectangleROI, CrossROI
from silx.gui.widgets.FrameBrowser import HorizontalSliderWithBrowser
from silx.gui.hdf5 import Hdf5TreeView, Hdf5TreeModel, NexusSortFilterProxyModel
from silx.gui import icons
import silx.io
from silx.io.utils import is_group, is_dataset, is_file
from silx.io.nxdata import is_valid_nxdata, get_default

from pygdatax.gui.customsilx import Hdf5TreeModelRw, Hdf5TreeViewRw
from pygdatax.icons import getQIcon
import os
from pathlib import Path
import fabio
from pygdatax import nxlib, gui
from pygdatax.instruments import xeussrx
import numpy as np

from pygdatax.flib import get_roi


def fit_distance_and_offset(x, distance, offset):
    """
    fitting function for the specular postion
    Args:
        x: goniometer position in degree
        distance: sample to detector distance
        offset: goniometer offset in degree

    Returns:

    """
    # 0.172 is the pixel size in mm
    return np.tan(2*np.deg2rad(x-offset))*distance / 0.172

FITMANAGER = FitManager()
FITMANAGER.loadtheories(fittheories)
FITMANAGER.addtheory("specular position",
                     function=fit_distance_and_offset,
                     parameters=["distance", "offset"])





def get_edf_rx_description(filepath):
    des = []
    if os.path.isfile(filepath):
        if filepath.endswith('.edf'):
            dataObj = fabio.open(filepath)
            try:
                des.append(os.path.basename(filepath))
                des.append(dataObj.header['Comment'])
                des.append(dataObj.header['om'])
                des.append(dataObj.header['count_time'])
            except KeyError:
                des.append(os.path.split(filepath[1]))
                des += 3 * ['']
    return des


class EdfRxFileTable(qt.QTableWidget):
    directory = ''
    file_extension = '.edf'
    fileSelectedChanged = qt.pyqtSignal(str)
    directBeamFile = None

    def __init__(self, parent=None):
        super(EdfRxFileTable, self).__init__(parent=parent)
        self.setColumnCount(4)
        self.setRowCount(4)
        self.setSelectionBehavior(qt.QAbstractItemView.SelectRows)
        self.setSelectionMode(qt.QAbstractItemView.SingleSelection)
        self.setHorizontalHeaderLabels(['File', 'comment', 'om (deg))', 'counting time'])
        self.currentItemChanged.connect(self.on_selectionChanged)
        self.setContextMenuPolicy(qt.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.generateMenu)

    def setDirectory(self, directory):
        folderPath = Path(directory)
        if folderPath.is_dir():
            self.directory = folderPath
            self.refresh()

    def refresh(self):
        self.currentItemChanged.disconnect()
        if os.path.isdir(self.directory):
            l = os.listdir(self.directory)
            # l.sort()
            fileList = []
            for item in l:
                if item.endswith(self.file_extension):
                    fileList.append(item)
            # self.clearContents()
            self.setRowCount(len(fileList))
            for i, file in enumerate(fileList):
                description = get_edf_rx_description(os.path.join(self.directory, file))
                for j, des in enumerate(description):
                    item = qt.QTableWidgetItem(des)
                    item.setFlags(qt.Qt.ItemIsSelectable | qt.Qt.ItemIsEnabled)
                    self.setItem(i, j, item)
                # check of the file was current set to parametric file
                filepath = os.path.join(self.directory, file)
                if filepath == self.directBeamFile:
                    self.set_row_bkg(i, qt.QColor("red"))
                    self.item(i, 0).setIcon(getQIcon('beam.ico'))

        self.sortItems(0, qt.Qt.AscendingOrder)
        self.currentItemChanged.connect(self.on_selectionChanged)

    def on_selectionChanged(self):
        row = self.currentRow()
        file = self.item(row, 0).text()
        self.fileSelectedChanged.emit(os.path.join(self.directory, file))

    def generateMenu(self, event):
        current_item = self.itemAt(event)
        # current_item = self.selectedItems()
        menu = qt.QMenu()
        directBeamAction = qt.QAction(getQIcon('beam.ico'), 'direct beam')
        directBeamAction.triggered.connect(self._set_direct_beam)
        sampleAction = qt.QAction('sample')
        sampleAction.triggered.connect(self._set_sample)
        # maskAction = qt.QAction(getQIcon('mask.ico'), 'mask')
        # maskAction.triggered.connect(self._set_mask)
        # build menu
        menu.addAction(directBeamAction)
        menu.addAction(sampleAction)
        # menu.addAction(maskAction)
        action = menu.exec_(self.mapToGlobal(event))

    def set_row_bkg(self, row, color):
        for i in range(self.columnCount()):
            item = self.item(row, i)
            item.setBackground(color)

    def _set_sample(self):
        for current_item in self.selectedItems():
            if current_item is not None:
                row = current_item.row()
                ncol = self.columnCount()
                first_col_item = self.item(row, 0)
                file = first_col_item.text()
                self.set_row_bkg(row, qt.QColor("white"))
                first_col_item.setIcon(qt.QIcon())
                fullfile = os.path.join(self.directory, file)
                # remove double reference
                if fullfile == self.directBeamFile:
                    self.directBeamFile = None
                # elif fullfile == self.maskFile:
                #     self.maskFile = None

    def _set_direct_beam(self):
        current_item = self.currentItem()
        if current_item is not None:
            current_eb_item = self.findItems(os.path.basename(str(self.directBeamFile)), qt.Qt.MatchExactly)
            # remove the previous empty cell icons
            if current_eb_item:
                self.set_row_bkg(current_eb_item[0].row(), qt.QColor("white"))
                filepath = os.path.join(self.directory, current_eb_item[0].text())
            row = current_item.row()
            ncol = self.columnCount()
            first_col_item = self.item(row, 0)
            file = first_col_item.text()
            self.set_row_bkg(row, qt.QColor("red"))
            first_col_item.setIcon(getQIcon('beam.ico'))
            # remove double reference
            fullfile = os.path.join(self.directory, file)
            self.directBeamFile = fullfile
            # if fullfile == self.maskFile:
            #     self.maskFile = None

    def get_sample_files(self):
        sampleList = []
        nRow = self.rowCount()
        for i in range(nRow):
            first_col_item = self.item(i, 0)
            file = first_col_item.text()
            # remove double reference
            fullfile = os.path.join(self.directory, file)
            if fullfile != self.directBeamFile:
                sampleList.append(fullfile)
        return sampleList, self.directBeamFile


class EdfRxTreatmentWidget(qt.QWidget):
    fileSelectedChanged = qt.pyqtSignal(str, list)
    treatementClicked = qt.pyqtSignal(str)
    treatementPerformed = qt.pyqtSignal(str)
    roiChanged = qt.pyqtSignal(list)

    def __init__(self, parent=None):
        super(EdfRxTreatmentWidget, self).__init__(parent=parent)
        # directory selector
        self.directoryLineEdit = qt.QLineEdit(parent=self)
        self.directoryPickerButton = qt.QPushButton()
        self.directoryPickerButton.setIcon(getQIcon('directory.ico'))
        self.refreshButton = qt.QPushButton()
        self.refreshButton.setIcon(getQIcon('refresh.ico'))
        # file table
        self.table = EdfRxFileTable(parent=self)
        # beam center coordinates
        self.x0LineEdit = qt.QLineEdit('566')
        self.y0LineEdit = qt.QLineEdit('906')
        # sample to detector distance
        self.distanceLineEdit = qt.QLineEdit('1214')
        # define the angular offset in deg
        self.offsetLineEdit = qt.QLineEdit('0')
        # define the chi angle
        self.chiLineEdit = qt.QLineEdit('0')
        # roi dimension
        self.roiWidthLineEdit = qt.QLineEdit('40')
        self.roiWidthLineEdit.setValidator(qt.QIntValidator())
        self.roiHeightLineEdit = qt.QLineEdit('20')
        self.roiHeightLineEdit.setValidator(qt.QIntValidator())

        # button to treat data
        self.treatButton = qt.QPushButton('treat')
        self.treatButton.setIcon(getQIcon('gear.ico'))
        self.treatButton.setToolTip('Compute reflectivity spectra')
        # parameter form layout
        formLayout = qt.QFormLayout()
        formLayout.addRow('x0 (pixels):', self.x0LineEdit)
        formLayout.addRow('y0 (pixels):', self.y0LineEdit)
        formLayout.addRow('distance (mm):', self.distanceLineEdit)
        formLayout.addRow('offset (°) :', self.offsetLineEdit)
        formLayout.addRow('chi (°) :', self.chiLineEdit)
        formLayout.addRow('roi width (pixels):', self.roiWidthLineEdit)
        formLayout.addRow('roi height (pixels):', self.roiHeightLineEdit)
        # general layout
        hlayout = qt.QHBoxLayout()
        hlayout.addWidget(qt.QLabel('directory :'))
        hlayout.addWidget(self.directoryLineEdit)
        hlayout.addWidget(self.directoryPickerButton)
        hlayout.addWidget(self.refreshButton)
        vlayout = qt.QVBoxLayout()
        vlayout.addLayout(hlayout)
        vlayout.addLayout(formLayout)
        vlayout.addWidget(self.table)
        vlayout.addWidget(self.treatButton)
        self.setLayout(vlayout)
        # connect signals
        self.directoryLineEdit.textChanged.connect(self.set_directory)
        self.directoryPickerButton.clicked.connect(self.choose_directory)
        self.table.fileSelectedChanged.connect(self.on_selectionChanged)
        self.treatButton.clicked.connect(self.treat)
        # parameter signal
        self.x0LineEdit.textEdited.connect(self.on_parameters_changed)
        self.y0LineEdit.textEdited.connect(self.on_parameters_changed)
        self.distanceLineEdit.textChanged.connect(self.on_parameters_changed)
        self.offsetLineEdit.textChanged.connect(self.on_parameters_changed)
        self.chiLineEdit.textChanged.connect(self.on_parameters_changed)
        self.roiWidthLineEdit.textChanged.connect(self.on_parameters_changed)
        self.roiHeightLineEdit.textChanged.connect(self.on_parameters_changed)

    def on_parameters_changed(self):
        row = self.table.currentRow()
        if row >=0:
            params = self.get_parameters()
            file = self.table.item(row, 0).text()
            path = os.path.join(self.table.directory, file)
            if path == self.table.directBeamFile:
                omega = 0
                offset = 0
                chi = 0
            else:
                omega = float(self.table.item(row, 2).text())
                offset = params['offset']
                chi = params['chi']
            # building roi
            try:
                x1, y1, x2, y2 = get_roi(params['x0'], params['y0'], params['roi_width'], params['roi_height'],
                                         omega-offset, params['distance'], pixel_size=0.172, chi=chi)
                # x1 = params['x0'] - params['roi_width'] / 2
                # x2 = params['x0'] + params['roi_width'] / 2
                # y1 = params['y0'] - params['roi_height'] / 2
                # y2 = params['y0'] + params['roi_height'] / 2
                # disp = np.tan(2 * np.deg2rad(omega - offset)) * params['distance'] / 0.172
                # y1 -= disp
                # y2 -= disp
                roi = [x1, y1, x2, y2]
            except TypeError:
                roi = 4 * [None]
            self.roiChanged.emit(roi)

    def treat(self):
        qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)
        try:
            x0 = float(self.x0LineEdit.text())
        except ValueError:
            x0 = None
        try:
            y0 = float(self.y0LineEdit.text())
        except ValueError:
            y0 = None
        try:
            offset = float(self.offsetLineEdit.text())
        except ValueError:
            offset = 0
        try:
            distance = float(self.distanceLineEdit.text())
        except ValueError:
            distance = None
        try:
            roi_width = float(self.roiWidthLineEdit.text())
        except ValueError:
            roi_width = None
        try:
            roi_height = float(self.roiHeightLineEdit.text())
        except ValueError:
            roi_height = None

        try:
            chi = float(self.chiLineEdit.text())
        except ValueError:
            chi = 0
        try:
            fileList, directBeamFile = self.table.get_sample_files()
            outputFolder = os.path.abspath(os.path.join(self.table.directory, os.pardir))
            outputFilename = os.path.relpath(self.table.directory, start=outputFolder) + '.nxs'
            outputFullPath = os.path.join(outputFolder, outputFilename)
            self.treatementClicked.emit(outputFullPath)
            nxlib.build_rxnexus_from_edf(fileList, directBeamFile, outputFullPath,
                                         offset=offset, chi=chi)
            xeussrx.set_center(outputFullPath, x0=x0, y0=y0)
            xeussrx.set_roi(outputFullPath, roi_width=roi_width, roi_height=roi_height)
            xeussrx.set_distance(outputFullPath, distance=distance)
            # offset is already set
            xeussrx.compute_ref(outputFullPath)
            self.treatementPerformed.emit(outputFullPath)
        except:
            print("treatment could not be performed")
        qt.QApplication.restoreOverrideCursor()

    def set_directory(self):
        text = self.directoryLineEdit.text()
        self.table.setDirectory(text)
        # if os.path.exists(text):
        #     os.chdir(text)

    def choose_directory(self):
        # if self.table.directory:
        #     if os.path.exists(self.table.directory):
        #         basedir = self.table.directory
        #     else:
        #         basedir = os.path.expanduser("~")
        # else:

        basedir = os.path.expanduser("~")
        fname = qt.QFileDialog.getExistingDirectory(self, 'Select data directory', directory=basedir,
                                                    options=qt.QFileDialog.DontUseNativeDialog)
        if fname:
            self.directoryLineEdit.setText(fname)
            # self.edfTab.table.setDirectory(fname)
            # self.nxsTab.setDirectory(fname)

    def on_selectionChanged(self):
        row = self.table.currentRow()
        if row >= 0:
            params = self.get_parameters()
            file = self.table.item(row, 0).text()
            path = os.path.join(self.table.directory, file)
            if path == self.table.directBeamFile:
                omega = 0
                offset = 0
                chi = 0
            else:
                omega = float(self.table.item(row, 2).text())
                offset = params['offset']
                chi = params['chi']
            # building roi
            try:
                x1, y1, x2, y2 = get_roi(params['x0'], params['y0'], params['roi_width'], params['roi_height'],
                                         omega - offset, params['distance'], pixel_size=0.172, chi=chi)
                # x1 = params['x0'] - params['roi_width']/2
                #
                # x2 = params['x0'] + params['roi_width'] / 2
                # y1 = params['y0'] - params['roi_height'] / 2
                # y2 = params['y0'] + params['roi_height'] / 2
                # disp = np.tan(2*np.deg2rad(omega-offset))*params['distance'] / 0.172
                # y1 -= disp
                # y2 -= disp
                roi = [x1, y1, x2, y2]
            except TypeError:
                roi = 4*[None]
            self.fileSelectedChanged.emit(path, roi)

    def get_parameters(self):
        params = {}
        try:
            params['x0'] = float(self.x0LineEdit.text())
        except ValueError:
            params['x0'] = None
        try:
            params['y0'] = float(self.y0LineEdit.text())
        except ValueError:
            params['y0'] = None
        try:
            params['offset'] = float(self.offsetLineEdit.text())
        except ValueError:
            params['offset'] = 0
        try:
            params['distance'] = float(self.distanceLineEdit.text())
        except ValueError:
            params['distance'] = None
        try:
            params['roi_width'] = float(self.roiWidthLineEdit.text())
        except ValueError:
            params['roi_width'] = None
        try:
            params['roi_height'] = float(self.roiHeightLineEdit.text())
        except ValueError:
            params['roi_height'] = None
        try:
            params['chi'] = float(self.chiLineEdit.text())
        except ValueError:
            params['chi'] = 0

        return params


# TODO: display stack with roi at the good position
class EdfViewerRX(gui.DataView):

    def __init__(self):
        super(EdfViewerRX, self).__init__(fitmanager=None)

    def displayEdf(self, file):
        self.clearCurves()
        self.setKeepDataAspectRatio(True)
        self.setXAxisLogarithmic(False)
        self.setYAxisLogarithmic(False)
        dataObj = fabio.open(file)
        data = dataObj.data
        self.addImage(data)

    def displayRoi(self, roi):
        # display roi of interation
        if roi == 4 * [None]:
            return
        self.roiManager.disconnect()
        roisList = self.roiManager.getRois()
        for r in roisList:
            if not isinstance(r, CrossROI):
                self.roiManager.removeRoi(r)
        currentRoi = RectangleROI()
        currentRoi.setGeometry(origin=[roi[0], roi[1]], size=[roi[2] - roi[0], roi[3] - roi[1]])
        self.roiManager.addRoi(currentRoi)
        self.roiManager.sigRoiAdded.connect(self.updateAddedRegionOfInterest)


    def displayH5pyObject(self, h5pyObjectList):
        if type(h5pyObjectList) is not list:
            h5pyObjectList = list(h5pyObjectList)
        self.clear()
        self.setKeepDataAspectRatio(False)
        c = ['blue', 'red', 'green', 'black', 'yellow', 'grey', 'magenta', 'cyan',
             'darkGreen', 'darkBrown', 'darkCyan', 'darkYellow', 'darkMagenta']

        for i, h5py_object in enumerate(h5pyObjectList):
            if is_group(h5py_object) or is_file(h5py_object):
                nxd = get_default(h5py_object)
                if nxd is None:
                    return
                elif not nxd.is_valid:
                    return
                legend = os.path.split(h5py_object.file.filename)[1] + h5py_object.name
                if nxd.is_curve:
                    xlabel = nxd.axes_names[0]
                    ylabel = nxd.signal_name
                    if 'units' in nxd.axes[0].attrs:
                        xlabel += ' [' + nxd.axes[0].attrs['units'] + ']'
                    if 'units' in nxd.signal.attrs:
                        ylabel += ' [' + nxd.signal.attrs['units'] + ']'
                    self.addCurve(nxd.axes[0], nxd.signal,
                                  yerror=nxd.errors,
                                  legend=legend,
                                  replace=False,
                                  color=colors.COLORDICT[c[i]],
                                  xlabel=xlabel,
                                  ylabel=ylabel,
                                  resetzoom=True)
                    self.setGraphXLabel(xlabel)
                    self.setGraphYLabel(ylabel)
                    self.setKeepDataAspectRatio(False)
                elif nxd.is_image:
                    if nxd.axes_names == [None, None]:
                        origin = (0., 0.)
                        scale = (1., 1.)
                        xlabel = 'x [pixel]'
                        ylabel = 'y [pixel]'
                        self.setKeepDataAspectRatio(True)
                        self.setXAxisLogarithmic(False)
                        self.setYAxisLogarithmic(False)
                    else:
                        # aspect_button = self.plotWindow.getKeepDataAspectRatioButton()
                        self.setKeepDataAspectRatio(False)
                        origin = (nxd.axes[1][0], nxd.axes[0][1])
                        scale_x = np.abs(nxd.axes[1][0] - nxd.axes[1][-1]) / len(nxd.axes[1])
                        scale_y = np.abs(nxd.axes[0][0] - nxd.axes[0][-1]) / len(nxd.axes[0])
                        scale = (scale_x, scale_y)
                        xlabel = nxd.axes_names[1]
                        ylabel = nxd.axes_names[0]
                        if 'units' in nxd.axes[1].attrs:
                            xlabel += ' [' + nxd.axes[1].attrs['units'] + ']'
                        if 'units' in nxd.axes[0].attrs:
                            ylabel += ' [' + nxd.axes[0].attrs['units'] + ']'

                    self.addImage(nxd.signal, replace=True,
                                  legend=legend, xlabel='x',
                                  ylabel='y',
                                  origin=origin,
                                  scale=scale)
                    self.setGraphXLabel(xlabel)
                    self.setGraphYLabel(ylabel)
                elif nxd.is_scatter:
                    xlabel = nxd.axes_names[0]
                    ylabel = nxd.axes_names[1]
                    if 'units' in nxd.axes[0].attrs:
                        xlabel += ' [' + nxd.axes[0].attrs['units'] + ']'
                    if 'units' in nxd.signal.attrs:
                        ylabel += ' [' + nxd.axes[1].attrs['units'] + ']'
                    self.addScatter(nxd.axes[0], nxd.axes[1], nxd.signal, symbol='.', copy=False)
                    self.setGraphXLabel(xlabel)
                    self.setGraphYLabel(ylabel)
                    self.setKeepDataAspectRatio(False)
                else:
                    return

            elif is_dataset(h5py_object):
                legend = os.path.split(h5py_object.file.filename)[1] + h5py_object.name
                if len(h5py_object.shape) == 2:
                    origin = (0., 0.)
                    scale = (1., 1.)
                    xlabel = 'x [pixel]'
                    ylabel = 'y [pixel]'
                    self.setKeepDataAspectRatio(True)
                    self.addImage(h5py_object, replace=True,
                                  legend=legend, xlabel='x',
                                  ylabel='y',
                                  origin=origin,
                                  scale=scale)
                    self.setGraphXLabel(xlabel)
                    self.setGraphYLabel(ylabel)
                elif len(h5py_object.shape) == 1:
                    xlabel = 'index'
                    ylabel = h5py_object.name
                    if 'units' in h5py_object.attrs:
                        ylabel += ' [' + str(h5py_object.attrs['units']) + ']'
                    x = np.arange(len(h5py_object)) + 1
                    self.addCurve(x, h5py_object,
                                  legend=legend,
                                  replace=False,
                                  color=colors.COLORDICT[c[i]],
                                  xlabel=xlabel,
                                  ylabel=ylabel,
                                  resetzoom=True)
                    self.setGraphXLabel(xlabel)
                    self.setGraphYLabel(ylabel)
                    self.setKeepDataAspectRatio(False)
                else:
                    return


# class NexusRXTreeWidget(qt.QWidget):
#     operationPerformed = qt.pyqtSignal()
#     selectedNodeChanged = qt.pyqtSignal(list)
#
#     def __init__(self):
#         super(NexusRXTreeWidget, self).__init__()
#         """Silx HDF5 TreeView"""
#         self.treeview = hdf5.Hdf5TreeView(self)
#         treemodel = hdf5.Hdf5TreeModel(self.treeview,
#                                        ownFiles=True
#                                        )
#         # treemodel.sigH5pyObjectLoaded.connect(self.__h5FileLoaded)
#         # treemodel.sigH5pyObjectRemoved.connect(self.__h5FileRemoved)
#         # treemodel.sigH5pyObjectSynchronized.connect(self.__h5FileSynchonized)
#         treemodel.setDatasetDragEnabled(False)
#         # self.treeview.setModel(treemodel)
#         self.__treeModelSorted = gui.hdf5.NexusSortFilterProxyModel(self.treeview)
#         self.__treeModelSorted.setSourceModel(treemodel)
#         self.__treeModelSorted.sort(0, qt.Qt.AscendingOrder)
#         self.__treeModelSorted.setSortCaseSensitivity(qt.Qt.CaseInsensitive)
#         self.treeview.setModel(self.__treeModelSorted)
#         self.treeview.setSelectionMode(qt.QAbstractItemView.ExtendedSelection)
#         # layout
#         # hlayout.addWidget(self.sync_btn)
#         vlayout = qt.QVBoxLayout()
#         vlayout.addWidget(self.treeview)
#         self.setLayout(vlayout)
#
#         # connect signals
#         # self.sync_btn.clicked.connect(self.sync_all)
#         self.treeview.selectionModel().selectionChanged.connect(self.on_tree_selection)
#
#     def load_files(self, files):
#         model = self.treeview.findHdf5TreeModel()
#         model.clear()
#         for file in files:
#             model.insertFile(file, row=-1)
#         self.treeview.expandToDepth(0)
#
#     def sync_all(self):
#         model = self.treeview.findHdf5TreeModel()
#         nrow = model.rowCount()
#
#         for n in range(nrow):
#             index = model.index(n, 0, qt.QModelIndex())
#             node = model.nodeFromIndex(index)
#             filename = node.obj.filename
#             model.removeH5pyObject(node.obj)
#             model.insertFile(filename, row=n)
#         self.treeview.expandToDepth(0)
#         self.operationPerformed.emit()
#
#     def on_tree_selection(self):
#         selected = list(self.treeview.selectedH5Nodes())
#         self.selectedNodeChanged.emit(selected)


class NexusRxViewer(gui.DataView):

    def __init__(self, parent=None):
        super(NexusRxViewer, self).__init__(fitmanager=FITMANAGER)
        self._browser_label = qt.QLabel("image index :")
        central_widget = self.centralWidget()
        self._browser = HorizontalSliderWithBrowser(self)
        layout = central_widget.layout()
        layout.addWidget(self._browser)
        central_widget.setLayout(layout)
        self._browser.hide()
        self.stack = None

    def displayStack(self, nxstack):
        shape = nxstack.shape
        self.stack = nxstack
        self._browser.setMinimum(0)
        self._browser.setMaximum(shape[2])
        self._browser.setValue(0)
        self._browser.show()
        self.addImage(nxstack.nxsignal[:, :, 0])


class NexusRxTreeWidget(qt.QWidget):
    selectedNodeChanged = qt.pyqtSignal(list)

    def __init__(self):
        super(NexusRxTreeWidget, self).__init__()
        self.treeview = Hdf5TreeViewRw(self)
        # treeModel = Hdf5TreeModel(self.treeview, ownFiles=False)
        treeModel = Hdf5TreeModelRw(self.treeview, ownFiles=False)
        # treeModel.sigH5pyObjectLoaded.connect(self.__h5FileLoaded)
        # treeModel.sigH5pyObjectRemoved.connect(self.__h5FileRemoved)
        # treeModel.sigH5pyObjectSynchronized.connect(self.__h5FileSynchonized)
        treeModel.setDatasetDragEnabled(True)
        self.__treeModelSorted = NexusSortFilterProxyModel(self.treeview)
        self.__treeModelSorted.setSourceModel(treeModel)
        self.__treeModelSorted.sort(0, qt.Qt.AscendingOrder)
        self.__treeModelSorted.setSortCaseSensitivity(qt.Qt.CaseInsensitive)
        self.treeview.setModel(self.__treeModelSorted)
        self.treeview.setSelectionMode(qt.QAbstractItemView.ExtendedSelection)
        self.treeview.addContextMenuCallback(self.customContextMenu)

        self._treeWindow = self._createTreeWindow(self.treeview)
        # layout
        layout = qt.QVBoxLayout()
        layout.addWidget(self._treeWindow)
        self.setLayout(layout)
        # connect signals
        self.treeview.selectionModel().selectionChanged.connect(self.on_tree_selection)

    def _createTreeWindow(self, treeView):
        toolbar = qt.QToolBar(self)
        toolbar.setIconSize(qt.QSize(16, 16))
        toolbar.setStyleSheet("QToolBar { border: 0px }")

        action = qt.QAction(toolbar)
        action.setIcon(icons.getQIcon("view-refresh"))
        action.setText("Refresh")
        action.setToolTip("Refresh all selected items")
        action.triggered.connect(self._refreshSelected)
        action.setShortcut(qt.QKeySequence(qt.Qt.Key_F5))
        toolbar.addAction(action)
        treeView.addAction(action)
        self.__refreshAction = action

        # Another shortcut for refresh
        action = qt.QAction(toolbar)
        action.setShortcut(qt.QKeySequence(qt.Qt.ControlModifier + qt.Qt.Key_R))
        treeView.addAction(action)
        # action.triggered.connect(self._refreshSelected())

        action = qt.QAction(toolbar)
        # action.setIcon(icons.getQIcon("view-refresh"))
        action.setText("Close")
        action.setToolTip("Close selected item")
        action.triggered.connect(self.__removeSelected)
        action.setShortcut(qt.QKeySequence(qt.Qt.Key_Delete))
        treeView.addAction(action)
        self.__closeAction = action

        toolbar.addSeparator()

        action = qt.QAction(toolbar)
        action.setIcon(icons.getQIcon("tree-expand-all"))
        action.setText("Expand all")
        action.setToolTip("Expand all selected items")
        action.triggered.connect(self.__expandAllSelected)
        action.setShortcut(qt.QKeySequence(qt.Qt.ControlModifier + qt.Qt.Key_Plus))
        toolbar.addAction(action)
        treeView.addAction(action)
        self.__expandAllAction = action

        action = qt.QAction(toolbar)
        action.setIcon(icons.getQIcon("tree-collapse-all"))
        action.setText("Collapse all")
        action.setToolTip("Collapse all selected items")
        action.triggered.connect(self.__collapseAllSelected)
        action.setShortcut(qt.QKeySequence(qt.Qt.ControlModifier + qt.Qt.Key_Minus))
        toolbar.addAction(action)
        treeView.addAction(action)
        self.__collapseAllAction = action

        action = qt.QAction("&Sort file content", toolbar)
        action.setIcon(icons.getQIcon("tree-sort"))
        action.setToolTip("Toggle sorting of file content")
        action.setCheckable(True)
        action.setChecked(True)
        action.triggered.connect(self.setContentSorted)
        toolbar.addAction(action)
        treeView.addAction(action)
        self._sortContentAction = action

        action = qt.QAction("&Load Nexus files", toolbar)
        action.setIcon(icons.getQIcon("document-open"))
        action.setToolTip("Load nexus files")
        action.setCheckable(False)
        # action.setChecked(True)
        action.triggered.connect(self.openNexusFiles)
        toolbar.addAction(action)
        treeView.addAction(action)
        self._openNexusFileAction = action

        action = qt.QAction("&Close Selected files", toolbar)
        action.setIcon(icons.getQIcon("close"))
        action.setToolTip("Close selected files")
        action.setCheckable(False)
        # action.setChecked(True)
        action.triggered.connect(self.__removeSelected)
        toolbar.addAction(action)
        treeView.addAction(action)
        self._closeSelected = action

        widget = qt.QWidget(self)
        layout = qt.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(toolbar)
        layout.addWidget(treeView)
        return widget

    def _refreshSelected(self):
        """Refresh all selected items
        """
        qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)

        selection = self.treeview.selectionModel()
        indexes = selection.selectedIndexes()
        selectedItems = []
        model = self.treeview.model()
        h5files = set([])
        while len(indexes) > 0:
            index = indexes.pop(0)
            if index.column() != 0:
                continue
            h5 = model.data(index, role=Hdf5TreeModel.H5PY_OBJECT_ROLE)
            rootIndex = index
            # Reach the root of the tree
            while rootIndex.parent().isValid():
                rootIndex = rootIndex.parent()
            rootRow = rootIndex.row()
            relativePath = self.__getRelativePath(model, rootIndex, index)
            selectedItems.append((rootRow, relativePath))
            h5files.add(h5.file)

        if len(h5files) == 0:
            qt.QApplication.restoreOverrideCursor()
            return

        model = self.treeview.findHdf5TreeModel()
        for h5 in h5files:
            self._synchronizeH5pyObject(h5)

        model = self.treeview.model()
        itemSelection = qt.QItemSelection()
        for rootRow, relativePath in selectedItems:
            rootIndex = model.index(rootRow, 0, qt.QModelIndex())
            index = self.__indexFromPath(model, rootIndex, relativePath)
            if index is None:
                continue
            indexEnd = model.index(index.row(), model.columnCount() - 1, index.parent())
            itemSelection.select(index, indexEnd)
        selection.select(itemSelection, qt.QItemSelectionModel.ClearAndSelect)

        qt.QApplication.restoreOverrideCursor()

    def __removeSelected(self):
        """Close selected items"""
        qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)

        selection = self.treeview.selectionModel()
        indexes = selection.selectedIndexes()
        selectedItems = []
        model = self.treeview.model()
        h5files = set([])
        while len(indexes) > 0:
            index = indexes.pop(0)
            if index.column() != 0:
                continue
            h5 = model.data(index, role=Hdf5TreeModel.H5PY_OBJECT_ROLE)
            rootIndex = index
            # Reach the root of the tree
            while rootIndex.parent().isValid():
                rootIndex = rootIndex.parent()
            rootRow = rootIndex.row()
            relativePath = self.__getRelativePath(model, rootIndex, index)
            selectedItems.append((rootRow, relativePath))
            h5files.add(h5.file)

        if len(h5files) != 0:
            model = self.treeview.findHdf5TreeModel()
            for h5 in h5files:
                row = model.h5pyObjectRow(h5)
                model.removeH5pyObject(h5)

        qt.QApplication.restoreOverrideCursor()

    def _synchronizeH5pyObject(self, h5):
        model = self.treeview.findHdf5TreeModel()
        # This is buggy right now while h5py do not allow to close a file
        # while references are still used.
        # FIXME: The architecture have to be reworked to support this feature.
        # model.synchronizeH5pyObject(h5)

        filename = h5.filename
        row = model.h5pyObjectRow(h5)
        index = self.treeview.model().index(row, 0, qt.QModelIndex())
        paths = self._getPathFromExpandedNodes(self.treeview, index)
        model.removeH5pyObject(h5)
        model.insertFile(filename, row)
        index = self.treeview.model().index(row, 0, qt.QModelIndex())
        self._expandNodesFromPaths(self.treeview, index, paths)

    def __getRelativePath(self, model, rootIndex, index):
        """Returns a relative path from an index to his rootIndex.
        If the path is empty the index is also the rootIndex.
        """
        path = ""
        while index.isValid():
            if index == rootIndex:
                return path
            name = model.data(index)
            if path == "":
                path = name
            else:
                path = name + "/" + path
            index = index.parent()

        # index is not a children of rootIndex
        raise ValueError("index is not a children of the rootIndex")

    def _getPathFromExpandedNodes(self, view, rootIndex):
        """Return relative path from the root index of the extended nodes"""
        model = view.model()
        rootPath = None
        paths = []
        indexes = [rootIndex]
        while len(indexes):
            index = indexes.pop(0)
            if not view.isExpanded(index):
                continue

            node = model.data(index, role=Hdf5TreeModel.H5PY_ITEM_ROLE)
            path = node._getCanonicalName()
            if rootPath is None:
                rootPath = path
            path = path[len(rootPath):]
            paths.append(path)

            for child in range(model.rowCount(index)):
                childIndex = model.index(child, 0, index)
                indexes.append(childIndex)

        return paths

    def _expandNodesFromPaths(self, view, rootIndex, paths):
        model = view.model()
        for path in paths:
            index = self.__indexFromPath(model, rootIndex, path)
            if index is not None:
                view.setExpanded(index, True)

    def __indexFromPath(self, model, rootIndex, path):
        elements = path.split("/")
        if elements[0] == "":
            elements.pop(0)
        index = rootIndex
        while len(elements) != 0:
            element = elements.pop(0)
            found = False
            for child in range(model.rowCount(index)):
                childIndex = model.index(child, 0, index)
                name = model.data(childIndex)
                if element == name:
                    index = childIndex
                    found = True
                    break
            if not found:
                return None
        return index

    def __expandAllSelected(self):
        """Expand all selected items of the tree.
        The depth is fixed to avoid infinite loop with recurssive links.
        """
        qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)

        selection = self.treeview.selectionModel()
        indexes = selection.selectedIndexes()
        model = self.treeview.model()
        while len(indexes) > 0:
            index = indexes.pop(0)
            if isinstance(index, tuple):
                index, depth = index
            else:
                depth = 0
            if index.column() != 0:
                continue

            if depth > 10:
                # Avoid infinite loop with recursive links
                break

            if model.hasChildren(index):
                self.treeview.setExpanded(index, True)
                for row in range(model.rowCount(index)):
                    childIndex = model.index(row, 0, index)
                    indexes.append((childIndex, depth + 1))
        qt.QApplication.restoreOverrideCursor()

    def __collapseAllSelected(self):
        """Collapse all selected items of the tree.
        The depth is fixed to avoid infinite loop with recurssive links.
        """
        selection = self.treeview.selectionModel()
        indexes = selection.selectedIndexes()
        model = self.treeview.model()
        while len(indexes) > 0:
            index = indexes.pop(0)
            if isinstance(index, tuple):
                index, depth = index
            else:
                depth = 0
            if index.column() != 0:
                continue

            if depth > 10:
                # Avoid infinite loop with recursive links
                break

            if model.hasChildren(index):
                self.treeview.setExpanded(index, False)
                for row in range(model.rowCount(index)):
                    childIndex = model.index(row, 0, index)
                    indexes.append((childIndex, depth + 1))

    def isContentSorted(self):
        """Returns whether the file content is sorted or not.
        :rtype: bool
        """
        return self.treeview.model() is self.__treeModelSorted

    def setContentSorted(self, sort):
        """Set whether file content should be sorted or not.
        :param bool sort:
        """
        sort = bool(sort)
        if sort != self.isContentSorted():

            # save expanded nodes
            pathss = []
            root = qt.QModelIndex()
            model = self.treeview.model()
            for i in range(model.rowCount(root)):
                index = model.index(i, 0, root)
                paths = self._getPathFromExpandedNodes(self.treeview, index)
                pathss.append(paths)

            self.treeview.setModel(
                self.__treeModelSorted if sort else self.__treeModelSorted.sourceModel())
            self._sortContentAction.setChecked(self.isContentSorted())

            # restore expanded nodes
            model = self.treeview.model()
            for i in range(model.rowCount(root)):
                index = model.index(i, 0, root)
                paths = pathss.pop(0)
                self._expandNodesFromPaths(self.treeview, index, paths)

    def customContextMenu(self, event):
        """Called to populate the context menu
        :param silx.gui.hdf5.Hdf5ContextMenuEvent event: Event
            containing expected information to populate the context menu
        """
        selectedObjects = list(event.source().selectedH5Nodes(ignoreBrokenLinks=False))  # that's an iterator
        menu = event.menu()

        if not menu.isEmpty():
            menu.addSeparator()

        all_files = True
        # check if all items are h5py files
        n_objecst = 0
        file_list = []
        for obj in selectedObjects:
            n_objecst += 1
            h5 = obj.h5py_object
            file_list.append(h5.filename)
            if not silx.io.is_file(h5):
                all_files = False
            # if silx.io.is_file(h5):
            #     action = qt.QAction("Close %s" % obj.local_filename, event.source())
            #     action.triggered.connect(lambda: self.treeview.findHdf5TreeModel().removeH5pyObject(h5))
            #     menu.addAction(action)
            #     action = qt.QAction("Synchronize %s" % obj.local_filename, event.source())
            #     action.triggered.connect(lambda: self._synchronizeH5pyObject(h5))
            #     menu.addAction(action)
        if all_files and n_objecst > 1:
            action = qt.QAction("Concatenate files", event.source())
            action.setIcon(getQIcon('concat.ico'))
            action.triggered.connect(lambda: self._concat(file_list))
            menu.addAction(action)
        else:
            for obj in selectedObjects:
                h5 = obj.h5py_object
                print(obj)
                if is_valid_nxdata(h5):
                    action = qt.QAction("Delete %s" % h5.name, event.source())
                    action.setIcon(icons.getQIcon("remove"))
                    action.triggered.connect(lambda: self._deleteDataset(obj))
                    menu.addAction(action)

    def on_tree_selection(self):
        """Emit the NexusRXTreeWidget.selectedNodeChangeSignal which is a list of
         h5py objects like :class:`h5py.File`, :class:`h5py.Group`, :class:`h5py.Dataset` or mimicked objects.

        :rtype: None
        """
        selected = list(self.treeview.selectedH5Nodes())
        for s in selected:
            print()
        self.selectedNodeChanged.emit(selected)

    def openNexusFiles(self):
        basedir = os.path.expanduser("~")
        fname = qt.QFileDialog.getOpenFileNames(None, 'Select Direct Beam', basedir,
                                               'Nexus files (*.nxs)',
                                                options=qt.QFileDialog.DontUseNativeDialog)
        if fname[0]:
            model = self.treeview.findHdf5TreeModel()
            for filePath in fname[0]:
                model.insertFile(filePath)

    def getSelectedFiles(self):
        """
        Returns selected filenames list
        Returns:

        """
        selection = self.treeview.selectionModel()
        indexes = selection.selectedIndexes()
        selectedItems = []
        model = self.treeview.model()
        h5files = set([])
        while len(indexes) > 0:
            index = indexes.pop(0)
            if index.column() != 0:
                continue
            h5 = model.data(index, role=Hdf5TreeModel.H5PY_OBJECT_ROLE)
            rootIndex = index
            # Reach the root of the tree
            while rootIndex.parent().isValid():
                rootIndex = rootIndex.parent()
            rootRow = rootIndex.row()
            relativePath = self.__getRelativePath(model, rootIndex, index)
            selectedItems.append((rootRow, relativePath))
            h5files.add(h5.file)
        return h5files

    def _deleteDataset(self, h5node):
        model = self.treeview.findHdf5TreeModel()
        path = h5node.local_name
        msg = qt.QMessageBox.warning(self, 'Warning', "Are your sure you want to delete this dataset : %s" % path,
                                     qt.QMessageBox.Yes | qt.QMessageBox.No)
        if msg == qt.QMessageBox.Yes:
            del h5node.local_file[path]
            self._synchronizeH5pyObject(h5node.local_file)
        else:
            print('canceled operation')

    def _concat(self, fileList):
        # firstname = h5files[0].filename
        directory = os.path.dirname(fileList[0])
        # name, done = qt.QInputDialog.getText(self, 'Concatenate files', 'new file name:', qt.QLineEdit.Normal, basename)
        name, _ = qt.QFileDialog.getSaveFileName(None, 'Save concatenated file', directory, 'Nexus files (*.nxs)',
                                                 options=qt.QFileDialog.DontUseNativeDialog)
        if name:
            h5File = h5py.File(name, mode='a')
            model = self.treeview.findHdf5TreeModel()
            row = -1
            if model.indexFromH5Object(h5File).isValid():
                row = model.indexFromH5Object(h5File).row()
                model.removeH5pyObject(h5File)
            xeussrx.concatenate(name, fileList)
            model.insertFile(name, row=row)
        return


class XeussRxMainWindow(qt.QMainWindow):
    """
    This window show an example of use of a Hdf5TreeView.

    The tree is initialized with a list of filenames. A panel allow to play
    with internal property configuration of the widget, and a text screen
    allow to display events.
    """

    def __init__(self):
        super(XeussRxMainWindow, self).__init__()
        self.plotWindow = EdfViewerRX()
        self.edfWidget = EdfRxTreatmentWidget(parent=self)
        self.treeWidget = NexusRxTreeWidget()
        tabWidget = qt.QTabWidget()

        tabWidget.addTab(self.edfWidget, 'raw data')
        tabWidget.addTab(self.treeWidget, 'nexus data')

        # self.nxsWidget = gui.NexusFileTable(parent=self)
        spliter = qt.QSplitter(qt.Qt.Horizontal)
        spliter.addWidget(tabWidget)
        spliter.addWidget(self.plotWindow)
        spliter.setStretchFactor(1, 1)
        main_panel = qt.QWidget(self)
        layout = qt.QVBoxLayout()
        layout.addWidget(spliter)
        layout.setStretchFactor(spliter, 1)
        main_panel.setLayout(layout)
        self.setCentralWidget(main_panel)
        #treatment dock widget
        self.treatmentDock = qt.QDockWidget('treatment', self)
        self.treatmentDock.setFeatures(qt.QDockWidget.DockWidgetFloatable |
                                       qt.QDockWidget.DockWidgetMovable)
        self.editor = gui.CommandTreatmentWidget(self, module=xeussrx,
                                                 decorator='@nxlib.rxtreatment_function')

        # self.setLayout(layout)
        # connect signals
        self.edfWidget.fileSelectedChanged.connect(self.plot)
        self.edfWidget.roiChanged.connect(self.plotWindow.displayRoi)
        self.treeWidget.selectedNodeChanged.connect(self.displayNxs)
        self.treatmentDock.setWidget(self.editor)
        self.treatmentDock.setFloating(False)
        # replace the addTabbedwidget metho of the plot window
        self.plotWindow._dockWidgets.append(self.treatmentDock)
        self.plotWindow.addDockWidget(qt.Qt.RightDockWidgetArea, self.treatmentDock)

        self.functionListWidget = gui.FunctionListWidget(parent=self, module=xeussrx,
                                                         decorator='@nxlib.rxtreatment_function')
        self.functionListDock = qt.QDockWidget('functions', self)
        self.functionListDock.setFeatures(qt.QDockWidget.DockWidgetFloatable |
                                          qt.QDockWidget.DockWidgetMovable)
        self.functionListDock.setFloating(False)
        self.functionListDock.setWidget(self.functionListWidget)
        self.plotWindow._dockWidgets.append(self.functionListDock)
        self.plotWindow.tabifyDockWidget(self.treatmentDock, self.functionListDock)
        self.functionListDock.show()

        # signal
        self.functionListWidget.runFunction.connect(self.runFunction)
        self.edfWidget.treatementClicked.connect(self.onRawTreatment)
        self.edfWidget.treatementPerformed.connect(self.onRawTreatmentDone)
        treeModel = self.treeWidget.treeview.findHdf5TreeModel()
        treeModel.sigH5pyObjectRemoved.connect(self.__h5FileRemoved)
        treeModel.sigH5pyObjectSynchronized.connect(self.__h5FileSynchonized)

    def onRawTreatment(self, nxsfilepath):
        # model = self.treeWidget.treeview.model()
        # model.clear()
        pass

    def onRawTreatmentDone(self, nxsfilepath):
        h5File = h5py.File(nxsfilepath)
        model = self.treeWidget.treeview.findHdf5TreeModel()
        if model.indexFromH5Object(h5File).isValid():
            model.synchronizeH5pyObject(h5File)
            # h5File.close()
        # model.insertFile(nxsfilepath)

    def plot(self, file, roi):
        self.plotWindow.displayEdf(file)
        self.plotWindow.displayRoi(roi)

    def displayNxs(self, nodes):
        # self.plotWindow.clear()
        # self.plotWindow.setKeepDataAspectRatio(False)
        # c = ['blue', 'red', 'green', 'black', 'yellow', 'grey', 'magenta', 'cyan',
        #      'darkGreen', 'darkBrown', 'darkCyan', 'darkYellow', 'darkMagenta']
        h5ObjectList = []
        for s in nodes:
            h5ObjectList.append(s.h5py_object)
        self.plotWindow.displayH5pyObject(h5ObjectList)

    def runFunction(self, cmdList):
        qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)
        if type(cmdList) is not list:
            cmdList = [cmdList]
        selectedH5Files = self.treeWidget.getSelectedFiles()
        model = self.treeWidget.treeview.findHdf5TreeModel()
        for h5file in selectedH5Files:
            for script in cmdList:
                row = model.h5pyObjectRow(h5file)
                index = model.index(row, 0, qt.QModelIndex())
                paths = self.treeWidget._getPathFromExpandedNodes(self.treeWidget.treeview, index)
                filename = h5file.filename
                # model.removeH5pyObject(h5file)
                # h5file.close()
                for line in script.splitlines():
                    cmd = 'xeussrx.' + line.replace('root', '\'' + filename.replace('\\', '/') + '\'')
                    try:
                        print(cmd)
                        eval(cmd)
                        # self.treeWidget._synchronizeH5pyObject(h5file)
                    except (ValueError, TypeError) as error:
                        print('command failed : %s ' % error)
                    except nx.NeXusError as error:
                        print(('Nexus error : %s') % error)

                    # else:
                    #     print('command : ' + cmd + 'not performed on:' + filename)
        self.treeWidget._refreshSelected()
        qt.QApplication.restoreOverrideCursor()

    def __h5FileRemoved(self, removedH5):
        removedH5.close()

    def __h5FileSynchonized(self, removedH5, loadedH5):
        removedH5.close()


def main():
    # unlock hdf5 files for file access during plotting
    os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'
    # warnings.filterwarnings("ignore", category=mplDeprecation)
    app = qt.QApplication([])
    # sys.excepthook = qt.exceptionHandler
    window = XeussRxMainWindow()
    window.show()
    result = app.exec_()
    # remove ending warnings relative to QTimer
    app.deleteLater()
    sys.exit(result)


if __name__ == '__main__':
    import sys
    import pygdatax.gui
    from silx.math.fit import FitManager

    os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'
    # warnings.filterwarnings("ignore", category=mplDeprecation)
    from silx.gui.fit import FitWidget
    import nexusformat.nexus as nx
    from silx.math.fit import FitManager, FitTheory, fittheories

    def linearfun(x, a, b):
        return a * x + b


    app = qt.QApplication([])
    # w = EdfRxTreatmentWidget()
    # w.directoryLineEdit.setText('/home/achennev/Bureau/PIL pour tiago/RX_tiago/9_11_2020/TH1_10_1000_pos1')
    # w = XeussRxMainWindow()
    # w.edfWidget.directoryLineEdit.setText('/home/achennev/Bureau/PIL pour tiago/RX_tiago/9_11_2020/TH1_10_1000_pos1')
    # w = NexusRxTreeWidget()
    w = XeussRxMainWindow()
    w.edfWidget.directoryLineEdit.setText('/home/achennev/Documents/collab lay theng/2020-02-18-LT/SiP2_pos1')
    model = w.treeWidget.treeview.findHdf5TreeModel()
    model.insertFile('/home/achennev/Documents/collab lay theng/2020-02-18-LT/SiP2_pos1.nxs')
    model.insertFile('/home/achennev/Documents/collab lay theng/2020-02-18-LT/SiP2_pos2.nxs')
    # model.insertFile('/home/achennev/Documents/collab lay theng/2020-02-18-LT/SiP2_merged.nxs')
    #
    # model = w._treeview.model()
    # model.insertFile('/home/achennev/Bureau/PIL pour tiago/2020-10-22-TOC/2020-10-22-TOC_0_52473.nxs')
    # w = NexusRxViewer()
    w.show()
    result = app.exec_()
    app.deleteLater()
    sys.exit(result)
