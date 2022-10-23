from fastapi import FastAPI,status
import urllib.request
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.transform import resize
import skimage  as sk
from app.models import *

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "nord"})

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/checkImgages",status_code=status.HTTP_200_OK, response_model=ResponseModel)
async def check_images(request: RequestModel):
    try:
        urllib.request.urlretrieve(request.urlImageOld, "app/media/old.png")
        urllib.request.urlretrieve(request.urlImageNew, "app/media/new.png")
        ref_image = imread("app/media/old.png")
        ref_image = rgb2gray(ref_image)
        impaired_image = imread('app/media/new.png')
        impaired_image = rgb2gray(impaired_image)
        impaired_image = resize(impaired_image, (ref_image.shape[0], ref_image.shape[1]),
                                anti_aliasing=True)
        score = sk.metrics.structural_similarity(ref_image, impaired_image, multichannel=True, gaussian_weights=True,
                                                 sigma=1.5, use_sample_covariance=False, data_range=1.0)
        print(score)
        match = score > 0.95
    except:
        match = False
        score = -1
    response = ResponseModel(match=match,score=score)

    return response
