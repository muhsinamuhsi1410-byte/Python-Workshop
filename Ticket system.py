print("PVP Ticket System")
name=input("Enter your name--")
age=int(input("Enter your age--"))
movie=input("Enter movie name--")
print("Seat types")
print("1.Silver-Rs-200")
print("2.Gold-Rs-300")
choice=int(input("Enter your choice--"))
tickets=int(input("Enter no of tickets--"))
if(choice==1):
    ticket_price=200
    seat="silver"
else:
    ticket_price=300
    seat="gold"
total=ticket_price*tickets
student=input("Are you a student?(yes/no):")
if student=="yes":
 discount=total*0.10
 total=total-discount
print("\n--------Movie Ticket=----")
print("Name:",name)
print("Age:",age)
print("Movie:",movie)
print("Seat type:",seat)
print("Number of Tickets:",tickets)
print("Ticket Price:",ticket_price)
print("Total amount",total)
if age<18:
    print("Note:Minor customer.")
else:
    print("Enjoy your Movie")