"""Qt implementation of _Renderer and GUI."""

# Authors: Guillaume Favelier <guillaume.favelier@gmail.com>
#          Eric Larson <larson.eric.d@gmail.com>
#
# License: Simplified BSD

from contextlib import contextmanager
import os
import platform
import sys
import weakref

import pyvista
from pyvistaqt.plotting import FileDialog, MainWindow

from qtpy.QtCore import Qt, Signal, QLocale, QObject, QLibraryInfo
from qtpy.QtGui import QIcon, QCursor
from qtpy.QtWidgets import (QComboBox, QDockWidget, QDoubleSpinBox, QGroupBox,
                            QHBoxLayout, QLabel, QToolButton, QMenuBar,
                            QSlider, QSpinBox, QVBoxLayout, QWidget,
                            QSizePolicy, QScrollArea, QStyle, QProgressBar,
                            QStyleOptionSlider, QLayout, QCheckBox,
                            QButtonGroup, QRadioButton, QLineEdit, QGridLayout,
                            QFileDialog, QPushButton, QMessageBox)

from ._pyvista import _PyVistaRenderer
from ._pyvista import (_close_all, _close_3d_figure, _check_3d_figure,  # noqa: F401,E501 analysis:ignore
                       _set_3d_view, _set_3d_title, _take_3d_screenshot)  # noqa: F401,E501 analysis:ignore
from ._abstract import (_AbstractDock, _AbstractToolBar, _AbstractMenuBar,
                        _AbstractStatusBar, _AbstractLayout, _AbstractWidget,
                        _AbstractWindow, _AbstractMplCanvas, _AbstractPlayback,
                        _AbstractBrainMplCanvas, _AbstractMplInterface,
                        _AbstractWidgetList, _AbstractAction, _AbstractDialog,
                        _AbstractKeyPress)
from ._utils import (_qt_disable_paint, _qt_get_stylesheet, _qt_is_dark,
                     _qt_detect_theme, _qt_raise_window)
from ..utils import safe_event
from ...utils import _check_option, get_config
from ...fixes import _compare_version

# Adapted from matplotlib
if (sys.platform == 'darwin' and
        _compare_version(platform.mac_ver()[0], '>=', '10.16') and
        QLibraryInfo.version().segments() <= [5, 15, 2]):
    os.environ.setdefault("QT_MAC_WANTS_LAYER", "1")


class _QtKeyPress(_AbstractKeyPress):
    _widget_id = 0
    _callbacks = dict()
    _to_qt = dict(
        escape=Qt.Key_Escape,
        up=Qt.Key_Up,
        down=Qt.Key_Down,
        left=Qt.Key_Left,
        right=Qt.Key_Right,
        comma=Qt.Key_Comma,
        period=Qt.Key_Period,
        page_up=Qt.Key_PageUp,
        page_down=Qt.Key_PageDown,
    )

    def _keypress_initialize(self, widget=None):
        widget = self._window if widget is None else widget
        self._widget_id = _QtKeyPress._widget_id
        _QtKeyPress._widget_id += 1
        _QtKeyPress._callbacks[self._widget_id] = dict()

        def keyPressEvent(event):
            text = event.text()
            widget_callbacks = _QtKeyPress._callbacks[self._widget_id]
            if text in widget_callbacks:
                callback = widget_callbacks[text]
                callback()
            else:
                key = event.key()
                if key in widget_callbacks:
                    callback = widget_callbacks[key]
                    callback()

        widget.keyPressEvent = keyPressEvent

    def _keypress_add(self, shortcut, callback):
        widget_callbacks = _QtKeyPress._callbacks[self._widget_id]
        if len(shortcut) > 1:  # special key
            shortcut = _QtKeyPress._to_qt[shortcut]
        widget_callbacks[shortcut] = callback

    def _keypress_trigger(self, shortcut):
        widget_callbacks = _QtKeyPress._callbacks[self._widget_id]
        if len(shortcut) > 1:  # special key
            shortcut = _QtKeyPress._to_qt[shortcut]
        widget_callbacks[shortcut]()


