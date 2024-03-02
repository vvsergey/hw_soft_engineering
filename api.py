from PIL import Image
from fastapi import FastAPI, UploadFile, File
import model as mdl

app = FastAPI()

model = mdl.load_model()


@app.get('/')
def root():
    return {"message": "Success"}


@app.post('/')
async def predict_process(file: UploadFile = File(...)):
    img = Image.open(file.file)
    x = mdl.preprocess_image(img)
    prd = model.predict(x)
    cls = mdl.get_predictions(prd)
    return {cls[0][1]}
