"""
Module for creating aligner interfaces (abstract objects) and their instantiations, used
for aligning files.
"""

import logging
import os
import zipfile
from abc import ABC, abstractmethod
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydicom
import regex as re
from fw_file.dicom import DICOM
from pandas.util._decorators import Appender
from pydicom.filebase import DicomBytesIO

import fw_gear_oct_qa.calc_QA as calc_QA

from .utils.docs import create_shared_doc_vars

log = logging.getLogger(__name__)

_shared_docs, _shared_doc_kwargs = create_shared_doc_vars()
_shared_doc_kwargs.update(
    {
        "file_type": """file_type: str
        An abstract class parameter implemented in the concrete objects, it is the type of file
         that contains the OCT slices to be aligned""",
        "file_ext": """file_ext: str
        An abstract class parameter implemented in the concrete objects, it is the file
        extension that is read in the factory() method to select the concrete subclass
        of OCTqa.""",
        "path_file": """path_file: str
        The path the the file being read""",
        "work_dir": """work_dir: PathLike
        The  path of the working directory for temporary work""",
        "gear_context": """GearToolkitContext object with acquisition metadata""",
        "qa_index": """qa_index: dict. Keys: 
            - Sharpness slope: array. Mean slope in transition between extra-retinal and intra-retinal regions of the OCT data.
            - Variance extraretinal: array. Mean variance of extra-retinal region of the OCT data.
            - Variance intraretinal: array. Mean variance of intra-retinal region of the OCT data.
            - Dynamic range: array. Mean Dynamic Range (ratio of brightest and darkest pixels) of OCT data
            - Outliers Slope: slice index of slices that have a slope above or below 1.5 times the Interquartile Range
            - Outliers Variance Extraretinal: slice index of slices that have a extraretinal variance above or below 1.5 times the Interquartile Range
            - Outliers Variance Intraretinal: slice index of slices that have a intraaretinal variance above or below 1.5 times the Interquartile Range
            - Outliers Dynamic range: slice index of slices that have a dynamic range above or below 1.5 times the Interquartile Range""",
        "oct_volumes": """oct_volumes: list
        Modified by a subclass' self.read_file() method, it contains the oct volumes (.npy or .dcm).""",
        "OCTqa": """The abstract base class that acts as an interface for oct-qa objects.
        This object is mainly used to read a raw input file with self.factory() method, which selects which subclass
        to use for reading and saving OCT data, and then uses its template method self.assess_quality()
        to perform the quality assessment.""",
        "numpyOCTqa": """An oct qa for OCT slices stored in numpy arrays (.npy).""",
        "dicomOCTqa": """An oct qa for OCT slices stored in Dicom files (.dcm).""",
        "zippedDicomOCTqa": """An oct qa for OCT slices stored in zipped Dicom files (.dcm.zip).""",
    }
)
_shared_docs[
    "OCTqa"
] = """
%(OCTqa)s

Params
------
%(file_type)s
%(file_ext)s
%(path_file)s
%(work_dir)s
%(oct_volumes)s
"""