class _QtDialog(_AbstractDialog):
    # from QMessageBox.StandardButtons
    supported_button_names = [
        "Ok", "Open", "Save", "Cancel", "Close", "Discard", "Apply",
        "Reset", "RestoreDefaults", "Help", "SaveAll", "Yes",
        "YesToAll", "No", "NoToAll", "Abort", "Retry", "Ignore"
    ]
    # from QMessageBox.Icon
    supported_icon_names = [
        "NoIcon", "Question", "Information", "Warning", "Critical"
    ]

    def _dialog_create(self, title, text, info_text, callback, *,
                       icon='Warning', buttons=[], modal=True, window=None):
        window = self._window if window is None else window
        widget = QMessageBox(window)
        widget.setWindowTitle(title)
        widget.setText(text)
        # icon is one of _QtDialog.supported_icon_names
        icon_id = getattr(QMessageBox, icon)
        widget.setIcon(icon_id)
        widget.setInformativeText(info_text)

        if not buttons:
            buttons = ["Ok"]

        button_ids = list()
        for button in buttons:
            # button is one of _QtDialog.supported_button_names
            button_id = getattr(QMessageBox, button)
            button_ids.append(button_id)
        standard_buttons = default_button = button_ids[0]
        for button_id in button_ids[1:]:
            standard_buttons |= button_id
        widget.setStandardButtons(standard_buttons)
        widget.setDefaultButton(default_button)

        @safe_event
        def func(button):
            button_id = widget.standardButton(button)
            for button_name in _QtDialog.supported_button_names:
                if button_id == getattr(QMessageBox, button_name):
                    widget.setCursor(QCursor(Qt.WaitCursor))
                    try:
                        callback(button_name)
                    finally:
                        widget.unsetCursor()
                        break

        widget.buttonClicked.connect(func)
        return _QtDialogWidget(widget, modal)


class _QtLayout(_AbstractLayout):
    def _layout_initialize(self, max_width):
        pass

    def _layout_add_widget(self, layout, widget, stretch=0,
                           *, row=None, col=None):
        """Add a widget to an existing layout."""
        if isinstance(widget, QLayout):
            layout.addLayout(widget)
        else:
            if isinstance(layout, QGridLayout):
                layout.addWidget(widget, row, col)
            else:
                layout.addWidget(widget, stretch)

    def _layout_create(self, orientation='vertical'):
        if orientation == 'vertical':
            layout = QVBoxLayout()
        elif orientation == 'horizontal':
            layout = QHBoxLayout()
        else:
            assert orientation == 'grid'
            layout = QGridLayout()
        return layout


