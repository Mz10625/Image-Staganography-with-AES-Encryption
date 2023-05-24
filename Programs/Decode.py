from PIL import ImageTk, Image
import Decrypt

class Decode_class():
    def __init__(self,imgfilename,output_directory_name,outputmsgfilename):
        self.imgfilename = imgfilename
        self.output_directory_name = output_directory_name
        self.outputmsgfilename = outputmsgfilename

    def decode_program(self):        
        count = 0
        end_symbol_present = 0
        #  image to binary
        img = Image.open(self.imgfilename)
        pixels = list(img.getdata())
        binary_pixels = [ format(pixel[0],'08b')+format(pixel[1],'08b')+format(pixel[2],'08b') for pixel in pixels]
        
        msg_binary = ""
        global msg_ascii
        msg_ascii = []

        for i in binary_pixels:
            if count >= 24:
                end_symbol_binary = msg_binary[count-24:count]
                if(end_symbol_binary == "001000110010010001000000"):                    
                    end_symbol_present = 1
                    break
            msg_binary = msg_binary + i[7:8]
            count = count + 1

            if count >= 24:
                end_symbol_binary = msg_binary[count-24:count]
                if(end_symbol_binary == "001000110010010001000000"):
                    end_symbol_present = 1
                    break
            msg_binary = msg_binary + i[15:16]
            count = count + 1 

            if count >= 24:
                end_symbol_binary = msg_binary[count-24:count]
                if(end_symbol_binary == "001000110010010001000000"):                    
                    end_symbol_present = 1
                    break
            msg_binary = msg_binary + i[23:24]
            count = count + 1
    
        j=0
        for i in range(0, len(msg_binary)-24, 8):
            msg_ascii.append(int(msg_binary[i:i+8], 2))
            j = j + 1
        
        if(end_symbol_present == 1):
            Decrypt_object = Decrypt.Decrypt_class(msg_ascii,self.output_directory_name,self.outputmsgfilename)
            Decrypt_object.decrypt()