@Appender(_shared_docs["OCTqa"] % _shared_doc_kwargs)
class OCTqa(ABC):
    @classmethod
    def factory(
        cls,
        path_file,
        output_dir: os.PathLike,
        work_dir: os.PathLike,
        save_figures_if_fail: bool,
    ):

        _, file_ext = os.path.splitext(path_file)

        file_exts = [sub.file_ext for sub in cls.__subclasses__()]

        result = None

        subclass_name = []
        for subclass in cls.__subclasses__():
            subclass_name.append(subclass.file_ext)
            if subclass.file_ext == file_ext:
                result = subclass(
                    path_file=path_file,
                    output_dir=output_dir,
                    work_dir=work_dir,
                    save_figures_if_fail=save_figures_if_fail,
                )
                break

        if not result:
            raise ValueError(
                f"Could not locate {cls.__name__} with file extension "
                f"Subclass: {subclass_name}"
                f"'{file_ext}'. Available file extensions: \n"
                f" {file_exts}"
            )

        return result

    def __init__(
        self,
        path_file,
        output_dir: os.PathLike,
        work_dir: os.PathLike,
        save_figures_if_fail: bool,
    ):
        self.path_file = path_file
        self.work_dir = work_dir
        self.output_dir = output_dir
        self.save_figures_if_fail = save_figures_if_fail
        self.oct_volumes = []
        self.dicom = []

    _shared_docs[
        "assess_quality"
    ] = """
    A template method that runs the methods for assessing the quality of  OCT slices.
    
    Params
    ------
    %(gear_context)s
    
    Returns
    -------
    %(qa_index)s
    output_csv: pd.DataFrame
        A dataframe with the following header: Slice number, Dynamic range, 
        Sharpness slope, Variance extraretinal, Variance intraretinal
    """

    @Appender(_shared_docs["assess_quality"] % _shared_doc_kwargs)
    def assess_quality(self):
        log.info("Starting assessment...")

        # Read the raw file
        log.info("Reading raw file stored in %s ..." % self.path_file)
        # loads data
        self.read_file()
        log.info("\tFinished reading oct volume.")

        # Asses the quality of the raw file
        log.info("Assessing the quality of the OCT volume...")

        QA_index = calc_QA.calc_all(self.oct_volumes)
        log.info("\tFinished assessing the quality of the OCT volume.")

        # Save outputs
        log.info("Saving dataframe with extra metadata...")
        filepath_out_csv = Path(self.output_dir).joinpath(
            Path(self.path_file).stem + "_QA_metadata.csv"
        )
        output_csv = pd.DataFrame(
            columns=[
                "Slice number",
                "Dynamic range",
                "Sharpness slope",
                "Variance extraretinal",
                "Variance intraretinal",
            ]
        )
        output_csv["Slice number"] = range(len(QA_index["Dynamic range"]))
        output_csv["Dynamic range"] = QA_index["Dynamic range"]
        output_csv["Sharpness slope"] = QA_index["Sharpness slope"]
        output_csv["Variance extraretinal"] = QA_index["Variance extraretinal"]
        output_csv["Variance intraretinal"] = QA_index["Variance intraretinal"]

        output_csv.to_csv(filepath_out_csv)

        return QA_index, output_csv

    def savefigures(self, dataframe):
        """
        Saves qa_index histograms as .png files.
        Args:
            - dataframe: pandas dataframe with all QA indexes per slice.

        """
        plt.figure()
        plt.hist(dataframe["Sharpness slope"], color="gray", edgecolor="black")
        plt.ylabel("Frequency", fontsize=14)
        plt.xlabel("Sharpness Slope", fontsize=14)
        figurepath_slope = Path(self.output_dir).joinpath(
            Path(self.path_file).stem + "_QA_slopes.png"
        )
        plt.savefig(figurepath_slope, dpi=1000)

        plt.figure()
        plt.hist(dataframe["Variance extraretinal"], color="gray", edgecolor="black")
        plt.ylabel("Frequency", fontsize=14)
        plt.xlabel("Variance Extraretinal", fontsize=14)
        figurepath_vExtra = Path(self.output_dir).joinpath(
            Path(self.path_file).stem + "_QA_varianceExtraretinal.png"
        )
        plt.savefig(figurepath_vExtra, dpi=1000)

        plt.figure()
        plt.hist(dataframe["Variance intraretinal"], color="gray", edgecolor="black")
        plt.ylabel("Frequency", fontsize=14)
        plt.xlabel("Variance Intraretinal", fontsize=14)
        figurepath_vIntra = Path(self.output_dir).joinpath(
            Path(self.path_file).stem + "_QA_varianceIntraretinal.png"
        )
        plt.savefig(figurepath_vIntra, dpi=1000)

        plt.figure()
        plt.hist(dataframe["Dynamic range"], color="gray", edgecolor="black")
        plt.ylabel("Frequency", fontsize=14)
        plt.xlabel("Dynamic Range", fontsize=14)
        figurepath_vIntra = Path(self.output_dir).joinpath(
            Path(self.path_file).stem + "_QA_dynamicRange.png"
        )
        plt.savefig(figurepath_vIntra, dpi=1000)

    @property
    @abstractmethod
    def file_type(self):
        """
        The file type of the raw input file to convert.
        """
        pass

    @property
    @abstractmethod
    def file_ext(self):
        """
        The extension of the raw input file to convert.
        """

    @abstractmethod
    def read_file(self) -> dict:
        """
        Loads OCT volume in ".npy" format
        """

        pass


