import os.path

import nexusformat.nexus as nx
import numpy as np
from lmfit.model import Model
from scipy import ndimage
from scipy.special import erf
from pygdatax import flib
from pygdatax import nxlib
from silx.image.bilinear import BilinearImage

@nxlib.rxtreatment_function
def set_roi(root: nx.NXroot, roi_width: int = 20, roi_height: int = 10) -> None:
    """
    Set roi width and height with the raw_data/direct_beam field
    Args:
        root: NXroot
        roi_width:
        roi_height:

    Returns:

    """
    if roi_width:
        root.raw_data.direct_beam.roi_width = roi_width
    if roi_height:
        root.raw_data.direct_beam.roi_height = roi_height


@nxlib.rxtreatment_function
def set_center(root: nx.NXroot, x0: float = None, y0: float = None) -> None:
    """
    Set beam center position within the raw_data/direct_beam field
    Args:
        root: NXroot
        x0: horizontal beam center position
        y0: vertical beam center

    Returns:

    """
    if x0:
        root.raw_data.direct_beam.x0 = x0
    if y0:
        root.raw_data.direct_beam.y0 = y0


@nxlib.rxtreatment_function
def set_distance(root: nx.NXroot, distance: float = None) -> None:
    """
    Set sample to detector distance in mm
    Args:
        root: NXroot
        distance: sample to detector distance in mm

    Returns:

    """
    root.raw_data.instrument.detector.distance = distance


@nxlib.rxtreatment_function
def set_offset(root: nx.NXroot, offset: float = None) -> None:
    """
    Set sample offset within the raw_data/sample/offset field
    Args:
        root: NXroot
        offset: sample angular offset in degree

    Returns:

    """
    if offset is not None:
        root.raw_data.sample.offset = offset

@nxlib.rxtreatment_function
def set_chi(root: nx.NXroot, chi: float = None) -> None:
    """
    Chi angle in deg
    Args:
        root: NXroot
        chi: angle between vertical detector axis and the sample normal in deg

    Returns:

    """
    root.raw_data.sample.chi = chi


@nxlib.rxtreatment_function
def find_center(root, roi=None):
    if roi is None:
        x0 = root.raw_data.direct_beam.x0.nxdata
        y0 = root.raw_data.direct_beam.y0.nxdata
        w = root.raw_data.direct_beam.roi_width.nxdata
        h = root.raw_data.direct_beam.roi_height.nxdata
        roi = flib.get_roi(x0, y0, w, h, 0, 0)
    cropM = flib.crop_image(root.raw_data.direct_beam.data.data.nxdata, roi)
    centerCrop = ndimage.measurements.center_of_mass(cropM, index='int')
    center = [centerCrop[1] + roi[0], centerCrop[0] + roi[1]]
    root.raw_data.direct_beam.x0 = center[0]
    root.raw_data.direct_beam.y0 = center[1]
    print('x0 = %.3f \n y0= %.3f' % (center[0], center[1]))


@nxlib.rxtreatment_function
def set_distance(root, distance=None):
    if distance:
        root.raw_data.instrument.detector.distance = distance


