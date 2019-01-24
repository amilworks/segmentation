
import nibabel as nib
import cv2
import numpy as np
#import h5py
# import logging
from bqapi.comm import BQCommError
from bqapi.comm import BQSession
import logging
import os


logging.basicConfig(filename='PythonScript.log',filemode='a',level=logging.DEBUG)
log = logging.getLogger('bq.modules')

#logging.basicConfig(filename='prediction.log',level=logging.DEBUG)


def segmentation(bq, log, image_og, image_mask, **kw):


    log.debug('kw is: %s', str(kw))
    # predictor_uniq = predictor_url.split('/')[-1]
    # reducer_uniq = reducer_url.split('/')[-1]
    # table_uniq = table_url.split('/')[-1]
    #
    # predictor_url = bq.service_url('blob_service', path=predictor_uniq)
    # predictor_path = os.path.join(kw.get('stagingPath', ''), 'predictor.sav')
    # predictor_path = bq.fetchblob(predictor_url, path=predictor_path)
    #
    # reducer_url = bq.service_url('blob_service', path=reducer_uniq)
    # reducer_path = os.path.join(kw.get('stagingPath', ''), 'reducer.sav')
    # reducer_path = bq.fetchblob(reducer_url, path=reducer_path)

    # Read hdf5 table
    # table_service = bq.service ('table')
    # image_service = bq.service('image')
    # # Get dataset
    # image_og = table_service.load_array(table_uniq, ms_path.lstrip('/'))
    # image_mk = table_service.load_array(table_uniq, ms_path.lstrip('/'))
    # ms_path default: '/DataContainers/SyntheticVolumeDataContainer/CellData/Phases'

    image_og = bq.load(image_url)
    image_mask = bq.load(image_mask)

    nii_img = nib.load(image_mask)
    nii_img = np.asarray(nii_img.get_fdata())

    mask = cv2.imread(image_og, cv2.IMREAD_GRAYSCALE)

    overlay = np.zeros_like(nii_img)

    for i in range(nii_img.shape[-1]):
        overlay[:,:,i] = np.where((nii_img[:,:,i] > 2) , mask, nii_img[:,:,i]*mask+mask/1.5)


    outtable_xml = table_service.store_array(overlay.swapaxes(-1,0), name='segmentation_output')
    return [ outtable_xml ]
    # out_strength_xml = """<tag name="Strength">
    #                             <tag name="Strength" type="string" value="%s"/>
    #                             <tag name="sbar_up" type="string" value="%s"/>
    #                             <tag name="sbar_low" type="string" value="%s"/>
    #                             <tag name="Volume Fraction" type="string" value="%s"/>
    #                             <tag name="link" type="resource" value="%s"/>
    #                       </tag>""" %(str(y[0]*eta),str(sbar_up*eta),str(sbar_low*eta),str(f1)+', '+str(f2), table_url)
    # return [out_strength_xml]
