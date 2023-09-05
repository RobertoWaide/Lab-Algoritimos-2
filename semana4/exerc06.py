def finish(students):
    for student, note in students.items():
        students[student] = sum(note) / len(note)
    
    for student, note in students.items():
        print(f"\nAluno(a) {student} - média {note:.1f}")
            
        

def study():
    students = {}
    while True:
        name = input("Digite o nome do aluno: ")
        if name == "":
            break
        note1 = float(input("Digite a primeira nota: "))
        note2 = float(input("Digite a segunda nota: "))
        
        students[name] = [note1,note2]
    
    return students


def main():
    students = study()
    finish(students)

main()
