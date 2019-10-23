#Squad
#9/11/19
#Geometry assignment

#Shapes
print('''
    *------------*
    |            | 
    |            | a
    |            |
    *------------*
          +--------------+
          /|                 /|
         / |                / |
        *--+-----------*  
        |  |               |  | a
        |  |               |  |
        |  |               |  |
        |  +-------------+
        | /                | / a
        |/                 |/ 
        *--------------*
               ___
              a
 
            _____
         .- ``` ' `-.           
       .'          /  `.         
      /           r     \\        
     ;           /        ;       
     |__________/_______ |     
     ;         d          ;
      \\                 /       
       \\`.           .'       
         `-._____.-'          
                       
   
              
            /|\\    
           / | \\
          /  |  \\
         /   h   \\
        /    |     \\
       /___|___\\
              b

''')

#Here are the variables

variable_a = int(input("Variable A = "))
variable_b = int(input("Variable B = "))
variable_c = int(input("Variable C = "))
variable_d = int(input("Variable D = "))
variable_h = int(input("Variable H = "))
variable_r = int(input("Variable R = "))
variable_pi = 3.1415

#Here is the square
sqr_area = 4*variable_a

#area of a square with square feet
sqr_area_sqrd = variable_a*variable_a

#This is the circumference of a circle
cir_circum = 2*variable_pi*variable_r

#The area of a triangle
tri_area = variable_h*variable_b/2

#Volume of a cube
cub_vol = variable_a**3

#Printing out the answers
print("Perimeter of a square:",sqr_area)
print("Area of a square:",sqr_area_sqrd)
print("Circumference of a circle:",cir_circum)
print("Area of a triangle:",tri_area)
print("Volume of a cube:",cub_vol) 

input()
