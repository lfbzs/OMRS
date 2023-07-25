from utils.mido_yin import Musical_Instruments,Determine_clef,Actual_Note_Time,Actual_High



def Make_score(mung_dir,musical='Acoustic_Grand_Piano'):
    # 添加乐器
    score = []
    score.append("${}".format(Musical_Instruments[musical]))
    # 读取路径
    f = open(mung_dir, 'r')
    for line in f.readlines():
        line = line.strip('\n').split()
        for index,note in enumerate(line):

            if note[-4:] == 'clef':
                clef = line[index]
                clef_0_yin = Determine_clef[clef]
                continue
            elif note[0] == 'R':
                score.append(note)
                continue
            elif note[0].isdigit():
                Relative_Time, Relative_Height = note.split("_")
                Actual_height = Actual_High[clef_0_yin][int(Relative_Height)]
                Actual_time = Actual_Note_Time[int(Relative_Time)]

                score.append([Actual_height,Actual_time])
    return score



if __name__ == '__main__':
    mung_path = '/Users/loufengbin/Documents/python/pythonProject/tensorflow/YOLO/yolov5-6.1/runs/detect/exp4/mung/001699.txt'
    score = Make_score(mung_path,'Acoustic_Grand_Piano')
    # print(score)