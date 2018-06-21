import os
import numpy as np
import cv2
import imutils
from imutils import face_utils
import dlib
import itertools
from PIL import ImageFilter
from PIL import Image

# Init dlib's face detector and facial landmark predictor
shape_predictor_file_path = "shape_predictor_68_face_landmarks.dat"
global detector, predictor # Why global? Because these are constant, only declared once and used further down the pipeline
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor_file_path)

def rect_to_bb(rect):
    """ take a bounding predicted by dlib and convert it
    to the format (x, y, w, h) as we would normally do
    with OpenCV """
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)

def shape_to_np(shape, dtype="int"):
    # initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=dtype)

    # loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coords[i] = (shape.part(i).x, shape.part(i).y)

    # return the list of (x, y)-coordinates
    return coords


def get_anchor_points(image):
    """ Image border anchor points.
        Start: top left corner, next: center top, continue clockwise.
        Total of 8 anchor points
        Necessary to make full image morphs
    """
    width = image.shape[1]
    height = image.shape[0]
    half_width = int(width/2)
    half_height = int(height/2)
    # +/- 1 to keep points within image frame (instead of on it)
    anchor_points = [
            [0+1,0+1], # top left
            [half_width, 0+1], # top middle
            [width-1, 0+1], # top right
            [width-1, half_height], # right middle
            [width-1, height-1], # bottom right
            [half_width, height-1], # bottom middle
            [0+1, height-1], # bottom left
            [0+1, half_height] # left middle
    ]
    return anchor_points


def get_facial_landmarks(image):
    # image = imutils.resize(image, width=500)
    # cv2.imshow("dd", gray)
    # cv2.waitKey(0)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale image
    rects = detector(gray, 1)

    # loop over the face detections
    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy
        # array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # convert dlib's rectangle to a OpenCV-style bounding box
        # [i.e., (x, y, w, h)], then draw the face bounding box
        # (x, y, w, h) = face_utils.rect_to_bb(rect)
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # show the face number
        # cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        return shape


def get_image_points(image):
    """ Includes facial landmarks + image border anchor points """
    facial_landmarks = get_facial_landmarks(image)
    anchor_points = get_anchor_points(image)
    if facial_landmarks is None:
        raise ValueError("No facial landmarks found! Check that a face is present in the image.")
    return np.append(facial_landmarks, anchor_points, axis=0)


# Read points from text file
def readPoints(path) :
    # Create an array of points.
    points = [];
    # Read points
    with open(path) as file :
        for line in file :
            x, y = line.split()
            points.append((int(x), int(y)))

    return points

# Check if a point is inside a rectangle
def rect_contains(rect, point) :
    if point[0] < rect[0] :
        return False
    elif point[1] < rect[1] :
        return False
    elif point[0] > rect[2] :
        return False
    elif point[1] > rect[3] :
        return False
    return True


def applyAffineTransform(src, srcTri, dstTri, size):
    """
    Apply affine transform calculated using srcTri and dstTri to src and
    output an image of size.
    """
    # Given a pair of triangles, find the affine transform.
    warpMat = cv2.getAffineTransform( np.float32(srcTri), np.float32(dstTri) )

    # Apply the Affine Transform just found to the src image
    dst = cv2.warpAffine( src, warpMat, (size[0], size[1]), None, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101 )

    return dst


def morphTriangle(img1, img2, img, t1, t2, t, alpha):
    """ Warps and alpha blends triangular regions from img1 and img2 to img """
    # Find bounding rectangle for each triangle
    r1 = cv2.boundingRect(np.float32([t1]))
    r2 = cv2.boundingRect(np.float32([t2]))
    r = cv2.boundingRect(np.float32([t]))

    # Offset points by left top corner of the respective rectangles
    t1Rect = []
    t2Rect = []
    tRect = []

    for i in range(0, 3):
        tRect.append(((t[i][0] - r[0]),(t[i][1] - r[1])))
        t1Rect.append(((t1[i][0] - r1[0]),(t1[i][1] - r1[1])))
        t2Rect.append(((t2[i][0] - r2[0]),(t2[i][1] - r2[1])))


    # Get mask by filling triangle
    mask = np.zeros((r[3], r[2], 3), dtype = np.float32)
    cv2.fillConvexPoly(mask, np.int32(tRect), (1.0, 1.0, 1.0), 16, 0);

    # Apply warpImage to small rectangular patches
    img1Rect = img1[r1[1]:r1[1] + r1[3], r1[0]:r1[0] + r1[2]]
    img2Rect = img2[r2[1]:r2[1] + r2[3], r2[0]:r2[0] + r2[2]]

    size = (r[2], r[3])
    warpImage1 = applyAffineTransform(img1Rect, t1Rect, tRect, size)
    warpImage2 = applyAffineTransform(img2Rect, t2Rect, tRect, size)

    # Alpha blend rectangular patches
    imgRect = (1.0 - alpha) * warpImage1 + alpha * warpImage2

    # Copy triangular region of the rectangular patch to the output image
    img[r[1]:r[1]+r[3], r[0]:r[0]+r[2]] = img[r[1]:r[1]+r[3], r[0]:r[0]+r[2]] * ( 1 - mask ) + imgRect * mask


