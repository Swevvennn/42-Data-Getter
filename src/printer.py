from rich import print
from time import sleep

def print_table(students):
    projects = []

    for stud in students:
        for project in students[stud]['projects']:
            if project['name'] not in projects:
                projects.append(project['name'])

    print("Intra\t\t|"+"|".join([f"{' '.join(project.split()[2:]):^8}" for project in sorted(projects)]))
    print("----------------"+"+--------"*len(projects))
    for stud in sorted(students, key=lambda stud: len(students[stud].get('projects', {})), reverse=True):
        printable = stud + '   \t'
        for name in sorted(projects):
            if name not in [students[stud]['projects'][i]['name'] for i in range(len(students[stud]['projects']))]:
                printable += f'|    -   '
            else:
                project = [students[stud]['projects'][i] for i in range(len(students[stud]['projects'])) if students[stud]['projects'][i]['name'] == name]
                if len(project) > 0:
                    color = "green" if project[0]['valid'] else "red" 
                    printable += f"|[{color}]{project[0]['mark']:^8}[/{color}]"
        print(printable)


def print_board(students, by):
        e = 1
        for stud in sorted(students, key=lambda stud: students[stud].get(by, 0), reverse=True if by != 'ratio' else False):
            sleep(0.05)
            if students[stud].get(by, 0) != 0:
                    print(f"{str(e)}.\t{stud}   \t{str(students[stud][by])}")
                    e += 1
