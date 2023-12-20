import os

def rename_files():
    
    folder = "~/Desktop/cod/source/bin"
    for count, filename in enumerate(os.listdir(folder)):
        my_dest = f"Picture {str(count)}.jpg"
        my_source = f"{folder}/{filename}"
        my_dest = f"{folder}/{my_dest}"
        
        #rename() will rename all the files
        os.rename(my_source, my_dest)
    
#driver code
if __name__ == "__main__":
    rename_files()
    