class _QtDock(_AbstractDock, _QtLayout):
    def _dock_initialize(self, window=None, name="Controls",
                         area="left", max_width=None):
        window = self._window if window is None else window
        qt_area = getattr(Qt, f'{area.capitalize()}DockWidgetArea')
        self._dock, self._dock_layout = _create_dock_widget(
            window, name, qt_area, max_width=max_width
        )
        if area == "left":
            window.setCorner(Qt.BottomLeftCorner, Qt.LeftDockWidgetArea)
        else:
            window.setCorner(Qt.BottomRightCorner, Qt.RightDockWidgetArea)

    def _dock_finalize(self):
        self._dock.setMinimumSize(self._dock.sizeHint().width(), 0)
        self._dock_add_stretch(self._dock_layout)

    def _dock_show(self):
        self._dock.show()

    def _dock_hide(self):
        self._dock.hide()

    def _dock_add_stretch(self, layout=None):
        layout = self._dock_layout if layout is None else layout
        layout.addStretch()

    def _dock_add_layout(self, vertical=True):
        layout = QVBoxLayout() if vertical else QHBoxLayout()
        return layout

    def _dock_add_label(
        self, value, *, align=False, layout=None, selectable=False
    ):
        layout = self._dock_layout if layout is None else layout
        widget = QLabel()
        if align:
            widget.setAlignment(Qt.AlignCenter)
        widget.setText(value)
        widget.setWordWrap(True)
        if selectable:
            widget.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self._layout_add_widget(layout, widget)
        return _QtWidget(widget)

    def _dock_add_button(
        self, name, callback, *, style='pushbutton', icon=None, tooltip=None,
        layout=None
    ):
        _check_option(
            parameter='style',
            value=style,
            allowed_values=('toolbutton', 'pushbutton')
        )
        if style == 'toolbutton':
            widget = QToolButton()
            widget.setText(name)
        else:
            widget = QPushButton(name)
            # Don't change text color upon button press
            widget.setStyleSheet(
                'QPushButton:pressed {color: none;}'
            )
        if icon is not None:
            widget.setIcon(self._icons[icon])

        _set_widget_tooltip(widget, tooltip)
        widget.clicked.connect(callback)

        layout = self._dock_layout if layout is None else layout
        self._layout_add_widget(layout, widget)
        return _QtWidget(widget)

    def _dock_named_layout(self, name, *, layout=None, compact=True):
        layout = self._dock_layout if layout is None else layout
        if name is not None:
            hlayout = self._dock_add_layout(not compact)
            self._dock_add_label(
                value=name, align=not compact, layout=hlayout)
            self._layout_add_widget(layout, hlayout)
            layout = hlayout
        return layout

    def _dock_add_slider(self, name, value, rng, callback, *,
                         compact=True, double=False, tooltip=None,
                         layout=None):
        layout = self._dock_named_layout(
            name=name, layout=layout, compact=compact)
        slider_class = QFloatSlider if double else QSlider
        cast = float if double else int
        widget = slider_class(Qt.Horizontal)
        _set_widget_tooltip(widget, tooltip)
        widget.setMinimum(cast(rng[0]))
        widget.setMaximum(cast(rng[1]))
        widget.setValue(cast(value))
        if double:
            widget.floatValueChanged.connect(callback)
        else:
            widget.valueChanged.connect(callback)
        self._layout_add_widget(layout, widget)
        return _QtWidget(widget)

    def _dock_add_check_box(self, name, value, callback, *, tooltip=None,
                            layout=None):
        layout = self._dock_layout if layout is None else layout
        widget = QCheckBox(name)
        _set_widget_tooltip(widget, tooltip)
        widget.setChecked(value)
        widget.stateChanged.connect(callback)
        self._layout_add_widget(layout, widget)
        return _QtWidget(widget)

    def _dock_add_spin_box(self, name, value, rng, callback, *,
                           compact=True, double=True, step=None,
                           tooltip=None, layout=None):
        layout = self._dock_named_layout(
            name=name, layout=layout, compact=compact)
        value = value if double else int(value)
        widget = QDoubleSpinBox() if double else QSpinBox()
        _set_widget_tooltip(widget, tooltip)
        widget.setAlignment(Qt.AlignCenter)
        widget.setMinimum(rng[0])
        widget.setMaximum(rng[1])
        widget.setKeyboardTracking(False)
        if step is None:
            inc = (rng[1] - rng[0]) / 20.
            inc = max(int(round(inc)), 1) if not double else inc
            widget.setSingleStep(inc)
        else:
            widget.setSingleStep(step)
        widget.setValue(value)
        widget.valueChanged.connect(callback)
        self._layout_add_widget(layout, widget)
        return _QtWidget(widget)

    def _dock_add_combo_box(self, name, value, rng, callback, *, compact=True,
                            tooltip=None, layout=None):
        layout = self._dock_named_layout(
            name=name, layout=layout, compact=compact)
        widget = QComboBox()
        _set_widget_tooltip(widget, tooltip)
        widget.addItems(rng)
        widget.setCurrentText(value)
        widget.currentTextChanged.connect(callback)
        widget.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self._layout_add_widget(layout, widget)
        return _QtWidget(widget)

    def _dock_add_radio_buttons(self, value, rng, callback, *, vertical=True,
                                layout=None):
        layout = self._dock_layout if layout is None else layout
        group_layout = QVBoxLayout() if vertical else QHBoxLayout()
        group = QButtonGroup()
        for val in rng:
            button = QRadioButton(val)
            if val == value:
                button.setChecked(True)
            group.addButton(button)
            self._layout_add_widget(group_layout, button)

        def func(button):
            callback(button.text())
        group.buttonClicked.connect(func)
        self._layout_add_widget(layout, group_layout)
        return _QtWidgetList(group)

    def _dock_add_group_box(self, name, *, collapse=None, layout=None):
        layout = self._dock_layout if layout is None else layout
        hlayout = QVBoxLayout()
        widget = QGroupBox(name)
        widget.setLayout(hlayout)
        self._layout_add_widget(layout, widget)
        return hlayout

    def _dock_add_text(self, name, value, placeholder, *, callback=None,
                       layout=None):
        layout = self._dock_layout if layout is None else layout
        widget = QLineEdit(value)
        widget.setPlaceholderText(placeholder)
        self._layout_add_widget(layout, widget)
        if callback is not None:
            widget.textChanged.connect(callback)
        return _QtWidget(widget)

    def _dock_add_file_button(
        self, name, desc, func, *, filter=None, initial_directory=None,
        save=False, is_directory=False, icon=False, tooltip=None, layout=None
    ):
        layout = self._dock_layout if layout is None else layout

        def callback():
            if is_directory:
                name = QFileDialog.getExistingDirectory(
                    directory=initial_directory
                )
            elif save:
                name = QFileDialog.getSaveFileName(
                    directory=initial_directory,
                    filter=filter
                )
            else:
                name = QFileDialog.getOpenFileName(
                    directory=initial_directory,
                    filter=filter
                )
            name = name[0] if isinstance(name, tuple) else name
            # handle the cancel button
            if len(name) == 0:
                return
            func(name)

        if icon:
            kwargs = dict(style='toolbutton', icon='folder')
        else:
            kwargs = dict()
        button_widget = self._dock_add_button(
            name=desc,
            callback=callback,
            tooltip=tooltip,
            layout=layout,
            **kwargs
        )
        return button_widget  # It's already a _QtWidget instance


