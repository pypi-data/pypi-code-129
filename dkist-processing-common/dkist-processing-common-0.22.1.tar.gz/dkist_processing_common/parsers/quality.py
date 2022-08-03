"""Support classes to define object attributes from header information."""
from typing import Optional
from typing import Union

from astropy.io import fits

from dkist_processing_common.parsers.l0_fits_access import L0FitsAccess
from dkist_processing_common.parsers.l0_fits_access import L1FitsAccess


class L1QualityFitsAccess(L1FitsAccess):
    """
    Define various attributes derived from header values.

    Parameters
    ----------
    hdu
        The input fits hdu
    name
        An optional name to be associated with the hdu
    auto_squeeze
        A boolean indicating whether to 'squeeze' out dimensions of size 1
    """

    def __init__(
        self,
        hdu: Union[fits.ImageHDU, fits.PrimaryHDU, fits.CompImageHDU],
        name: Optional[str] = None,
        auto_squeeze: bool = True,
    ):
        super().__init__(hdu=hdu, name=name, auto_squeeze=auto_squeeze)

        self.fried_parameter: float = self.header["ATMOS_R0"]
        self.date_begin: str = self.header["DATE-BEG"]
        self.light_level: float = self.header["LIGHTLVL"]
        self.health_status: str = self.header["DSHEALTH"]
        self.ao_status: int = self.header.get("AO_LOCK", None)
