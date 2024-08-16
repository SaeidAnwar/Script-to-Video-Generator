import cv2
import os

def create_slideshow(end, word, word_count, image_paths):
    print("Creating slideshow.....")
    frames_per_second = 25
    total_play_time = end[-1]
    total_frames = int(frames_per_second*total_play_time) + 1
    line_end_time = []
    end_idx = 0
    for i in word_count:
        end_idx += i
        print(end_idx, len(end))
        if end_idx <= len(end):
            line_end_time.append(end[end_idx-1])

    img_arr = []
    size = (0, 0)
    width = 0
    height = 0
    for image_path in image_paths:
        img = cv2.imread(image_path)
        img_arr.append(img)
        width, height, layers = img.shape
        size = (width, height)
    
    print("len of img arr, line end time arr")
    print(len(word_count))
    print(len(img_arr))
    print(len(line_end_time))

    slideshow = cv2.VideoWriter('./Output/output.avi',cv2.VideoWriter_fourcc(*'DIVX'), frames_per_second, size)

    image_idx = 0
    word_idx = 0
    for i in range(total_frames):
        time_elapsed = i/frames_per_second
        font = cv2.FONT_HERSHEY_SIMPLEX
        textsize = cv2.getTextSize(word[word_idx], font, 2, 5)[0]

        nwidth = int((width/2) - (textsize[0]/2))
        nheight = int((height/2) - (textsize[1]/2))
        image_with_text = img_arr[image_idx].copy()
        cv2.putText(image_with_text, word[word_idx], (nwidth, nheight), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(image_with_text, word[word_idx], (nwidth, nheight), font, 2, (255, 255, 255), 3, cv2.LINE_AA)
        slideshow.write(image_with_text)

        if time_elapsed >= line_end_time[image_idx] and image_idx < len(img_arr)-1:
            image_idx += 1
        if time_elapsed >= end[word_idx] and word_idx < len(word)-1:
            word_idx += 1

    slideshow.release() 
    print("Slideshow created!")