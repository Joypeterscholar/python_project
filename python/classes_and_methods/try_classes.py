# class Human{
# private int num = 7;
#
# public static int addTwo(){
# num += 2;
# return num;
# }
#
# }
# Human.addTwo

# class Human:
#     num = 7
#     def __init__(self, num):
#         self.num = num
#     def addTwo(self):
#         self.num += 2
#         return self.num
#
# # Human human = new Human();
# human1 = Human
# print(human1.addTwo())

try:
    score1 = int(input("Enter a number: "))
    score2 = int(input("Enter a number: "))

    print(score1 + score2)
except:
    print("You can't do this")