class QFloatSlider(QSlider):
    """Slider that handles float values."""

    floatValueChanged = Signal(float)

    def __init__(self, ori, parent=None):
        """Initialize the slider."""
        super().__init__(ori, parent)
        self._opt = QStyleOptionSlider()
        self.initStyleOption(self._opt)
        self._gr = self.style().subControlRect(
            QStyle.CC_Slider, self._opt, QStyle.SC_SliderGroove, self)
        self._sr = self.style().subControlRect(
            QStyle.CC_Slider, self._opt, QStyle.SC_SliderHandle, self)
        self._precision = 10000
        super().valueChanged.connect(self._convert)

    def _convert(self, value):
        self.floatValueChanged.emit(value / self._precision)

    def minimum(self):
        """Get the minimum."""
        return super().minimum() / self._precision

    def setMinimum(self, value):
        """Set the minimum."""
        super().setMinimum(int(value * self._precision))

    def maximum(self):
        """Get the maximum."""
        return super().maximum() / self._precision

    def setMaximum(self, value):
        """Set the maximum."""
        super().setMaximum(int(value * self._precision))

    def value(self):
        """Get the current value."""
        return super().value() / self._precision

    def setValue(self, value):
        """Set the current value."""
        super().setValue(int(value * self._precision))

    # Adapted from:
    # https://stackoverflow.com/questions/52689047/moving-qslider-to-mouse-click-position  # noqa: E501
    def mousePressEvent(self, event):
        """Add snap-to-location handling."""
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        sr = self.style().subControlRect(
            QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)
        if (event.button() != Qt.LeftButton or sr.contains(event.pos())):
            super().mousePressEvent(event)
            return
        if self.orientation() == Qt.Vertical:
            half = (0.5 * sr.height()) + 0.5
            max_ = self.height()
            pos = max_ - event.y()
        else:
            half = (0.5 * sr.width()) + 0.5
            max_ = self.width()
            pos = event.x()
        max_ = max_ - 2 * half
        pos = min(max(pos - half, 0), max_) / max_
        val = self.minimum() + (self.maximum() - self.minimum()) * pos
        val = (self.maximum() - val) if self.invertedAppearance() else val
        self.setValue(val)
        event.accept()
        # Process afterward so it's seen as a drag
        super().mousePressEvent(event)