@nxlib.rxtreatment_function
def compute_ref(root: nx.NXroot) -> None:
    omega = root.raw_data.sample.om.nxdata
    count_time = root.raw_data.sample.count_time.nxdata
    theta = omega-root.raw_data.sample.offset.nxdata
    wavelength = root.raw_data.instrument.source.incident_wavelength.nxdata
    nPoints = len(theta)
    q = 4*np.pi/wavelength*np.sin(theta*np.pi/180)
    r = np.zeros(nPoints)
    dr = np.zeros(nPoints)
    count = np.zeros(nPoints)
    specPosX = np.zeros(nPoints)
    specPosY = np.zeros(nPoints)
    distance = root.raw_data.instrument.detector.distance.nxdata
    x0 = root.raw_data.direct_beam.x0.nxdata
    y0 = root.raw_data.direct_beam.y0.nxdata
    roi_width = root.raw_data.direct_beam.roi_width.nxdata
    roi_height = root.raw_data.direct_beam.roi_height.nxdata
    if 'chi' in root.raw_data.sample:
        chi = root.raw_data.sample.chi.nxdata
    else:
        chi = 0
    # d = root.raw_data.image_stack.data.nxdata
    sumEB = flib.sumSpec(root.raw_data.direct_beam.data.data.nxdata, 0, distance, x0, y0,
                         roi_width, roi_height, pixelSize=0.172, chi=chi)
    sumEB /= root.raw_data.direct_beam.count_time.nxdata
    root.raw_data.direct_beam.flux = nx.NXfield(sumEB, attrs={'units': r's$^{-1}$'})
    # with root.raw_data.image_stack.data as slab:
    #     ni, nj, nk = slab.nxdims
    #     size = [1, 1, Nk]
    #     for i in range(Ni):
    #         for j in range(Nj):
    #             value = slab.nxget([i, j, 0], size)
    # Ni, Nj, Nk = slab.nxdims
    # size = [1, 1, Nk]
    # for i in range(Ni):
    #     for j in range(Nj):
    #         value = slab.nxget([i, j, 0], size)
    for i in range(nPoints):
        if flib.roi_is_on_gap(x0, y0, roi_width, roi_height, theta[i], distance):
            count[i] = np.nan
            specPosX[i] = np.nan
            specPosY[i] = np.nan
        else:
            d = root.raw_data.image_stack.data[i, :, :].nxdata
            count[i] = flib.sumSpec(d, theta[i], distance, x0, y0,
                                    roi_width, roi_height, pixelSize=0.172,chi=chi)
            # correction by solid angle
            count[i] /= np.cos(2*np.deg2rad(theta[i]))**3
            # find specular position
            specPosX[i], specPosY[i] = flib.getSpecularPostion(d, x0, y0, roi_width, roi_height, theta[i],
                                                               distance, pixelSize=0.172, extraHeight=60, extraWidth=60,
                                                               chi=chi)

    # specular data
    data = nx.NXdata()
    r = count / sumEB / root.raw_data.sample.count_time.nxdata
    # removing nan
    # index = ~np.isnan(count)
    # q = q[index]
    # r = r[index]
    # specPosX = specPosX[index]
    # specPosY = specPosY[index]
    # count = count[index]
    # omega = omega[index]
    data.nxsignal = nx.NXfield(r, name='R')
    data.nxerrors = r / np.sqrt(count)
    data.nxaxes = [nx.NXfield(q, name='Q', attrs={'units': r'$\AA^{-1}$'})]
    # specular postion
    # remove nan
    index = ~np.isnan(r / np.sqrt(count))
    specular_position = nx.NXdata()
    specular_position.nxsignal = nx.NXfield(y0-specPosY[index], name='specPosY')
    # remove nan from specualr position

    specular_position.nxaxes = [nx.NXfield(omega[index], name='omega', attrs={'units': 'deg'})]
    specular_position.specPosX = nx.NXfield(x0-specPosX[index], name='specPosX')

    if 'reflectivity' in root.keys():
        if 'specular_position' in root.reflectivity.keys():
            del root['reflectivity/specular_position']
            root.reflectivity.specular_position = specular_position
        if 'data' in root.reflectivity.keys():
            del root['reflectivity/data']
            root.reflectivity.data = data

        if 'data_corr' in root.reflectivity.keys():
            del root['reflectivity/data_corr']
    else:
        ref = nx.NXentry()
        ref.data = data
        ref.attrs['default'] = 'data'
        ref.specular_position = specular_position
        root.reflectivity = ref
        root.attrs['default'] = 'reflectivity'
    return

@nxlib.rxtreatment_function
def cut(root: nx.NXroot, xmin: float = None, xmax: float = None) -> None:
    if 'reflectivity' in root.keys():
        if 'data' in root.reflectivity.keys():
            q = root.reflectivity.data.Q.nxdata
            r = root.reflectivity.data.R.nxdata
            dr = root.reflectivity.data.R_errors.nxdata
            index1 = np.nonzero(q >= xmin)
            index2 = np.nonzero(q <= xmax)
            index = np.intersect1d(index1, index2)
            data = nx.NXdata(nx.NXfield(r[index], name='R'), axes=[nx.NXfield(q[index], name='Q', attrs={'units': r'$\AA^{-1}$'})],
                             errors=dr[index])
            del root['reflectivity/data']
            root.reflectivity.data = data
        if 'data_corr' in root.reflectivity.keys():
            pass


