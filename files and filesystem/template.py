#!/usr/bin/python
import os


def template(template_file, names_file, out_dir):
    try:
        with open(names_file, encoding="windows-1252") as file:
            if os.path.exists(out_dir) is False:
                os.mkdir(out_dir)
            for line in file:
                if line.strip():
                    #line = line.decode("utf-8")
                    print(line, end='')

                    name = line.replace('\n', '')
                    my_file = open(out_dir + "//" + name + ".txt", mode='w', encoding="utf-8")

                    with open(template_file, encoding='utf8') as template:
                        for t in template:
                            print(t + '\n', end='')
                            t = t.replace('{NAME}', name)
                            t.encode()
                            my_file.write(t)

                    my_file.close()
    except OSError as e:
        print(f"Sorry, but your file couldn't be opened: {e}")


template("template.txt", "names.txt", "template")