class _QtToolBar(_AbstractToolBar, _QtLayout):
    def _tool_bar_initialize(self, name="default", window=None):
        self.actions = dict()
        window = self._window if window is None else window
        self._tool_bar = window.addToolBar(name)
        self._tool_bar_layout = self._tool_bar.layout()

    def _tool_bar_add_button(self, name, desc, func, *, icon_name=None,
                             shortcut=None):
        icon_name = name if icon_name is None else icon_name
        icon = self._icons[icon_name]
        self.actions[name] = _QtAction(self._tool_bar.addAction(
            icon, desc, func))
        if shortcut is not None:
            self.actions[name].set_shortcut(shortcut)

    def _tool_bar_update_button_icon(self, name, icon_name):
        self.actions[name].set_icon(self._icons[icon_name])

    def _tool_bar_add_text(self, name, value, placeholder):
        pass

    def _tool_bar_add_spacer(self):
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self._tool_bar.addWidget(spacer)

    def _tool_bar_add_file_button(self, name, desc, func, *, shortcut=None):
        weakself = weakref.ref(self)

        def callback(weakself=weakself):
            weakself = weakself()
            if weakself is None:
                return
            return FileDialog(
                weakself._window,
                callback=func,
            )

        self._tool_bar_add_button(
            name=name,
            desc=desc,
            func=callback,
            shortcut=shortcut,
        )

    def _tool_bar_add_play_button(self, name, desc, func, *, shortcut=None):
        self._tool_bar_add_button(
            name=name, desc=desc, func=func, icon_name=None, shortcut=shortcut)


class _QtMenuBar(_AbstractMenuBar):
    def _menu_initialize(self, window=None):
        self._menus = dict()
        self._menu_actions = dict()
        self._menu_bar = QMenuBar()
        self._menu_bar.setNativeMenuBar(False)
        window = self._window if window is None else window
        window.setMenuBar(self._menu_bar)

    def _menu_add_submenu(self, name, desc):
        self._menus[name] = self._menu_bar.addMenu(desc)
        self._menu_actions[name] = dict()

    def _menu_add_button(self, menu_name, name, desc, func):
        menu = self._menus[menu_name]
        self._menu_actions[menu_name][name] = \
            _QtAction(menu.addAction(desc, func))


class _QtStatusBar(_AbstractStatusBar, _QtLayout):
    def _status_bar_initialize(self, window=None):
        window = self._window if window is None else window
        self._status_bar = window.statusBar()

    def _status_bar_add_label(self, value, *, stretch=0):
        widget = QLabel(value)
        self._layout_add_widget(self._status_bar.layout(), widget, stretch)
        return _QtWidget(widget)

    def _status_bar_add_progress_bar(self, stretch=0):
        widget = QProgressBar()
        self._layout_add_widget(self._status_bar.layout(), widget, stretch)
        return _QtWidget(widget)

    def _status_bar_update(self):
        self._status_bar.layout().update()


class _QtPlayback(_AbstractPlayback):
    def _playback_initialize(self, func, timeout, value, rng,
                             time_widget, play_widget):
        self.figure.plotter.add_callback(func, timeout)


