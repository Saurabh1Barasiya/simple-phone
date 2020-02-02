from gtts import gTTS
from playsound import playsound
import time

class Phone:
    def __init__(self,Phone_name,model,colour,prize):
        self.P_N=Phone_name
        self.P_M=model
        self.P_C=colour
        self.P_P=prize
        self.save={}
        self.outgoing=[]
        self.save_message={}
        self.password=123456
        self.my_audio=gTTS("Hello my version is global 1.0 latest")
        self.my_audio.save("version.mp3")
        self.my_audio1=gTTS(f"Please wait i check for update latest version {time.sleep(5)} ok done we have installed latest verion in your device")
        self.my_audio1.save("update.mp3")

    def show_detail(self):
        print(f"Phone name is {self.P_N}")
        print(f"Phone model is {self.P_M}")
        print(f"Phone colour is {self.P_C}")
        print(f"Phone prize is {self.P_P}")

    def add_context(self):
        while True:
             self.number=input("Please enter number")
             if len(self.number) == 10:
                   self.number=self.number
                   self.name=input("please enter name")
                   self.name=self.name.title()
                   self.save.update(dict(zip([self.number],[self.name])))
                   print("current dictionary is",self.save)
                   break
             else:
                 print("Invalid number try again")
                 continue

    def show_context_detail(self):
        if bool(self.save):
            print("number and name are")
            for self.number,self.name in self.save.items():
                print(f"{self.number} ---  {self.name}")
        else:
            print("context are empty")

    def Out_goint_detail(self):
        if bool(self.outgoing):
            print("Your out going call detail are")
            for index,number in enumerate(self.outgoing,1):
                print(f"{index} ----- {number}")
        else:
            print("Outgoing list is empty")


    def call(self):
        self.pas=int(input("Please enter password"))
        if self.pas == self.password:
            while True:
                self.number=input("Please enter number")
                if len(self.number) == 10:
                    self.number=int(self.number)
                    print(f"calling {self.number}")
                    self.outgoing.append(self.number)
                    while True:
                       self.end=int(input("Press 1 for end call"))
                       if self.end == 1:
                           break
                       else:
                            print("Invalid number")
                            continue
                    break
                else:
                    print("Please enter valid number")
                    continue
        else:
            print("wrong password")
        
    def context(self):
        while True:
            self.pas=int(input("Please enter password"))
            if self.pas == self.password:
                self.cheack = int(input("Press 1 for add context \nPress 0 for show context detail"))
                if self.cheack == 1:
                    self.add_context()
                    break
                elif self.cheack == 0:
                    self.show_context_detail()
                    break
                else:
                    print("Invalid input Try again")
                    continue
            else:
                print("wrong password try again")
                continue

    def show_message(self):
        if bool(self.save_message):
            print("number and message are")
            for self.number,self.message in self.save_message.items():
                print(f"{self.number} ---  {self.message}")
        else:
            print("Message Box are empty")

    def send_message(self):
        while True:
            self.number=input("Please enter number that you want to send the message")
            if len(self.number) == 10:
                self.number = self.number
                self.mess=input("Please enter your messaage")
                self.save_message.update(dict(zip([self.number],[self.mess])))
                print("current dictionary is",self.save_message)
                break
            else:
                print("Invaid input for number\n Try again")
                continue

    
    def message(self):
        while True:
            self.pas1=int(input("Please enter password"))
            if self.pas1 == self.password:    
                self.num1=int(input("Press 1 for show message \nPress 0 for send message"))
                if self.num1 == 1:
                    self.show_message()
                    break
                elif self.num1 == 0:
                    self.send_message()
                    break
                else:
                    print("Invalid input\nInput must 0 or 1")
                    print("try again")
                    continue
            else:
                print("wrong password try again")
                continue

    def search_number(self):
        if bool(self.save):
            self.num=input("Please enter number to search name")
            if self.num  in self.save:
                self.n=self.save.get(self.num)
                print("search sucessfull")
                print(f"name is --  {self.n}")
        else:
            print("Context Box are empty")

    def search_name(self):
        if bool(self.save):
            self.nam=input("Please enter name to search number")
            #if self.nam  in self.save:
            for self.number,self.name in self.save.items():
                if self.nam.title() == self.name:
                #self.n=self.save.get(self.num)
                  print("search sucessfull")
                  print(f"number is --  {self.number}")
                  break
            else:
                print("search unsucessfull")
        else:
            print("Context Box are empty")


    def search(self):
        while True:
            self.pas=int(input("Please enter password"))
            if self.pas == self.password:
                self.cheack = int(input("Press 0 for search name \nPress 1 for search number"))
                if self.cheack == 1:
                    self.search_name()
                    break
                elif self.cheack == 0:
                    self.search_number()
                    break
                else:
                    print("Invalid input Try again")
                    continue
            else:
                print("wrong password try again")
                continue
    def play_audio(self):
            playsound("version.mp3")

    def version(self):
        self.play_audio()
        print("OK_SAURABH my version is global 2.0 latest")
        
    def cheack_update(self):
            playsound("update.mp3")




if __name__ == "__main__":
    print("Make sure your internet connection is enabled otherwise its not work")
    p1=Phone(input("Please input phone name"),input("Please input phone model"),input("Please input phone colour"),int(input("Pleasse input phone prize")))
    while True:
        print("\n\n\n")
        print("Please enter your choice")
        print("1. Show_detail")
        print("2. Context")
        print("3. Call")
        print("4. Message")
        print("5. Outgoing detail")
        print("6. Search")
        print("7. Version Detail")
        print("8. Update your version")
        print("9. Exit")
        choice=int(input(""))
        if choice == 1:
               p1.show_detail()
        elif choice == 2:
                p1.context()
        elif choice == 3:
                p1.call()
        elif choice == 4:
                p1.message()
        elif choice == 5:
                p1.Out_goint_detail()
        elif choice == 6:
            p1.search()
        elif choice == 7:
            p1.version()
        elif choice == 8:
            p1.cheack_update()
        elif choice == 9:
                exit()
        else:
                print("Invalid input try again")
                continue
input("Press enter for exit")        
