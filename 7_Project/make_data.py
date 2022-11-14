import numpy as np
import skimage.draw as draw
import skimage.filters as filter
import skimage.feature as feature
import skimage.io as skio

def make_images(n_small,n_big,p_high, name):

    # Bright
    N = (3000,3000)
    im = np.zeros(N)

    for i in range(n_small):
        pos = np.random.choice(range(N[0]),2)
        p = draw.disk(pos,10,shape=N)
        im[p] = 1
    for i in range(n_big):
        pos = np.random.choice(range(N[0]),2)
        p = draw.disk(pos,30,shape=N)
        im[p] = 1

    #GFP
    m = feature.blob_log(im,10,30)

    im2 = np.zeros(N)
    for i in m:
        if i[2] < 11 and np.random.rand() < p_high:
            pos = np.random.choice(range(N[0]),2)
            p = draw.disk(i[:2].astype(int),10,shape=N)
            im2[p] = 1+np.random.randn()*0.0
        elif i[2] < 11:
            pos = np.random.choice(range(N[0]),2)
            p = draw.disk(i[:2].astype(int),10,shape=N)
            im2[p] = .1+np.random.randn()*0.0
        else:
            pos = np.random.choice(range(N[0]),2)
            p = draw.disk(i[:2].astype(int),20,shape=N)
            im2[p] = .05+np.random.randn()*0.0

    im2 = filter.gaussian(im2,10)
    im2 += np.min(im2)

    skio.imsave("data/"+name+"_bright_field_image.tif",im)
    skio.imsave("data/"+name+"_GFP_image.tif",im2)

    return

conditions = [
    [500,300,.3,"Control"],
    [500,300,.3,"Condition_1"],
    [300,500,.3,"Condition_2"],
    [500,300,.3,"Condition_3"],
    [500,300,.35,"Condition_4"],
    [500,300,.6,"Condition_5"],
    [500,300,.3,"Condition_6"],
    [500,300,.3,"Condition_7"],
]

np.random.seed(0)
for i in conditions:
    make_images(i[0],i[1],i[2],i[3])