@nxlib.rxtreatment_function
def autoset_roi(root: nx.NXroot) -> None:
    m = root.raw_data.direct_beam.data.data.nxdata
    x0 = root.raw_data.direct_beam.x0.nxdata
    y0 = root.raw_data.direct_beam.y0.nxdata
    roi_width = root.raw_data.direct_beam.roi_width.nxdata
    roi_height = root.raw_data.direct_beam.roi_height.nxdata
    x1 = x0 - roi_width/2-30
    y1 = y0 - roi_height/2-30
    x2 = x0 + roi_width/2+30
    y2 = y0 + roi_height/2+30
    cropM = flib.crop_image(m, [x1, y1, x2, y2])
    y, x = np.indices(cropM.shape)

    def function(u, v, amplitude, sigx, sigy, u0, v0, bkg):
        val = amplitude * np.exp(-((u - u0) ** 2 / (2 * sigx ** 2) + (v - v0) ** 2 / (2 * sigy ** 2))) + bkg
        return val.flatten()

    model = Model(function, independent_vars=["u", "v"],
                  param_names=["amplitude", "sigx", "sigy", "u0",
                               "v0", "bkg"])
    params = model.make_params()
    params['bkg'].value = 0
    params['bkg'].vary = False
    params['amplitude'].value = np.max(cropM)
    params['sigy'].value = 2
    params['sigx'].value = 2
    params['u0'].value = roi_width/2
    params['v0'].value = roi_height/2
    result = model.fit(cropM.flatten(), u=x, v=y, params=params)
    print(result.fit_report())
    fitParams = result.params
    root.raw_data.direct_beam.roi_width = int(np.abs(15*fitParams['sigx'].value))
    root.raw_data.direct_beam.roi_height = int(np.abs(15*fitParams['sigy'].value))


