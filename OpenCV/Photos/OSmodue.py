import os


""" print(os.getcwd())

os.chdir('/home/akhil-joseph/OpenCV/')

print(os.getcwd())

print(len(os.listdir('/home/akhil-joseph/OpenCV/Photos')))
 """
print(os.environ.get('HOME'))

'test.txt'

file_path= os.path.join(os.environ.get('HOME'),'test.txt')
print(file_path )