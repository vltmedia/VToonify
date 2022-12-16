import numpy  as np
from PIL import Image
import glob

def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

if __name__ == '__main__':
    style = 'isekai'
    exstyle_path = f'./checkpoint/vtoonify_d_{style}/exstyle_code.npy'
    dataset_path = f'./data/{style}/images/train/*.*'
    
    
    files = glob.glob(dataset_path)
    
    exstyles = np.load(exstyle_path, allow_pickle='TRUE').item()
    
    matches = []
    
    for key in exstyles.keys():
        for file in files:
            if key in file:
                matches.append((key, file))
    
    divisor = int(len(matches) / 4)
    maxCount = divisor * 4
    cleanedMatches = matches[:maxCount]
    gridSize = [int(len(cleanedMatches) / 4), 4]
    
    # Create an array of PIL Images from matches
    imgs = [Image.open(cleanedMatches[1]) for cleanedMatches in cleanedMatches]
    outputFile = f'./data/{style}/images/style_index.jpg'
    image_grid(imgs,gridSize[0],gridSize[1]).save(outputFile)
    
    print(f'Output file: {outputFile}')