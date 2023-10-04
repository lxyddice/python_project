from importlib import import_module
import re

def generate_skill_value(skill_description, increases, level):
    pattern = r"\[(.*?)\]|\<(.*?)\>"
    values = re.findall(pattern, skill_description)
    updated_description = skill_description

    for i, value in enumerate(values):
        original_value = value[0] if value[0] else value[1]

        if '%' in original_value:
            original_value = float(original_value.strip('%'))
            updated_value = int(original_value + (level - 1) * increases[i])
            updated_value = f"{{{{color|#0098DC|{updated_value}%}}}}"
        else:
            try:
                original_value = float(original_value)
                updated_value = int(original_value + (level - 1) * increases[i])
            except ValueError:
                continue

        if value[0]:
            updated_description = updated_description.replace(f"[{value[0]}]", f"{{{{color|#0098DC|{updated_value}}}}}")
        else:
            updated_description = updated_description.replace(f"<{value[1]}>", f"{{{{color|#0098DC|{updated_value}}}}}")

    return updated_description

def generate_mediawiki_template(skill_name, skill_description, num_levels, increases, s1, s2):
    template = "{{技能\n"
    template += f"|技能名={skill_name}\n"
    template += f"|技能类型1={s1}\n"
    template += f"|技能类型2={s1}\n"

    for i in range(1, num_levels + 1):
        if i == 8:
            updated_skill_name = f"技能专精1"
        elif i == 9:
            updated_skill_name = f"技能专精2"
        elif i == 10:
            updated_skill_name = f"技能专精3"
        else:
            updated_skill_name = f"技能{i}"
        
        level_description = generate_skill_value(skill_description, increases, i)
        template += f"|{updated_skill_name}描述={level_description}\n"
        template += f"|{updated_skill_name}初始=0\n"
        template += f"|{updated_skill_name}消耗=0\n"
        template += f"|{updated_skill_name}持续=0\n"

    template += "|备注=\n}}"
    return template

skill_description = input("请输入技能的一级描述：")
increase_str = input("请输入增加量，以逗号分隔：")
s1 = input("请输入回复方式")
s2 = input("请输入触发方式")
increases = [float(increase) for increase in increase_str.split(",")]
skill_name = input("请输入技能名字：")
num_levels = 10  # 设置生成的等级数目
mediawiki_template = generate_mediawiki_template(skill_name, skill_description, num_levels, increases, s1, s2)

print("生成的mediawiki模板如下：")
print(mediawiki_template)
