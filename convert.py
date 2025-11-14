import moviepy.editor as moviepy
print('Convert')
loc=input('Enter path of video')
name=input('Enter new path with format')
clip=moviepy.VideoFileClip(loc)
clip.write_videofile(name)

'''
import moviepy.editor as moviepy
n='E:\\V\Software\\convert\\aos\\Alchemy of Souls S020'
fm1='.avi'
fm2='.mp4'
for i in range(1,6):
    s=n+str(i)+fm1
    ss=n+str(i)+fm2
    clip=moviepy.VideoFileClip(s)
    clip.write_videofile(ss)
    '''