# FIXME: take into acount chi angle for integration
@nxlib.rxtreatment_function
def offspecular_angular_map(root: nx.NXroot) -> None:
    """
    compute the off specular data
    Args:
        root:

    Returns:

    """
    nPoints = len(root.raw_data.sample.om.nxdata)
    imageShape = root.raw_data.direct_beam.data.data.nxdata.shape
    x0 = root.raw_data.direct_beam.x0.nxdata
    y0 = root.raw_data.direct_beam.y0.nxdata
    roi_width = root.raw_data.direct_beam.roi_width.nxdata
    distance = root.raw_data.instrument.detector.distance.nxdata
    pixel_size = root.raw_data.instrument.detector.x_pixel_size.nxdata

    if 'chi' in root.raw_data.sample:
        chi = root.raw_data.sample.chi.nxdata
    else:
        chi = 0

    alphai = root.raw_data.sample.om.nxdata - root.raw_data.sample.offset.nxdata
    yGrid, xGrid = np.indices(imageShape)
    rGrid = np.sqrt((y0-yGrid)**2+(xGrid-x0)**2) * pixel_size
    # profile start point
    endPt = [0, x0 - np.tan(np.deg2rad(chi))*y0]
    startPt = [imageShape[0], x0 + np.tan(np.deg2rad(chi))*(imageShape[0]-y0)]
    profileData = []
    profileAlphai = []
    profileAlphaf_alphai = []

    for i in range(nPoints):
        # roi = [x0 - roi_width / 2 + h_disp[i], 0, x0 + roi_width / 2 + h_disp[i], imageShape[0]]
        # d = root.raw_data.image_stack.data[i, :, :]
        bilinear = BilinearImage(root.raw_data.image_stack.data[i, :, :].nxdata / root.raw_data.sample.count_time.nxdata[i])
        profileData.append(bilinear.profile_line((startPt[0] - 0.5, startPt[1] - 0.5),
                                                 (endPt[0] - 0.5, endPt[1] - 0.5),
                                                 roi_width,
                                                 method='mean'))  # method can be mean or sum
        profileAlphai.append(alphai[i] * np.ones_like(profileData[i]))  # method can be mean or sum
        bilinear = BilinearImage(np.rad2deg(np.arctan(rGrid/distance))-2*alphai[i])
        profileAlphaf_alphai.append(bilinear.profile_line((startPt[0] - 0.5, startPt[1] - 0.5),
                                                          (endPt[0] - 0.5, endPt[1] - 0.5),
                                                          roi_width,
                                                          method='mean'))  # method can be mean or sum

        # cropM = flib.crop_image(d.nxdata, roi)
        # offMap[:, i] = np.sum(cropM, axis=1) / root.raw_data.sample.count_time.nxdata[i]
        # offMap[:, i] = profile
    offMap = np.array(profileData).flatten()
    alphai = np.array(profileAlphai).flatten()
    alphaf_alphai = np.array(profileAlphaf_alphai).flatten()
    indexes = ~np.isnan(offMap)
    offMap = offMap[indexes]
    alphai = alphai[indexes]
    alphaf_alphai = alphaf_alphai[indexes]
    offData = nx.NXdata()
    offData.nxsignal = nx.NXfield(offMap.flatten(), name='data')
    offData.nxaxes = [nx.NXfield(alphaf_alphai.flatten(), name='alpha_f_minus_alpha_i', attrs={'units': 'deg'}),
                      nx.NXfield(alphai.flatten(), name='alpha_i', attrs={'units': 'deg'})
                      ]
    # offData.ai = nx.NXfield(alphai)
    # offData.af = nx.NXfield(alphaf_alphai)
    if 'off_specular' in root.keys():
        if 'data' in root.off_specular:
            del root['off_specular/data']
        root.off_specular.data = offData
        root.off_specular.attrs['default'] = 'data'
    else:
        entry = nx.NXentry()
        entry.attrs['default'] = 'data'
        entry.data = offData
        root.off_specular = entry


@nxlib.rxtreatment_function
def bin_angular_offspecular(root: nx.NXroot, x_bins: int = 1000, y_bins: int = 200) -> None:
    """
    bin the angular off specualr map to a (x_bins, y_bins) 2D array for easier represention and store it with the off_specular/data_binned entry
    Args:
        root: NXroot
        qx_bins: number of bins for qx
        qz_bins: number of bins for qz
    """
    if 'off_specular' not in root.keys():
        print("no off specular data found")
        return
    else:
        if 'data' not in root.off_specular:
            print("no off specular data found")
            return

    data = root.off_specular.data.data.nxdata
    alphai = root.off_specular.data.alpha_i.nxdata
    alphaf_alphai = root.off_specular.data.alpha_f_minus_alpha_i.nxdata
    alphi_edges = np.histogram_bin_edges(alphai, bins=y_bins)
    alphf_edges = np.histogram_bin_edges(alphaf_alphai, bins=x_bins)

    count, b, c = np.histogram2d(alphai, alphaf_alphai, (alphi_edges, alphf_edges))
    count1 = np.maximum(1, count)
    bins_azim = b[1:]
    x = (b[1:] + b[:-1]) / 2.0
    # bins_deg = c[1:]
    y = (c[1:] + c[:-1]) / 2.0
    sum_, b, c = np.histogram2d(alphai, alphaf_alphai, (alphi_edges, alphf_edges),
                                weights=data)
    i = sum_ / count1
    i[count == 0] = -1
    i_masked = np.ma.masked_less(i, 0, copy=True)
    i = sum_ / count1
    i[count == 0] = -1
    if 'data_binned' in root.off_specular:
        del root['off_specular/data_binned']
    root.off_specular.data_binned = nx.NXdata(signal=i, name='data',
                                              axes=(nx.NXfield(x, name='alpha_i'),
                                                    nx.NXfield(y, name='alpha_f_minus_alpha_i'))
                                              )