def create_morph_image(image1, image2, blend, warp):
    # Convert Mat to float data type
    img1 = np.float32(image1)
    img2 = np.float32(image2)
    # Create arrays of corresponding points
    points1 = get_image_points(image1)
    points2 = get_image_points(image2)
    points = [];

    if len(points1) is not len(points2):
        raise ValueError("Different amount of facial landmarks found in the two images. Make sure a face is clearly visible in both.")

    # Compute weighted average point coordinates
    for i in range(0, len(points1)):
        x = ( 1 - warp ) * points1[i][0] + warp * points2[i][0]
        y = ( 1 - warp ) * points1[i][1] + warp * points2[i][1]
        points.append( (np.floor(x),np.floor(y)) )

    # Allocate space for final output
    # calc morph image dimensions
    m_width = (1-warp)*img1.shape[0] + warp*img2.shape[0]
    m_height = (1-warp)*img1.shape[1] + warp*img2.shape[1]
    m_size = (int(m_width), int(m_height), 3) # TODO: If int floors, can the size be too small?
    imgMorph = np.zeros(m_size, dtype = img1.dtype)


    triangle_points = []
    # Rectangle to be used with Subdiv2D, use size of morph image
    size = imgMorph.shape
    rect = (0, 0, size[1], size[0])
    # Create an instance of Subdiv2D
    subdiv = cv2.Subdiv2D(rect)
    for p in points:
        subdiv.insert(p)
    triangleList = subdiv.getTriangleList()
    for t in triangleList:
        pt1 = (t[0], t[1])
        pt2 = (t[2], t[3])
        pt3 = (t[4], t[5])
        if rect_contains(rect, pt1) and rect_contains(rect, pt2) and rect_contains(rect, pt3):
            pt1_idx = points.index(pt1)
            pt2_idx = points.index(pt2)
            pt3_idx = points.index(pt3)
            triangle_points.append( (pt1_idx, pt2_idx, pt3_idx) )

    # Get triangle points
    for t_p in triangle_points:
        x = int( t_p[0] )
        y = int( t_p[1] )
        z = int( t_p[2] )

        t1 = [points1[x], points1[y], points1[z]]
        t2 = [points2[x], points2[y], points2[z]]
        t = [ points[x], points[y], points[z] ]

        # Morph one triangle at a time.
        morphTriangle(img1, img2, imgMorph, t1, t2, t, blend)

    return imgMorph, points


def get_morph_image(input_dir, filename1, filename2, morph_method, blend, warp):
    # Read images
    # image1 = cv2.imread( os.path.join(input_dir, filename1),1 )
    # image2 = cv2.imread( os.path.join(input_dir, filename2),1 )
    image1 = cv2.imread(filename1, 1)
    image2 = cv2.imread(filename2, 1)

    if morph_method == "full_image":
        imgMorph, points = create_morph_image(image1, image2, blend, warp)
        return imgMorph
    elif morph_method == "face_swap_morph":
        imgMorph, points = create_morph_image(image1, image2, blend, warp)
        imgMorphNoBlend, points = create_morph_image(image1, image2, 0.0, warp)
    else:
        raise NotImplementedError("No such morph method implemented!")

    # add average image points to morphed image
    facial_points_warped = points[:-8]
    # for (x, y) in facial_points_warped:
    #     cv2.circle(imgMorph, (int(x), int(y)), 3, (0, 0, 255), -1)

    hull = []
    facial_points_warped = [(int(x),int(y)) for x,y in facial_points_warped]
    # NOTE: points to convexhull should be integer
    hullIndex = cv2.convexHull(np.array(facial_points_warped), returnPoints=False)
    for idx in hullIndex:
        x,y = facial_points_warped[idx[0]]
        x,y = int(x), int(y)
        hull.append( (x,y) )
        # cv2.circle(imgMorph, (x, y), 3, (255, 0, 0), -1)

    # Calculate Mask
    hull8U = []
    for i in range(0, len(hull)):
        hull8U.append((hull[i][0], hull[i][1]))

    mask = np.zeros(imgMorph.shape, dtype = np.float32)
    cv2.fillConvexPoly(mask, np.int32(hull8U), (255, 255, 255))
    r = cv2.boundingRect(np.float32([hull]))
    center = ((r[0]+int(r[2]/2), r[1]+int(r[3]/2)))

    # To do seamless cloning, I need: src, dst, mask
    # SRC: use mask to take facial region from blend/warp image
    # facial_mask is then placed ontop of the no-blend/warp image

    # TODO: improve this!
    imgMorphNoBlend = np.uint8(imgMorphNoBlend)
    facial_mask = np.copy(imgMorphNoBlend)
    mask_idx = np.where(mask > 0)
    m_x = mask_idx[0]
    m_y = mask_idx[1]
    int_imgMorph = np.uint8(imgMorph)
    for i, x in enumerate(m_x):
        y = m_y[i]
        facial_mask[x,y] = int_imgMorph[x,y]

    # seamless cloning requires: source, destination, mask and center
    output = cv2.seamlessClone(facial_mask, imgMorphNoBlend, np.uint8(mask), center, cv2.NORMAL_CLONE)
    return output

