# Image-Staganography-with-AES-Encryption
Image Steganography python software to hide data within an Image file.

Options available in software are

Encoding :
Data is encrypted using AES 128 bits block cipher before encoding in image file.
Image file with only .jpeg extension is required for encoding.
Amount of data that can be encoded is dependent on image resolution. More data can be encoded in high resolution image.

Decoding :
Software will produce a text file only if input image contains hidden data.
If there is no encoded data in image file, output will not be produced after decoding.