@nxlib.rxtreatment_function
def bin_q_offspecular(root: nx.NXroot, qx_bins: int = 1000, qz_bins: int = 200) -> None:
    """
    bin the angular off specualr map to a (x_bins, y_bins) 2D array for easier represention and store it with the off_specular/data_binned entry
    Args:
        root: NXroot
        qx_bins: number of bins for qx
        qz_bins: number of bins for qz
    """
    if 'off_specular' not in root.keys():
        print("no off specular data found")
        return
    else:
        if 'data_Q' not in root.off_specular:
            print("no off specular data found")
            return

    data = root.off_specular.data_Q.data.nxdata
    qx = root.off_specular.data_Q.Qx.nxdata
    qz = root.off_specular.data_Q.Qz.nxdata
    qx_edges = np.histogram_bin_edges(qx, bins=qx_bins)
    qz_edges = np.histogram_bin_edges(qz, bins=qz_bins)

    count, b, c = np.histogram2d(qx, qz, (qx_edges, qz_edges))
    count1 = np.maximum(1, count)
    bins_azim = b[1:]
    x = (b[1:] + b[:-1]) / 2.0
    # bins_deg = c[1:]
    y = (c[1:] + c[:-1]) / 2.0
    sum_, b, c = np.histogram2d(qx, qz, (qx_edges, qz_edges),
                                weights=data)
    i = sum_ / count1
    i[count == 0] = -1
    i_masked = np.ma.masked_less(i, 0, copy=True)
    i = sum_ / count1
    i[count == 0] = -1
    if 'data_Q_binned' in root.off_specular:
        del root['off_specular/data_Q_binned']
    root.off_specular.data_Q_binned = nx.NXdata(signal=i, name='data',
                                                axes=(nx.NXfield(y, name='Qz'),
                                                      nx.NXfield(x, name='Qx'))
                                                )


@nxlib.rxtreatment_function
def offspecular_q_map(root: object) -> None:
    ##### old version requireing previious angular off specular  map
    # if 'off_specular' not in root.keys():
    #     print('angular off specular map needs to be calculated first')
    #     return
    # data = root.off_specular.data.data.nxdata
    # alphai = np.deg2rad(root.off_specular.data.alpha_i.nxdata)
    # alphaf = np.deg2rad(root.off_specular.data.alpha_f_minus_alpha_i.nxdata + alphai)
    # wavelentgh = root.raw_data.instrument.source.incident_wavelength.nxdata
    # qx = 2 * np.pi/wavelentgh*(np.cos(alphaf)-np.cos(alphai))
    # qz = 2 * np.pi/wavelentgh*(np.sin(alphaf)+np.sin(alphai))
    # data = root.off_specular.data.data.nxdata
    # if 'data_Q' in root['off_specular']:
    #     del root['off_specular/data_Q']
    # data = nx.NXdata(data, [qx, qz])
    # root.off_specular.data_Q = data

    nPoints = len(root.raw_data.sample.om.nxdata)
    imageShape = root.raw_data.direct_beam.data.data.nxdata.shape
    # offMap = np.empty((imageShape[0], nPoints))
    # stack = root.raw_data.image_stack.data.nxdata
    x0 = root.raw_data.direct_beam.x0.nxdata
    y0 = root.raw_data.direct_beam.y0.nxdata
    roi_width = root.raw_data.direct_beam.roi_width.nxdata
    distance = root.raw_data.instrument.detector.distance.nxdata
    wavelength = root.raw_data.instrument.source.incident_wavelength
    omGrid, yGrid = np.meshgrid(root.raw_data.sample.om.nxdata, np.arange(imageShape[0]))
    alphaiGrid = np.deg2rad(omGrid - root.raw_data.sample.offset.nxdata)
    alphafGrid = np.deg2rad(np.arctan((y0 - yGrid) * 0.172 / distance) * 180 / np.pi) - alphaiGrid
    qxGrid = 2 * np.pi / wavelength * (np.cos(alphafGrid)-np.cos(alphaiGrid))
    qzGrid = 2 * np.pi / wavelength * (np.sin(alphafGrid)+np.sin(alphaiGrid))
    roi = [x0 - roi_width / 2, 0, x0 + roi_width / 2, imageShape[0]]
    offMap = np.empty_like(alphaiGrid)
    for i in range(nPoints):
        d = root.raw_data.image_stack.data[i, :, :]
        cropM = flib.crop_image(d.nxdata, roi)
        offMap[:, i] = np.sum(cropM, axis=1) / root.raw_data.sample.count_time.nxdata[i]
    # q = np.sin(np.deg2rad(alphai+alphaf))*4*np.pi/1.542

    offData = nx.NXdata()
    offData.nxsignal = nx.NXfield(offMap.flatten(), name='data')
    offData.nxaxes = [nx.NXfield(qxGrid.flatten(), name='Qx', attrs={'units': r'$\AA^{-1}$'}),
                      nx.NXfield(qzGrid.flatten(), name='Qz', attrs={'units': r'$\AA^{-1}$'})
                      ]
    if 'off_specular' in root.keys():
        if 'data_Q' in root['off_specular']:
            del root['off_specular/data_Q']
        root.off_specular.data_Q = offData
        root.off_specular.attrs['default'] = 'data_Q'
    else:
        entry = nx.NXentry()
        entry.attrs['default'] = 'data_Q'
        entry.data_Q = offData
        root.off_specular = entry