@Appender(
    _shared_docs["OCTqa"]
    % {
        **_shared_doc_kwargs,
        **{"OCTqa": _shared_doc_kwargs["numpyOCTqa"]},
    }
)
class numpyOCTqa(OCTqa):

    file_type = "numpy"
    file_ext = ".npy"

    def read_file(self):
        """
        Loads OCT volume in ".npy" format
        """

        self.oct_volumes = np.load(self.path_file)


@Appender(
    _shared_docs["OCTqa"]
    % {
        **_shared_doc_kwargs,
        **{"OCTqa": _shared_doc_kwargs["dicomOCTqa"]},
    }
)
class dicomOCTqa(OCTqa):

    file_type = "dicom"
    file_ext = ".dcm"

    def read_file(self):
        """
        Loads OCT volume in ".dcm" format
        """
        dcm = DICOM(self.path_file)
        rows = dcm.rows
        columns = dcm.columns
        slices = dcm.Number_of_Frames
        deserialized_bytes = np.frombuffer(dcm.PixelData, dtype=np.uint8)
        self.oct_volumes = np.reshape(
            deserialized_bytes, newshape=(slices, rows, columns)
        )
        self.dicom = dcm


@Appender(
    _shared_docs["OCTqa"]
    % {
        **_shared_doc_kwargs,
        **{"OCTqa": _shared_doc_kwargs["zippedDicomOCTqa"]},
    }
)
class zippedDicomOCTqa(OCTqa):

    file_type = "zip"
    file_ext = ".zip"

    def unzip(self, zip_archive):
        """
        Args:
            -zip_archive is a zipfile object (from zip_archive = zipfile.ZipFile(filename, 'r') for example)
        Returns:
            -file_list: a dictionary of file names and file like objects (StringIO's)
        The filter in the if statement skips directories and dot files
        """

        file_list = []
        for file_name in zip_archive.namelist():
            if not os.path.basename(file_name).startswith(
                "."
            ) and not file_name.endswith("/"):
                file_object = zip_archive.open(file_name, "r")
                file_like_object = DicomBytesIO(file_object.read())
                file_object.close()
                file_like_object.seek(0)
                name = os.path.basename(file_name)
                file_list.append((name, file_like_object))
        return file_list

    def read_file(self):
        """
        Loads OCT volume in ".dcm.zip" format
        """
        zip_archive = zipfile.ZipFile(self.path_file, "r")
        unzipped_file = self.unzip(zip_archive)
        log.warning(
            "Ordering slices by number in name. Please make sure that the zipped files are numbered in order."
        )
        pattern = r"(\d\d*)\..*"
        unzipped_file = sorted(
            unzipped_file, key=lambda x: int(re.findall(pattern, x[0])[0])
        )
        height, width = pydicom.dcmread(
            unzipped_file[0][1], force=True
        ).pixel_array.shape
        result = np.zeros([len(unzipped_file), height, width])
        log.info("Reading unzipped DICOM files...")
        for idx in range(len(unzipped_file)):
            zip_archive = zipfile.ZipFile(self.path_file, "r")
            unzipped_file = self.unzip(zip_archive)
            unzipped_file = sorted(
                unzipped_file, key=lambda x: int(re.findall(pattern, x[0])[0])
            )
            dcm = pydicom.dcmread(unzipped_file[idx][1], force=True)
            result[idx] = dcm.pixel_array
        log.info("Reading complete!")
        self.oct_volumes = result
