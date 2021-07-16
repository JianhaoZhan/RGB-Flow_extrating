This repository is used to extract RGB/Flow frames from video, from UCF-101, HMDB-51 and NTU-RGB-D etc.

# file structure：
UCF-101:
PATH/HMDB51/brush_hair/April_09_brush_hair_u_nm_np1_ba_g.avi
HMDB-51:
PATH/UCF101/ApplyEyeMakeup/v_ApplyEyeMakeup_g01_c01.avi
NTU-RGB-D:
PATH/NTU_RGB_D/nturgbd_rgb_s001/S001C001P001R001A001_rgb.avi

# example：
HMDB-51:

rgb+flow:   
```python
python extract_frames_flows.py  /home/eed-server3/Downloads/dataset/HMDB-101/   /home/eed-server3/Downloads/dataset/res_HMDB-101 0 51  0
```
rgb:            
```python
python extract_frames.py  /home/eed-server3/Downloads/dataset/HMDB-101/   /home/eed-server3/Downloads/dataset/res_HMDB-101 0 51
```
UCF-101:   

rgb+flow:   
```python
python extract_frames_flows.py /home/eed-server3/Downloads/dataset/UCF-101/   /home/eed-server3/Downloads/dataset/res_UCF-101 0 101  0
```
rgb:            
```python
python extract_frames.py /home/eed-server3/Downloads/dataset/UCF-101/   /home/eed-server3/Downloads/dataset/res_UCF-101  0  101
```
NTU-RGB-D:（此rgb文件由于帧率、文件结构等不同于UCF而重写）

rgb:            
```python
python extract_frames_ntu_rgb.py  /New-8T/mars/NTU_RGB_D/   /New-8T/mars/NTU_RGB/  0  17              
```


# when you need to extract flow stream, you need to compile:
```
export OPENCV=/usr/local/

g++ -std=c++11 tvl1_videoframes.cpp -o tvl1_videoframes -I${OPENCV}include/opencv4/ -L${OPENCV}lib -lopencv_objdetect -lopencv_features2d -lopencv_imgproc -lopencv_highgui -lopencv_core -lopencv_imgcodecs -lopencv_cudaoptflow -lopencv_cudaarithm
```

