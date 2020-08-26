import csv
import random
from PIL import Image
from torchvision import transforms, datasets
from torch.autograd import Variable
import torch
import os
import shutil

# style info
style_name = []
style_csv = os.path.join('style_info', 'style_class.txt')
with open(style_csv, 'r') as f:
    for line in f.readlines():
        name = line.split(' ')[1][:-1]
        style_name.append(name)

# predict genre
data_dir = 'images'
trans = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

img_dir = "generated images"
result = []

for file in os.listdir(img_dir):
    if file.split('.')[-1] != 'jpg':
        continue
    path = os.path.join(img_dir, file)
    img = Image.open(path).convert('RGB')
    img_tensor = trans(img).float()
    img_tensor = img_tensor.unsqueeze_(0)

    model = torch.load('model.pth')
    model.eval()

    var = Variable(img_tensor)
    output = model(var)
    _, preds = torch.max(output.data, 1)
    index = preds.data.numpy()[0]
    classes = datasets.ImageFolder(os.path.join(data_dir, 'val'), trans).classes
    style = classes[index]
    print('preds:', os.path.basename(path), style)

    # style = 'still_life'
    info = []
    count = {idx: 0 for idx in range(27)}
    style_info = os.path.join('style_info', style + '.csv')
    with open(style_info, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            info.append(row)

    for each in info:
        count[int(each[1])] += 1

    count = sorted(count.items(), key=lambda d:d[1], reverse=True)
    # nums = {}
    # for each in count:
    #     if each[1] < 100:
    #         continue
    #     nums[each[0]] = each[1]
    # for key, val in nums.items():
    #     print('%s-%s: %s' %(key, style_name[key], val))
    # selected_style = int(input('Input the index of the style selected:'))

    selected_style = count[0][0]
    selected_info = [each for each in info if int(each[1]) == selected_style]
    for i in range(5):
        choice = random.choice(selected_info)[0]
        new_name = os.path.basename(path).split('.')[0] + '-style%d' % i + '.jpg'
        new_path = os.path.join('style images', new_name)
        shutil.copy(choice, new_path)