import PySimpleGUI as sg

def gui():
    sg.theme('GrayGrayGray')
    layout = [
        [sg.Text("\n\t  BMI Calculator by Tant0\n\n")],
        [sg.Text("Input Height (cm) : "), sg.Input(size=(25)), sg.Text("\n")],
        [sg.Text("Input Weight (kg) : "), sg.Input(size=25),sg.Text("\n")],
        [sg.Text("\n\n\n\n\n\n           "), sg.Submit(size=(8,2)),sg.Cancel(size=(8,2))]
    ]
    window=sg.Window("BMI Calculator",layout,size = (300,300))
    while True:
        event, values = window.read()
        window.close()
        if event==sg.WIN_CLOSED or event=="Cancel":
            break;
        return out(values)


def out(value):
    sg.theme('GrayGrayGray')
    bb=int(value[1])
    tb=int(value[0])
    bmi=bb/((tb/100)*(tb/100))
    if bmi<18.5:
        layout = [
        [sg.Text('\n\t Your Body Mass Index is')],
        [sg.Text("\t\t {:.2f}".format(bmi))],
        [sg.Text("\n\t    You are classified as\n\n\t       UNDERWEIGHT")],
        [sg.Text("\n\n\t      Calculate More ?")],
        [sg.Text("           "),sg.Button("Yes",size=(8,2)),sg.Exit(size=(8,2))]
    ]
    elif 18.5<=bmi<25:
        layout = [
        [sg.Text('\n\t Your Body Mass Index is')],
        [sg.Text("\t\t {:.2f}".format(bmi))],
        [sg.Text("\n\t    You are classified as\n\n\t           NORMAL")],
        [sg.Text("\n\n\t      Calculate More ?")],
        [sg.Text("           "),sg.Button("Yes",size=(8,2)),sg.Exit(size=(8,2))]
    ]
    elif 25<=bmi<40:
        layout = [
        [sg.Text('\n\t Your Body Mass Index is')],
        [sg.Text("\t\t {:.2f}".format(bmi))],
        [sg.Text("\n\t    You are classified as\n\n\t       OVERWEIGHT")],
        [sg.Text("\n\n\t      Calculate More ?")],
        [sg.Text("           "),sg.Button("Yes",size=(8,2)),sg.Exit(size=(8,2))]
    ]
    elif bmi>=40:
        layout = [
        [sg.Text('\n\t Your Body Mass Index is')],
        [sg.Text("\t\t {:.2f}".format(bmi))],
        [sg.Text("\n\t    You are classified as\n\n\t          OBESSE")],
        [sg.Text("\n\n\t      Calculate More ?")],
        [sg.Text("           "),sg.Button("Yes",size=(8,2)),sg.Exit(size=(8,2))]
    ]
    window = sg.Window("BMI Calculator",layout,size=(300,300)  )
    event, values = window.read()
    if event == 'Yes':
        window.close()
        gui()
    elif event==sg.WIN_CLOSED or event =="Exit":
        window.close()
gui()