import os
import pysrt
import time
import pickle

if __name__ == '__main__':
    filesName = []
    allSubtitles = [["" , []]]

    # C:\Users\romai\Dataset deeplearning
    # r'\FIXE_ROMAIN\Dataset deeplearning'
    # f = open(r"C:\Users\romai\DatasetDeeplearning\1176340_en.srt", encoding='utf8')
    # print(f.read())

    complete_file_list = os.listdir(r'\\FIXE_ROMAIN\DatasetDeeplearning')
    filelist = []
    for file in complete_file_list:
        if file.endswith('_1a1.mp4') or file.endswith('_1b1.mp4'):
            if file not in filelist:
                file = file.split("_")
                file = file[0]
                file = file + "_en.srt"
                if file in complete_file_list and file not in filelist:
                    filelist.append(file)
    for file in filelist:
        paragraphes = [[]]
        # subtitleNumber = []
        f = open(os.path.join(r'\\FIXE_ROMAIN\DatasetDeeplearning', file), encoding='utf-8')
        lines = f.readlines()
        for line in lines:  # Separates paragraphes
            if line == '\n':
                paragraphes.append([])
            else:
                paragraphes[-1].append(line)
        for i in range(3):
            paragraphes.pop(-1)  # Remove blank lines at the end

        paragraphesWithoutSentences = []
        paragraphesWithSentences = []
        personSpeaking = ""
        editedParagraphes = []

        for element in paragraphes:
            personSpeaking = ''
            try:
                text = element[2][3:]
                personSpeaking = element[2][0]

                if " " not in text:
                    paragraphesWithoutSentences.append(element)
                else:
                    paragraphesWithSentences.append(element)
            except IndexError:
                pass

        for element in paragraphesWithoutSentences:
            editedParagraphe = [None, None, None]
            editedParagraphe[1] = [str(element[1][0:12])] + [str(element[1][17:29])]
            editedParagraphe[0] = element[2][3:-1]
            editedParagraphe[2] = element[2][0]
            editedParagraphes.append(editedParagraphe)

        with open('pkl/' + file + '.pkl', 'wb') as outfile:
            pickle.dump(editedParagraphes, outfile, pickle.HIGHEST_PROTOCOL)