@nxlib.rxtreatment_function
def footprint_correction(root: nx.NXroot, length: float = None, width: float = None, beam_profile: str = 'uniform') -> None:
    """
    Correct the reflectivyty data by the
    Args:
        root: NXroot
        length: sample length
        width: beam width
        beam_profile: 'uniform (default) or 'gaussian'
    """
    if length is None:
        length = root.raw_data.sample.length.nxdata
    else:
        root.raw_data.sample.length = length
    if width is None:
        width = root.raw_data.instrument.slit.y_gap.nxdata
    else:
        root.raw_data.instrument.slit.y_gap = width
    if 'reflectivity' in root:
        theta = np.arcsin(root.reflectivity.data.Q.nxdata * root.raw_data.instrument.source.incident_wavelength.nxdata /
                          (4*np.pi))
        thetaf = np.arcsin(width/length)
        if beam_profile == 'uniform':
            fp = 1/np.sin(theta)*width/length
            fp[theta >= thetaf] = 1
        elif beam_profile == 'gaussian':
            fp = 1/erf(np.sin(theta)*length/2/(2**0.5*width))
        else:
            print('Wrong beam profile. It should be be uniform or gaussian')
            return
        r_corr = root.reflectivity.data.nxsignal.nxdata * fp
        r_corr_error = root.reflectivity.data.nxerrors.nxdata * fp
        data_corr = nx.NXdata(signal=nx.NXfield(r_corr, name='R_corr'),
                              axes=root.reflectivity.data.nxaxes,
                              errors=r_corr_error)

        if 'data_corr' in root.reflectivity:
            del root['reflectivity/data_corr']
        root.reflectivity.data_corr = data_corr
        root.reflectivity.attrs['default'] = "data_corr"


@nxlib.rxtreatment_function
def save_as_txt(root: nx.NXroot) -> None:
    """
    Save the reflecticity spectra within two text files. One corresponds to the non corrected data, the other to the footprint
    corrected data
    Args:
        root: NXroot

    Returns:

    """
    if 'reflectivity' in root:
        x = root.reflectivity.data.nxaxes[0].nxdata
        y = root.reflectivity.data.nxsignal.nxdata
        dy = root.reflectivity.data.nxerrors.nxdata
        # remove nan
        index = ~np.isnan(dy)
        mat = np.stack((x[index], y[index], dy[index]))
        newfile = root.file_name.split('.')[0] + '.txt'
        header = 'Q \t R \t dR'
        np.savetxt(newfile, mat.transpose(), delimiter='\t', header=header)
        if 'data_corr' in root.reflectivity:
            x = root.reflectivity.data_corr.nxaxes[0].nxdata
            y = root.reflectivity.data_corr.nxsignal.nxdata
            dy = root.reflectivity.data_corr.nxerrors.nxdata
            # remove nan
            index = ~np.isnan(dy)
            mat = np.stack((x[index], y[index], dy[index]))
            newfile = root.file_name.split('.')[0] + '_corr' + '.txt'
            header = 'Q \t R_corrected \t dR_corrected '
            np.savetxt(newfile, mat.transpose(), delimiter='\t', header=header)


