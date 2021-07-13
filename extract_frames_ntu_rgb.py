'''
For HMDB51 and UCF101 datasets:

Code extracts frames from video at a rate of 25fps and scaling the
larger dimension of the frame is scaled to 256 pixels.
After extraction of all frames write a "done" file to signify proper completion
of frame extraction.

Usage:
  python extract_frames.py video_dir frame_dir
  
  video_dir => path of video files
  frame_dir => path of extracted jpg frames

'''

import sys, os
import numpy as np
import subprocess
from tqdm import tqdm
       

def extract(vid_dir, frame_dir, start, end, redo=False):
  l = ['nturgbd_rgb_s001', 'nturgbd_rgb_s002', 'nturgbd_rgb_s003', 'nturgbd_rgb_s004', 'nturgbd_rgb_s005', 'nturgbd_rgb_s006', 'nturgbd_rgb_s007', 'nturgbd_rgb_s008', 'nturgbd_rgb_s009', 'nturgbd_rgb_s010', 'nturgbd_rgb_s011', 'nturgbd_rgb_s012', 'nturgbd_rgb_s013', 'nturgbd_rgb_s014', 'nturgbd_rgb_s015', 'nturgbd_rgb_s016', 'nturgbd_rgb_s017']
  class_list = l[start:end]

  print("Classes =", class_list)
  
  for ic,cls in enumerate(class_list): 
    if not os.path.exists(vid_dir + cls):
        os.makedirs(vid_dir + cls)
    vlist = sorted(os.listdir(vid_dir + cls))
    print("")
    print(ic+1, len(class_list), cls, len(vlist))
    print("")
    for v in tqdm(vlist):
      outdir = os.path.join(frame_dir, cls, v.split('_')[0])
      # Checking if frames already extracted
      if os.path.isfile( os.path.join(outdir, 'done') ) and not redo: continue
      try:  
        os.system('mkdir -p "%s"'%(outdir))
        # check if horizontal or vertical scaling factor
        o = subprocess.check_output('ffprobe -v error -show_entries stream=width,height -of default=noprint_wrappers=1 "%s"'%(os.path.join(vid_dir, cls, v)), shell=True).decode('utf-8')
        lines = o.splitlines()
        width = int(lines[0].split('=')[1])
        height = int(lines[1].split('=')[1])
        resize_str = '-1:256' if width>height else '256:-1'

        # extract frames
        os.system('ffmpeg -i "%s" -r 30 -q:v 2 -vf "scale=%s" "%s"  > /dev/null 2>&1'%( os.path.join(vid_dir, cls, v), resize_str, os.path.join(outdir, '%05d.jpg')))
        nframes = len([ fname for fname in os.listdir(outdir) if fname.endswith('.jpg') and len(fname)==9])
        if nframes==0: raise Exception 

        os.system('touch "%s"'%(os.path.join(outdir, 'done') ))
      except:  
        print("ERROR", cls, v)

if __name__ == '__main__':
  vid_dir   = sys.argv[1]
  frame_dir = sys.argv[2]
  start     = int(sys.argv[3])
  end       = int(sys.argv[4])
  extract(vid_dir, frame_dir, start, end, redo=True)