class _QtMplInterface(_AbstractMplInterface):
    def _mpl_initialize(self):
        from qtpy import QtWidgets
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
        self.canvas = FigureCanvasQTAgg(self.fig)
        FigureCanvasQTAgg.setSizePolicy(
            self.canvas,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        FigureCanvasQTAgg.updateGeometry(self.canvas)


class _QtMplCanvas(_AbstractMplCanvas, _QtMplInterface):
    def __init__(self, width, height, dpi):
        super().__init__(width, height, dpi)
        self._mpl_initialize()


class _QtBrainMplCanvas(_AbstractBrainMplCanvas, _QtMplInterface):
    def __init__(self, brain, width, height, dpi):
        super().__init__(brain, width, height, dpi)
        self._mpl_initialize()
        if brain.separate_canvas:
            self.canvas.setParent(None)
        else:
            self.canvas.setParent(brain._renderer._window)
        self._connect()


class _QtWindow(_AbstractWindow):
    def _window_initialize(
        self, *, window=None, central_layout=None, fullscreen=False
    ):
        super()._window_initialize()
        self._interactor = self.figure.plotter.interactor
        if window is None:
            self._window = self.figure.plotter.app_window
        else:
            self._window = window

        if fullscreen:
            self._window.setWindowState(Qt.WindowFullScreen)

        if central_layout is not None:
            central_widget = self._window.centralWidget()
            if central_widget is None:
                central_widget = QWidget()
                self._window.setCentralWidget(central_widget)
            central_widget.setLayout(central_layout)
        self._window_load_icons()
        self._window_set_theme()
        self._window.setLocale(QLocale(QLocale.Language.English))
        self._window.signal_close.connect(self._window_clean)
        self._window_before_close_callbacks = list()
        self._window_after_close_callbacks = list()

        # patch closeEvent
        def closeEvent(event):
            # functions to call before closing
            accept_close_event = True
            for callback in self._window_before_close_callbacks:
                ret = callback()
                # check if one of the callbacks ignores the close event
                if isinstance(ret, bool) and not ret:
                    accept_close_event = False

            if accept_close_event:
                self._window.signal_close.emit()
                event.accept()
            else:
                event.ignore()

            # functions to call after closing
            for callback in self._window_after_close_callbacks:
                callback()
        self._window.closeEvent = closeEvent

    def _window_load_icons(self):
        self._icons["help"] = QIcon.fromTheme("help")
        self._icons["play"] = QIcon.fromTheme("play")
        self._icons["pause"] = QIcon.fromTheme("pause")
        self._icons["reset"] = QIcon.fromTheme("reset")
        self._icons["scale"] = QIcon.fromTheme("scale")
        self._icons["clear"] = QIcon.fromTheme("clear")
        self._icons["movie"] = QIcon.fromTheme("movie")
        self._icons["restore"] = QIcon.fromTheme("restore")
        self._icons["screenshot"] = QIcon.fromTheme("screenshot")
        self._icons["visibility_on"] = QIcon.fromTheme("visibility_on")
        self._icons["visibility_off"] = QIcon.fromTheme("visibility_off")
        self._icons["folder"] = QIcon.fromTheme("folder")

    def _window_clean(self):
        self.figure._plotter = None
        self._interactor = None

    def _window_close_connect(self, func, *, after=True):
        if after:
            self._window_after_close_callbacks.append(func)
        else:
            self._window_before_close_callbacks.append(func)

    def _window_close_disconnect(self, after=True):
        if after:
            self._window_after_close_callbacks.clear()
        else:
            self._window_before_close_callbacks.clear()

    def _window_get_dpi(self):
        return self._window.windowHandle().screen().logicalDotsPerInch()

    def _window_get_size(self):
        w = self._interactor.geometry().width()
        h = self._interactor.geometry().height()
        return (w, h)

    def _window_get_simple_canvas(self, width, height, dpi):
        return _QtMplCanvas(width, height, dpi)

    def _window_get_mplcanvas(self, brain, interactor_fraction, show_traces,
                              separate_canvas):
        w, h = self._window_get_mplcanvas_size(interactor_fraction)
        self._interactor_fraction = interactor_fraction
        self._show_traces = show_traces
        self._separate_canvas = separate_canvas
        self._mplcanvas = _QtBrainMplCanvas(
            brain, w, h, self._window_get_dpi())
        return self._mplcanvas

    def _window_adjust_mplcanvas_layout(self):
        canvas = self._mplcanvas.canvas
        self._mpl_dock, dock_layout = _create_dock_widget(
            self._window, "Traces", Qt.BottomDockWidgetArea)
        dock_layout.addWidget(canvas)

    def _window_get_cursor(self):
        return self._window.cursor()

    def _window_set_cursor(self, cursor):
        self._interactor.setCursor(cursor)
        self._window.setCursor(cursor)

    def _window_new_cursor(self, name):
        return QCursor(getattr(Qt, name))

    @contextmanager
    def _window_ensure_minimum_sizes(self):
        sz = self.figure.store['window_size']
        adjust_mpl = (self._show_traces and not self._separate_canvas)
        # plotter:            pyvista.plotting.qt_plotting.BackgroundPlotter
        # plotter.interactor: vtk.qt.QVTKRenderWindowInteractor.QVTKRenderWindowInteractor -> QWidget  # noqa
        # plotter.app_window: pyvista.plotting.qt_plotting.MainWindow -> QMainWindow  # noqa
        # plotter.frame:      QFrame with QVBoxLayout with plotter.interactor as centralWidget  # noqa
        # plotter.ren_win:    vtkXOpenGLRenderWindow
        self._interactor.setMinimumSize(*sz)
        # Lines like this are useful for debugging these issues:
        # print('*' * 80)
        # print(0, self._interactor.app_window.size().height(), self._interactor.size().height(), self._mpl_dock.widget().height(), self._mplcanvas.canvas.size().height())  # noqa
        if adjust_mpl:
            mpl_h = int(round((sz[1] * self._interactor_fraction) /
                              (1 - self._interactor_fraction)))
            self._mplcanvas.canvas.setMinimumSize(sz[0], mpl_h)
            self._mpl_dock.widget().setMinimumSize(sz[0], mpl_h)
        try:
            yield  # show
        finally:
            # 1. Process events
            self._process_events()
            self._process_events()
            # 2. Get the window and interactor sizes that work
            win_sz = self._window.size()
            ren_sz = self._interactor.size()
            # 3. Undo the min size setting and process events
            self._interactor.setMinimumSize(0, 0)
            if adjust_mpl:
                self._mplcanvas.canvas.setMinimumSize(0, 0)
                self._mpl_dock.widget().setMinimumSize(0, 0)
            self._process_events()
            self._process_events()
            # 4. Compute the extra height required for dock decorations and add
            win_h = win_sz.height()
            if adjust_mpl:
                win_h += max(
                    self._mpl_dock.widget().size().height() - mpl_h, 0)
            # 5. Resize the window and interactor to the correct size
            #    (not sure why, but this is required on macOS at least)
            self._interactor.window_size = (win_sz.width(), win_h)
            self._interactor.resize(ren_sz.width(), ren_sz.height())
            self._process_events()
            self._process_events()

    def _window_set_theme(self, theme=None):
        if theme is None:
            default_theme = _qt_detect_theme()
        else:
            default_theme = theme
        theme = get_config('MNE_3D_OPTION_THEME', default_theme)
        stylesheet = _qt_get_stylesheet(theme)
        self._window.setStyleSheet(stylesheet)
        if _qt_is_dark(self._window):
            QIcon.setThemeName('dark')
        else:
            QIcon.setThemeName('light')

    def _window_create(self):
        return _MNEMainWindow()


class _QtWidgetList(_AbstractWidgetList):
    def __init__(self, src):
        self._src = src
        self._widgets = list()
        if isinstance(self._src, QButtonGroup):
            widgets = self._src.buttons()
        else:
            widgets = src
        for widget in widgets:
            if not isinstance(widget, _QtWidget):
                widget = _QtWidget(widget)
            self._widgets.append(widget)

    def set_enabled(self, state):
        for widget in self._widgets:
            widget.set_enabled(state)

    def get_value(self, idx):
        return self._widgets[idx].get_value()

    def set_value(self, idx, value):
        if isinstance(self._src, QButtonGroup):
            self._widgets[idx].set_value(True)
        else:
            self._widgets[idx].set_value(value)


class _QtWidget(_AbstractWidget):
    def set_value(self, value):
        if isinstance(self._widget, (QRadioButton, QToolButton, QPushButton)):
            self._widget.click()
        else:
            if hasattr(self._widget, "setValue"):
                self._widget.setValue(value)
            elif hasattr(self._widget, "setCurrentText"):
                self._widget.setCurrentText(value)
            elif hasattr(self._widget, "setChecked"):
                self._widget.setChecked(value)
            else:
                assert hasattr(self._widget, "setText")
                self._widget.setText(value)

    def get_value(self):
        if hasattr(self._widget, "value"):
            return self._widget.value()
        elif hasattr(self._widget, "currentText"):
            return self._widget.currentText()
        elif hasattr(self._widget, "checkState"):
            return self._widget.checkState() != Qt.Unchecked
        else:
            assert hasattr(self._widget, "text")
            return self._widget.text()

    def set_range(self, rng):
        self._widget.setRange(rng[0], rng[1])

    def show(self):
        self._widget.show()

    def hide(self):
        self._widget.hide()

    def set_enabled(self, state):
        self._widget.setEnabled(state)

    def is_enabled(self):
        return self._widget.isEnabled()

    def update(self, repaint=True):
        self._widget.update()
        if repaint:
            self._widget.repaint()

    def get_tooltip(self):
        assert hasattr(self._widget, 'toolTip')
        return self._widget.toolTip()

    def set_tooltip(self, tooltip):
        assert hasattr(self._widget, 'setToolTip')
        self._widget.setToolTip(tooltip)

    def set_style(self, style):
        stylesheet = ""
        for key, val in style.items():
            stylesheet = stylesheet + f"{key}:{val};"
        self._widget.setStyleSheet(stylesheet)


class _QtDialogCommunicator(QObject):
    signal_show = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)


