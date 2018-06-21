# SOURCE https://github.com/spmallick/learnopencv/tree/master/FaceMorph
#!/usr/bin/env python

import os
import cv2
import imutils
import argparse
import dlib
from utils import *

def main(INPUT_DIR, INPUT_DIR_2, OUTPUT_DIR, BLEND, WARP, MORPH_METHOD, FILTER, MORPH_WIDTH, CALLBACK=None):
    # CALLBACK: the callback kwarg is used by the GUI, to receive and send information to this process.
    # It is a function defined in main_gui.py

    # Different image pairs depending on whether 1 or 2 input directories are supplied (see config.py for more info)
    if INPUT_DIR_2:
        image_pairs, (N,M) = get_all_image_pairs_from_two_folders(INPUT_DIR, INPUT_DIR_2, MORPH_METHOD)
        nr_morphs = len(image_pairs)
    else:
        image_pairs, nr_image_files = get_all_image_pairs(INPUT_DIR, MORPH_METHOD)
        nr_morphs = get_nr_morphs(nr_image_files, MORPH_METHOD)

    print("Processing images:")
    for i, (filename1, filename2) in enumerate(image_pairs):
        img_morph = get_morph_image(INPUT_DIR, filename1, filename2, MORPH_METHOD, BLEND, WARP)
        # Morphed image will be a combined version of input images
        # with same file format as the first image
        rest1, file_ext = os.path.splitext(filename1)
        name1_no_ext = os.path.split(rest1)[1]
        rest2, _ = os.path.splitext(filename2)
        name2_no_ext = os.path.split(rest2)[1]

        filename_morph = name1_no_ext + "___" + name2_no_ext + file_ext

        # apply filter to morphed image
        if not FILTER == "none":
            img_morph = post_processing(img_morph, FILTER)

        # set width of morph image
        if MORPH_WIDTH > 0:
            img_morph = imutils.resize(img_morph, width=MORPH_WIDTH)

        # save image to output directory (create it, if it doesn't exist)
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
        cv2.imwrite(os.path.join(OUTPUT_DIR, filename_morph), img_morph)

        # number of images processed
        print(i+1, ":", nr_morphs)
        # Used by GUI:
        # Input: number of images processed and total number of morphs.
        # Return: Whether or not this process should terminate
        if CALLBACK:
            cancel = CALLBACK(i+1, nr_morphs)
            if cancel:
                CALLBACK(-1,-1)
                break


# if this file is called directly, as a command-line tool
if __name__ == '__main__':
    from config import *

    # Handle commandline arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--in_dir", required=False, help="path to input images")
    ap.add_argument("-i2", "--in_dir_2", required=False, help="path to second folder of input images")
    ap.add_argument("-o", "--out_dir", required=False, help="path to save morph images to")
    ap.add_argument("-b", "--blend", required=False, type=float, help="blend value")
    ap.add_argument("-w", "--warp", required=False, type=float, help="warp value")
    ap.add_argument("-m", "--morph_method", required=False, help="Morphing method: full_image OR face_swap_morph")
    ap.add_argument("-f", "--filter", required=False, help="post processing filter")
    ap.add_argument("-mw", "--morph_width", required=False, type=int, help="set width of morphed image")
    args = vars(ap.parse_args())

    # Make commandline args (if any) override config file values
    INPUT_DIR       = args["in_dir"] if args["in_dir"] else INPUT_DIR
    INPUT_DIR_2     = args["in_dir_2"] if args["in_dir_2"] else INPUT_DIR_2
    OUTPUT_DIR      = args["out_dir"] if args["out_dir"] else OUTPUT_DIR
    BLEND           = args["blend"] if args["blend"] else BLEND
    WARP            = args["warp"] if args["warp"] else WARP
    MORPH_METHOD    = args["morph_method"] if args["morph_method"] else MORPH_METHOD
    FILTER          = args["filter"] if args["filter"] else FILTER
    MORPH_WIDTH     = args["morph_width"] if args["morph_width"] else MORPH_WIDTH

    main(INPUT_DIR, INPUT_DIR_2, OUTPUT_DIR, BLEND, WARP, MORPH_METHOD, FILTER, MORPH_WIDTH)
