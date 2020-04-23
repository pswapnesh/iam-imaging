# iam-imaging

This is a general purpose image processing utility. 
## Description
This package processes all images in a src_folder and save them in the dst_folder using processing functions supplied by user. 
arguments: see Usage below for syntax
-p or --plug <user_file.py>
-s or --src <path to source folder>
-d or --dst <path to destination folder>

The user_file.py MUST contain five functions: 
1. image_read(im)
2. image_save(fname,im)
3. pre_processing(im)
4. processing(im)
5. post_processing(im)

If no plugin is supplied, default functions are used. 
skimage.imread
skimage.imsave
identity_function
identity_function
identity_function

## Usage:
iam-imaging -p /path/to/folder/a_python_file.py -s /path/to/src_folder/*.tif -d /path/to/dst_folder/*.tif


