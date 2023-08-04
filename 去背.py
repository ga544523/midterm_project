from PIL import Image
import numpy as np
column, row = 256,256
vis=np.zeros((column,row))
    
import queue
img=Image.open('test_short._hair.png')


q = queue.Queue()

q.put((0,0))
q.put((0,255))
q.put((255,0))
q.put((255,255))
vis[0][0]=1
vis[0][255]=1
vis[255][0]=1
vis[255][255]=1

col=230
while(q.empty()==False):
    i,j=q.get()

    img.putpixel( (j, i), (0, 0, 0, 0) )
    vis[i][j]=1
    if(i+1<256):
        if(img.getpixel((j,i+1))[0]>col and img.getpixel((j,i+1))[1]>col and img.getpixel((j,i+1))[2]>col and vis[i+1][j]==0):
            vis[i+1][j]=1
            q.put((i+1,j))
    if(i-1>=0):
        if(img.getpixel((j,i-1))[0]>col and img.getpixel((j,i-1))[1]>col and img.getpixel((j,i-1))[2]>col and vis[i-1][j]==0):
            vis[i-1][j]=1
            q.put((i-1,j))
        
    if(j+1<256):
        if(img.getpixel((j+1,i))[0]>col and img.getpixel((j+1,i))[1]>col and img.getpixel((j+1,i))[2]>col and vis[i][j+1]==0):
            vis[i][j+1]=1
            q.put((i,j+1))
        
    if(j-1>=0):
        if(img.getpixel((j-1,i))[0]>col and img.getpixel((j-1,i))[1]>col and img.getpixel((j-1,i))[2]>col and vis[i][j-1]==0):
            vis[i][j-1]=1
            q.put((i,j-1))


'''         
for i in range(0,256,1):
    for j in range(0,256,1):
        
        if(img.getpixel((j,i))[0]>250 and img.getpixel((j,i))[1]>250 and img.getpixel((j,i))[2]>250):
            img.putpixel( (j, i), (0, 0, 0, 0) )
'''



         
img.save('test_short_hair1.png')
1/0