@nxlib.rxtreatment_function
def fit_distance_and_offset(root: nx.NXroot, fit_distance: bool = True, fit_offset: bool = True, om_range: list = [-20, 20]) -> None:
    if 'reflectivity' not in root:
        return

    def fun(x, distance, offset):
        return np.tan(2*np.deg2rad(x-offset)) * distance / 0.172

    model = Model(fun)
    distanceIni = root.raw_data.instrument.detector.distance.nxdata
    offsetIni = root.raw_data.sample.offset.nxdata
    params = model.make_params(distance=distanceIni, offset=offsetIni)
    params['distance'].vary = fit_distance
    params['offset'].vary = fit_offset

    om = root.reflectivity.specular_position.omega.nxdata
    specPos = root.reflectivity.specular_position.specPosY.nxdata
    index = np.logical_and(om >= om_range[0], om <= om_range[1])

    res = model.fit(specPos[index], params, x=om[index])
    print(res.fit_report())
    # res.plot()
    root.raw_data.instrument.detector.distance = res.params['distance'].value
    root.raw_data.sample.offset = res.params['offset'].value
    fitData = nx.NXdata(nx.NXfield(res.best_fit, name='specPosY', attrs={'units': 'deg'}),
                        nx.NXfield(om[index], name='omega',attrs={'units': 'deg'}))
    if 'fit_specular_position' in root.reflectivity:
        del root['reflectivity/fit_specular_position']
    root.reflectivity.fit_specular_position = fitData


# @nxlib.rxtreatment_function(output_file=True)
def concatenate(outputFile: str, fileList: list) -> str:
    # root1 = nx.nxload(file1, mmode='r+')
    # root2 = nx.nxload(file2, mmode='r+')
    root_concat = nx.NXroot()
    root_concat.attrs['NX_class'] = b'NXroot'
    root_concat.reflectivity = nx.NXentry()

    q_concat = []
    r_concat = []
    dr_concat = []

    q_fp = []
    r_fp = []
    dr_fp = []

    for file in fileList:
        root = nx.nxload(file, mode='r')
        with root.nxfile:
            if 'reflectivity' in root.keys() and 'reflectivity':
                if 'data' in root.reflectivity.keys():
                    q_concat.append(root.reflectivity.data.Q.nxdata)
                    r_concat.append(root.reflectivity.data.R.nxdata)
                    dr_concat.append(root.reflectivity.data.R_errors.nxdata)
                if 'data_corr' in root.keys():
                    q_fp.append(root.reflectivity.data_corr.Q.nxdata)
                    r_fp.append(root.reflectivity.data_corr.R_corr.nxdata)
                    dr_fp.append(root.reflectivity.data_corr.R_corr_errors.nxdata)

    q_concat = np.array(q_concat).flatten()
    r_concat = np.array(r_concat).flatten()
    dr_concat = np.array(dr_concat).flatten()
    # sort arrays
    indexes = np.argsort(q_concat)
    q_concat = q_concat[indexes]
    r_concat = r_concat[indexes]
    dr_concat = dr_concat[indexes]
    # remove nan
    indexes = ~np.isnan(r_concat)
    q_concat = q_concat[indexes]
    r_concat = r_concat[indexes]
    dr_concat = dr_concat[indexes]
    # remove negative value
    indexes = np.nonzero(r_concat >= 0)
    q_concat = q_concat[indexes]
    r_concat = r_concat[indexes]
    dr_concat = dr_concat[indexes]
    # footprint corrected reflectivity
    q_fp = np.array(q_fp).flatten()
    r_fp = np.array(r_fp).flatten()
    dr_fp = np.array(dr_fp).flatten()
    indexes = np.argsort(q_fp)
    q_fp = q_fp[indexes]
    r_fp = r_fp[indexes]
    dr_fp = dr_fp[indexes]
    # remove nan
    indexes = ~np.isnan(r_fp)
    q_fp = q_fp[indexes]
    r_fp = r_fp[indexes]
    dr_fp = dr_fp[indexes]

    data = nx.NXdata(nx.NXfield(r_concat, name='R'),
                     axes=[nx.NXfield(q_concat, name='Q', attrs={"units": r'$\AA^{-1}$'})],
                     errors=dr_concat)
    root_concat.reflectivity.data = data
    root_concat.reflectivity.attrs['default'] = 'data'
    root_concat.attrs['default'] = 'reflectivity'

    data = nx.NXdata(nx.NXfield(r_fp, name='R_corr'),
                     axes=[nx.NXfield(q_fp, name='Q', attrs={"units": r'$\AA^{-1}$'})],
                     errors=dr_fp)
    root_concat.reflectivity.data_corr = data
    root_concat.raw_data = nx.NXentry()
    root = nx.nxload(fileList[0], mode='r')
    with root.nxfile:
        root_concat.raw_data.sample = root.raw_data.sample
        root_concat.raw_data.instrument = root.raw_data.instrument
    if os.path.exists(outputFile):
        os.remove(outputFile)
    root_concat.save(outputFile, mode='w')
    root_concat.close()





