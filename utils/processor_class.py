
import os
from .visualizers import generate_mel_spectogram
from tqdm.notebook import tqdm

class DataProcessor():

    def __init__(self, main_data_dir, val_dir = None, test_dir= None, do_train_val_test_split = False):
        self.main_dir = main_data_dir
        self.val_dir = val_dir
        self.test_dir = test_dir  
        self.initialize_files()      
        #self.convert_ogg2wav()
        #self.generate_dir_spectrograms()


    def initialize_files(self):

        self.train_wavfiles = [os.path.join(root, name)
            for root, dirs, files in os.walk(self.main_dir)#"data/nlp_keyword_bucket/train_1/")
            for name in files
            if name.endswith((".wav"))]

        if self.val_dir: 

            self.val_wavfiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(self.val_dir)#"data/nlp_keyword_bucket/val_1/")
                for name in files
                if name.endswith((".wav"))]

        if self.test_dir:

            self.test_wavfiles = [os.path.join(root, name)
                for root, dirs, files in os.walk(self.test_dir)#"data/nlp_keyword_bucket/test_1/")
                for name in files
                if name.endswith((".wav"))]

    def convert_ogg2wav(self):
        for filename in self.train_wavfiles:
            words = re.findall(r"[\w']+", filename)
            os.system("ffmpeg -y -i {0} {0}".format(filename))

        if self.val_dir:
            for filename in self.val_wavfiles:
                words = re.findall(r"[\w']+", filename)
                os.system("ffmpeg -y -i {0} {0}".format(filename))

        if self.test_dir:
            for filename in self.test_wavfiles:
                words = re.findall(r"[\w']+", filename)
                os.system("ffmpeg -y -i {0} {0}".format(filename))


    def generate_dir_spectrograms(self):

        for train_wavfl in tqdm(self.train_wavfiles, position=0, leave=True):
          generate_mel_spectogram(train_wavfl)
          
        if self.val_dir:
            for val_wavfl in tqdm(self.val_wavfiles, position=0, leave=True):
              generate_mel_spectogram(val_wavfl)
        
        if self.test_dir:
            for test_wavfl in tqdm(self.test_wavfiles, position=0, leave=True):
              generate_mel_spectogram(test_wavfl)


    def purge_wav_files(self):
        for filepath in self.train_wavfiles:
            if filepath.lower().endswith('.wav'):
                os.remove(filepath)

        

        if self.val_dir: 
            for filepath in self.val_wavfiles:
                if filepath.lower().endswith('.wav'):
                    os.remove(filepath)


        if self.test_dir:

            for filepath in self.test_wavfiles:
                if filepath.lower().endswith('.wav'):
                    os.remove(filepath)

