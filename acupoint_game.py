import random

ACUPOINTS = {
    "合谷": {
        "location": "位于手背，第1、2掌骨间，当第二掌骨桡侧的中点处",
        "function": "主治头痛、感冒等",
    },
    "足三里": {
        "location": "位于小腿前外侧，当犊鼻下3寸，胫骨前嵴旁1横指",
        "function": "主治胃痛、腹胀等",
    },
    "内关": {
        "location": "位于前臂掌侧，腕横纹上2寸，掌长肌腱与桡侧腕屈肌腱之间",
        "function": "主治心悸、胸痛等",
    },
    "涌泉": {
        "location": "在足底，当足底前三分之一与后面三分之二交点处",
        "function": "主治头晕、失眠等",
    },
    "曲池": {
        "location": "在肘横纹外侧端",
        "function": "主治手臂酸痛、便秘等",
    },
}


def generate_options(correct_location):
    locations = [info["location"] for info in ACUPOINTS.values()]
    options = [correct_location]
    while len(options) < 4 and len(options) < len(locations):
        choice = random.choice(locations)
        if choice not in options:
            options.append(choice)
    random.shuffle(options)
    return options


def ask_question(name):
    correct_loc = ACUPOINTS[name]["location"]
    options = generate_options(correct_loc)
    print(f"\n请问穴位【{name}】位于哪里？")
    for idx, opt in enumerate(options, 1):
        print(f" {idx}. {opt}")
    answer = input("请输入选项数字：")
    if answer.isdigit() and 1 <= int(answer) <= len(options):
        if options[int(answer)-1] == correct_loc:
            print("回答正确！")
            return True
    print(f"回答错误，正确答案是：{correct_loc}")
    return False


def play_level(names):
    score = 0
    for name in names:
        if ask_question(name):
            score += 1
    print(f"本关得分：{score}/{len(names)}")
    return score


def daily_challenge():
    print("\n=== 每日挑战 ===")
    names = random.sample(list(ACUPOINTS.keys()), 3)
    play_level(names)


def main():
    print("欢迎来到经络腧穴学习游戏！")
    print("1. 开始关卡模式")
    print("2. 每日挑战")
    choice = input("请选择模式：")
    if choice.strip() == "2":
        daily_challenge()
        return

    level1 = ["合谷", "足三里", "内关"]
    level2 = list(ACUPOINTS.keys())
    total = 0
    print("\n=== 第一关 ===")
    total += play_level(level1)

    input("\n按回车键进入第二关...")
    print("\n=== 第二关 ===")
    total += play_level(level2)

    print(f"\n总得分：{total}/{len(level1) + len(level2)}")
    print("感谢游玩！记得常练习穴位位置。")


if __name__ == "__main__":
    main()
