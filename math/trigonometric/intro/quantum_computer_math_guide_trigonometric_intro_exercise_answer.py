import math
import json

answer_file_name ="quantum_computer_math_guide_trigonometric_intro_exercise_answers.json"
correct = "正解です！おめでとうございます！🎉"
incorrect = "不正解です・・・。もう一度考え直してみましょう。"

f = open(answer_file_name, 'r')

answer_json = json.load(f)

def check_answer_exercise(answer,exercise):
    if answer == float(answer_json[exercise]):
        return correct
    else:
        return incorrect