class _QtDialogWidget(_QtWidget):
    def __init__(self, widget, modal):
        super().__init__(widget)
        self._modal = modal
        self._communicator = _QtDialogCommunicator()
        self._communicator.signal_show.connect(self.show)

    def trigger(self, button):
        button_id = getattr(QMessageBox, button)
        for current_button in self._widget.buttons():
            if self._widget.standardButton(current_button) == button_id:
                current_button.click()

    def show(self, thread=False):
        if thread:
            self._communicator.signal_show.emit()
        else:
            if self._modal:
                self._widget.exec()
            else:
                self._widget.show()


class _QtAction(_AbstractAction):
    def trigger(self):
        self._action.trigger()

    def set_icon(self, icon):
        self._action.setIcon(icon)

    def set_shortcut(self, shortcut):
        self._action.setShortcut(shortcut)


class _Renderer(_PyVistaRenderer, _QtDock, _QtToolBar, _QtMenuBar,
                _QtStatusBar, _QtWindow, _QtPlayback, _QtDialog,
                _QtKeyPress):
    _kind = 'qt'

    def __init__(self, *args, **kwargs):
        fullscreen = kwargs.pop('fullscreen', False)
        super().__init__(*args, **kwargs)
        self._window_initialize(fullscreen=fullscreen)

    def show(self):
        super().show()
        with _qt_disable_paint(self.plotter):
            with self._window_ensure_minimum_sizes():
                self.plotter.app_window.show()
        self._update()
        for plotter in self._all_plotters:
            plotter.updateGeometry()
            plotter._render()
        # Ideally we would just put a `splash.finish(plotter.window())` in the
        # same place that we initialize this (_init_qt_app call). However,
        # the window show event is triggered (closing the splash screen) well
        # before the window actually appears for complex scenes like the coreg
        # GUI. Therefore, we close after all these events have been processed
        # here.
        self._process_events()
        splash = getattr(self.figure, 'splash', False)
        if splash:
            splash.close()
        _qt_raise_window(self.plotter.app_window)