def automatic_treatment(data_folder, distance=1216):
    file = nxlib.build_rxnexus_from_directory(data_folder, distance=distance)
    find_center(file)
    autoset_roi(file)
    compute_ref(file)
    root = nx.nxload(file)
    offset = root.raw_data.sample.offset.nxdata
    root.close()
    fit_distance_and_offset(file, fit_distance=True, fit_offset=True, om_range=[offset+0.2, offset+1.5])
    compute_ref(file)



if __name__ == '__main__':
    ########################################################################################
    # folder = '/home/achennev/Bureau/PIL pour tiago/RX_tiago/9_11_2020/TH10_10_1_pos1'
    # # folder2 = '/home/achennev/Bureau/PIL pour tiago/RX_tiago/9_11_2020/TH10_10_1_pos2'
    # folder = '/home/achennev/Bureau/PIL pour tiago/RX_tiago/9_11_2020/wafer_nue_pos1'
    # folder2 = '/home/achennev/Bureau/PIL pour tiago/RX_tiago/9_11_2020/wafer_nue_pos2'
    #
    # file = os.path.join(folder, 'wafer_nue_pos1.nxs')
    #
    # set_distance(file, distance=1214)
    # set_offset(file, offset=-0.12)
    # find_center(file, roi=[460, 900, 600, 1000])
    # autoset_roi(file)
    #
    # # autoset_roi(file2)
    # # set_roi(file, roi_height=5)
    # # set_roi(file2, roi_width=60, roi_height=40)
    # compute_ref(file)
    # footprint_correction(file, width=0.269, length=26)
    # off_specular_map(file)
    # remap_offspecular(file, qx_bins=300, qz_bins=300)
    # save_as_txt(file)
    # # file2 = os.path.join(folder2, 'wafer_nue_pos2.nxs')
    # # set_distance(file2, distance=1212)
    # # set_offset(file2, offset=-0.137)
    # # find_center(file2, roi=[460, 960, 600, 1020])
    # #
    # # compute_ref(file2)
    # # footprint_correction(file2)
    ###########################################################################
    # folder = '/home/achennev/Bureau/PIL pour tiago/RX_tiago/9_11_2020/TH1_10_2000rpm_pos1'
    # folder = '/home/achennev/Documents/xeuss/Depot_Au_EchSOLEIL_pos2'
    # automatic_treatment(folder, distance=1214)
    file = '/home/achennev/Documents/collab lay theng/2020-02-18-LT/SiP2_pos1.nxs'
    offspecular_angular_map(file)
