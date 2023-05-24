from PIL import ImageTk, Image
import os

class Encode_class():
    def __init__(self,imgfilename,encrypted_data,output_directory_name,outputimgfilename):
        self.imgfilename = imgfilename
        self.output_directory_name = output_directory_name
        self.outputimgfilename = outputimgfilename
        self.encrypted_data = encrypted_data
    
    def encode(self,msg_binary,binary_pixels,index):
        i=0
        while(i < len(msg_binary)):
            if(i % 3 == 0):
                r = (binary_pixels[index][0:8])
                r = r[:-1] + msg_binary[i]
                temp = r   
                i = i+1
            elif(i % 3 == 1):
                r = (binary_pixels[index][8:16])
                r = r[:-1] + msg_binary[i]
                temp = temp + r   
                i = i+1            
            elif(i % 3 == 2):
                r = (binary_pixels[index][16:24])
                r = r[:-1] + msg_binary[i]
                temp = temp + r   
                i = i+1                  
                binary_pixels[index] = temp
            if(i % 3 == 0):
                index = index + 1
        if(len(temp)<24):
            temp = temp + binary_pixels[index][len(temp):24]
            binary_pixels[index] = temp  
        return index

    def reconstruct(self,binary_pixels,img,output_directory_name,outputimgfilename):
        # Convert the binary pixels back to RGB tuples
        rgb_pixels = [tuple(int(binary[i:i+8], 2) for i in range(0, 24, 8)) for binary in binary_pixels]
        os.chdir(output_directory_name)
        output_img = Image.new(img.mode, img.size)
        output_img.putdata(rgb_pixels)
        output_img.save(outputimgfilename+".png")

    def encode_program(self):
        #  image to binary
        img = Image.open(self.imgfilename)
        pixels = list(img.getdata())
        binary_pixels = [ format(pixel[0],'08b')+format(pixel[1],'08b')+format(pixel[2],'08b') for pixel in pixels]
        msg_binary = ''.join(format(i,'08b') for i in self.encrypted_data)
        # Add a symbol to indicate end of message in binary pixels of image
        end_symbol = "#$@"
        for i in end_symbol:
            msg_binary += format(ord(i),'08b') 
        index = 0
        end_symbol_position = 0
        index = self.encode(msg_binary,binary_pixels,index)        

        self.reconstruct(binary_pixels,img,self.output_directory_name,self.outputimgfilename)