def post_processing(img_np, filter_method):
    # convert numpy image to Pillow Image
    img_np = np.uint8(img_np)
    img_np_rgb = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB) # BGR --> RGB (opencv uses BGR format)
    img_pil = Image.fromarray( img_np_rgb, mode='RGB' )

    # add filter
    implemented_filters = ["contour", "sharpen", "blur", "smooth", "smooth_more", "detail", "edge_enhance"]
    if not filter_method in implemented_filters:
        raise TypeError("Filter method not implemented!")
    filter_str = "ImageFilter." + filter_method.upper()
    img_filter = img_pil.filter( eval(filter_str) )

    # convert back to numpy image
    img_np_filter = np.array(img_filter.getdata()).astype(np.uint8).reshape( (img_filter.size[1],img_filter.size[0],3) )
    img_np_filter_bgr = cv2.cvtColor(img_np_filter, cv2.COLOR_RGB2BGR) # RGB --> BGR
    return img_np_filter_bgr


def get_nr_input_images(input_dir):
    for _,_, files in os.walk(input_dir):
        return len(files)

def get_nr_morphs(N, morph_method):
    nr_morphs = 0
    if morph_method == "full_image":
        nr_morphs = int( (N**2-N)/2 )
    elif morph_method == "face_swap_morph":
        nr_morphs = int( N*(N-1) )
    return nr_morphs


def get_all_image_pairs(input_dir, morph_method):
    image_files = []
    allowed_image_formats = [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".pbm", ".pgm", ".ppm"]
    for _,_, filenames in os.walk(input_dir):
        for fn in filenames:
            # only select image files (with allowed format)
            file_ext = os.path.splitext(fn)[1].lower()
            if file_ext in allowed_image_formats:
                image_files.append( os.path.join(input_dir,fn) )
            else:
                print("Ignoring file:", fn)

    image_pairs = []
    if morph_method == "full_image":
        image_pairs = itertools.combinations(image_files, 2)
    elif morph_method == "face_swap_morph":
        image_pairs = itertools.permutations(image_files, 2)
    return image_pairs, len(image_files)


def get_all_image_pairs_from_two_folders(in_dir_1, in_dir_2, morph_method):
    # input: two dirs
    # output: image pairs, nr of source images: N, M
    # images are only matched with images from the other folder
    image_files = [ [], [] ]
    allowed_image_formats = [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".pbm", ".pgm", ".ppm"]
    for i, input_dir in enumerate( [in_dir_1, in_dir_2] ):
        for _,_, filenames in os.walk(input_dir):
            for fn in filenames:
                # only select image files (with allowed format)
                file_ext = os.path.splitext(fn)[1].lower()
                if file_ext in allowed_image_formats:
                    image_files[i].append( os.path.join(input_dir,fn) )
                else:
                    print("Ignoring file:", fn)
    print(image_files)

    image_pairs = []
    if morph_method == "full_image": # order doesn't matter
        for img1 in image_files[0]:
            for img2 in image_files[1]:
                image_pairs.append( (img1,img2) )
    elif morph_method == "face_swap_morph": # order matters
        for img1 in image_files[0]:
            for img2 in image_files[1]:
                image_pairs.append( (img1,img2) )
        # flip order
        for img1 in image_files[1]:
            for img2 in image_files[0]:
                image_pairs.append( (img1,img2) )

    return image_pairs, ( len(image_files[0]), len(image_files[1]) )
