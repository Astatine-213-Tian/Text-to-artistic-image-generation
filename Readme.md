# Text to artistic image generation 
### [See on ArXiv](https://arxiv.org/abs/2205.02439)

## Introduction

This project page provides code that helps you to generate artistic from text description.

## How to use

### Step 1: Text to realistic image generation

In this step, we utilzie the pre-trained model provided by the [DM-GAN](https://github.com/MinfengZhu/DM-GAN). Please check their repository for the implementation details.

#### Environment required

- Python 2.7
- Pytorch 0.4
- Tensorflow 1.12.0

#### Traning / Evaluating the model

If you need to train the model for more epochs or evaluate the model, please clone the origninal [DM-GAN](https://github.com/MinfengZhu/DM-GAN) repository.

#### Generating images

If you only need to use the pre-traind model to generate images from your own captions, change the content of the file `example_captions.txt` in either `data/birds/` or `data/coco/` folder, depending on the pre-trained model you choose.

Then follow the instruction below:

- Go to `code/` folder

- Bird: `python main.py --cfg cfg/eval_DMGAN.yml`
- Coco: `python main.py --cfg cfg/eval_DMGAN.yml`

### Step 2: Style recommendation

In this step, we intend to classify the images generate based on the content and recommend suitable style images.

#### Environment required

- Python 3.5+

- Pytorch 1.6

#### Using pre-trianed model

1. Download the pre-trained model from [here](https://drive.google.com/file/d/1_ywoRKeovAeFLUNf-5EP-jjzEpCzhq58/view?usp=sharing). 
2. Put image generated in step 1 under the folder `generated images`
3. Run the file `select_style_image.py` to randomly select the 5 style images for step 3. Selected images will be put in the `style images` folder. 

#### Traning the model

Classifying generated image by genres existed in [WikiArt](https://www.wikiart.org/en/paintings-by-genre)

1. Donwload [images](https://drive.google.com/file/d/1_fx4Sr9AY9yzFLYOb9jhtGRfzGN4r_sn/view?usp=sharing) classified by genre.
2. Run the file `Finetune.py`

### Step 3: Style transfer

In this step, we transfer the style of the style image selected in step 2 to content image generated in step 1.

#### Environment required

- Python 3.5+
- Set up [Magenta environment](https://github.com/magenta/magenta/blob/master/README.md).
- Install [tf-slim](https://github.com/tensorflow/tensorflow/blob/e062447136faa0a3513e3b0690598fee5c16a5db/tensorflow/contrib/slim/README.md) 

#### Using pre-trained model

Follow the instructions from [here](https://github.com/magenta/magenta/tree/master/magenta/models/arbitrary_image_stylization#stylizing-an-image-using-a-pre-trained-model). 

#### Traning the model

1. Download [tfrecord](https://drive.google.com/file/d/193NRRmpU5nsfdkOyJ9A44IELw6YaeKC0/view?usp=sharing) file for wikiart images
2. Follow the instructions from [here](https://github.com/magenta/magenta/tree/master/magenta/models/arbitrary_image_stylization#train-a-model-on-a-large-dataset-with-data-augmentation-to-run-on-mobile).
