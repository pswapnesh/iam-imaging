import glob
import numpy as np
import argparse 
from importlib.util import spec_from_file_location
import os
import iam_imaging
from skimage.io import imread,imsave


def main():
    parser = argparse.ArgumentParser(description='Process images from source folder and save in destination folder')
    parser.add_argument('-p','--plug', help='Path of a python file containing four functions: image_io.py, pre_processing.py, processing.py,post_processing.py', required=False)
    parser.add_argument('-s','--src', help='Path of source folder with images', required=True)
    parser.add_argument('-d','--dst', help='Path of destination folder', required=True)
    args = vars(parser.parse_args())

    if args['plug'] == None:
        image_read = iam_imaging.imread
        image_save = iam_imaging.imsave
        pre_processing = iam_imaging.pre_processing
        processing = iam_imaging.processing
        post_processing = iam_imaging.post_processing
    else:
        try:
            io = spec_from_file_location(args['plug'])
            image_read = io.image_read
            image_save = io.image_save
            pre_processing = io.pre_processing
            processing = io.processing
            post_processing = io.post_processing

        except ImportError as err:
            print('Error: bad plugin', err)

    if args['src'] == None:
        print('No source images mentioned: example /path/to/src/folder/*.tif')
    else:
        src_folder = args['src']

    if args['dst'] == None:
        print('No destination directory mentioned: example /path/to/destination/*.tif')
    else:
        dst_folder = args['dst']
        tmp = dst_folder.split('*')
        save_format = tmp[1]
        dst_folder = tmp[0]
    
    flist = glob.glob(src_folder)
    for f in flist:
        im = image_read(f)
        im = pre_processing(im)
        im = processing(im)
        im = post_processing(im)
        image_save(dst_folder + os.path.basename(f) + 'processed.' + save_format,im)
    
