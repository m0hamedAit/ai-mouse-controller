
from pathlib import Path
from Control import mouseControl
from voiceRecog import listening 
from multiprocessing import Process, freeze_support


# from tkinter import *
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter.constants import CENTER, FALSE

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")




def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


#to run mouseControl and voice recognition in parallel 
def startControl():
    global process1
    global process2
    process1 = Process(target=mouseControl)
    process2 = Process(target=listening)
    process1.start()
    process2.start()
    

#kill processes
def stopControl():
    process1.kill()
    process2.kill()


def main():
    window = Tk()
    p = PhotoImage(file="assets/Picture1.png")
    window.title("Cursor Controler")
    window.iconphoto(False,p)

    window.geometry("541x314")
    window.configure(bg = "#EBBE9B")
    canvas = Canvas(
        window,
        bg = "#EBBE9B",
        height = 314,
        width = 541,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        541.0,
        314.0,
        fill="#EBBE9B",
        outline="")

    canvas.create_text(
        87.0,
        20.0,
        anchor="nw",
        text="Click Start to start controling the cursor with just your face,\nand Stop to stop it \nCommand :\n - Right Click\n - Left Click\n - Double Click\n -  Scroll Up\n - Scroll Down\n - Scroll Left\n - Scroll Right\n - Write\n",
        justify="center",
        fill="#000000",
        font=("Roboto", 14 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        bg="#EBBE9B",
        highlightthickness=0,
        command= startControl,
        relief="flat"
    )

    button_1.place(
        x=126.0,
        y=250.0,
        #width=114.0,
        #height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        bg="#EBBE9B",
        command= stopControl,
        relief="flat"
    )
    button_2.place(
        x=316.0,
        y=250.0,
        #width=114.0,
        #height=34.0
    )

    window.resizable(False, False)
    window.mainloop()


if __name__=="__main__":
    main()
#     window = Tk()
#     p = PhotoImage(file="../assets/Picture1.png")
#     window.title("Cursor Controler")
#     window.iconphoto(False,p)

#     window.geometry("541x314")
#     window.configure(bg = "#EBBE9B")
#     canvas = Canvas(
#         window,
#         bg = "#EBBE9B",
#         height = 314,
#         width = 541,
#         bd = 0,
#         highlightthickness = 0,
#         relief = "ridge"
#     )

#     canvas.place(x = 0, y = 0)
#     canvas.create_rectangle(
#         0.0,
#         0.0,
#         541.0,
#         314.0,
#         fill="#EBBE9B",
#         outline="")

#     canvas.create_text(
#         87.0,
#         75.0,
#         anchor="nw",
#         text="Click Start to start controling the cursor with just your face,\nand Stop to stop it \neyes work as left and right click",
#         justify="center",
#         fill="#000000",
#         font=("Roboto", 14 * -1)
#     )

#     button_image_1 = PhotoImage(
#         file=relative_to_assets("button_1.png"))
#     button_1 = Button(
#         image=button_image_1,
#         borderwidth=0,
#         bg="#EBBE9B",
#         highlightthickness=0,
#         command= startControl,
#         relief="flat"
#     )

#     button_1.place(
#         x=126.0,
#         y=221.0,
#         #width=114.0,
#         #height=34.0
#     )

#     button_image_2 = PhotoImage(
#         file=relative_to_assets("button_2.png"))
#     button_2 = Button(
#         image=button_image_2,
#         borderwidth=0,
#         highlightthickness=0,
#         bg="#EBBE9B",
#         command= stopControl,
#         relief="flat"
#     )
#     button_2.place(
#         x=316.0,
#         y=221.0,
#         #width=114.0,
#         #height=34.0
#     )

#     window.resizable(False, False)
#     window.mainloop()


#  TODO fix bug : probably by creating separated thread for gui window 