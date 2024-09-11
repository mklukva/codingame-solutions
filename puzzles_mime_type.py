'''
 MIME types are used in numerous internet protocols to associate a media type (html, image, video ...) with the content sent. The MIME type is generally inferred from the extension of the file to be sent.

You have to write a program that makes it possible to detect the MIME type of a file based on its name.

Rules
You are provided with a table which associates MIME types to file extensions. You are also given a list of names of files to be transferred and for each one of these files, you must find the MIME type to be used.

The extension of a file is defined as the substring which follows the last occurrence, if any, of the dot character within the file name.
If the extension for a given file can be found in the association table (case insensitive, e.g. TXT is treated the same way as txt), then print the corresponding MIME type. If it is not possible to find the MIME type corresponding to a file, or if the file doesn’t have an extension, print UNKNOWN.

'''
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime_dict = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_dict[ext.lower()] = mt

for i in range(q):
    fname = input()  # One file name per line.
    key = fname.split('.')[-1].lower()
    if key in mime_dict and '.' in fname:
        print(mime_dict[key])
    else:
        print('UNKNOWN')
