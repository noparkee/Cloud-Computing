import boto3
import urllib.parse
import os
from PIL import Image, ImageFilter

print('Loading function')

s3 = boto3.client('s3')
CG = os.environ['COLOR_OR_GRAY']

def check_type(key):
    type = key[-4:]
    type = type.replace('.', '')          # get image file type
    
    if (type != 'jpg') and (type != 'png') and (type != 'jpeg') and (type != 'gif'):
        return False
    else:
        return True
    
def make_square(image_path, src):
    image = Image.open(image_path)
    img_width, img_height = image.size
    
    if img_width > img_height:
        img = image.crop((img_width//2 - img_height//2, 0, img_width//2 + img_height//2, img_height))
    else:
        img = image.crop((0, img_height//2 - img_width//2, img_width, img_height//2 + img_width//2))
    
    if CG == 'gray' or CG == 'grey':
        img = img.convert('L')
    
    dst = 'square-' + src
    result_path = '/tmp/' + dst
    img.save(result_path)
    
    print("Transformation Complete!")

    return result_path
    
def lambda_handler(event, context):
    srcbucket = event['Records'][0]['s3']['bucket']['name']
    srckey = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    if not check_type(srckey):
        print("Type Error!")
        return False
    
    dstbucket = srcbucket + '-output'
    if srcbucket == dstbucket:
        print("Same Bucket Error!")
        return False
        
    if CG == 'gray':
        dstkey = 'output-gray-' + srckey
    elif CG == 'grey':
        dstkey = 'output-grey-' + srckey
    else:
        dstkey = 'output-color-' + srckey
    
    download_path = '/tmp/{}'.format(srckey)               # image download
    s3.download_file(srcbucket, srckey, download_path)
    
    upload_path = make_square(download_path, srckey)        # make square
    
    try:                                                    # upload
        s3.upload_file(upload_path, dstbucket, dstkey)
        print('Upload!')
        return True
    except:
        print('Fail to upload!')
        return False
    