def _set_widget_tooltip(widget, tooltip):
    if tooltip is not None:
        widget.setToolTip(tooltip)


def _create_dock_widget(window, name, area, *, max_width=None):
    # create dock widget
    dock = QDockWidget(name)
    # add scroll area
    scroll = QScrollArea(dock)
    dock.setWidget(scroll)
    # give the scroll area a child widget
    widget = QWidget(scroll)
    scroll.setWidget(widget)
    scroll.setWidgetResizable(True)
    dock.setAllowedAreas(area)
    dock.setTitleBarWidget(QLabel(name))
    window.addDockWidget(area, dock)
    dock_layout = QVBoxLayout()
    widget.setLayout(dock_layout)
    # Fix resize grip size
    # https://stackoverflow.com/a/65050468/2175965
    styles = ['margin: 4px;']
    if max_width is not None:
        styles.append(f'max-width: {max_width};')
    style_sheet = 'QDockWidget { ' + '  \n'.join(styles) + '\n}'
    dock.setStyleSheet(style_sheet)
    return dock, dock_layout


@contextmanager
def _testing_context(interactive):
    from . import renderer
    orig_offscreen = pyvista.OFF_SCREEN
    orig_testing = renderer.MNE_3D_BACKEND_TESTING
    orig_interactive = renderer.MNE_3D_BACKEND_INTERACTIVE
    renderer.MNE_3D_BACKEND_TESTING = True
    if interactive:
        pyvista.OFF_SCREEN = False
        renderer.MNE_3D_BACKEND_INTERACTIVE = True
    else:
        pyvista.OFF_SCREEN = True
        renderer.MNE_3D_BACKEND_INTERACTIVE = False
    try:
        yield
    finally:
        pyvista.OFF_SCREEN = orig_offscreen
        renderer.MNE_3D_BACKEND_TESTING = orig_testing
        renderer.MNE_3D_BACKEND_INTERACTIVE = orig_interactive


# In theory we should be able to do this later (e.g., in _pyvista.py when
# initializing), but at least on Qt6 this has to be done earlier. So let's do
# it immediately upon instantiation of the QMainWindow class.
# TODO: This should eventually allow us to handle
# https://github.com/mne-tools/mne-python/issues/9182

class _MNEMainWindow(MainWindow):
    def __init__(self, parent=None, title=None, size=None):
        super().__init__(parent, title, size)
        self.setAttribute(Qt.WA_ShowWithoutActivating, True)
