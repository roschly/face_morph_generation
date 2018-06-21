import os


# INPUT_DIR: Path to directory containing images (does NOT go into subfolders)
#   If only one input folder supplied, each image in that folder is morphed with
#   every other image in the same folder
INPUT_DIR = os.path.join(os.getcwd(), "images_no_subfolders")

# INPUT_DIR_2: Optional second directory containing images (does NOT go into subfolders)
#   If two input folders are given (by supplying input_dir_2 as well),
#   each image in one folder is only morphed with every image in the other folder.
INPUT_DIR_2 = None

# OUTPUT_DIR: Path to directory/folder where morph images will be saved
# A folder is created if it doesn't already exist
#   Does NOT go into subfolders
OUTPUT_DIR = os.path.join(os.getcwd(), "morphs")


# MORPH_METHOD: The method for morphing images
# Implemented methods: face_swap_morph, full_image
#   full_image:
#       The full image of both images are used
#       Nr morphed images created: (N^2-N)/2
#   face_swap_morph:
#       One image is used as background + surrounding head
#       The face is swapped with the face of the morphed image.
#       Nr morphed images created: N^2-N
MORPH_METHOD = "face_swap_morph"


# BLEND: Determines the mix of pixel values
#   Blend should be a float between [0.0, 1.0]
#
# WARP: Determines the mix of face shapes
#   Warp should be a float between [0.0, 1.0]
#
# Examples of BLEND and WARP:
# blend = 0.5, warp = 0.5 ==> The most equal morph of the two images
# blend = 0.0, warp = 0.0 ==> First image is unaltered
# blend = 1.0, warp = 1.0 ==> Second image is unaltered
# blend = 0.0, warp = 1.0 ==> Use first image's pixels, warped to match the second image's facial form
BLEND = 0.5
WARP = 0.5

# FILTER: A post processing filter
#   Implemented filters:
#   ["none", "contour", "sharpen", "blur", "smooth", "smooth_more", "detail", "edge_enhance"]
#   See link for details: http://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
FILTER = "sharpen"

# MORPH_WIDHT: Width of morphed image
#   Aspect ratio is preserved, so height is calculated based on WIDTH
#   Width is in pixels
#   Width == -1: means width is determined by input images
MORPH_WIDTH = -1
